# agent-setup — Pi 环境复刻包

在任意全新 Windows 机器上完整复刻我的 [Pi coding agent](https://github.com/earendil-works/pi-coding-agent) 环境——**除账号登录外的一切**。

## 覆盖范围

| 内容 | 来源 | 复刻方式 |
|------|------|---------|
| Pi 本体 | npm `@earendil-works/pi-coding-agent` | `setup.ps1` 安装 |
| 5 个配置文件(settings/mcp/open-tui/claude-code-style/models-store) | `~/.pi/agent/` | `pi/` 目录直拷 |
| 3 个本地扩展(orca-agent-status/orca-prefill/orca-titlebar-spinner) | `~/.pi/agent/extensions/` | `pi/extensions/` 直拷 |
| orca-cli 技能 | `~/.pi/agent/skills/` | `pi/skills/` 直拷 |
| 34 个共享技能 + browser-qa.md | `~/.agents/` | `agents-skills/` 全量 vendor |
| 14 个 pi 扩展包(~360MB) | settings.json `packages` 清单 | **首次启动 pi 自动安装**，不入库 |

## 不覆盖(设计如此)

- `auth.json` — 账号凭据,复刻后手动 `/login`
- `sessions/` `missions/` `run-history.jsonl` 及各类缓存 — 运行时数据
- `~/.pi/agent/npm/` `bin/` — 由 pi 自动重建

## 使用

**新机器复刻:**

```powershell
git clone https://github.com/HSJ-BanFan/agent-setup.git
cd agent-setup
pwsh setup.ps1     # 装 node(缺则 winget)→ 装 pi → 拷配置
pi                 # 启动后 /login,扩展包自动安装
```

> 国内网络若 npm 慢,先配好代理再跑。

**本机配置变更后回写仓库:**

```powershell
pwsh snapshot.ps1  # 导出配置+技能,自动扫密钥,git diff 核对后提交
```

## 维护约定

- 配置以 `snapshot.ps1` 导出为准,不手编 `pi/` 下文件(会被下次导出覆盖)
- `models-store.json` 已验证仅含 provider 定义无密钥;新增 provider 后跑一次 snapshot 的密钥扫描确认
