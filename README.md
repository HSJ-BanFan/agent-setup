# Agent 配置仓库 (agent-setup)

本仓库用于**跨机器快速复刻 AI 开发智能体环境**,包含 4 个主要 agent 的完整配置、
52 个共享技能和 Docker AI 基础设施模板。

> ⚠️ **安全声明**:本仓库已做脱敏处理,不含任何 API 密钥。
> 所有 `YOUR_*_KEY_HERE` / `YOUR_API_KEY` 占位符需要在新机器上替换为真实值。

## 覆盖范围

| Agent | 配置内容 | 目录 |
|---|---|---|
| **Claude Code** | settings.json、插件(claude-hud 等,含地址与方案)、MCP 服务器 | [`claude-code/`](claude-code/) |
| **Codex** | config.toml(anyrouter 网关)、auth 模板、插件 | [`codex/`](codex/) |
| **Pi** | settings.json、models、扩展(含自动会话命名)、MCP、包列表 | [`pi/`](pi/) |
| **OpenCode** | opencode.jsonc(MCP 服务器) | [`opencode/`](opencode/) |
| **CC-Switch** | 供应商切换工具配置说明 | [`cc-switch/`](cc-switch/) |
| **共享技能** | 52 个跨 agent 技能(设计/开发/工具链) | [`skills/`](skills/) |
| **AI 基础设施** | Docker 容器清单 + cli-proxy-api 部署模板 | [`infra/`](infra/) |

## 快速导航

| 你想了解 | 看这里 |
|---|---|
| Claude Code 插件/ MCP 配置 | [`claude-code/plugins.md`](claude-code/plugins.md) |
| Pi 扩展 / MCP / 包 | [`pi/extensions.md`](pi/extensions.md) |
| 各工具完整复刻步骤 | 各子目录 `README.md` |

## 快速开始(新机器)

```bash
# 1. 克隆仓库
git clone https://github.com/<你的用户名>/agent-setup.git
cd agent-setup

# 2. 一键复刻(Windows)
.\setup.ps1

# 或(Linux/macOS)
./setup.sh

# 3. 按提示填入 API keys(见各目录 README)
```

> 详细步骤:每个子目录都有 `README.md`,包含该工具的安装与配置说明。

## 架构概览

```
┌─────────────────────────────────────────────────────┐
│                 你的 AI 开发环境                      │
├──────────┬──────────┬──────────┬────────────────────┤
│ Claude   │  Codex   │   Pi     │     OpenCode       │
│  Code    │          │          │                    │
├──────────┴──────────┴──────────┴────────────────────┤
│              共享技能库 ~/.agents/skills             │
│         (52 skills: 设计/开发/工具/工作流)            │
├─────────────────────────────────────────────────────┤
│          CC-Switch(供应商切换 + 本地代理)            │
├─────────────────────────────────────────────────────┤
│     Docker AI 基础设施                               │
│  9router(20128)  grok2api(21434,免费grok)           │
│  kiro-rs(18990,本地模型)  cli-proxy-api(18318)      │
└─────────────────────────────────────────────────────┘
```

## 模型路由速查

| 用途 | 端点 | 模型 | 说明 |
|---|---|---|---|
| Claude Code 主路由 | `127.0.0.1:15721`(cc-switch) | deepseek-v4-flash | 自动写回 env |
| Codex | `anyrouter.top/v1` | gpt-5.6-sol | auth.json 存 key |
| Pi 默认 | opencode-go provider | deepseek-v4-flash | settings.json |
| 会话命名(扩展) | `127.0.0.1:21434`(grok) → `18990`(kiro) | grok-chat-fast / claude-haiku-4.5 | 免费,fallback 链 |
| 免费 Grok | `127.0.0.1:21434` | grok-chat-fast | 2-8s 波动 |
| 本地模型 | `127.0.0.1:18990` | claude-haiku-4.5 等 | 1-3s 稳定 |

## 维护

- 修改配置后:更新对应目录文件 → commit → push
- 新机器复刻:clone → setup 脚本 → 填 key
- 技能更新:重新复制 `~/.agents/skills/*` 到 `skills/`
