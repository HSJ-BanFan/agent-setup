# Pi 配置复刻

Pi 是终端里的编程智能体(https://github.com/earendil-labs/pi-coding-agent)。

## 文件说明

| 文件 | 说明 | 敏感内容 |
|---|---|---|
| `settings.json` | 主配置:默认 provider/模型/主题/技能路径/包列表 | 无 |
| `models.example.json` | 自定义 provider 模板(ds-proxy → 本地代理) | ⚠️ apiKey 已脱敏 |
| `auto-session-name.example.json` | 自动命名扩展的 LLM 配置模板 | ⚠️ apiKey 已脱敏 |
| `agent/extensions/` | 扩展源码(4 个) | 无(已确认无明文 key) |

## 复刻步骤

### 1. 安装 Pi

```bash
npm install -g @earendil-works/pi-coding-agent
```

### 2. 复制配置

```bash
# Windows (PowerShell)
Copy-Item pi/settings.json "$env:USERPROFILE\.pi\agent\settings.json"
Copy-Item pi/models.example.json "$env:USERPROFILE\.pi\agent\models.json"
Copy-Item pi/agent/extensions/*.ts "$env:USERPROFILE\.pi\agent\extensions\"

# Linux/macOS
mkdir -p ~/.pi/agent ~/.pi/agent/extensions
cp pi/settings.json ~/.pi/agent/settings.json
cp pi/models.example.json ~/.pi/agent/models.json
cp pi/agent/extensions/*.ts ~/.pi/agent/extensions/
```

### 3. 安装包依赖(settings.json 中 packages 列表)

```bash
pi  # 首次启动时按提示安装,或手动:
npm install -g pi-mcp-adapter pi-subagents pi-web-access context-mode @juicesharp/rpiv-todo @narumitw/pi-goal pi-simplify @narumitw/pi-plan-mode pi-open-tui
```

### 4. 配置模型

`settings.json` 默认使用 `opencode-go` provider + `deepseek-v4-flash` 模型。
`models.json` 模板包含 `ds-proxy`(本地 18318 代理),修改 `apiKey` 为你的实际值即可。

### 5. 自动命名扩展(可选)

`agent/extensions/auto-session-name.ts` 会自动为会话生成标题。
复制 `auto-session-name.example.json` 到 `~/.pi/agent/auto-session-name.json` 并填入你的 LLM 端点:

```json
{
  "enabled": true,
  "models": [
    { "baseUrl": "http://127.0.0.1:21434", "apiKey": "YOUR_KEY", "model": "grok-chat-fast", "timeoutMs": 12000 },
    { "baseUrl": "http://127.0.0.1:18990", "apiKey": "YOUR_KEY", "model": "claude-haiku-4.5", "timeoutMs": 8000 }
  ]
}
```

> 支持多端点 fallback:优先第一个,超时/失败自动切换下一个,全部失败回退启发式截取。

### 6. 技能

Pi 通过 `settings.json` 的 `skills` 数组加载技能(指向 `~/.claude/skills`、`~/.codex/skills`)。
这两个目录在本机是指向 `~/.agents/skills/` 的符号链接,见根目录 `skills/README.md`。
