# Claude Code 配置复刻

本目录包含 Claude Code 的配置文件模板。API 密钥已脱敏,需要在新机器上重新配置。

## 文件说明

| 文件 | 说明 | 敏感内容 |
|---|---|---|
| `settings.json` | 主配置:环境变量(模型映射)、claude-hud 插件、主题 | ⚠️ 需按新环境调整 |
| `plugins/known_marketplaces.json` | 插件市场注册(claude-hud) | 无 |
| `plugins/installed_plugins.json` | 已安装插件清单 | 无 |

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

### 3. 安装 claude-hud 插件

```bash
claude plugin marketplace add jarrodwatts/claude-hud
claude plugin install claude-hud
```

> 或在 Claude Code 内输入 `/plugin marketplace add jarrodwatts/claude-hud` 后安装。
> 插件启用后会自动出现在 `enabledPlugins`,无需手动编辑。

### 4. 配置模型端点(重要)

`settings.json` 中的 `env` 段按你的模型路由方案调整:

```json
"env": {
  "ANTHROPIC_BASE_URL": "http://127.0.0.1:15721",   // cc-switch 本地代理(或你的中转地址)
  "ANTHROPIC_AUTH_TOKEN": "PROXY_MANAGED",          // cc-switch 托管时自动写入
  "ANTHROPIC_DEFAULT_OPUS_MODEL_NAME": "deepseek-v4-flash"  // 模型映射
}
```

- **使用 cc-switch**:启动 cc-switch → 添加 Claude provider → 切换,它会自动写回 env
- **使用官方账号**:删除 `env` 段,运行 `claude` 登录官方账号
- **直连中转**:把 `ANTHROPIC_BASE_URL` 和 `ANTHROPIC_AUTH_TOKEN` 改成你的中转配置

### 5. statusLine(claude-hud 状态栏)

`statusLine.command` 中的 node 路径 `"/e/Program Files/nodejs/node"` 是本机路径。
新机器上若 node 不在该路径,改用 `node` 命令或更新路径:

```bash
# 查看 node 路径
which node   # Windows Git Bash 下
```

### 6. 技能(共享技能库)

Claude Code 通过符号链接引用 `~/.agents/skills/` 下的技能:

```bash
# 在仓库根目录执行 setup 脚本,或手动:
# Windows: 用 mklink /D 创建符号链接(需管理员或开发者模式)
# Linux/macOS: ln -s ~/.agents/skills/<name> ~/.claude/skills/<name>
```

详见仓库根目录 `skills/README.md` 和 `setup.ps1` / `setup.sh`。
