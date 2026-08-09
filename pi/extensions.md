# Pi 扩展与 MCP

## 扩展清单(源码已包含在 `agent/extensions/`)

| 扩展 | 文件 | 功能 | 地址/来源 |
|---|---|---|---|
| **orca-agent-status** | `orca-agent-status.ts` | 与 Orca 面板同步 agent 状态 | Orca 自动管理 |
| **orca-prefill** | `orca-prefill.ts` | Orca 会话预填 | Orca 自动管理 |
| **orca-titlebar-spinner** | `orca-titlebar-spinner.ts` | Orca 标题栏状态动画 | Orca 自动管理 |

> orca-* 扩展由 Orca 面板自动生成管理。
> 扩展加载:放入 `~/.pi/agent/extensions/`,在 pi 内 `/reload` 生效。

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
| `pi-codeui` | TUI 工作区增强:Git 变更面板/diff/搜索/Vim(对话优先,接近 grok-build 体验) |
| `earendil-works/pi-review` | 代码审查(/review 命令,官方) |
| `@ogulcancelik/pi-session-recall` | 历史会话回忆(session_query 工具) |

> 安装方式:`pi install`(而非 npm),pi-review 为 git 源:`pi install git:github.com/earendil-works/pi-review`;
> pi-session-recall 为 npm 源:`pi install npm:@ogulcancelik/pi-session-recall`。

## Pi 技能

Pi 通过 `settings.json` 的 `skills` 数组加载共享技能(`~/.claude/skills`、`~/.codex/skills`,
本机均为指向 `~/.agents/skills/` 的符号链接,见根目录 `skills/README.md`)。
