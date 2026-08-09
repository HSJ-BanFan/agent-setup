# Agent 配置仓库 (agent-setup)

本仓库是 **AI 开发环境配置技能包**:跨机器快速复刻完整环境。
包含 4 个主要 agent 的配置、64 个共享技能、MCP/插件方案和 Docker AI 基础设施模板,
并内置**配置技能**(`SKILL.md`),让任意 AI agent(pi / opencode / Claude Code / Codex)
在陌生机器上自动引导完成配置。

> ⚠️ **安全声明**:本仓库已做脱敏处理,不含任何 API 密钥。
> 所有 `YOUR_*_KEY_HERE` / `YOUR_API_KEY` 占位符需要在新机器上替换为真实值。

## 给 AI Agent 的入口

| 文件 | 用途 |
|---|---|
| [`SKILL.md`](SKILL.md) | **配置技能主入口**:agent 读取后按流程执行 |
| [`skill/tool-index.md`](skill/tool-index.md) | **所有工具的源仓库地址索引**(安装/配置/端口) |
| [`skill/sources.json`](skill/sources.json) | 机器可读的源仓库清单 |
| [`skill/routing.md`](skill/routing.md) | 任务 → 执行路径路由矩阵 |
| [`RULES.md`](RULES.md) | 执行规则(安全/来源/顺序/平台) |
| [`AGENTS.md`](AGENTS.md) | 平台中立仓库指令 |

## 覆盖范围

| 项 | 内容 | 目录 |
|---|---|---|
| **Claude Code** | settings.json、claude-hud 插件、MCP 服务器 | [`claude-code/`](claude-code/) |
| **Codex** | config.toml、auth 模板、插件 | [`codex/`](codex/) |
| **Pi** | settings.json、models、4 个扩展、MCP、包列表 | [`pi/`](pi/) |
| **OpenCode** | opencode.jsonc(MCP 服务器) | [`opencode/`](opencode/) |
| **CC-Switch** | 供应商切换工具配置说明 | [`cc-switch/`](cc-switch/) |
| **共享技能** | 64 个跨 agent 技能 | [`skills/`](skills/) |
| **AI 基础设施** | 9router / grok2api / kiro-rs / cli-proxy-api / cpa-manager | [`infra/`](infra/) |

## 快速开始(新机器)

```bash
# 1. 克隆仓库
git clone https://github.com/<你的用户名>/agent-setup.git
cd agent-setup

# 2. 让 AI 代劳(推荐):把本仓库路径告诉你的 agent(pi/opencode/claude),
#    它会读取 SKILL.md 自动引导完成配置

# 或一键复刻(Windows)
.\setup.ps1

# 或(Linux/macOS)
./setup.sh

# 3. 按提示填入 API keys(见各目录 README)
```

> 详细步骤:每个子目录都有 `README.md`;工具来源见 [`skill/tool-index.md`](skill/tool-index.md)。

## 架构概览

```
┌─────────────────────────────────────────────────────┐
│            AI 开发环境(Claude Code / Codex /         │
│             Pi / OpenCode / CC-Switch)              │
├─────────────────────────────────────────────────────┤
│           共享技能库 ~/.agents/skills(64 个)         │
├─────────────────────────────────────────────────────┤
│     Docker AI 基础设施                              │
│  9router(20128)  grok2api(21434,免费grok)           │
│  kiro-rs(18990,本地模型)  cli-proxy-api(18318)      │
│  cpa-manager(18317)                                 │
└─────────────────────────────────────────────────────┘
```

> 基础设施各服务的源仓库、端口与部署方式见 [`skill/tool-index.md`](skill/tool-index.md) §D。
