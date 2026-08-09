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
- **启用**: 安装后自动出现在 `~/.claude/settings.json` 的 `enabledPlugins`:
  ```json
  "enabledPlugins": { "claude-hud@claude-hud": true }
  ```
- **状态栏配置**(settings.json 中 `statusLine.command`):
  ```json
  "statusLine": {
    "type": "command",
    "command": "cols=${COLUMNS:-}; case \"$cols\" in \"\"|*[!0-9]*) cols=$(stty size 2>/dev/null </dev/tty | awk '{print $2}');; esac; case \"$cols\" in \"\"|*[!0-9]*) cols=120;; esac; export COLUMNS=$(( cols > 4 ? cols - 4 : 1 )); plugin_dir=$(ls -1d \"${CLAUDE_CONFIG_DIR:-$HOME/.claude}\"/plugins/cache/*/claude-hud/*/ 2>/dev/null | sort -V | tail -1); plugin_win=$(cygpath -m \"$plugin_dir\"); exec \"<NODE路径>\" \"${plugin_win}dist/index.js\"",
    "refreshInterval": 5
  }
  ```
  > `<NODE路径>` 替换为本机 node 路径(`which node` 查看;Windows Git Bash 下如 `/e/Program Files/nodejs/node`)

### 2. claude-plugins-official — Claude 官方插件集

- **地址**: https://github.com/anthropics/claude-plugins-official
- **用途**: 官方插件市场(含 claude-code-setup 等)
- **安装**:
  ```bash
  claude plugin marketplace add anthropics/claude-plugins-official
  ```

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

> 凭证获取:
> - GitHub Token: https://github.com/settings/tokens(需 `repo` 权限)
> - MCPR: https://mcp-router.ai(或对应部署的管理端)

## 其他常用 MCP(可选)

| 服务器 | 地址/方案 | 说明 |
|---|---|---|
| context7 | `https://mcp.context7.com/mcp`(远程) | 库文档查询 |
| gh_grep | `https://mcp.grep.app`(远程) | GitHub 代码搜索 |

远程 MCP 直接声明 URL 即可,无需本地命令:
```json
{
  "mcpServers": {
    "context7": { "type": "remote", "url": "https://mcp.context7.com/mcp" }
  }
}
```
