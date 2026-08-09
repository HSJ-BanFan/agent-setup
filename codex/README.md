# Codex 配置复刻

## 文件说明

| 文件 | 说明 |
|---|---|
| `config.toml` | Codex 主配置:模型、provider(anyrouter)、信任目录、沙箱、插件 |
| `auth.example.json` | 认证文件模板(含密钥字段,值需自行填写) |

## 复刻步骤

### 1. 安装 Codex

```bash
npm install -g @openai/codex
# 或参考官方文档: https://github.com/openai/codex
```

### 2. 复制配置

```bash
# Windows (PowerShell)
Copy-Item codex/config.toml "$env:USERPROFILE\.codex\config.toml"

# Linux/macOS
mkdir -p ~/.codex && cp codex/config.toml ~/.codex/config.toml
```

### 3. 配置 API Key

```bash
codex login
# 或手动创建 ~/.codex/auth.json:
```

```json
{
  "OPENAI_API_KEY": "你的API密钥"
}
```

> `config.toml` 中的 `[model_providers.custom]` 使用了 anyrouter 网关
> (`https://anyrouter.top/v1`, OpenAI 兼容)。
> 换网关只需改 `base_url` 并更新 `auth.json` 中的密钥。

### 4. 信任目录

`config.toml` 中 `[projects.*]` 段声明了可信项目目录(免除权限确认)。
按新机器的路径修改 `<USERNAME>` 或删除不需要的条目。

### 5. 模型

- 默认模型:`gpt-5.6-sol`(anyrouter 网关模型名,按需修改)
- `model_reasoning_effort = "medium"`:推理强度

### 6. 技能

Codex 会读取 `~/.codex/skills/` 下的技能。
本仓库的共享技能库在 `skills/` 目录(52 个技能),
复制或软链到 `~/.codex/skills/` 即可:

```bash
# Linux/macOS
ln -s ~/.agents/skills/* ~/.codex/skills/
# Windows
# 用 setup.ps1 脚本自动处理,或逐个 mklink
```
