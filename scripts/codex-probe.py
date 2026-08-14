#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
codex-probe.py — Codex 挤号+保号 一体流程 (基于分类探测)

原理: 中转站(NewAPI 面板)在模型通道满时返回 HTTP 500 + error.code=get_channel_failed
("当前模型 gpt-5.6-sol 通道已经达到上限"), 每次都是新的彩票, 没有排队位。
官方 Codex App 有服务端队列所以 20 分钟必进; API 侧只能靠探测撞窗口。

完整流程 (--fullflow):
  挤号: 每 --probe-sec 秒发最小真实请求, 解析状态码+error.code 分类记录
        -> 一旦某模型返回 200 (通道开了):
           [可选 --fire] 立即发送你的真实消息(挤进去干活), 保存回复
           -> 切到 保号: 每 --keepalive-sec 秒发真实请求占住
           -> 保号失败(通道又满) -> 自动回到 挤号, 循环
  永久错误 (key 挂了 / 模型没映射 / 免费日上限) -> 停止, exit 3

用法 (一条命令):
  python codex-probe.py --fullflow --fire "帮我修一下 main.ts"
  python codex-probe.py --fullflow                          # 只保号, 不干活
  python codex-probe.py --stats                             # 统计 probe.log
  python codex-probe.py --clean [--yes] [--wipe-logs]       # 清理测试会话文件
  python codex-probe.py                                     # 纯可用性监控(不挤)
  python codex-probe.py --fullflow --models gpt-5.6-sol,gpt-5.6-luna --base-url https://xxx/v1

常用参数:
  --probe-sec 8       挤号探测间隔(秒, 带 jitter)
  --keepalive-sec 300 保号间隔(秒, 非高峰)
  --max-tries 0       挤号最大轮数(0=无限)
  --peak-start 8 --peak-end 24   高峰期窗口(本地小时), 默认 08:00-23:59 高峰
  --peak-probe-sec 4             高峰期挤号间隔(秒, 异步, 最多 --max-inflight 在途)
  --peak-keepalive-sec 120       高峰期保号间隔(秒, 防被挤掉)
  --max-inflight 2               异步探测最大并发(不给服务器加压)
  --key / 环境变量 ANYROUTER_API_KEY / ~/anyrouter.key / ~/.codex/auth.json

统计 (--stats): 解析 probe.log, 输出总探测数/成功率/错误分类/进入记录/保号与发消息表现,
  以及按小时的进入分布(找容量窗口)。

清理 (--clean): 删除测试产生的会话文件 —— 旧版 codex CLI 在隔离 CODEX_HOME
  (~/.codex-queue/codex-home) 里的会话/日志, codex-neutr, logs/ 等, 保留 auth.json 与
  config.toml 以及 probe.log 统计。加 --wipe-logs 会连同 probe.log / last-reply.txt 一起删。

