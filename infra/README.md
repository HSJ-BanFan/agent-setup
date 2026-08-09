# AI 基础设施(Docker)说明

本机用于 AI 开发的 Docker 容器清单。**API 密钥已脱敏,模型路由细节不在此仓库维护。**

## 容器清单

| 容器 | 端口 | 用途 |
|---|---|---|
| `9router` (9router-router) | 20128 | 模型路由网关 + Dashboard |
| `grok2api` (grok2api:local) | 21434 | Grok 免费模型池(Web SSO) |
| `kiro-rs` (zyphrzero/kiro-rs) | 18990 | 本地 Claude 兼容模型 |
| `cli-proxy-api` (eceasy/cli-proxy-api) | 18318 | CLI 统一代理(路由/配额/统计) |
| `cpa-manager` (seakee/cpa-manager) | 18317 | CPA 凭证管理器 |
| `kiro-rs-redis` (redis:7) | 6379 | kiro-rs 缓存 |

## 端口速查(供各 agent 配置引用)

| 端口 | 服务 | 调用方式 |
|---|---|---|
| `18318` | cli-proxy-api | OpenAI 兼容 `/v1/chat/completions`,`x-api-key` 认证 |
| `20128` | 9router | `/v1` OpenAI 兼容,需 API key |
| `21434` | grok2api | `/v1` OpenAI 兼容,Bearer 认证 |
| `18990` | kiro-rs | `/v1` OpenAI 兼容,Bearer 认证 |
| `15721` | cc-switch 本地代理 | Claude Code 的 ANTHROPIC_BASE_URL |

## cli-proxy-api 部署

`cliproxy/docker-compose.yml` 提供 cli-proxy-api + cpa-manager 的编排模板:

```bash
cd infra/cliproxy
# 准备 config.yaml(参考:https://github.com/eceasy/cli-proxy-api 的配置文档)
# 填入你的 provider API keys 后:
docker compose up -d
```

配置要点:
- `config.yaml` 通过 volume 挂载,provider 的 API keys 配置在其中
- 模型名前缀路由(如 `g2a/*` → grok2api、`ds/*` → DeepSeek),具体模型清单在 config.yaml 中按需维护
- 本机另需运行:9router、grok2api、kiro-rs 容器(各自独立部署,密钥存于各自环境)

## 调用示例(经 18318 代理)

```bash
curl -X POST http://localhost:18318/v1/chat/completions \
  -H "Content-Type: application/json" \
  -H "x-api-key: YOUR_PROXY_KEY" \
  -d '{"model":"g2a/grok-chat-fast","messages":[{"role":"user","content":"hi"}]}'
```

## 经验备忘

- 免费 grok 池(`grok-chat-fast`)响应 2-8s 波动大;Build 模型(grok-4.5 等)通常无可用账号
- kiro-rs 本地推理 1-3s 稳定,适合作为 fallback
- 各容器密钥:换机器需重新获取(9router 控制台 / grok2api 管理页 / kiro-rs 本地生成)
