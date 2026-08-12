# Claude Code 插件与 MCP 配置

## 插件清单(含地址与配置方案)

### 1. claude-hud — 状态栏 HUD

- **地址**: https://github.com/jarrodwatts/claude-hud
- **用途**: 在 Claude Code 状态栏显示模型、token 用量、耗时等 HUD 信息
- **安装**:
  ```bash
  claude plugin marketplace add jarrodwatts/claude-hud
  claude plugin install claude-hud
  ```
  或在 Claude Code 内 `/plugin marketplace add jarrodwatts/claude-hud`
- **启用**: `enabledPlugins` 中 `"claude-hud@claude-hud": true`
  > 当前安装版本: **0.7.0**
- **状态栏配置**(settings.json 中 `statusLine.command`,macOS/Linux 变体):
  ```json
  "statusLine": {
    "type": "command",
    "command": "bash -c 'cols=${COLUMNS:-}; case \"$cols\" in \"\"|*[!0-9]*) cols=$(stty size </dev/tty 2>/dev/null | awk '\"'\"'{print $2}'\"'\"');; esac; case \"$cols\" in \"\"|*[!0-9]*) cols=120;; esac; export COLUMNS=$(( cols > 4 ? cols - 4 : 1 )); plugin_dir=$(ls -d \"${CLAUDE_CONFIG_DIR:-$HOME/.claude}\"/plugins/cache/*/claude-hud/*/ 2>/dev/null | awk -F/ '\"'\"'{ print $(NF-1) \"\\t\" $(0) }'\"'\"' | grep -E '\"'\"'^[0-9]+\\.[0-9]+\\.[0-9]+[[:space:]]'\"'\"' | sort -t. -k1,1n -k2,2n -k3,3n -k4,4n | tail -1 | cut -f2-); exec \"/opt/homebrew/bin/node\" \"${plugin_dir}dist/index.js\" --extra-cmd \"echo Happy coding!\"'",
    "refreshInterval": 5
  }
  ```
  > node 路径 `/opt/homebrew/bin/node` 为本机路径,新机器替换为 `which node` 的结果。
  > **Windows Git Bash 变体**(无 bash -c 包裹,用 `cygpath -m` + Windows node):
  > `cols=${COLUMNS:-}; case "$cols" in ""|*[!0-9]*) cols=$(stty size 2>/dev/null </dev/tty | awk '{print $2}');; esac; case "$cols" in ""|*[!0-9]*) cols=120;; esac; export COLUMNS=$(( cols > 4 ? cols - 4 : 1 )); plugin_dir=$(ls -1d "${CLAUDE_CONFIG_DIR:-$HOME/.claude}"/plugins/cache/*/claude-hud/*/ 2>/dev/null | sort -V | tail -1); plugin_win=$(cygpath -m "$plugin_dir"); exec "/e/Program Files/nodejs/node" "${plugin_win}dist/index.js" --extra-cmd "echo Happy coding!"`
- **自定义文案**: 命令末尾 `--extra-cmd "echo Happy coding!"` 显示自定义标签,需在 `env` 设 `CLAUDE_HUD_ALLOW_EXTRA_CMD=1` 才生效。
- **文案颜色**: `~/.claude/plugins/claude-hud/config.json` 设 `"colors": { "custom": "yellow" }`。
  > ⚠️ 0.7.0 中 extra label 默认走 `colors.label`(dim 暗色)。要**单独**给文案着色,
  > 需改插件 dist 两处 `push(label(ctx.extraLabel, colors), 'extra')` →
  > `push(customColor(ctx.extraLabel, colors), 'extra')`:
  > - `dist/render/lines/project.js`(多行布局)
  > - `dist/render/session-line.js`(单行布局)
  > **插件更新会覆盖此修改**,需重新打补丁。

### 2. claude-plugins-official — Claude 官方插件集(14 个已装)

