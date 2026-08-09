# 工具源仓库索引 (Tool Index)

本文件是本仓库的**核心索引**:列出复刻 AI 开发环境所需的全部工具的**官方源仓库地址**、
安装方式、端口与配置要点。AI agent 在陌生机器上配置时,以此为准获取来源,
**不使用未经验证的第三方镜像/山寨源**。

> 约定:`{HOME}` = 用户主目录。所有密钥字段在仓库中为 `YOUR_*_KEY_HERE` 占位。

## A. AI 编码 Agent 工具

| 工具 | 源仓库 | 安装 | 配置位置 | 备注 |
|---|---|---|---|---|
| **Claude Code** | https://github.com/anthropics/claude-code | `npm install -g @anthropic-ai/claude-code` | `{HOME}/.claude/settings.json`、`{HOME}/.claude.json` | 官方 CLI;本仓库 `claude-code/` |
| **Codex** | https://github.com/openai/codex | `npm install -g @openai/codex` | `{HOME}/.codex/config.toml`、`auth.json` | OpenAI 官方;本仓库 `codex/` |
| **Pi** | https://github.com/earendil-works/pi | `npm install -g @earendil-works/pi-coding-agent` | `{HOME}/.pi/agent/settings.json`、`models.json` | 终端编码框架;本仓库 `pi/` |
| **OpenCode** | https://github.com/sst/opencode | `curl -fsSL https://opencode.ai/install \| bash` 或 `npm i -g opencode-ai` | `{HOME}/.config/opencode/opencode.jsonc` | 官网 opencode.ai;本仓库 `opencode/` |
| **CC-Switch** | https://github.com/farion1231/cc-switch | 官网 ccswitch.io 下载桌面安装包 | `{HOME}/.cc-switch/`(settings.json + SQLite) | 多 agent 供应商切换;本仓库 `cc-switch/` |

## B. 插件 / 扩展 / 技能源

| 工具 | 源仓库 | 安装方式 | 说明 |
|---|---|---|---|
| **claude-hud** | https://github.com/jarrodwatts/claude-hud | `claude plugin marketplace add jarrodwatts/claude-hud` | Claude Code 状态栏 HUD |
| **claude-plugins-official** | https://github.com/anthropics/claude-plugins-official | `claude plugin marketplace add anthropics/claude-plugins-official` | Claude 官方插件集 |
| **Anthropic Skills** | https://github.com/anthropics/skills | clone 后复制 `skills/*` 到 `{HOME}/.agents/skills/` | 官方技能库(pdf/docx/xlsx/pptx/webapp-testing 等) |
| **Pi 扩展(自研)** | 本仓库 `pi/agent/extensions/` | 复制到 `{HOME}/.pi/agent/extensions/` 后 `/reload` | auto-session-name(会话自动命名)等 4 个 |
| **共享技能库** | 本仓库 `skills/`(64 个技能) | 复制到 `{HOME}/.agents/skills/`,各 agent 符号链接引用 | 详见 `skills/README.md` |

## C. MCP 服务器源

| MCP | 源仓库 / 地址 | 配置方式 | 所需凭证 |
|---|---|---|---|
| **GitHub MCP** | https://github.com/modelcontextprotocol/servers | `npx -y @modelcontextprotocol/server-github` | `GITHUB_PERSONAL_ACCESS_TOKEN`(GitHub Settings → Tokens,`repo` 权限) |
| **MCP Router (mcpr)** | 按部署环境(mcp-router 服务端) | `mcpr connect`(stdio) | `MCPR_TOKEN` |
| **context7** | https://github.com/upstash/context7(公共端点 mcp.context7.com) | 远程 MCP:`{"type":"remote","url":"https://mcp.context7.com/mcp"}` | 无 |
| **gh_grep** | https://mcp.grep.app(公共端点) | 远程 MCP:`{"type":"remote","url":"https://mcp.grep.app"}` | 无 |

> MCP 声明位置:Claude Code → `{HOME}/.claude.json` 的 `mcpServers`;
> Pi → `{HOME}/.pi/agent/mcp.json`;OpenCode → `opencode.jsonc` 的 `mcp`。
> 完整示例见 `claude-code/plugins.md` 与 `pi/extensions.md`。

## D. AI 基础设施(Docker / 网关)

| 服务 | 源仓库 | 部署方式 | 端口 | 用途 |
|---|---|---|---|---|
| **9router** | https://github.com/decolua/9router | `npm install -g 9router` 或 Docker(`9router-router` 镜像) | **20128**(dashboard) | 免费 AI 路由网关:连接 40+ 供应商,RTK 省 token,自动 fallback |
| **grok2api** | https://github.com/chenyme/grok2api | Docker(`grok2api:local`,宿主机 **21434** → 容器 8000) | **21434** | 免费 Grok 模型池(Web SSO 多账号),OpenAI 兼容 |
| **kiro-rs** | https://github.com/ZyphrZero/kiro.rs | Docker(`zyphrzero/kiro-rs`,宿主机 **18990** → 容器 8990) | **18990** | 本地 Claude 兼容代理(Rust),1-3s 稳定,适合 fallback |
| **cli-proxy-api** | https://github.com/router-for-me/CLIProxyAPI | Docker(`eceasy/cli-proxy-api`,宿主机 **18318** → 容器 8317),compose 见本仓库 `infra/cliproxy/` | **18318** | CLI 统一代理:模型前缀路由、配额、用量统计、冷却 |
| **cpa-manager** | https://github.com/seakee/CPA-Manager | Docker(`seakee/cpa-manager`,宿主机 **18317**) | **18317** | CPA 凭证管理 WebUI(基于 cli-proxy-api) |
| **kiro-rs-redis** | https://hub.docker.com/_/redis | Docker(`redis:7-alpine`) | 6379 | kiro-rs 缓存(内部) |

### 基础设施调用速查(OpenAI 兼容)

| 端点 | 认证 | 说明 |
|---|---|---|
| `http://127.0.0.1:18318/v1/chat/completions` | `x-api-key` | cli-proxy-api,模型名前缀路由(如 `g2a/grok-chat-fast`、`ds/deepseek-v4-flash`) |
| `http://127.0.0.1:21434/v1/chat/completions` | `Bearer` | grok2api 直连 |
| `http://127.0.0.1:18990/v1/chat/completions` | `Bearer` | kiro-rs 直连 |
| `http://127.0.0.1:20128/v1` | `x-api-key` | 9router |

## E. 密钥存放位置(复刻时引导用户填写)

| 密钥 | 存放文件 | 说明 |
|---|---|---|
| OpenAI/网关 key | `{HOME}/.codex/auth.json` → `OPENAI_API_KEY` | Codex 用 |
| cli-proxy-api 各 provider key | `infra/cliproxy/config.yaml`(挂载进容器) | 网关上游 |
| grok2api key | grok2api 管理面板(容器内) | 免费池访问 |
| kiro-rs key | kiro-rs 配置(容器内) | 本地推理 |
| cc-switch 供应商 key | `{HOME}/.cc-switch/cc-switch.db` | 应用内添加 |
| GITHUB_TOKEN / MCPR_TOKEN | 各 agent 的 mcpServers env | MCP 认证 |

## 更新维护

- 新增工具时:在本文件 + `sources.json` 同步登记
- 源仓库地址变更:及时更新,避免 agent 使用过期/山寨源
