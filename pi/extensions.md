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
| `pi-goal-list-loop-audit` | 自主目标控制台:面试式目标 + 审计队列 + 永续循环(替代 @narumitw/pi-goal) |
| `pi-simplify` | 简化输出 |
| `@narumitw/pi-plan-mode` | 计划模式 |
| `pi-open-tui` | TUI 增强(header/footer 计量) |
| `pi-hashline-edit-pro` | 哈希锚定 read/replace(3 字符哈希、碰撞解决、撤销) |
| `pi-rtk-optimizer` | 读压缩 + 源码过滤 + 命令重写(上下文优化) |
| `@ff-labs/pi-fff` | FFF 模糊文件/内容搜索 |
| `@vigolium/piolium` | 多阶段安全审计(子代理/隔离上下文) |
| `@plannotator/pi-extension` | 交互式计划批注审查(/plan 批注、代码/PR 审查) |
| `pi-lens` | LSP 诊断/类型检查/ast-grep 结构规则/依赖图(编辑后自动反馈) |
| `earendil-works/pi-review` | 代码审查(/review 命令,官方) |
| `@quintinshaw/pi-dynamic-workflows` | 动态工作流:fan-out 子代理/模型路由/worktree 隔离/记账,TUI + /deep-research 等 5 个工作流 |

> 安装方式:`pi install`(而非 npm),pi-review 为 git 源:`pi install git:github.com/earendil-works/pi-review`。

## Pi 技能

Pi 通过 `settings.json` 的 `skills` 数组加载共享技能(`~/.claude/skills`、`~/.codex/skills`,
本机均为指向 `~/.agents/skills/` 的符号链接,见根目录 `skills/README.md`)。
