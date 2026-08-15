# 任务路由矩阵 (Routing)

AI agent 按此矩阵把用户请求映射到本仓库的具体文件与执行路径。

## 用户任务 → 执行路径

| 用户说... | 路由到 | 执行动作 |
|---|---|---|
| "复刻/配置整个环境"、"换新电脑" | `SKILL.md` 工作流程 + `setup.ps1` / `setup.sh` | 全流程:识别平台 → 逐工具安装 → 配置 → 验证 |
| "安装 Claude Code" | `skill/tool-index.md` §A + `claude-code/README.md` | npm 全局安装 → 复制 settings.json → 配置模型端点 |
| "安装 Codex" | `skill/tool-index.md` §A + `codex/README.md` | npm 安装 → 复制 config.toml → 引导填 auth.json |
| "安装 Pi" | `skill/tool-index.md` §A + `pi/README.md` | npm 安装 → 复制 settings/models/扩展 → /reload |
| "安装 OpenCode" | `skill/tool-index.md` §A + `opencode/README.md` | 官方脚本安装 → 复制 opencode.jsonc → auth login |
| "配置 CC-Switch" | `cc-switch/README.md` | 安装 → 添加供应商 → 确认代理/插件集成开关 |
| "安装/配置 Orca" | `skill/tool-index.md` §A + `orca/README.md` | 官网安装 → 复制 hooks 到 `~/.orca/agent-hooks/` → 在 Orca 中建 agent 终端 |
| "复制 Orca hooks" | `orca/agent-hooks/` | 直接复制(无敏感信息,环境变量传 token) |
| "装 claude-hud" | `skill/tool-index.md` §B + `claude-code/plugins.md` | marketplace add → plugin install → 验证状态栏 |
| "接 MCP(GitHub/context7...)" | `skill/tool-index.md` §C + `claude-code/plugins.md`、`pi/extensions.md` | 按对应 agent 的 mcpServers 声明,引导填 token |
| "部署 9router/grok2api/kiro-rs/cli-proxy-api/cpa/NapCat/Watchtower" | `skill/tool-index.md` §D + `infra/README.md`、`infra/docker-desktop/`、`infra/cliproxy/docker-compose.yml` | docker compose / 官方部署 → 配置密钥 → 验证端口与自动更新 scope |
| "同步/安装技能" | `skills/README.md` | 复制到 `~/.agents/skills/` → 为各 agent 建符号链接 |
| "我的 agent 连不上模型" | `RULES.md` + 各 agent README 的"配置模型端点"章节 | 检查代理端口/环境变量/密钥 |

## 执行优先级(遇到冲突时)

1. **安全第一**:不写真实密钥进仓库、先备份再覆盖、不改用户未要求的配置
2. **官方源优先**:安装一律用 `tool-index.md` 中的官方源仓库
3. **验证闭环**:每个工具装完必须验证(`--version` / 端口连通 / 配置生效)
4. **最小干预**:能复制模板解决的不手写;能脚本解决的不逐步执行

## 平台分支

| 平台 | 脚本 | 符号链接方式 | 注意 |
|---|---|---|---|
| Windows | `setup.ps1`(PowerShell) | `mklink /D`(需管理员/开发者模式),失败退化为复制 | Git Bash 下 node 路径用 `which node` 获取 |
| Linux/macOS | `setup.sh` | `ln -s` | GitHub 拉取失败时提示配置代理 |

## 验证命令速查

```bash
claude --version          # Claude Code
codex --version           # Codex
pi --version              # Pi
opencode --version        # OpenCode
docker ps                 # 基础设施容器状态
curl -s http://127.0.0.1:20128/   # 9router dashboard
curl -s http://127.0.0.1:18318/v1/models -H "x-api-key: YOUR_KEY"  # cli-proxy-api
```
