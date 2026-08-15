---
name: agent-env-setup
description: >
  AI 开发环境一键复刻技能。在陌生机器上通过任意 AI agent(pi / opencode / Claude Code / Codex)
  快速、智能地配置完整的 AI 编码环境:安装并配置 Claude Code、Codex、Pi、OpenCode、
  CC-Switch,部署本地 AI 基础设施(9router / grok2api / kiro-rs / cli-proxy-api / CPA Manager Plus / NapCat / Watchtower),
  接入 MCP 服务器,同步 60+ 共享技能与扩展。
  使用场景:新电脑配置、环境迁移、docker 服务搭建、MCP/插件接入。
license: MIT
---

# Agent 环境配置技能 (agent-env-setup)

本仓库是**可执行的环境配置技能包**:任何 AI agent 读取本技能后,
就能在陌生机器上引导用户完成整个 AI 开发环境的安装与配置。

## 工作流程(按顺序执行)

### 1. 先读这些

| 文件 | 用途 |
|---|---|
| `README.md` | 仓库结构总览 |
| `skill/tool-index.md` | **所有工具的源仓库地址 + 安装方式**(核心索引) |
| `skill/sources.json` | 机器可读的源仓库清单(JSON) |
| `skill/routing.md` | 用户任务 → 执行路径的路由矩阵 |
| `RULES.md` | 必须遵守的执行规则(安全/顺序/验证) |
| `ENVIRONMENT.md` | **复刻完整性说明**:可复刻 / 需手动 / 不可复刻清单 |

### 2. 判断用户意图(路由)

用户说... | 执行...
|---|---|
| "配置/复刻环境"、"换电脑" | 完整流程:识别平台 → 逐工具安装 → 配置 → 验证 |
| "安装/配置 XXX"(单工具) | 查 `skill/routing.md` 对应路径 |
| "部署 docker 服务" | 走 `infra/` 流程(9router / grok2api / kiro-rs / cli-proxy-api / CPA Manager Plus / NapCat / Watchtower) |
| "接入 MCP" | 查 `claude-code/plugins.md`、`pi/extensions.md` 的 MCP 章节;DSH 走 `dsh/cordis.patch.yml` |
| "配置/复刻 DSH(DeepSeek Harness)" | 运行 `dsh/install.ps1`(配置 + 49 技能 + MCP),按输出指引填密钥 |
| "同步技能" | 走 `skills/` 流程(复制 + 符号链接) |

### 3. 执行通用流程

对每个要安装的工具:

1. **查源**:从 `skill/tool-index.md` 获取官方源仓库地址(不猜测、不用山寨源)
2. **装工具**:按该仓库 README/文档的官方方式安装(npm / curl / docker)
3. **复制配置**:从本仓库对应目录(`claude-code/`、`codex/`、`pi/`、`opencode/`)复制配置模板
4. **填密钥**:所有 `YOUR_*_KEY` 占位符引导用户填入真实值;**密钥只写用户本机文件,绝不提交**
5. **验证**:运行该工具 `--version` 或对应验证命令确认安装成功
6. **善后**:提示用户重启相关服务 / `/reload` 扩展 / 重新登录

### 4. 验证清单(完成后逐项检查)

- [ ] `claude --version`、`codex --version`、`pi --version`、`opencode --version` 均可用
- [ ] Claude Code 能连上模型端点(cc-switch 代理或官方账号)
- [ ] `~/.claude/settings.json` 中 claude-hud 插件已启用且状态栏正常
- [ ] MCP 服务器(github / mcp-router / context7)在对应 agent 中可见
- [ ] 技能已同步:`~/.agents/skills/` 存在且各 agent 能发现
- [ ] docker 容器(如部署)全部 `Up` 状态

## 关键提示
