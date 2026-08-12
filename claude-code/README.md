# Claude Code 配置复刻

本目录包含 Claude Code 的配置文件模板。API 密钥已脱敏,需要在新机器上重新配置。
> **不含代理配置**:本仓库不包含任何代理/中转端点或 token(如 `ANTHROPIC_BASE_URL` / `ANTHROPIC_AUTH_TOKEN`)。

## 文件说明

| 文件 | 说明 | 敏感内容 |
|---|---|---|
| `settings.json` | 主配置:模型、claude-hud 插件、hooks、权限、状态栏 | 无(占位路径用 `$HOME` 表达) |
| `plugins/known_marketplaces.json` | 插件市场注册(claude-hud / claude-plugins-official) | 无 |
| `plugins/installed_plugins.json` | 已安装插件清单(claude-hud 0.6.0) | 无 |

## 复刻步骤

### 1. 安装 Claude Code

```bash
npm install -g @anthropic-ai/claude-code
```

### 2. 复制配置

```bash
# Windows (PowerShell)
Copy-Item claude-code/settings.json "$env:USERPROFILE\.claude\settings.json"

# Linux/macOS
mkdir -p ~/.claude && cp claude-code/settings.json ~/.claude/settings.json
```

> `settings.json` 中的 hook/statusLine 使用 `$HOME` 表达用户目录,复制后无需改动即可在本机生效。

### 3. 安装 claude-hud 插件

```bash
claude plugin marketplace add jarrodwatts/claude-hud
claude plugin install claude-hud
```

> 或在 Claude Code 内输入 `/plugin marketplace add jarrodwatts/claude-hud` 后安装。
> 插件启用后会自动出现在 `enabledPlugins`,无需手动编辑。

### 4. 登录模型

默认使用官方账号登录即可:

```bash
claude
# 首次运行按提示 /login 授权
```

> 若需经网关/中转路由模型(如 `ANTHROPIC_BASE_URL` + `ANTHROPIC_AUTH_TOKEN`),
> 按你的方案在 `settings.json` 的 `env` 段补充,或使用 [cc-switch](../cc-switch/README.md) 自动写回。
> **本仓库默认不含代理 env,请勿提交真实端点/token。**

### 5. 启用 hooks(可选)

`settings.json` 中的 `hooks` 段包含两类:

| 来源 | 作用 | 依赖文件 |
|---|---|---|
| **CCG** | 会话上下文注入 / 技能路由 / 工作流状态 | `~/.claude/hooks/ccg/*.js`(由 CCG npm 包安装) |
| **Orca** | 向 Orca 上报 agent 事件(权限/工具调用/停止等) | `~/.orca/agent-hooks/claude-hook.sh`(由 Orca 生成) |

> 未安装对应组件时,hook 命令会自动跳过(`if [ -f ... ]` 守卫),不影响 Claude Code 运行。

### 6. 权限与安全设置

- `permissions.allow`: 白名单命令(示例含 `Bash(*codeagent-wrapper*)`)
- `skipDangerousModePermissionPrompt: true`: 危险模式免确认
- `includeCoAuthoredBy: false`: 提交不带 co-authored 署名

按需调整,不必照抄。

### 7. statusLine(claude-hud 状态栏)

`statusLine.command` 中的 node 路径 `/opt/homebrew/bin/node` 是本机路径。
新机器上若 node 不在此路径,改用 `which node` 的结果:

```bash
which node   # 复制到 command 中的 exec 路径
```

### 8. 技能(共享技能库)

Claude Code 通过符号链接引用 `~/.agents/skills/` 下的技能:

```bash
# 在仓库根目录执行 setup 脚本,或手动:
# Windows: 用 mklink /D 创建符号链接(需管理员或开发者模式)
# Linux/macOS: ln -s ~/.agents/skills/<name> ~/.claude/skills/<name>
```

详见仓库根目录 `skills/README.md` 和 `setup.ps1` / `setup.sh`。
