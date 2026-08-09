// @auto-session-name
// 自动为 pi 会话生成有意义的标题,让 /resume 列表可读。
// - 监听用户输入,在会话尚未命名时自动命名(不覆盖手动 /name)
// - /name-sessions 命令可批量命名当前项目目录下的历史会话(只处理未命名的,先备份)

import {
  readdirSync,
  readFileSync,
  writeFileSync,
  copyFileSync,
  appendFileSync,
  existsSync,
  mkdirSync,
} from "node:fs"
import { join, basename } from "node:path"
import { randomUUID } from "node:crypto"
import os from "node:os"

const MAX_LEN = 42
const MIN_GOOD_LEN = 12

// ---------- 标题工具 ----------

function clean(raw: string): string {
  let t = raw
    .replace(/https?:\/\/\S+/g, " ") // URLs
    .replace(/<[^>]*>/g, " ") // HTML/XML 标签
    .replace(/```[\s\S]*?```/g, " ") // code blocks
    .replace(/`[^`]*`/g, " ") // inline code
    .replace(/[#>*_~|\[\](){}]/g, " ") // markdown symbols
    .replace(/[\u{1F300}-\u{1FAFF}\u{2600}-\u{27BF}\u{FE0F}]/gu, " ") // emoji
    .replace(/\s+/g, " ")
    .trim()
  // 中英文之间不需要空格,压缩多余空格
  t = t.replace(/([\u4e00-\u9fa5])\s+([\u4e00-\u9fa5])/g, "$1$2")
  return t
}

function truncate(s: string, n: number): string {
  return s.length <= n ? s : s.slice(0, n).trimEnd() + "…"
}

function isTrivial(text: string): boolean {
  const t = text.trim().toLowerCase()
  if (!t) return true
  if (t.length < 5) return true
  if (/^\/[a-z]/i.test(t)) return true // 斜杠命令
  // 纯问候/确认
  if (/^(ok|okay|好|好的|收到|了解|嗯|hello|hi|hey|thanks|thank you|谢谢|yes|no|行|可以|在吗|你好|在不在)[\s。.!！~～?？]*$/i.test(t)) return true
  return false
}

function makeTitle(messages: string[]): string | null {
  // 先清理再判断,避免 URL/HTML/符号残留进标题
  const cleaned = messages.map((m) => clean(m))
  const meaningful = cleaned.filter((m) => !isTrivial(m))
  if (meaningful.length === 0) return null
  // 第一条足够具体就直接用
  const first = meaningful[0]
  if (first.length >= MIN_GOOD_LEN) return truncate(first, MAX_LEN)
  // 否则从累积消息里挑最长、信息量最大的
  let best = first
  for (const m of meaningful) {
    if (m.length > best.length) best = m
  }
  if (best.length < MIN_GOOD_LEN) return null
  return truncate(best, MAX_LEN)
}

// ---------- 批量命名历史会话 ----------

interface SessionInfo {
  type: string
  name?: string
}

function firstUserTextInFile(file: string): { text: string; hasName: boolean } {
  let hasName = false
  let firstUser = ""
  const lines = readFileSync(file, "utf8").split("\n")
  for (const line of lines) {
    if (!line.trim()) continue
    let obj: Record<string, unknown>
    try {
      obj = JSON.parse(line)
    } catch {
      continue
    }
    if (obj.type === "session_info") {
      if (obj.name) hasName = true
      continue
    }
    if (obj.type !== "message" || firstUser) continue
    const msg = obj.message as { role?: string; content?: unknown }
    if (msg?.role !== "user") continue
    const content = msg.content
    if (Array.isArray(content)) {
      for (const part of content as { type?: string; text?: string }[]) {
        if (part?.type === "text" && typeof part.text === "string" && part.text.trim()) {
          firstUser = part.text.trim()
          break
        }
      }
    } else if (typeof content === "string" && content.trim()) {
      firstUser = content.trim()
    }
  }
  return { text: firstUser, hasName }
}

function renameSessionFile(file: string, dryRun: boolean): "renamed" | "skipped" | "none" | "error" {
  const { text, hasName } = firstUserTextInFile(file)
  if (hasName) return "skipped"
  const title = makeTitle([text])
  if (!title) return "none"
  if (dryRun) return "renamed"
  try {
    copyFileSync(file, file + ".bak") // 安全网
    const entry: SessionInfo = {
      type: "session_info",
      id: randomUUID().replace(/-/g, "").slice(0, 8),
      parentId: null,
      timestamp: new Date().toISOString(),
      name: title,
    }
    appendFileSync(file, JSON.stringify(entry) + "\n")
    return "renamed"
  } catch (e) {
    return "error"
  }
}

// ---------- 可选 LLM 摘要(低成本)----------

interface LLMEndpoint {
  baseUrl: string
  apiKey: string
  model: string
  timeoutMs?: number
}

interface LLMConfig {
  enabled?: boolean
  // 单端点(向后兼容)
  baseUrl?: string
  apiKey?: string
  model?: string
  timeoutMs?: number
  // 多端点 fallback 链(优先使用前面的,失败/超时自动回退)
  models?: LLMEndpoint[]
}

function llmConfigPath(): string {
  return join(
    process.env.PI_CONFIG_DIR || os.homedir(),
    ".pi",
    "agent",
    "auto-session-name.json",
  )
}

function loadLLMConfig(): LLMConfig {
  try {
    const p = llmConfigPath()
    if (existsSync(p)) return JSON.parse(readFileSync(p, "utf8"))
  } catch {
    /* ignore */
  }
  return {}
}

// 从配置解析端点列表:优先 models 数组,否则用旧的单端点字段
function endpointsFromConfig(cfg: LLMConfig): LLMEndpoint[] {
  if (Array.isArray(cfg.models) && cfg.models.length > 0) {
    return cfg.models.filter((m) => m?.baseUrl && m?.apiKey && m?.model)
  }
  if (cfg.baseUrl && cfg.apiKey && cfg.model) {
    return [{ baseUrl: cfg.baseUrl, apiKey: cfg.apiKey, model: cfg.model, timeoutMs: cfg.timeoutMs }]
  }
  return []
}

// 用单个端点生成标题。输入截断 400 字符、输出限 30 token、超时/失败返回 null。
async function llmTitleOne(text: string, ep: LLMEndpoint): Promise<string | null> {
  const controller = new AbortController()
  const timer = setTimeout(() => controller.abort(), ep.timeoutMs || 15000)
  try {
    const res = await fetch(ep.baseUrl.replace(/\/+$/, "") + "/v1/chat/completions", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
        Authorization: "Bearer " + ep.apiKey,
      },
      body: JSON.stringify({
        model: ep.model,
        max_tokens: 30,
        temperature: 0.2,
        messages: [
          {
            role: "system",
            content:
              "You are a session-title generator. Given a user message, output ONE short title (max 20 characters, Chinese preferred) that summarizes the intent. Rules: output ONLY the title; no greetings; no explanations; no punctuation at end; never address the user.",
          },
          { role: "user", content: "Message: " + text.slice(0, 400) },
        ],
      }),
      signal: controller.signal,
    })
    clearTimeout(timer)
    if (!res.ok) return null
    const data = await res.json()
    const t: string = data?.choices?.[0]?.message?.content?.trim() || ""
    if (!t) return null
    const cleaned = clean(t)
    // 质量检查:太长/太短/含对话式开头都视为不合格,交给下一个端点或启发式
    if (cleaned.length < 4 || cleaned.length > 24) return null
    if (/^(是的|可以|好的|你好|好的，|可以的|当然|请|您|你好！)/.test(cleaned)) return null
    return truncate(cleaned, MAX_LEN)
  } catch {
    clearTimeout(timer)
    return null
  }
}

// 依次尝试所有端点,第一个成功即返回。
async function llmTitle(text: string, cfg: LLMConfig): Promise<string | null> {
  if (!cfg.enabled) return null
  const eps = endpointsFromConfig(cfg)
  for (const ep of eps) {
    const t = await llmTitleOne(text, ep)
    if (t) return t
  }
  return null
}

// ---------- 扩展主体 ----------

export default function (pi: any) {
  const pending: string[] = []
  let userNamed = false
  let namedThisSession = false
  const llmCfg = loadLLMConfig()

  pi.on("session_start", () => {
    pending.length = 0
    namedThisSession = false
    // 恢复会话:如果已有名字(包括用户手动设置过的),不再自动覆盖
    try {
      userNamed = !!pi.getSessionName()
    } catch {
      userNamed = false
    }
  })

  pi.on("session_info_changed", (event: { name?: string }) => {
    if (event?.name) userNamed = true // 任何已命名的状态都视为用户/已有命名
  })

  pi.on("input", (event: { text?: string; source?: string }, ctx: any) => {
    if (userNamed || namedThisSession) return
    if (event?.source === "extension") return
    const raw = event?.text
    if (!raw || !raw.trim()) return
    if (raw.trim().startsWith("/")) return // 斜杠命令不参与命名

    const text = clean(raw)
    if (isTrivial(text)) return
    pending.push(text)

    // 已累积足够信息就生成标题(本会话只自动命名一次)。
    // 后台异步执行,不阻塞用户消息处理:LLM(多端点 fallback)失败自动回退启发式。
    if (pending.length >= 1 && !namedThisSession) {
      namedThisSession = true // 先占位,避免并发重复命名
      const snapshot = pending[pending.length - 1]
      void (async () => {
        let title: string | null = null
        if (llmCfg.enabled) title = await llmTitle(snapshot, llmCfg)
        if (!title) title = makeTitle(pending)
        if (title) {
          try {
            pi.setSessionName(title)
          } catch {
            /* ignore */
          }
        }
      })()
    }
  })

  // 查看/开关 LLM 摘要配置
  pi.registerCommand("llm-title", {
    description:
      "LLM 会话摘要标题: /llm-title status 查看, /llm-title on|off 开关(需配置 ~/.pi/agent/auto-session-name.json)",
    handler: async (args: string, ctx: any) => {
      const a = args.trim().toLowerCase()
      const cfg = loadLLMConfig()
      if (a === "status") {
        const eps = endpointsFromConfig(cfg)
        const st = cfg.enabled && eps.length > 0
          ? `已启用 (${eps.map((e) => e.model + "@" + e.baseUrl.replace(/^https?:\/\//, "")).join(" → ")})`
          : "未启用(零成本启发式)。要启用: 配置 ~/.pi/agent/auto-session-name.json 并设 enabled=true"
        ctx?.ui?.notify("LLM 标题: " + st, "info")
        return
      }
      if (a === "on" || a === "off") {
        cfg.enabled = a === "on"
        writeFileSync(llmConfigPath(), JSON.stringify(cfg, null, 2))
        ctx?.ui?.notify(`LLM 标题已${a === "on" ? "启用" : "关闭"} (下次会话生效)`, "info")
        return
      }
      ctx?.ui?.notify("用法: /llm-title status|on|off", "info")
    },
  })

  // 批量命名当前项目的历史会话
  pi.registerCommand("name-sessions", {
    description:
      "批量命名当前项目的历史会话(自动从第一条消息生成标题,跳过已命名的,先备份)。用法: /name-sessions [dry] 或 /name-sessions all [dry](处理所有项目)",
    handler: async (args: string, ctx: any) => {
      const parts = args.trim().split(/\s+/)
      const all = parts[0] === "all"
      const dryRun = parts.includes("dry") || parts.includes("--dry")
      const sessionFile: string | undefined = (() => {
        try {
          return ctx?.sessionManager?.getSessionFile?.()
        } catch {
          return undefined
        }
      })()

      const sessionsRoot = join(
        process.env.PI_CONFIG_DIR || process.env.HOME || os.homedir(),
        ".pi",
        "agent",
        "sessions",
      )
      if (!existsSync(sessionsRoot)) {
        ctx?.ui?.notify("未找到会话目录", "error")
        return
      }

      const dirs = all ? readdirSync(sessionsRoot, { withFileTypes: true }) : []
      const targets: string[] = []
      if (all) {
        for (const d of dirs) {
          if (d.isDirectory()) {
            for (const f of readdirSync(join(sessionsRoot, d.name))) {
              if (f.endsWith(".jsonl")) targets.push(join(sessionsRoot, d.name, f))
            }
          }
        }
      } else {
        // 当前项目目录:用 cwd 编码推断
        const cwd = ctx?.cwd || process.cwd()
        const enc = "--" + cwd.replace(/[\\/:]/g, "-") + "--"
        const currentDir = join(sessionsRoot, enc)
        if (existsSync(currentDir)) {
          targets.push(
            ...readdirSync(currentDir)
              .filter((f) => f.endsWith(".jsonl"))
              .map((f) => join(currentDir, f)),
          )
        }
      }

      // 跳过当前正在写的会话文件
      const activeBase = sessionFile ? basename(sessionFile) : ""
      const candidates = targets.filter((f) => basename(f) !== activeBase)

      let renamed = 0
      let skipped = 0
      let noTitle = 0
      let errors = 0
      const examples: string[] = []
      for (const f of candidates) {
        const r = renameSessionFile(f, dryRun)
        if (r === "renamed") {
          renamed++
          if (examples.length < 5) examples.push(truncate(clean(firstUserTextInFile(f).text), 50))
        } else if (r === "skipped") skipped++
        else if (r === "none") noTitle++
        else errors++
      }

      const mode = dryRun ? "(dry-run 预演)" : "(已写入)"
      const msg = `name-sessions ${mode}: ${renamed} 个已命名, ${skipped} 个已有名字跳过, ${noTitle} 个无可提取标题, ${errors} 个出错`
      ctx?.ui?.notify(msg, "info")
      if (dryRun && examples.length) {
        console.log("示例标题:")
        examples.forEach((e) => console.log("  · " + e))
      }
    },
  })
}
