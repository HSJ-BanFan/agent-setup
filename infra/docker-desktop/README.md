# Docker Desktop 基础设施编排

面向 Windows Docker Desktop 的脱敏模板，默认启动 grok2api、CLIProxyAPI、CPA Manager Plus 和标签隔离的 Watchtower；NapCat 与 Redis 通过 Compose profile 按需启用。

## 部署前准备

1. 确认 Docker Desktop 已运行，且待用端口没有被另一套 WSL Docker Engine 占用。
2. 创建 `config/grok2api/config.yaml` 与 `config/cli-proxy-api/config.yaml`，按各官方仓库文档填写；真实密钥不得提交。
3. 若从另一套 Docker 迁移，先停止源容器再复制 bind mount/volume 数据，尤其不要同时启动同一 QQ 会话的两个 NapCat。

## 启动

```powershell
Set-Location infra\docker-desktop

# AI 网关 + Watchtower
docker compose up -d

# 同时启用 NapCat
docker compose --profile qq up -d

# 同时启用 NapCat 与 Redis
docker compose --profile qq --profile cache up -d
```

端口：

| 服务 | 地址/端口 |
|---|---|
| grok2api | `http://127.0.0.1:21434` |
| CLIProxyAPI | `http://127.0.0.1:18318` |
| CPA Manager Plus | `http://127.0.0.1:18317` |
| NapCat WebUI / OneBot | `http://127.0.0.1:6099` |
| Redis（可选） | `127.0.0.1:6379` |

AstrBot 在另一个 Docker Desktop Compose 项目中时，可通过 `host.docker.internal:6099` 访问 NapCat；NapCat 反向 WebSocket 可指向 AstrBot 发布到宿主机的端口。

## 自动更新

- grok2api、CLIProxyAPI、CPA Manager Plus 同时设置 `pull_policy: always` 和 Watchtower 标签。
- Watchtower 只处理 `desktop-ai` scope 且明确启用标签的容器，每天 04:00 UTC 检查，滚动重启并清理旧镜像。
- NapCat、Redis 和本地构建镜像默认不自动更新，避免账号会话或本地修改被无提示替换。
- Docker socket 等同于 Docker Engine 管理权限；只运行可信 Watchtower 镜像，不要把 socket 暴露给普通业务容器。

手动立即更新：

```powershell
docker compose pull
docker compose up -d --remove-orphans
```

可选 Telegram 通知：

```powershell
Copy-Item .env.example .env
# 在 .env 写入新 Bot Token/Chat ID 后：
docker compose -f compose.yaml -f compose.notify.yaml up -d watchtower
```

Token 若曾进入日志、终端录屏或聊天记录，应立即在 BotFather 轮换。

## 验证与回滚

```powershell
docker compose ps
curl.exe -I http://127.0.0.1:21434/
curl.exe -I http://127.0.0.1:18317/
curl.exe -I http://127.0.0.1:18318/
docker logs --tail 50 watchtower-desktop
```

若迁移验证失败，先执行 `docker compose down` 释放端口，再启动原 Engine 中保留的容器。不要在确认数据完整前删除源容器或源数据目录。
