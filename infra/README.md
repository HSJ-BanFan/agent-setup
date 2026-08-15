# AI 基础设施(Docker)说明

本机用于 AI 开发的 Docker 容器清单。**API 密钥已脱敏,模型路由细节不在此仓库维护。**

## 容器清单

| 容器 | 端口 | 用途 |
|---|---|---|
| `9router` (9router-router) | 20128 | 模型路由网关 + Dashboard |
| `grok2api` (ghcr.io/chenyme/grok2api) | 21434 | Grok 免费模型池(Web SSO) |
| `kiro-rs` (zyphrzero/kiro-rs) | 18990 | 本地 Claude 兼容模型 |
| `cli-proxy-api` (eceasy/cli-proxy-api) | 18318 | CLI 统一代理(路由/配额/统计) |
| `cpa-manager-plus` (seakee/cpa-manager-plus) | 18317 | CPA 凭证管理器与用量面板 |
| `kiro-rs-redis` (redis:7) | 6379 | kiro-rs 缓存 |
| `napcat` (mlikiowa/napcat-docker,可选) | 6099 | QQ / OneBot WebUI 与接口 |
| `watchtower` (containrrr/watchtower) | 无 | 标签隔离的容器自动更新 |

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

> 此文件保留旧版 `cpa-manager` 兼容部署；新建 Docker Desktop 环境优先使用 `docker-desktop/` 中的 CPA Manager Plus。

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

## Docker Desktop 一体化部署

Windows Docker Desktop 用户优先使用 [`docker-desktop/`](docker-desktop/)：它包含 grok2api、CLIProxyAPI、CPA Manager Plus、可选 NapCat/Redis，以及标签隔离的 Watchtower 自动更新模板。真实配置和数据均在该目录的 ignored 路径中，不进入 Git。

若 WSL 原生 Docker 已占用相同端口，必须先停止源容器再切换；保留源数据，验证 Desktop 正常后再决定是否清理。

## 自动更新

- Compose 启动时通过 `pull_policy: always` 获取最新发布镜像。
- Watchtower 仅更新带 `com.centurylinklabs.watchtower.enable=true` 且 scope 匹配的容器。
- NapCat、Redis 和本地构建镜像默认手动更新，避免账号状态或本地代码被静默替换。

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
