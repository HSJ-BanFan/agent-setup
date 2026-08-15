# 环境复刻完整性说明

本仓库的目标是**高保真复刻**,但不是 100% 字节级复制——以下明确列出
**可复刻 / 需手动 / 不可复刻** 三部分,供 AI agent 和新机器用户对照。

## ✅ 可完整复刻(仓库已包含)

| 类别 | 内容 | 复刻方式 |
|---|---|---|
| Agent 配置 | Claude Code / Codex / Pi / OpenCode 的配置模板 | 复制 + 填 key |
| DSH(DeepSeek Harness) | settings.yaml + cordis.patch.yml(3 MCP)+ 49 技能 | `dsh/install.ps1` |
| 插件 | claude-hud(含 marketplace 注册与状态栏方案) | 命令安装 |
| MCP | GitHub / mcp-router / context7 / gh_grep 方案 | 声明 + 填 token |
| 扩展 | Pi 的 3 个扩展(orca 集成) | 复制 + `/reload` |
| 技能 | 64 个共享技能(完整内容) | 复制到 `~/.agents/skills/` + 符号链接 |
| Orca | agent-hooks(12 个脚本,无敏感)+ cli 技能 + 安装说明 | 复制到 `~/.orca/agent-hooks/` |
| 基础设施 | 9router / grok2api / kiro-rs / cli-proxy-api / CPA Manager Plus / 可选 NapCat / Watchtower 部署方案 | 按 `infra/` + tool-index 部署 |
| 供应商切换 | CC-Switch 应用设置项(代理/插件集成/语言) | 按 `cc-switch/README.md` |

## ⚠️ 需手动配置(涉及密钥/账号,仓库只给模板)

| 项 | 说明 | 获取方式 |
|---|---|---|
| Codex API key | `~/.codex/auth.json` → `OPENAI_API_KEY` | 供应商控制台 |
| 网关供应商 keys | cli-proxy-api `config.yaml`、9router、grok2api、kiro-rs | 各自管理面板 |
| CC-Switch 供应商 | 在应用内重新添加(含 key) | cc-switch UI |
| MCP tokens | `GITHUB_PERSONAL_ACCESS_TOKEN`、`MCPR_TOKEN` | GitHub Settings / mcp-router 部署 |
| Claude Code 登录 | 官方账号登录或配置模型端点 | `claude` 登录 / cc-switch 切换 |
| Pi models | `~/.pi/agent/models.json` 的 apiKey | 按 `pi/models.example.json` 填写 |

## ❌ 不可复刻(个人数据/账户,换机需重新生成或迁移)

| 项 | 原因 |
|---|---|
| **各平台的登录态与订阅** | Claude/ChatGPT/Gemini/Grok 账号 session 与订阅绑定账户,不可复制 |
| **claude-mem 记忆库** | `E:\MySecondBrain\.claude-mem` 是个人知识记忆,按需手动迁移 |
| **会话历史** | 各 agent 的 sessions 历史(属于个人工作记录) |
| **Orca 工作区数据** | 应用数据目录中的 worktree/卡片/自动化实例状态 |
| **本地项目路径** | 各配置中的 `trusted projects`、工作目录需按新机器修改 |
| **环境变量(系统级)** | 如 `GGR_AGENT_*`(pi 模型路由)等,按新机器 provider 重新设置 |
| **Docker 数据卷** | 容器内积累的统计/日志/账号池数据 |
