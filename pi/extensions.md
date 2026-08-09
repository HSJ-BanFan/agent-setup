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

## Pi 包(Packages)— 常驻 6 个

`settings.json` 中 `packages` 列表(全部为 npm 包,地址即包名):

| 包 | 功能 |
|---|---|
| `pi-mcp-adapter` | MCP 适配 |
| `pi-subagents` | 子代理 |
| `context-mode` | 上下文管理模式 |
| `pi-hashline-edit-pro` | 哈希锚定 read/replace(3 字符哈希、碰撞解决、撤销) |
| `earendil-works/pi-review` | 代码审查(/review,官方) |
| `pi-open-tui` | TUI 增强(header/footer/editor) |

> 安装方式:`pi install`(而非 npm)。pi-review 为 git 源:
> `pi install git:github.com/earendil-works/pi-review`。
>
> **精简原则**:仅常驻这 6 个,重型工具按需 `pi -e <package>` 临时加载
> (如安全审计 `pi -e npm:@vigolium/piolium`、动态工作流 `pi -e npm:@quintinshaw/pi-dynamic-workflows`)。

## Pi 技能

Pi 通过 `settings.json` 的 `skills` 数组加载共享技能(`~/.claude/skills`、`~/.codex/skills`,
本机均为指向 `~/.agents/skills/` 的符号链接,见根目录 `skills/README.md`)。
