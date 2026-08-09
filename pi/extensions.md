# Pi 扩展与 MCP

## 扩展清单(源码已包含在 `agent/extensions/`)

| 扩展 | 文件 | 功能 | 地址/来源 |
|---|---|---|---|
| **auto-session-name** | `auto-session-name.ts` | 自动为会话生成标题(LLM 摘要 + 启发式回退),`/name-sessions` 批量命名 | 本仓库自研 |
| **orca-agent-status** | `orca-agent-status.ts` | 与 Orca 面板同步 agent 状态 | Orca 自动管理 |
| **orca-prefill** | `orca-prefill.ts` | Orca 会话预填 | Orca 自动管理 |
| **orca-titlebar-spinner** | `orca-titlebar-spinner.ts` | Orca 标题栏状态动画 | Orca 自动管理 |

> orca-* 扩展由 Orca 面板自动生成管理,`auto-session-name` 为手动安装。
> 扩展加载:放入 `~/.pi/agent/extensions/`,在 pi 内 `/reload` 生效。

### auto-session-name 配置

配置文件:`~/.pi/agent/auto-session-name.json`(模板见 `auto-session-name.example.json`):

```json
{
  "enabled": true,
  "models": [
    { "baseUrl": "http://127.0.0.1:21434", "apiKey": "YOUR_KEY", "model": "grok-chat-fast", "timeoutMs": 12000 },
    { "baseUrl": "http://127.0.0.1:18990", "apiKey": "YOUR_KEY", "model": "claude-haiku-4.5", "timeoutMs": 8000 }
  ]
}
```

- 多端点 fallback:依次尝试,全部失败回退启发式(取首条消息截断)
- 命令:`/llm-title status|on|off`、`/name-sessions [dry|all]`
- 费用:本地 grok2api / kiro-rs,免费

## Pi 的 MCP

Pi 的 MCP 配置在 `~/.pi/agent/mcp.json`:

```json
{
  "mcpServers": {
    "github": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-github"],
      "env": { "GITHUB_PERSONAL_ACCESS_TOKEN": "你的Token" }
    }
  },
  "imports": []
}
```

配置后需在 pi 内重启或 `/reload` 生效。`mcp.json` 中的 `imports` 可用于引入共享 MCP 定义。

## Pi 包(Packages)

`settings.json` 中 `packages` 列表(全部为 npm 包,地址即包名):

| 包 | 功能 |
|---|---|
| `pi-mcp-adapter` | MCP 适配 |
| `pi-subagents` | 子代理 |
| `pi-web-access` | 网页访问 |
| `context-mode` | 上下文管理模式 |
| `@juicesharp/rpiv-todo` | 任务清单 |
| `@narumitw/pi-goal` | 目标跟踪 |
| `pi-simplify` | 简化输出 |
| `@narumitw/pi-plan-mode` | 计划模式 |
| `pi-open-tui` | TUI 增强 |

## Pi 技能

Pi 通过 `settings.json` 的 `skills` 数组加载共享技能(`~/.claude/skills`、`~/.codex/skills`,
本机均为指向 `~/.agents/skills/` 的符号链接,见根目录 `skills/README.md`)。
