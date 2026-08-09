# OpenCode 配置复刻

OpenCode(https://opencode.ai)是终端 AI 编码助手。

## 文件说明

| 文件 | 说明 | 敏感内容 |
|---|---|---|
| `opencode.jsonc` | 全局配置:MCP 服务器(context7、gh_grep) | 无 |

## 复刻步骤

### 1. 安装 OpenCode

```bash
# 参考官方文档: https://opencode.ai/docs
curl -fsSL https://opencode.ai/install | bash
# 或: npm install -g opencode-ai
```

### 2. 复制配置

```bash
# Windows: 配置目录在 %USERPROFILE%\.config\opencode\
Copy-Item opencode/opencode.jsonc "$env:USERPROFILE\.config\opencode\opencode.jsonc"

# Linux/macOS
mkdir -p ~/.config/opencode
cp opencode/opencode.jsonc ~/.config/opencode/opencode.jsonc
```

### 3. 登录模型提供商

```bash
opencode auth login
# 选择你的 provider(如 OpenAI 兼容网关),填入 API key
```

### 4. MCP 服务器

配置中注册了两个远程 MCP:
- `context7` — 库文档查询
- `gh_grep` — GitHub 代码搜索

两者均为公共远程服务,无需本地配置。项目级 MCP 配置在项目内的 `.opencode/` 或 `.mcp.json`。