日志: ~/.codex-queue/probe.log   回复: ~/.codex-queue/last-reply.txt
退出码: 0=正常结束  2=达到 max-tries  3=永久错误(换 key/换中转)
"""
import argparse, json, os, random, re, sys, time
from concurrent.futures import ThreadPoolExecutor

# Windows GBK 控制台强制 UTF-8 输出, 避免中文乱码
if hasattr(sys.stdout, "reconfigure"):
    try: sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    except Exception: pass

try:
    import requests
except ImportError:
    sys.exit("缺少 requests 库, 请先: pip install requests")

DEFAULT_BASE = "https://anyrouter.top/v1"
# 实测你的中转 /responses 只映射了 gpt-5.6-sol; luna/terra/5-codex 都是 404
# 想多模型/多中转一起探测: --models a,b --base-url https://xxx/v1
DEFAULT_MODELS = ["gpt-5.6-sol"]

LOG_FILE = os.path.join(os.path.expanduser("~"), ".codex-queue", "probe.log")
REPLY_FILE = os.path.join(os.path.expanduser("~"), ".codex-queue", "last-reply.txt")

KEEPALIVE_TEXT = "\u4f60\u597d"          # 保号消息 (你好)
PERMANENT_CATS = ("AUTH", "MODEL_404", "DAILY_CAP")

# ---------------------------------------------------------------- 请求体
def build_body(model: str, text: str = KEEPALIVE_TEXT) -> dict:
    """最小但真实的 /responses 请求, 与 codex-queue.ps1 的保号请求体逐字段一致 (~19-40 tokens)。"""
    return {
        "model": model,
        "input": [{"type": "message", "role": "user",
                   "content": [{"type": "input_text", "text": text}]}],
        "stream": False,
        "store": False,
        "reasoning": {"effort": "low", "context": "all_turns"},
        "tool_choice": "auto",
        "parallel_tool_calls": False,
        "include": ["reasoning.encrypted_content"],
        "prompt_cache_key": "019fdfda-test",
        "text": {"verbosity": "low"},
        "client_metadata": {"x-codex-turn-metadata": "{\"installation_id\":\"t\",\"session_id\":\"t\"}"},
    }

# ---------------------------------------------------------------- 错误分类
def classify(status: int, err, body_txt: str) -> tuple:
    """返回 (分类, 详情)。基于 AnyRouter 文档 + NewAPI 实测错误码。"""
    if not isinstance(err, dict):
        err = {}   # 有些响应体 error 字段是字符串/缺失, 防御性处理
    code = err.get("code", "") or ""
    msg = err.get("message", "") or body_txt[:120]
    if status == 200:
        return "AVAILABLE", "通道可用, 立即开打!"
    if status == 500 and "get_channel_failed" in code:
        return "CHANNEL_BUSY", "中转的通道全满 (get_channel_failed) —— 纯靠运气, 继续试"
    if status == 404:
        return "MODEL_404", f"该中转没映射这个模型: {msg} —— 换模型或换中转"
    if status == 429:
        if code == "free_tier_daily_limit_exceeded":
            return "DAILY_CAP", "免费额度日上限, Retry-After 可能是几小时, 别傻等"
        if code == "rate_limit_exceeded":
            return "KEY_RATE", "你的 key 触发每分钟限流, 按 Retry-After 退避"
        if code == "ip_rate_limit_exceeded":
            return "IP_RATE", "匿名 IP 触发限流"
        return "RATE", f"429: {msg}"
    if status in (401, 403):
        return "AUTH", f"鉴权失败: {msg} —— 检查 key"
    if status in (500, 502, 503, 504):
        return "UPSTREAM", f"上游 5xx: {msg}"
    if status == 0:
        return "NETWORK", f"网络错误: {msg}"
    return "OTHER", f"HTTP {status}: {msg}"

# ---------------------------------------------------------------- key
def get_key(arg_key: str):
    if arg_key:
        return arg_key
    if os.environ.get("ANYROUTER_API_KEY"):
        return os.environ["ANYROUTER_API_KEY"]
    for p in (os.path.expanduser("~/anyrouter.key"),
              os.path.expanduser("~/.codex/auth.json")):
        if os.path.exists(p):
            try:
                if p.endswith(".json"):
                    return json.load(open(p)).get("OPENAI_API_KEY")
                v = open(p).read().strip()
                if v:
                    return v
            except Exception:
                pass
    return None

# ---------------------------------------------------------------- 单次探测
def probe_one(base: str, key: str, model: str, text: str = KEEPALIVE_TEXT, timeout: int = 30) -> dict:
    t0 = time.time()
    try:
        r = requests.post(f"{base}/responses",
                          headers={"Authorization": f"Bearer {key}"},
                          json=build_body(model, text), timeout=timeout)
        status, dt = r.status_code, round(time.time() - t0, 1)
        err, body_txt = None, ""
        try:
            j = r.json()
            err = j.get("error") if isinstance(j, dict) else None
            body_txt = json.dumps(j, ensure_ascii=False)[:150]
        except Exception:
            body_txt = r.text[:150]
        cat, detail = classify(status, err, body_txt)
        return {"model": model, "status": status, "dt": dt, "cat": cat,
                "detail": detail, "retry_after": r.headers.get("Retry-After", "")}
    except Exception as e:
        return {"model": model, "status": 0, "dt": round(time.time() - t0, 1),
                "cat": "NETWORK", "detail": str(e)[:120], "retry_after": ""}

def probe_all(base: str, key: str, models: list) -> list:
    """并发探测所有模型(小并发, 别把自己打成爬虫)。"""
    with ThreadPoolExecutor(max_workers=min(len(models), 3)) as ex:
        return list(ex.map(lambda m: probe_one(base, key, m), models))

# ---------------------------------------------------------------- 发真实消息
def send_message(base: str, key: str, model: str, message: str) -> dict:
    """通道刚开时立刻发真实消息(挤进去干活)。"""
    t0 = time.time()
    try:
        r = requests.post(f"{base}/responses",
                          headers={"Authorization": f"Bearer {key}"},
                          json=build_body(model, message), timeout=180)
        reply = ""
        if r.status_code == 200:
            try:
                j = r.json()
                out = j.get("output") or j.get("output_text") or j
                reply = json.dumps(out, ensure_ascii=False)[:500]
            except Exception:
                reply = r.text[:300]
        return {"status": r.status_code, "dt": round(time.time() - t0, 1), "reply": reply}
    except Exception as e:
        return {"status": 0, "dt": round(time.time() - t0, 1), "reply": str(e)[:200]}

# ---------------------------------------------------------------- 提示音
def play_success():
    try:
        import winsound
        winsound.MessageBeep(winsound.MB_ICONASTERISK)
        for f in (880, 1175, 880, 1175):
            winsound.Beep(f, 150)
    except Exception:
        print("\a\a\a", end="", flush=True)

# ---------------------------------------------------------------- 日志
def log(line: str, console: bool = True):
    """写入 probe.log (始终) + 控制台 (console=True 时)。
    挤号阶段同类 busy 错误在控制台去重, 但文件里每条都记, 保证 --stats 准确。"""
    ts = time.strftime("%Y-%m-%d %H:%M:%S")
    if console:
        print(f"[{ts}] {line}", flush=True)
    try:
        with open(LOG_FILE, "a", encoding="utf-8") as f:
            f.write(f"[{ts}] {line}\n")
    except Exception:
        pass

# ---------------------------------------------------------------- 纯监控模式
def run_watch(args, key, base, models):
    log(f"监控模式 | models={models} | base={base} | probe-sec={args.probe_sec}s")
    stats = {"ok": 0, "fail": 0, "last_ok": None}
    n = 0
    last_cat = {}
    while True:
        n += 1
        results = probe_all(base, key, models)
        for res in results:
            m, cat = res["model"], res["cat"]
            if cat == "AVAILABLE":
                stats["ok"] += 1
                stats["last_ok"] = time.strftime("%H:%M:%S")
                log(f"探测 #{n} | {m:16s} | HTTP {res['status']} {res['dt']}s | >>>>>> {res['detail']} <<<<<<")
                if args.fire:
                    log(f"通道开了! 发送真实消息 -> {m}")
                    fr = send_message(base, key, m, args.fire)
                    if fr["status"] == 200:
                        log(f"真实消息发送成功! HTTP 200 {fr['dt']}s | 回复: {fr['reply'][:300]}")
                    else:
                        log(f"真实消息失败 HTTP {fr['status']}: {fr['reply'][:200]}")
                    return
            else:
                stats["fail"] += 1
                if cat == "AUTH":
                    log(f"探测 #{n} | {m:16s} | 永久错误 [{cat}]: {res['detail']} -> key 已挂, 停止 (exit 3)")
                    sys.exit(3)
                notable = cat != last_cat.get(m) or n % 15 == 0
                log(f"探测 #{n} | {m:16s} | HTTP {res['status']} {res['dt']}s | [{cat}] {res['detail']}"
                    + (f" | Retry-After={res['retry_after']}" if res["retry_after"] else ""),
                    console=notable)
            last_cat[m] = cat
        if n % 30 == 0:
            tot = stats["ok"] + stats["fail"]
            rate = 100.0 * stats["ok"] / tot if tot else 0
            log(f"--- 统计: 成功 {stats['ok']}/{tot} ({rate:.1f}%) | 最近成功: {stats['last_ok'] or '无'} ---")
        time.sleep(args.probe_sec + random.uniform(0, 1.5))

# ---------------------------------------------------------------- 一体流程
def is_peak(args) -> bool:
    """高峰期判断(本地时间)。默认 08:00-23:59 高峰, 00:00-07:59 非高峰。
    --peak-start 8 --peak-end 24; 跨天窗口如 22->8; 相等则全天高峰。"""
    s, e = args.peak_start, args.peak_end
    h = time.localtime().tm_hour
    if s == e:
        return True
    if s < e:
        return s <= h < e
    return h >= s or h < e

def p_probe_sec(args) -> float:
    """当前模式的挤号间隔(高峰更频繁)。"""
    return args.peak_probe_sec if is_peak(args) else args.probe_sec

def p_keepalive_sec(args) -> float:
    """当前模式的保号间隔(高峰更频繁, 防被挤掉)。"""
    return args.peak_keepalive_sec if is_peak(args) else args.keepalive_sec

def run_fullflow(args, key, base, models):
    from concurrent.futures import ThreadPoolExecutor
    log(f"===== 一体流程启动 ===== | models={models} | base={base}")
    log(f"挤号: {args.probe_sec}s(高峰 {args.peak_probe_sec}s) | 保号: {args.keepalive_sec}s(高峰 {args.peak_keepalive_sec}s)"
        + (f" | fire 消息: {args.fire!r}" if args.fire else " | 只保号不干活"))
    phase = "probe"                    # probe=挤号 / keepalive=保号
    active_model = models[0]
    n = 0                              # 挤号发射次数
    keep_n = 0                         # 保号轮数
    last_cat = {}
    stats = {"ok": 0, "fail": 0, "entered": 0}
    last_peak = None
    # 异步探测: 固定节奏发射 + 最多 --max-inflight 个在途, 卡住的请求不拖慢节奏,
    # 同时并发上限保证不给中转太大压力
    pool = ThreadPoolExecutor(max_workers=max(1, args.max_inflight))
    inflight = []                      # [(model, future)] 在途探测
    next_fire = 0.0
    mi = 0                             # 多模型轮询游标

    while True:
        # ---- 高峰/非高峰模式切换提示 ----
        pk = is_peak(args)
        if pk != last_peak:
            log(f"=== {'高峰' if pk else '非高峰'}模式: 挤号 {p_probe_sec(args):.0f}s / 保号 {p_keepalive_sec(args):.0f}s ===")
            last_peak = pk

        # ================= 挤号: 异步探测撞窗口 =================
        if phase == "probe":
            # 1) 收在途结果
            done_res = []
            for model, rnd, fut in list(inflight):
                if fut.done():
                    inflight.remove((model, rnd, fut))
                    try:
                        res = fut.result()
                        res["round"] = rnd
                        done_res.append(res)
                    except Exception as e:
                        done_res.append({"model": model, "round": rnd, "status": 0, "dt": 0,
                                         "cat": "NETWORK", "detail": str(e)[:100], "retry_after": ""})

            # 2) 处理结果: 有 200 就抢进去
            for res in done_res:
                rnd = res.get("round", n)
                m, cat = res["model"], res["cat"]
                if cat == "AVAILABLE":
                    active_model = m
                    stats["ok"] += 1
                    stats["entered"] += 1
                    log(f"!!!!!!!!!! 挤号成功 (第 {rnd} 轮, 模型 {active_model}, HTTP 200) !!!!!!!!!!")
                    play_success()
                    if args.fire:
                        log(f"通道已开, 发送真实消息 -> {active_model}: {args.fire!r}")
                        fr = send_message(base, key, active_model, args.fire)
                        if fr["status"] == 200:
                            log(f"真实消息发送成功! HTTP 200 {fr['dt']}s")
                            if fr["reply"]:
                                log(f"回复: {fr['reply'][:400]}")
                            try:
                                with open(REPLY_FILE, "w", encoding="utf-8") as f:
                                    f.write(fr["reply"])
                            except Exception:
                                pass
                            log(f"回复已保存: {REPLY_FILE}")
                        else:
                            cat2, detail = classify(fr["status"], {}, fr["reply"])
                            if cat2 in PERMANENT_CATS:
                                log(f"真实消息永久失败 [{cat2}]: {detail} -> 停止 (exit 3)")
                                sys.exit(3)
                            log(f"真实消息失败 HTTP {fr['status']}: {fr['reply'][:150]} -> 回到挤号")
                            phase = "probe"
                            last_cat = {}
                            n = 0
                            next_fire = 0.0
                            break
                    # fire 成功 / 未设 fire -> 进入保号 (fire 失败已在上面 break 留在挤号)
                    for _, _, f2 in inflight:
                        f2.cancel()
                    inflight = []
                    phase = "keepalive"
                    keep_n = 0
                    last_cat = {}
                    log(">>> 已挤进去, 切换到 保号 (每 %ds 一次真实请求占住) <<<" % p_keepalive_sec(args))
                    break
                if cat in PERMANENT_CATS:
                    log(f"挤号 #{rnd} | {m:16s} | 永久错误 [{cat}]: {res['detail']} -> 停止 (exit 3)")
                    sys.exit(3)
                stats["fail"] += 1
                notable = cat != last_cat.get(m) or rnd % 15 == 0
                log(f"挤号 #{rnd} | {m:16s} | HTTP {res['status']} {res['dt']}s | [{cat}] {res['detail']}"
                    + (f" | Retry-After={res['retry_after']}" if res["retry_after"] else ""),
                    console=notable)
                last_cat[m] = cat
            if phase == "keepalive":
                continue

            # 3) 到点且并发未满 -> 异步发射下一发
            if len(inflight) < args.max_inflight and time.monotonic() >= next_fire:
                model = models[mi % len(models)]
                mi += 1
                n += 1
                if args.max_tries > 0 and n > args.max_tries:
                    log(f"达到 max-tries={args.max_tries}, 退出 (exit 2)")
                    sys.exit(2)
                inflight.append((model, n, pool.submit(probe_one, base, key, model)))
                next_fire = time.monotonic() + p_probe_sec(args) + random.uniform(0, 1.0)

            # 4) 统计 + 节奏控制(无在途时睡到下次发射, 有在途时轻轮询)
            if n % 30 == 0 and n > 0:
                tot = stats["ok"] + stats["fail"]
                rate = 100.0 * stats["ok"] / tot if tot else 0
                log(f"--- 统计: 成功 {stats['ok']}/{tot} ({rate:.1f}%) | 已进入 {stats['entered']} 次 ---")
            if not inflight:
                time.sleep(min(max(next_fire - time.monotonic(), 0), 1.0))
            else:
                time.sleep(0.2)

        # ================= 保号: 每 (高峰120s/平时300s) 一次真实请求 =================
        else:
            keep_n += 1
            res = probe_one(base, key, active_model)   # 你好 = 最小真实请求, 占住
            cat = res["cat"]
            if cat == "AVAILABLE":
                log(f"保号 #{keep_n} | {active_model:16s} | HTTP 200 {res['dt']}s | 通道仍开")
                time.sleep(p_keepalive_sec(args) + random.uniform(0, 5))
            elif cat in PERMANENT_CATS:
                log(f"保号 #{keep_n} | 永久错误 [{cat}]: {res['detail']} -> 停止 (exit 3)")
                sys.exit(3)
            else:
                log(f"保号 #{keep_n} | HTTP {res['status']} [{cat}] {res['detail']} -> 通道关了, 回到挤号")
                phase = "probe"
                last_cat = {}
                n = 0
                next_fire = 0.0
                time.sleep(p_probe_sec(args) + random.uniform(0, 1.5))

# ---------------------------------------------------------------- 统计
LINE_RE = re.compile(r"\[(\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2})\] (.*)")

def run_stats(args):
    from collections import Counter
    path = LOG_FILE
    if not os.path.exists(path) or os.path.getsize(path) == 0:
        print(f"还没有可统计的日志: {path}")
        print("先跑一次 --fullflow 或监控模式, 才会产生数据。")
        return
    raw = open(path, encoding="utf-8", errors="replace").read().splitlines()

    cats = Counter()            # 挤号错误分类计数
    entered = []                # (时间, 原文) 每次成功进入
    keep_ok = keep_lost = 0     # 保号 成功/掉线
    fire_ok = fire_fail = 0     # 真实消息 成功/失败
    enter_hour = Counter()      # 按小时进入分布
    n_probe = 0
    last_ts = None

    for line in raw:
        m = LINE_RE.match(line)
        if not m:
            continue
        ts, content = m.group(1), m.group(2)
        last_ts = ts
        if "挤号成功" in content:
            entered.append((ts, content))
            enter_hour[ts[11:13]] += 1
        elif content.startswith("保号"):
            if "通道仍开" in content:
                keep_ok += 1
            elif "回到挤号" in content or "通道关了" in content:
                keep_lost += 1
        elif "真实消息发送成功" in content:
            fire_ok += 1
        elif "真实消息失败" in content or "真实消息永久失败" in content:
            fire_fail += 1
        elif "挤号 #" in content:
            n_probe += 1
            cm = re.search(r"\[([A-Z0-9_]+)\]", content)
            if cm:
                cats[cm.group(1)] += 1

    ok = len(entered)          # 每次“挤号成功”= 一次 HTTP 200 探测成功
    fail = sum(cats.values())
    tot = n_probe + ok         # 探测总次数 = 失败日志行 + 成功进入次数
    rate = 100.0 * ok / tot if tot else 0.0

    print("=" * 52)
    print(" Codex 挤号/保号 统计报告")
    print("=" * 52)
    print(f"日志文件: {path}")
    print(f"统计区间: {raw[0][1:20] if raw else '-'}  ~  {last_ts or '-'}")
    print("-" * 52)
    print(f"挤号总探测次数        : {tot}")
    print(f"成功进入通道次数      : {ok}  (成功率 {rate:.2f}%)")
    print("-" * 52)
    if entered:
        print("进入通道记录 (时间):")
        for ts, _ in entered:
            print(f"   {ts}")
    print("-" * 52)
    print("挤号失败分类 (Top):")
    if cats:
        for cat, c in cats.most_common():
            print(f"   {cat:16s} {c}")
    else:
        print("   (无失败记录)")
    print("-" * 52)
    print(f"保号: 成功 {keep_ok} 次 | 掉线回挤号 {keep_lost} 次")
    print(f"真实消息: 发送成功 {fire_ok} 次 | 失败 {fire_fail} 次")
    print("-" * 52)
    if enter_hour:
        print("按小时进入分布 (找容量窗口, 时间=服务器日志时间):")
        for hour, c in sorted(enter_hour.items()):
            bar = "#" * min(c, 40)
            print(f"   {hour}:00  {c:4d}  {bar}")
    print("=" * 52)

# ---------------------------------------------------------------- 清理
BASE_DIR = os.path.join(os.path.expanduser("~"), ".codex-queue")

def run_clean(args):
    """删除测试产生的会话/日志文件。保留 auth.json + config.toml (隔离 CODEX_HOME 配置)
    以及 probe.log 统计; --wipe-logs 时连 probe.log / last-reply.txt 也删。"""
    targets = []   # (path, kind, desc)
    codex_home = os.path.join(BASE_DIR, "codex-home")
    if os.path.isdir(codex_home):
        for name in sorted(os.listdir(codex_home)):
            if name in ("auth.json", "config.toml"):
                continue
            p = os.path.join(codex_home, name)
            targets.append((p, "dir" if os.path.isdir(p) else "file", f"隔离 CODEX_HOME 会话: {name}"))
    for sub in ("codex-neutr", "logs"):
        p = os.path.join(BASE_DIR, sub)
        if os.path.exists(p):
            targets.append((p, "dir", f"旧版会话/日志目录: {sub}"))
    for fn in ("last-message.txt", "activity.log"):
        p = os.path.join(BASE_DIR, fn)
        if os.path.exists(p):
            targets.append((p, "file", f"旧版残留文件: {fn}"))
    if args.wipe_logs:
        for fn in ("probe.log", "last-reply.txt"):
            p = os.path.join(BASE_DIR, fn)
            if os.path.exists(p):
                targets.append((p, "file", f"本脚本日志: {fn}"))

    if not targets:
        print("没有可清理的测试会话文件 ✅")
        return
    print(f"将清理 {len(targets)} 项测试会话文件:")
    for p, _, desc in targets:
        print(f"  - {p}   ({desc})")
    if not args.yes:
        r = input("确认清理? [y/N] ").strip().lower()
        if r not in ("y", "yes"):
            print("已取消")
            return
    removed = 0
    for p, kind, _ in targets:
        try:
            if kind == "dir":
                import shutil; shutil.rmtree(p)
            else:
                os.remove(p)
            removed += 1
        except Exception as e:
            print(f"  ! 清理失败: {p}: {e}")
    if args.wipe_logs:
        print(f"已清理 {removed} 项 ✅ (含 probe.log / last-reply.txt)")
    else:
        print(f"已清理 {removed} 项 ✅ (保留 auth.json/config.toml 与 probe.log 统计)")

# ---------------------------------------------------------------- main
def main():
    ap = argparse.ArgumentParser(description="Codex 挤号+保号 一体流程")
    ap.add_argument("--key", default="")
    ap.add_argument("--base-url", default=DEFAULT_BASE)
    ap.add_argument("--models", default=",".join(DEFAULT_MODELS))
    ap.add_argument("--probe-sec", type=float, default=8.0, help="挤号探测间隔(秒, 非高峰)")
    ap.add_argument("--interval", type=float, default=None, help="兼容旧参数, 等价于 --probe-sec")
    ap.add_argument("--keepalive-sec", type=float, default=300.0, help="保号间隔(秒, 非高峰)")
    ap.add_argument("--peak-start", type=int, default=8, help="高峰期开始小时(本地时间, 默认8点)")
    ap.add_argument("--peak-end", type=int, default=24, help="高峰期结束小时(默认24; 跨天如22->8; 相等=全天高峰)")
    ap.add_argument("--peak-probe-sec", type=float, default=4.0, help="高峰期挤号间隔(秒)")
    ap.add_argument("--peak-keepalive-sec", type=float, default=120.0, help="高峰期保号间隔(秒, 防被挤掉)")
    ap.add_argument("--max-inflight", type=int, default=2, help="异步探测最大在途并发(控制服务器压力)")
    ap.add_argument("--max-tries", type=int, default=0, help="挤号最大轮数, 0=无限")
    ap.add_argument("--fullflow", action="store_true", help="一体流程: 挤号->[发消息]->保号->自动回挤号")
    ap.add_argument("--fire", default="", help="通道开时自动发送的真实消息")
    ap.add_argument("--stats", action="store_true", help="统计 probe.log 并输出报告")
    ap.add_argument("--clean", action="store_true", help="清理测试会话文件 (codex-home 会话/logs 等)")
    ap.add_argument("--yes", action="store_true", help="--clean 免确认")
    ap.add_argument("--wipe-logs", action="store_true", help="--clean 时连同 probe.log/last-reply.txt 一起删")
    ap.add_argument("--log-file", default="", help="日志文件路径(默认 ~/.codex-queue/probe.log; 测试可用临时文件避免污染)")
    ap.add_argument("--reply-file", default="", help="真实消息回复保存路径(默认 ~/.codex-queue/last-reply.txt)")
    args = ap.parse_args()

    if args.log_file:
        global LOG_FILE
        LOG_FILE = os.path.abspath(os.path.expanduser(args.log_file))
    if args.reply_file:
        global REPLY_FILE
        REPLY_FILE = os.path.abspath(os.path.expanduser(args.reply_file))

    if args.stats:
        run_stats(args)
        return
    if args.clean:
        run_clean(args)
        return

    if args.interval is not None:
        args.probe_sec = args.interval

    key = get_key(args.key)
    if not key:
        sys.exit("没找到 key: 用 --key 或环境变量 ANYROUTER_API_KEY 或 ~/anyrouter.key")
    models = [m.strip() for m in args.models.split(",") if m.strip()]
    if not models:
        sys.exit("--models 不能为空")
    base = args.base_url.rstrip("/")

    os.makedirs(os.path.dirname(LOG_FILE), exist_ok=True)

    if args.fullflow:
        run_fullflow(args, key, base, models)
    else:
        run_watch(args, key, base, models)

if __name__ == "__main__":
    main()
