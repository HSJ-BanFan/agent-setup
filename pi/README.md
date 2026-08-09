# Pi 配置复刻

Pi 是终端里的编程智能体(https://github.com/earendil-labs/pi-coding-agent)。

## 文件说明

| 文件 | 说明 | 敏感内容 |
|---|---|---|
| `settings.json` | 主配置:默认 provider/模型/主题/技能路径/包列表 | 无 |
| `auth.example.json` | **默认 provider(opencode-go)的 API key 模板** | ⚠️ 必填 |
| `models.example.json` | 自定义 provider 模板(ds-proxy → 本地代理) | ⚠️ apiKey 已脱敏 |
| `open-tui.json` | open-tui 包配置(状态栏段、遥测开关) | 无 |
| `mcp.example.json` | MCP 服务器模板(GitHub 等) | ⚠️ token 已脱敏 |
| `agent/extensions/` | 扩展源码(4 个) | 无(已确认无明文 key) |

## 复刻步骤

### 1. 安装 Pi(保持最新版)

```bash
npm install -g @earendil-works/pi-coding-agent   # 最新稳定版,无需固定版本
```

### 2. 复制配置

```bash
# Windows (PowerShell)
Copy-Item pi/settings.json "$env:USERPROFILE\.pi\agent\settings.json"
Copy-Item pi/auth.example.json "$env:USERPROFILE\.pi\agent\auth.json"   # 然后填入 key
Copy-Item pi/models.example.json "$env:USERPROFILE\.pi\agent\models.json"
Copy-Item pi/open-tui.json "$env:USERPROFILE\.pi\agent\open-tui.json"
Copy-Item pi/mcp.example.json "$env:USERPROFILE\.pi\agent\mcp.json"      # 按需填 token
Copy-Item pi/agent/extensions/*.ts "$env:USERPROFILE\.pi\agent\extensions\"

# Linux/macOS
mkdir -p ~/.pi/agent ~/.pi/agent/extensions
cp pi/settings.json ~/.pi/agent/settings.json
cp pi/auth.example.json ~/.pi/agent/auth.json          # 然后填入 key
cp pi/models.example.json ~/.pi/agent/models.json
cp pi/open-tui.json ~/.pi/agent/open-tui.json
cp pi/mcp.example.json ~/.pi/agent/mcp.json            # 按需填 token
cp pi/agent/extensions/*.ts ~/.pi/agent/extensions/
```

### 3. 关键:填入 auth.json(默认 provider 凭据)

`settings.json` 的 `defaultProvider` 为 `opencode-go`,其 API key 存放在 `auth.json`:

```json
{
  "opencode-go": {
    "type": "api_key",
    "key": "你的OpenCode网关key"
  }
}
```

> opencode-go 端点需要路由(https://opencode.ai/go),key 从你的 OpenCode 网关获取。

### 4. 安装包依赖(settings.json 中 packages 列表)

```bash
pi  # 首次启动时按提示安装,或手动:
pi install npm:pi-mcp-adapter pi-subagents pi-web-access context-mode @juicesharp/rpiv-todo @narumitw/pi-goal pi-simplify @narumitw/pi-plan-mode pi-open-tui
pi install git:github.com/earendil-works/pi-review
```

### 5. 配置模型

`settings.json` 默认使用 `opencode-go` provider + `deepseek-v4-flash` 模型。
`models.json` 模板包含 `ds-proxy`(本地 18318 代理),修改 `apiKey` 为你的实际值即可。

### 6. 技能

Pi 通过 `settings.json` 的 `skills` 数组加载技能(指向 `~/.claude/skills`、`~/.codex/skills`)。
这两个目录在本机是指向 `~/.agents/skills/` 的符号链接,见根目录 `skills/README.md`。
