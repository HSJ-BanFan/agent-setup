# CC-Switch 配置复刻

CC-Switch 是多 API 供应商切换工具,统一管理 Claude Code / Codex / Gemini 等智能体的模型供应商。

> ⚠️ 本目录不包含任何 API 密钥。供应商的密钥存储在 cc-switch 本地数据库中
> (`~/.cc-switch/cc-switch.db`),换机器后需重新添加。

## 应用设置(建议保持一致)

`~/.cc-switch/settings.json` 关键项:

| 设置 | 本机值 | 说明 |
|---|---|---|
| `enableClaudePluginIntegration` | `true` | 启用 Claude 插件集成(自动写入 Claude Code 的 env) |
| `enableLocalProxy` | `true` | 本地代理(默认端口 15721),Claude Code 通过它访问供应商 |
| `language` | `zh` | 界面语言 |
| `launchOnStartup` / `silentStartup` | `true` | 开机自启 |
| `skillSyncMethod` | `auto` | 技能自动同步 |

## 供应商结构(新机器需重新添加)

本机的供应商配置结构(不含密钥):

### Claude Code(app_type: claude)

| 供应商 | 端点 | 说明 |
|---|---|---|
| (claude providers 已清空) | - | 按需重新添加 |

### Codex(app_type: codex)

| 供应商 | 端点 | 说明 |
|---|---|---|
| OpenAI Official | chatgpt.com | 官方 |
| 9router | 本地 20128 | 本地路由网关 |
| any | https://anyrouter.top | 聚合网关 |
| AIHub | https://aihub.top | 聚合网关 |

### Gemini / GrokBuild / OpenCode

- Gemini: google 官方(`gemini-official`)
- GrokBuild: `default` / Grok Official
- OpenCode: `OpenCode Go`(https://opencode.ai/go,需路由)

## 复刻步骤

1. 安装 CC-Switch(Windows: https://github.com/farion1231/cc-switch 下载安装)
2. 启动后逐个添加供应商:
   - 供应商类型选对应用(Claude Code / Codex / Gemini ...)
   - 填入端点 URL 和 API key(与旧机器相同的 key,或新 key)
3. 设置 → 确认 `enableClaudePluginIntegration`、`enableLocalProxy` 开启
4. 切换到你需要的供应商,cc-switch 会自动写回对应 agent 的配置(如 Claude Code 的 `~/.claude/settings.json` env)