- **地址**: https://github.com/anthropics/claude-plugins-official
- **安装**: `claude plugin marketplace add anthropics/claude-plugins-official`
- 安装方式:`claude plugin install <name>@claude-plugins-official`,或在 Claude Code 内 `/plugin install`

| 插件 | 类型 | 用途 |
|---|---|---|
| **skill-creator** | skill | 创建/改进/测评 skill |
| **claude-md-management** | skill+cmd | 维护 CLAUDE.md 质量 |
| **code-simplifier** | agent | 代码简化重构 |
| **frontend-design** | skill | 生产级前端界面设计 |
| **context7** | MCP | 文档实时查询(匿名可用) |
| **github** | MCP | 官方 GitHub MCP(需 token) |
| **playwright** | MCP | E2E 测试/浏览器自动化 |
| **serena** | MCP | 语义代码搜索 |
| **chrome-devtools-mcp** | skills(6) | 控制真实 Chrome/性能调试 |
| **typescript-lsp** | LSP | TypeScript 代码智能 |
| **pyright-lsp** | LSP | Python 代码智能 |
| **gopls-lsp** | LSP | Go 代码智能 |
| **jdtls-lsp** | LSP | Java 代码智能 |
| **security-guidance** | hooks | AI 代码安全审查(零常驻) |

> **github 插件**是远程 HTTP MCP(`https://api.githubcopilot.com/mcp/`),
> 需在 `env` 设 `GITHUB_PERSONAL_ACCESS_TOKEN`(可用 `gh auth token` 获取)。
> ⚠️ **该 token 敏感,请勿提交仓库。**
> **security-guidance** 前置:Claude Code ≥2.1.144、Python 3.8+;审查走 `ANTHROPIC_BASE_URL`。
> LSP 各自启动一个后台语言服务器进程,不用对应语言时可 `enabledPlugins` 置 false 关闭。

### 3. Codex 插件(github@openai-api-curated)

- **地址**: OpenAI 官方 API 插件(Codex 内置市场)
- **配置**: 在 `~/.codex/config.toml`:
  ```toml
  [plugins."github@openai-api-curated"]
  enabled = true
  ```
- **用途**: 使用 OpenAI API 的代码审查/质量策展功能

## MCP 服务器配置

MCP 服务器通过 cc-switch 管理(存于 cc-switch 数据库 `mcp_servers` 表),
或直接在 `~/.claude.json` 的 `mcpServers` 中声明:

```json
{
  "mcpServers": {
    "github": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-github"],
      "env": {
        "GITHUB_PERSONAL_ACCESS_TOKEN": "你的GitHubToken"
      }
    },
    "mcp-router": {
      "command": "mcpr",
      "args": ["connect"],
      "env": {
        "MCPR_TOKEN": "你的MCPRToken"
      },
      "type": "stdio"
    }
  }
}
```

| 服务器 | 方案 | 所需凭证 |
|---|---|---|
| **github** | `npx @modelcontextprotocol/server-github`(官方 GitHub MCP) | `GITHUB_PERSONAL_ACCESS_TOKEN` |
| **mcp-router** | `mcpr connect`(MCP Router 聚合器,统一管理多个 MCP) | `MCPR_TOKEN` |

> ⚠️ `github`、`context7` 已由 claude-plugins-official 插件提供,与上表手动配置**二选一**,勿重复启用。

> 凭证获取:
> - GitHub Token: https://github.com/settings/tokens(需 `repo` 权限)
> - MCPR: https://mcp-router.ai(或对应部署的管理端)

## 其他常用 MCP(可选)

| 服务器 | 地址/方案 | 说明 |
|---|---|---|
| context7 | `https://mcp.context7.com/mcp`(远程) | 库文档查询(插件已装,匿名可用) |
| gh_grep | `https://mcp.grep.app`(远程) | GitHub 代码搜索 |

远程 MCP 直接声明 URL 即可,无需本地命令:
```json
{
  "mcpServers": {
    "context7": { "type": "remote", "url": "https://mcp.context7.com/mcp" }
  }
}
```
