# OpenCode 配置复刻

OpenCode(https://opencode.ai)是终端 AI 编码助手。

## 文件说明

| 文件 | 说明 | 敏感内容 |
|---|---|---|
| `opencode.jsonc` | 全局配置:模型 provider(OpenCode Go,占位 key)、远程 MCP(context7、gh_grep) | ⚠️ `apiKey` 为占位符,需替换为真实 key |

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

### 3. 配置模型 provider(重要)

`opencode.jsonc` 中的 `provider.opencode-go` 是 OpenAI 兼容网关(OpenCode Go)。
把 `apiKey` 占位符替换为你的真实 key:

```jsonc
"options": {
  "baseURL": "https://opencode.ai/zen/go/v1",
  "apiKey": "你的真实key"        // 替换 YOUR_OPENCODE_API_KEY
}
```

> **安全**:真实 key 仅存在于本地,勿提交到仓库。
> 也可用 `opencode auth login` 选择其他 provider(如官方 OpenAI/Anthropic)。

### 4. MCP 服务器

配置中注册了两个远程 MCP:
- `context7` — 库文档查询
- `gh_grep` — GitHub 代码搜索

两者均为公共远程服务,无需本地配置。项目级 MCP 配置在项目内的 `.opencode/` 或 `.mcp.json`。
