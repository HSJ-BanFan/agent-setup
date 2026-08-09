# Orca(Agent 编排工具)配置复刻

Orca 是 **AI 代理编排桌面应用**(Agent Development Environment):
管理多个并行 agent(Claude Code / Codex / Pi / OpenCode / Gemini / Grok 等)的
worktrees、终端、仓库、自动化与内置浏览器,并提供编排层(任务 DAG、决策门)。

## 源仓库与安装

| 项 | 地址 |
|---|---|
| 源仓库 | https://github.com/stablyai/orca |
| 官网 / 文档 | https://www.onorca.dev(含 CLI 参考、编排文档) |
| 安装 | 官网下载桌面安装包(本机: `AppData/Local/Programs/orca/Orca.exe`) |

## 本目录内容

| 文件 | 说明 |
|---|---|
| `agent-hooks/` | Orca 为各 agent 自动生成的 hook 脚本(全部通过环境变量传 token,**无敏感信息**) |
| `orca-cli-skill.md` | orca-cli 技能(引导 agent 使用 orca CLI 的发现存根) |

### agent-hooks 覆盖的 agent

```
antigravity-hook.cmd + 4 个事件包装(pre/post/stop)   → Antigravity
claude-hook.cmd、claude-statusline.cmd               → Claude Code(含状态栏)
codex-hook.cmd                                       → Codex
gemini-hook.cmd                                      → Gemini CLI
grok-hook.cmd                                        → Grok
kimi-hook.sh                                         → Kimi
```

### Hook 机制说明

- Orca 启动 agent 终端时注入环境变量:`ORCA_AGENT_HOOK_PORT`(本机 hook 端口)、
  `ORCA_AGENT_HOOK_TOKEN`(会话令牌)、`ORCA_PANE_KEY`、`ORCA_AGENT_LAUNCH_TOKEN` 等
- hook 脚本把 agent 事件(会话开始/工具调用/停止等)POST 到
  `http://127.0.0.1:<PORT>/hook/<agent>`(Claude 状态栏走 `/statusline/claude`)
- **复刻时无需修改**:脚本读取环境变量,与具体机器无关,直接复制到 `~/.orca/agent-hooks/` 即可

## 复刻步骤

```bash
# 1. 安装 Orca 桌面应用(官网下载)

# 2. 复制 hooks(Windows)
Copy-Item orca/agent-hooks/* "$env:USERPROFILE\.orca\agent-hooks\"

# 3. 在 Orca 中为各 agent 创建终端/工作区,Orca 会自动挂接 hooks

# 4. (可选)Pi 扩展:Orca 管理的 pi 会话会注入 orca 扩展
#    (~/.pi/agent/extensions/orca-*.ts,见 pi/extensions.md)
```

## 相关组件

| 组件 | 位置 | 说明 |
|---|---|---|
| pi 扩展 | `pi/agent/extensions/orca-*.ts`(3 个) | Orca 与 pi 的状态同步/预填/标题栏 |
| orca-cli 技能 | `skills/orca-cli/`(共享技能库内) | agent 使用 orca CLI 的指南 |
| 编排层 | Orca 内置(orchestration run/task/dispatch) | 见 https://www.onorca.dev/docs/cli/orchestration |

> 注意:Orca 的会话/工作区数据存储在应用数据目录(不属于配置),不做复刻。
