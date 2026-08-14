# Windows 重装前开发环境与账号迁移审计

审计日期：2026-08-14（Asia/Shanghai）
设备：MECHREVO JiguangE Series GM5AR5E
当前用户：`Meiosis`

> 本文是本机敏感资产的**脱敏索引**。只记录账号标识、数量、状态、文件位置和迁移方式，不包含任何明文密码、Cookie、Token、API Key 或私钥内容。本文仍含邮箱、项目路径等隐私信息，禁止公开发布或提交到公共仓库。

## 1. 结论：满足这些条件后再重装

当前最容易造成不可逆损失的是账号凭据、未提交代码、浏览器/密码管理器恢复方式，以及散落在 C 盘用户目录里的本地配置。用户已明确选择**不迁移旧 Docker/WSL 数据**；grok2api 只保留可重新导入的账号文件。

### P0：必须完成

- [x] 将 GitHub 仓库 `HSJ-BanFan/agent-setup` 改为 Private，并再次通过 API 验证。
- [x] 从 grok2api 导出 `grok_web` 1,579、`grok_console` 1,477、`grok_build` 476，共 3,532 个可重新导入账号；已用 `age` 加密并验证。
- [x] 对 grok-register 的一致性数据库备份、自动化项目 `.env`、`mail_credentials.txt` 和 `accounts_*.txt` 加密归档。
- [x] 记录 MuMu 模拟器 1 中部落冲突助手的 QQ `1601647237`，并加密保存 580 项配置、脚本包和 APK。
- [x] 生成完整应用清单，并保存 `codex-fullflow.cmd` 与 `codex-probe.py`。
- [ ] 将 `C:\Users\Meiosis\.ssh\id_ed25519` 保存到可信密码管理器或加密离线介质；这是三个 `.age` 归档的唯一解密私钥。
- [ ] 备份所有高风险 dirty Git 仓库；其中有大量未提交、未跟踪文件，重新 clone 无法恢复。
- [ ] 备份 C 盘桌面项目与数据，尤其是 `mysql-learning`、`xianyu_data.db` 和 4 个没有远程仓库的本地 Git 项目。
- [ ] 备份 GitHub CLI/AI Agent 配置、CC-Switch 数据库，以及 Windows 用户/机器级密钥环境变量。
- [ ] 在浏览器界面手工确认密码同步、Passkey、扩展和书签；仅复制浏览器目录不能保证重装后解密 Cookie/密码。
- [ ] 将备份放在不会被格式化的外置盘或另一台机器，并至少抽查一次恢复内容。

### P1：强烈建议

- [ ] 完整或选择性备份 Claude/Codex/Gemini/Grok/Orca 的会话历史。
- [ ] 导出 Wi-Fi 配置、Windows Terminal、PowerShell Profile、VS Code 设置和扩展列表。
- [ ] 导出驱动，至少保留神舟/机械革命机型驱动和 NVIDIA 驱动安装包。
- [x] 对三个加密账号归档生成 SHA-256，并完成一次完整解密校验。
- [ ] 将加密归档和 SHA-256 清单复制到第二位置。

## 2. 审计范围与总体统计

- Windows、开发工具链、全局包管理器、VS Code 扩展、Conda 环境。
- Windows Credential Manager、Git/GitHub/Gitee、SSH、主流 AI Agent 和浏览器配置档。
- `E:\MySecondBrain`、`E:\orac_workspaces` 与 C 盘用户目录中的重点项目和 Git 工作树。
- Docker/WSL 仅做现状识别；按用户决定，不迁移旧卷、VHDX 或 Ubuntu 数据。
- 共检测到 73 个 `.git` 工作树；剔除缓存、部署目录等 4 个嵌套工作树后，主项目约 69 个。
- 共发现 91 个 `.env*`、78 个明显账号/凭据文件、20 个业务数据库。

本次已生成应用/账号清单、三个 `age` 加密归档和 Codex 脚本副本，并将 GitHub 仓库改为 Private。为导出 grok2api 账号临时启动了 Docker，完成后已停止。没有备份 Docker/WSL 数据盘，也没有把任何明文密码、Token、Cookie、API Key 或私钥写入仓库。

## 3. 机器与磁盘基线

### 硬件

| 项目 | 当前值 |
|---|---|
| 机型 | MECHREVO JiguangE Series GM5AR5E |
| CPU | Intel Core i5-12450H，8 核 12 线程 |
| 内存 | 31.7 GB |
| 独显 | NVIDIA GeForce RTX 4050 Laptop GPU，驱动 `32.0.15.8180` |
| 其他显示驱动 | GameViewer Virtual Display、MuMu Virtual Display |

### 分区

| 盘符 | 标签 | 容量 | 可用空间 | 重装风险 |
|---|---|---:|---:|---|
| C: | 系统盘 | 474.9 GB | 90.2 GB | 预计会格式化，用户目录内容必须迁移 |
| D: | 剪辑 | 512.5 GB | 442.0 GB | 不应依赖“重装不会碰数据盘”，仍需离线备份关键数据 |
| E: | workworkwork | 511.5 GB | 252.6 GB | 主要开发项目、WSL、Docker 数据都在此 |
| F: | 游戏娱乐 | 839.0 GB | 336.4 GB | 可作为临时副本，但不能替代外置/异机备份 |

四个卷当前均显示 100% BitLocker 加密，但状态为 `Protection Off` 且 `Key Protectors: None Found`。这意味着当前没有可导出的恢复保护器；不要误以为已经保存了 BitLocker 恢复密钥。若重装后重新启用保护，先把新恢复密钥保存到异机或 Microsoft 账号。

## 4. 开发软件重装清单

完整的 315 条应用记录、62 条注册表补充、242 个快捷方式目标、61 个 VS Code 扩展、8 个 Conda 环境与 33 个 npm 全局包见 `docs/installed-apps-2026-08-14.md`。

### 操作系统与基础设施

| 软件/组件 | 当前版本或状态 |
|---|---|
| Windows | Windows 11 专业版，Build 26200 |
| PowerShell | 7.6.4 |
| Git | 2.54 |
| GitHub CLI | 2.87.3 |
| Docker Engine / Compose / Desktop | 29.5.3 / 5.1.4 / 4.78 |
| WSL | Ubuntu 24.04.3，WSL 2 |
| VS Code | 1.119 |
| Orca | 1.4.180 |

### 编程语言与构建工具

| 工具 | 当前版本 |
|---|---|
| Node.js / npm / pnpm | 24.14.1 / 11.11 / 11.5.2 |
| Bun / Deno | 1.3.10 / 2.6.4 |
| Python | 3.12、3.9；uv 另管理 3.11、3.10 |
| Java / Maven | 21 / 3.9.9 |
| .NET SDK | 10 |
| Go | 1.25.4 |
| Rust | 1.97 |

### Visual Studio Build Tools

已安装两套：

- Visual Studio 生成工具 2026：18.5.11709.299
- Visual Studio 生成工具 2022：17.14.37411.7

两套都应恢复以下核心组件：MSBuild、Roslyn、C++ x86/x64 编译器、VC Redist、Windows 11 SDK 26100、CMake、测试工具、AddressSanitizer、Vcpkg、Native Desktop Core、VC Tools workload。2026 版另含 `VC.Tools.143.x86.x64` 组件组。

### Android SDK

当前路径：`C:\Users\Meiosis\AppData\Local\Android\Sdk`

已安装：

- Android Emulator 37.1.11
- Platform Tools 37.0.1
- Android Platform 35，revision 2
- `system-images;android-35;google_apis;x86_64`，revision 9
- `cmdline-tools` 与 licenses 目录

重装后应恢复 licenses，或重新接受 Android SDK license。

### AI/开发 CLI

| CLI | 当前版本/状态 |
|---|---|
| Claude Code | 2.1.231 |
| Codex | 0.147.0 |
| OpenCode | 1.18.18 |
| Gemini CLI | 0.49.0；当前 OAuth 客户端已被服务端判定不再支持 |
| DSH | 0.1.0-rc.6 |
| 9router CLI | 0.4.27 |
| Pi | 当前未安装 |
| mcpr | 当前未安装 |
| Ollama | 检测到安装痕迹，但命令当前不可用 |

仓库自身可作为重建入口：

```powershell
Set-Location 'E:\orac_workspaces\agent-setup'
.\setup.ps1
```

先安装 PowerShell、Git、语言运行时和必要编译工具，再运行 Agent 配置脚本。Docker/WSL 如有需要在后续全新安装，不作为旧数据恢复前置条件。

### Conda 环境

Conda 根目录：`E:\gongjv_yilai\anaconda`

- `base`
- `XianYu`
- `astrbot`
- `frida17`
- `ghidra-mcp`
- `hooker39`
- `mitmproxy311`
- `xhs`

不要仅复制 `envs` 目录作为唯一恢复方式。重装前应对每个仍需使用的环境执行 `conda env export --from-history`，同时保留项目 lock/requirements 文件。

### 其他全局包管理器

- Chocolatey 2.7.0：`jadx 1.5.5`、Java Runtime 8/JRE 8。
- Scoop：仅记录了一个失败状态的 `opencode`；无需按现状恢复。
- Cargo：`binwalk 3.1.0`、`rtk 0.1.0`。
- uv tool：`nano-pdf 0.2.1`。
- pipx：当前未安装。
- Bun 全局：`pptxgenjs 4.0.1`。
- pnpm 全局列表为空，且 pnpm 全局 bin 当前不在 PATH，重装时需修正。

### npm 全局包

```text
@alibaba-group/open-code-review@1.8.7
@anthropic-ai/claude-code@2.1.231
@deepseek-ai/dsh@0.1.0-rc.6
@google/gemini-cli@0.49.0
@jackwener/opencli@1.7.4
@jinzcdev/markmap-mcp-server@0.1.1
@modelcontextprotocol/server-github@2025.4.8
@modelcontextprotocol/server-sequential-thinking@2026.7.4
@musistudio/claude-code-router@2.0.0
@openai/codex@0.147.0
@quasar/cli@2.5.0
@upstash/context7-mcp@3.2.1
@z_ai/coding-helper@0.0.6
9router@0.4.27
better-sqlite3@12.6.2
chrome-devtools-mcp@0.12.1
codewhale@0.8.47
fast-context-mcp@1.4.2
firecrawl-mcp@3.20.4
gemini-cli-chinese@0.1.0
hexo-cli@4.3.2
mcp-chrome-bridge@1.0.31
mcporter@0.7.3
oh-my-codex@0.20.1
opencode-ai@1.18.18
pm2@7.0.1
pnpm@11.5.2
pptxgenjs@4.0.1
token-optimizer-mcp@2.17.0
ui-ux-pro-max-cli@2.11.0
uipro-cli@2.2.3
wrangler@4.90.0
xreach-cli@0.3.0
```

## 5. 全局账号与凭据位置

### Windows、Git 与代码托管

| 类型 | 账号标识 | 当前位置/迁移说明 |
|---|---|---|
| Windows/Microsoft | `3330876408@qq.com` | Windows Credential Manager；重装后重新登录 Microsoft 账号 |
| Git 全局身份 | `HSJ-BanFan` / `meijiahao94@gmail.com` | `C:\Users\Meiosis\.gitconfig` |
| GitHub CLI | 活动：`HSJ-BanFan`；另有 `Meilunova` | `C:\Users\Meiosis\AppData\Roaming\GitHub CLI\hosts.yml` 和 Windows Credential Manager |
| WSL GitHub CLI | `HSJ-BanFan`，HTTPS，token scopes 包含 gist/read:org/repo/workflow | WSL 的 `/home/meilunova/.config/gh/hosts.yml`；建议重装后重新 `gh auth login` |
| Windows Git Credential Manager | GitHub：`Meilunova`、`HSJ-BanFan`、`meijiahao94-cpu` | Windows Credential Manager；无法依赖文件复制恢复 |
| Gitee | `meiosis94` | Windows Credential Manager |
| SSH 文件密钥 | ED25519，公钥注释 `3330876408@qq.com` | `C:\Users\Meiosis\.ssh\id_ed25519*`；必须加密离线备份 |
| SSH Agent 密钥 | `REDpassSSHAgentKey` 及证书 | 私钥不在 `.ssh`，由 REDpass/密码管理器注入；确认其云同步和恢复方式 |
| GPG | 未检测到 `gpg` 命令或本机 GPG 私钥清单 | 无需按本次结果迁移 |

Git 使用系统级 `Git Credential Manager`。复制 `hosts.yml` 可能保留元数据，但 OAuth/token 可能失效；重装后仍要逐账号验证。

### AI Agent 与模型服务账号

| 工具 | 当前账号/方式 | 关键位置 |
|---|---|---|
| Claude Code | 官方 OAuth；实际请求经 CC-Switch `127.0.0.1:15721` | `C:\Users\Meiosis\.claude.json`、`.claude\settings.json`、`.claude\config.json` |
| CC-Switch | 本地数据库含代理/供应商配置 | `C:\Users\Meiosis\.cc-switch\cc-switch.db`、`settings.json`、`backups\`；约 189 MB |
| Codex | API key 登录；模型 `gpt-5.6-sol`；端点 `https://anyrouter.top/v1` | `C:\Users\Meiosis\.codex\config.toml`、`auth.json` |
| OpenCode | OpenCode Go 凭据 | `C:\Users\Meiosis\.config\opencode`、`C:\Users\Meiosis\.local\share\opencode\auth.json` 与数据库 |
| Gemini CLI | 活动账号 `meijiahao94@gmail.com`；OAuth 文件存在 | `C:\Users\Meiosis\.gemini\oauth_creds.json`、`google_accounts.json`、`settings.json`；当前 CLI OAuth 客户端需重新登录/升级 |
| Grok CLI | `pra_alexandresP@hotmail.com`，显示名 Timothy Floyd | `C:\Users\Meiosis\.grok\auth.json.bak*`、`config.toml`；访问令牌已过期，但备份中有刷新凭据，仍建议重新登录 |
| DSH | CPA、OpenCode Go、DeepSeek 三类凭据 | `C:\Users\Meiosis\.dsh\.credentials.yaml`、`profiles\`、`storages\` |
| Kiro | 另有 AWS SSO 缓存 | `C:\Users\Meiosis\.aws\sso\cache\kiro-auth-token.json`；服务端账号见 Kiro 项目清单 |
| Orca | Codex pane 账号、设备、E2EE、编排数据库和运行时配置 | `C:\Users\Meiosis\AppData\Roaming\orca`，约 1.58 GB；关键文件包括 `codex-pane-accounts.json`、`orca-e2ee-keypair.json`、`orchestration.db` |

Agent 数据目录体积较大：

| 目录 | 大约大小 | 建议 |
|---|---:|---|
| `C:\Users\Meiosis\.claude` | 571 MB | 完整备份可保留项目/会话历史 |
| `C:\Users\Meiosis\.codex` | 2.56 GB | `logs_2.sqlite` 约 1 GB；配置/认证必备，日志与缓存可选 |
| `C:\Users\Meiosis\.gemini` | 1.81 GB | OAuth、settings、项目历史必备，tmp/cache 可选 |
| `C:\Users\Meiosis\.grok` | 2.65 GB | auth backup、config、settings 必备，会话/插件按需 |
| `C:\Users\Meiosis\AppData\Roaming\orca` | 1.58 GB | 账号、设备、E2EE 和编排数据优先 |

### 浏览器配置档

| 浏览器 | 检测到的配置档/账号 | 数据目录 |
|---|---|---|
| Chrome | Default；`maingocdangpha13101999@gmail.com`；`nhuh72123@gmail.com` | `C:\Users\Meiosis\AppData\Local\Google\Chrome\User Data` |
| Edge | `3330876408@qq.com` | `C:\Users\Meiosis\AppData\Local\Microsoft\Edge\User Data` |
| Firefox | 2 个配置档 | `C:\Users\Meiosis\AppData\Roaming\Mozilla\Firefox` |

Cookie、浏览器密码和部分 OAuth 状态受 Windows DPAPI 保护。干净重装后，即使复制整个 User Data，也可能无法解密。优先依赖浏览器同步与官方密码导出；导出的密码 CSV 是明文，必须立即放入加密容器并在恢复后删除。

### Windows Credential Manager 中的其他开发条目

- Gemini Antigravity
- Zed：MiniMax API 端点与本地 `18318` 代理端点
- GeekGeekRun JobAgent：OpenAI 与 local-proxy
- pgAdmin4 master password
- HiveTerm session refresh token
- OneDrive 与 Microsoft SSO 条目

这些凭据不能通过 `cmdkey /list` 导出明文，也不应尝试写入报告；重装后逐项重新登录或从密码管理器恢复。

### 环境变量中的密钥名称

只记录变量名，不记录值：

- 用户级：`BIGMODEL_API_KEY`、`GITHUB_PAT_TOKEN`、`XREACH_AUTH_TOKEN`
- 机器级：`GITHUB_TOKEN`

重装前应将值从 Windows 环境变量复制到加密密码库，恢复后重新注入；不要写进仓库或普通文本备份。

### 包管理器与终端配置

- npm：`C:\Users\Meiosis\.npmrc`，当前只检测到 `registry`、`prefix`、`cache` 键。
- Docker：`C:\Users\Meiosis\.docker\config.json`，使用 `desktop` credential store，当前上下文 `desktop-linux`。
- NuGet：`C:\Users\Meiosis\AppData\Roaming\NuGet\NuGet.Config`。
- Windows Terminal：`C:\Users\Meiosis\AppData\Local\Packages\Microsoft.WindowsTerminal_8wekyb3d8bbwe\LocalState\settings.json`。
- PowerShell：`C:\Users\Meiosis\Documents\PowerShell` 和 `Documents\WindowsPowerShell`。
- VS Code：`C:\Users\Meiosis\AppData\Roaming\Code\User`，约 249 MB。
- PowerShell 历史：`C:\Users\Meiosis\AppData\Roaming\Microsoft\Windows\PowerShell\PSReadLine\ConsoleHost_history.txt`，约 1 MB；历史中可能有旧密钥，备份时应加密并审查。

## 6. grok2api：最关键迁移对象

### 当前运行部署

| 项目 | 当前值 |
|---|---|
| 容器 | `grok2api` |
| 镜像 | `grok2api:local` |
| 端口 | `21434 -> 8000` |
| 数据卷 | `grok2api_grok2api-data`，约 34.42 MB（Docker 统计）；含 media 后此前扫描约 37 MB |
| 主数据库 | 卷内 `/app/data/backend.db`，同时存在 `-wal`、`-shm` |
| 配置 | `E:\MySecondBrain\dev-workspace-data\repos\ai\tooling\grok2api\config.yaml` |
| 管理员用户名 | `admin` |
| 客户端 Key | 5 个，仅记录数量 |
| 出口节点 | 2 个 |
| 数据库健康 | 应用健康检查 `ok`；账号表可读 |

### 实时账号库摘要

| 指标 | 数量 |
|---|---:|
| 总账号 | 3,532 |
| `grok_web` | 1,579 |
| `grok_console` | 1,477 |
| `grok_build` | 476 |
| 启用 / 禁用 | 3,323 / 209 |
| `auth_status=active` | 3,532 |
| SSO / OAuth | 3,056 / 476 |
| 唯一邮箱 | 1,840 |
| 已加密主凭据 | 3,532 |
| 已加密刷新凭据 | 476 |

邮箱域名分布：

- `kovotria.dpdns.org`：2,051
- `outlook.com`：1,039
- `meilunaria.dpdns.org`：442

### 当前迁移策略：可移植账号导出

用户不迁移旧 Docker 数据，因此不再备份 `grok2api_grok2api-data` 或 `docker_data.vhdx`。项目管理 API 能按 provider 导出可重新导入的 JSON；导出过程会解密 access token、refresh token 和已配置的 Cloudflare Cookie，所以 JSON 必须立即加密。

已完成导出并核对：

| Provider | 导出数量 |
|---|---:|
| `grok_web` | 1,579 |
| `grok_console` | 1,477 |
| `grok_build` | 476 |
| **合计** | **3,532** |

加密归档：`private/encrypted/grok2api-accounts-2026-08-14.tar.age`

SHA-256：`ED268F330FC214DCABB066F44CF580D75D100E95F0353EF7CC75BF0A32E48803`

### 项目目录里的旧数据

- `E:\MySecondBrain\dev-workspace-data\repos\ai\tooling\grok2api\data\accounts.db`：约 1,295 个旧 token 账号。
- `...\data\backend.db`：约 200 个早期迁移账号。
- `...\backups\20260727-171415\`：包含历史配置、数据库和 bootstrap 管理凭据文件，应按敏感数据备份。
- Git 工作树：4 个 tracked 改动、10 个 untracked、2 个 stash。

旧库不是当前 3,532 账号实时库的替代品；如果保留，仅作为历史追溯和去重材料，并应加密。

### 已执行的导出与加密流程

1. 临时启动 Docker Desktop 和 `grok2api`。
2. 使用 `POST /api/admin/v1/auth/login` 获取短期管理员 access token。
3. 分别请求 `GET /api/admin/v1/accounts/export?provider=...`。
4. 同时核对 JSON 内账号数组数量与 `X-Exported-Accounts` 响应头。
5. 将三个 JSON、`MANIFEST.txt` 和 `SHA256SUMS.txt` 打包。
6. 使用 SSH ED25519 公钥接收者通过 `age 1.3.1` 加密。
7. 用对应私钥完整解密并比较 tar SHA-256。
8. 删除全部临时明文，并停止 `grok2api` 与 Docker Desktop。

项目目录仍有未提交改动和 stash；若这些代码需要保留，应按 Git 工作树章节单独处理，但不再复制旧 Docker 数据。

### 恢复验证

- 新部署 grok2api 后，分别导入三个 provider JSON；不依赖旧 `credentialEncryptionKey`。
- 核对账号总数 3,532，以及 `grok_web` 1,579、`grok_console` 1,477、`grok_build` 476。
- 重新创建客户端 key 和出口节点配置；它们不在账号导出 JSON 中。
- 用一个低风险测试账号执行实际请求，确认凭据可用。

## 7. 其他账号型项目与数据库

### 9router

根目录：`E:\MySecondBrain\dev-workspace-data\projects\automation\tooling\fan_dai\9router`

当前数据库：`data\db\data.sqlite`

- 21 个供应商连接，9 个调用 key，1 个 provider node，10 个 combo。
- 当前供应商连接：Gemini 11 个全启用；OpenRouter 3 个全禁用；另有 DeepSeek、GLM CN、NVIDIA、OpenCode Go、Xiaomi TokenPlan 及一个 Anthropic-compatible 节点；Cline 当前禁用。
- 当前调用历史 76,593 条。
- 当前数据库 `PRAGMA quick_check` 报 34 条 `Page ... never used`。
- 最新通过 `quick_check` 的备份：`data\db\backups\schema-0-to-1-0.5.30-20260711-121536\data.sqlite`，时间 2026-07-11 20:15:38。
- 该干净备份有 25 个供应商连接、9 个 key、2 个 node、10 个 combo、70,172 条调用历史；它与当前业务状态不同，不能直接无脑覆盖。

迁移时应同时保留：

- 当前 `data.sqlite`、`data.sqlite-wal`、`data.sqlite-shm`
- 最新干净备份及所有历史备份
- `data\auth\cli-secret`
- `data\machine-id`
- `data\mitm\rootCA.key` 与证书；CA 私钥必须按最高敏感级别保存
- 整个 `data\` 目录和 `docker-compose.yml`

恢复前应先复制数据库，在副本上评估 `.recover`/重建索引；不要拿 2026-07-11 备份直接覆盖当前库。

### grok-register

存在两套不同用途的数据：

1. 账号管理应用：`E:\MySecondBrain\dev-workspace-data\repos\ai\tooling\grok\grok-register`
   - 主库 `data\grok.db`，同时存在 WAL/SHM。
   - 197 个基础邮箱账号、782 个别名。
   - 954 次注册：637 成功、313 失败，其余为其他状态。
   - 634 个 SSO 身份。
   - 一致性数据库备份已通过 `PRAGMA integrity_check`，并进入 `private/encrypted/grok-register-credentials-2026-08-14.tar.age`。
   - 浏览器自动化配置档未纳入本次账号包；重装后应通过邮箱凭据/refresh token 重新建立登录态。
   - Git：13 tracked、1 untracked、10 stash。

2. 批量注册脚本：`E:\MySecondBrain\dev-workspace-data\repos\automation\tooling\grok-register`
   - `mail_credentials.txt` 有 235 条邮箱凭据。
   - 多个 `accounts_*.txt`、`.env`、`config.json`。
   - 实际 `.env`、`mail_credentials.txt` 与 10 个 `accounts_*.txt` 已和数据库一起加密。
   - 基础邮箱、782 个别名及这些文本中提取的邮箱标识见 `private/account-identifiers-2026-08-14.md`。

加密归档 SHA-256：`F0158514C340B942F2807039170EC532CD2463603F801F87ECA81C91DD065D9B`。

### Kiro-RS

- 15 个账号：10 个 IdC、5 个 social。
- 12 个启用、3 个禁用。
- 5 个客户端 key。
- 关键文件：`data\credentials.json`、`data\client_api_keys.json`、`data\config.json`、`data\traces.db`。
- Docker 当前绑定的是 `E:\MySecondBrain\dev-workspace\projects\automation\tooling\kiro-rs`，同时在 `dev-workspace-data\projects\automation\tooling\kiro-rs` 看到镜像路径。恢复前需确认哪一份是权威数据，不要只备份其中一个。
- Redis 卷 `kiro-rs_redis-data` 当前仅约 264 B，但仍可一起导出。

### CLIProxyAPI 与 CPA Manager

根目录：`E:\MySecondBrain\dev-workspace-data\projects\automation\tooling\fan_dai\cliproxy`

- 当前 `auth\` 目录只有日志。
- `auth.bak\` 有 3 个 Antigravity 和 3 个 Codex Plus 凭据，涉及：
  - `maingocdangpha13101999@gmail.com`
  - `meijiahao94@gmail.com`
  - `nhuh72123@gmail.com`
- 这些备份令牌已经过期，迁移价值主要是账号映射；重装后大概率需要重新登录。
- 必备文件：`config.yaml`、全部配置备份、`auth\`、`auth.bak\`、`plugins\`、`plugins\usage-statistics\usage.db`。
- CPA Manager 数据卷：`cliproxy_cpa-manager-data`，约 193.5 MB。

### 其他项目

| 项目 | 账号/数据摘要 | 必备位置 |
|---|---|---|
| chatgpt2api | 1 个账号 | `E:\MySecondBrain\dev-workspace-data\repos\ai\api\chatgpt2api` 的运行数据、配置与数据库 |
| gemini-balance | 日志中出现 12 个不同 API key | `...\projects\ai\tooling\gemini-balance\.env.sqlite`、`data\default_db.sqlite3` |
| gpt-load | 11 个 API key | `...\fan_dai\gpt-load\.env`、`data\gpt-load.db` |
| 闲鱼自动回复 | Cookie 账号 ID `4190178269`、`2219801763568`；1 个本地管理员 | `...\xian_yu\xianyu-auto-reply` 的 data/config/.env，以及桌面 `xianyu_data.db` |
| AI-Goofish | `mei.json` 中 17 个 Cookie，采集于 2026-04-28 | Docker 绑定的 `E:\MySecondBrain\dev-workspace\projects\automation\cli\yun_ying\xian_yu\ai-goofish-monitor` 整目录 |
| Cloudflare | 账号 `3330876408@qq.com` | Cloudflare Tunnel、项目 `.env`/配置和浏览器账号；重装后验证 Tunnel token |
| NapCat | 匿名卷含完整 QQ 登录态和消息数据库 | 匿名卷 `e304af...b944`，约 1.756 GB；另备份 `...\AsrtBot\napcat\data` 与 AstrBot plugin_data |
| Blog/Solace | 管理员 `admin` / `meijiahao94@gmail.com`；含 Cloudflare Tunnel、PostgreSQL、图床、GitHub 凭据 | `E:\MySecondBrain\Blog`，尤其 `.env*`、`config.personal.toml`、`config\`、`uploads\` |
| OutlookEmailPlus | 当前数据库 0 账号；`.env` 有 Microsoft 客户端与管理密码 | `...\repos\automation\cli\outlookEmailPlus\.env`、`data\`、`.runtime\`、`plugins\` |
| FrciblyK12 | 当前账号数据库 0 账号 | `...\repos\automation\tooling\FrciblyK12\data` 与实际 `.env` |
| Odysseus | 2 个模型端点，0 个邮箱账号 | 项目 `data\`、`logs\`、`.env`、SSH/HuggingFace 缓存；Docker 绑定路径使用 `dev-workspace` |
| Gemini API | 1 个 Cookie 缓存文件 | `E:\MySecondBrain\dev-workspace-data\repos\ai\api\gemini-api` 的运行数据 |
| MuMuAINovel | settings 表中有 API key | `...\repos\ai\tooling\MuMuAINovel` 的后端数据库与实际 `.env` |
| MySQL 学习环境 | Docker 绑定的本地 MySQL data；约 3.617 GB；有本地 root 密码文件 | `C:\Users\Meiosis\Desktop\mysql-learning`，重装 C 盘会直接删除 |

## 8. Docker 资产（仅记录，不迁移旧数据）

用户已明确放弃旧 Docker 卷、绑定数据和 91.26 GB 数据盘。下表只用于说明原机器曾运行哪些服务；重装后按需要全新部署。

### 当前关键卷

| Docker 卷 | 大约大小 | 内容（仅审计参考） |
|---|---:|---|
| `grok2api_grok2api-data` | 34.42 MB | 账号已改用可移植 JSON 导出 |
| `grok2api_quality_guard_state` | 7.4 KB | 放弃 |
| `cliproxy_cpa-manager-data` | 193.5 MB | 放弃，重装后重建 |
| `e304af...b944` | 1.756 GB | NapCat QQ 登录态；按用户决定放弃 |
| `blog_postgres-data` | 65.83 MB | 放弃 |
| `blog_postgres_data` | 48.78 MB | 放弃 |
| `aitoearn_mongodb-data` | 245 MB | 放弃 |
| `aitoearn_rustfs-data` | 1.434 MB | 放弃 |
| `aitoearn_redis-data` | 4.38 KB | 放弃 |
| `kiro-rs_redis-data` | 264 B | 可重建 |
| `odysseus_chromadb-data` | 0 B | 可重建 |
| `odysseus_searxng-data` | 168 B | 可重建 |
| `odysseus_ntfy-cache` | 0 B | 可重建 |

还存在 `n8n_data`、旧的 `grok2api-data`、`grok2api_warp-data` 和若干匿名卷；均不纳入本次迁移。Docker Desktop 数据盘 `E:\docker\wsl\data\DockerDesktopWSL\disk\docker_data.vhdx` 也不复制。

## 9. WSL（仅记录，不迁移旧发行版）

| 项目 | 当前值 |
|---|---|
| 发行版 | Ubuntu 24.04.3，用户 `meilunova` |
| VHDX | `E:\WSL\Ubuntu\ext4.vhdx`，约 5.75 GB |
| 旧备份 | `E:\WSLBackup\Ubuntu-backup-20260429.tar`，约 1.82 GB，已过时 |
| Node/npm | 22.22.2 / 10.9.7 |
| Git/gh | 2.43 / 2.45 |
| Python | 3.12.3 |
| Git 全局身份 | 未设置 |
| GitHub CLI | `HSJ-BanFan` 已登录 |
| SSH 文件 | WSL `~/.ssh` 未发现文件 |

不导出 `ext4.vhdx` 或 Ubuntu tar。重装后如仍需要 WSL，直接安装新的 Ubuntu，并重新配置 Git、Node、Python 与 GitHub CLI。Docker WSL 集成旧值 `Ubuntu-20.04` 不再迁移。

## 10. 不能依赖重新 clone 的 Git 工作树

### E 盘高风险仓库

| 仓库 | tracked 改动 | untracked | stash |
|---|---:|---:|---:|
| `E:\MySecondBrain\dev-workspace-data\repos\geekgeekrun` | 2 | 298 | 0 |
| `...\projects\automation\cli\yun_ying\wechat.backup-20260616-pre-filter-repo` | 99 | 15 | 0 |
| `...\projects\ai\tooling\everything-claude-code` | 78 | 1 | 0 |
| `...\projects\automation\cli\zi_dong_hua\x` | 41 | 6 | 0 |
| `...\repos\recruiting\scraper\get_jobs` | 22 | 21 | 0 |
| `...\projects\automation\tooling\wechat_app\huasj\hsj` | 20 | 19 | 1 |
| `...\repos\ai\tooling\image-forge` | 19 | 8 | 0 |
| `...\repos\ai\content-agent\AiToEarn` | 17 | 9 | 0 |
| `...\repos\ai\tooling\grok\grok-register` | 13 | 1 | 10 |
| `...\repos\ai\tooling\grok2api` | 4 | 10 | 2 |

推荐至少做两份：

1. 直接归档整个仓库目录，包括 `.git`、stash、untracked 文件。
2. 在确认不含密钥后，将应长期保留的工作提交到私有远程。

不要用 `git clean`、`git reset --hard` 或重新 clone 来“整理”这些目录。

### C 盘无远程仓库项目

| 仓库 | tracked 改动 | untracked | 远程 |
|---|---:|---:|---|
| `C:\Users\Meiosis\Desktop\fastapi` | 0 | 2 | 无 |
| `C:\Users\Meiosis\Desktop\terraria.wiki` | 0 | 3 | 无 |
| `C:\Users\Meiosis\Desktop\Python-Learning-Lab` | 1 | 3 | 无 |
| `C:\Users\Meiosis\Desktop\terra-agent` | 2 | 2 | 无 |

这些仓库在系统盘上且没有远程，必须完整复制目录。

## 11. C 盘必须迁出的数据

除标准的 Desktop/Documents/Downloads 外，当前明确发现：

- `C:\Users\Meiosis\Desktop\mysql-learning`：约 3.617 GB，230 个文件；含 MySQL 数据目录、SQL、Kettle、notebooks、日志、`.mysql_root_pass.txt`。
- `C:\Users\Meiosis\Desktop\xianyu_data.db`：约 2.9 MB。
- 桌面 4 个无远程 Git 项目，见上一节。
- `C:\Users\Meiosis\Desktop\安卓逆向`、`简历-知识`、`闲鱼商品`、`word`、`ying` 等非仓库目录。
- `C:\Users\Meiosis\Documents\Cline`、`Codex`、`PowerShell`、`Navicat`、`pastemd`、`Simple Sticky Notes`。
- `C:\Users\Meiosis\.ssh`、`.gitconfig`、`.npmrc`、`.docker`、`.aws`、`.cc-switch` 和各 AI Agent 目录。
- `AppData\Roaming\Code\User`、GitHub CLI、Orca、Firefox、NuGet。
- `AppData\Local` 下 Chrome、Edge、Android SDK、Windows Terminal、CC-Switch WebView 数据。

桌面 `codex-fullflow.cmd` 及其依赖 `C:\Users\Meiosis\codex-probe.py` 已复制到本仓库 `scripts/`。源文件 SHA-256 分别为 `0FBCC93C3D45A90F8C1A9B0559D6F80A5AE4AD9579186E28E0AF7D8187E362CB` 与 `40103B9E467E5C0802DC7B097D91BE622D63F72E054EC1E0C706C1332F9A8087`。

MuMu 模拟器 1 的整个 17.4 GB 数据盘不迁移；部落冲突助手所需 QQ、580 项配置、脚本包和 APK 已单独加密为 `private/encrypted/mumu-coc-assistant-2026-08-14.tar.age`。

## 12. 浏览器、Passkey、Wi-Fi 与系统账号的手工动作

### 浏览器

- [ ] Chrome、Edge、Firefox 分别确认同步已完成。
- [ ] 导出书签。
- [ ] 密码若未云同步，使用浏览器官方导出；明文 CSV 立即加密。
- [ ] 检查 Passkey 所属平台。很多 Passkey 不能导出，只能依赖 Google/Microsoft/密码管理器同步或站点恢复码。
- [ ] 保存 GitHub、Google、Microsoft、Cloudflare 等账号的 2FA 恢复码。
- [ ] 记录关键扩展，尤其是密码管理器、代理、开发者工具。
- [ ] 不把 Cookie 复制视为可靠迁移方案；关键服务应准备重新登录。

### Wi-Fi

检测到 12 个 WLAN 配置档，包括 `33514`、`33514_5G`、`JXUTCM*`、`HUAWEI-R1G5AF*`、`CMCC-AB` 等。

如需导出包含密码的 XML：

```powershell
netsh wlan export profile key=clear folder='X:\reinstall-backup-2026-08-14\wifi'
```

该导出包含明文 Wi-Fi 密码，必须放入加密介质，恢复后及时删除。

### 驱动

```powershell
pnputil /export-driver * 'X:\reinstall-backup-2026-08-14\drivers'
```

优先保留网卡、芯片组、NVIDIA、触控板、声卡，以及 GameViewer/MuMu 虚拟显示驱动的安装来源。

## 13. 建议的备份目录结构

```text
reinstall-backup-2026-08-14/
├─ manifest/
│  ├─ SHA256.csv
│  └─ restore-notes.md
├─ c-drive-user-data/
├─ agent-configs/
├─ browser-exports/
├─ git-worktrees/
├─ private-encrypted/
│  ├─ grok2api-accounts-2026-08-14.tar.age
│  ├─ grok-register-credentials-2026-08-14.tar.age
│  └─ mumu-coc-assistant-2026-08-14.tar.age
├─ project-databases/
├─ wifi/
└─ drivers/
```

生成校验清单：

```powershell
$ReinstallRoot = 'X:\reinstall-backup-2026-08-14'
Get-ChildItem -LiteralPath $ReinstallRoot -File -Recurse |
  Get-FileHash -Algorithm SHA256 |
  Export-Csv -NoTypeInformation -Encoding UTF8 (Join-Path $ReinstallRoot 'manifest\SHA256.csv')
```

至少随机验证：三个 `age` 归档能用目标 SSH 私钥解密、grok2api 数量正确、`grok.db` `integrity_check` 为 `ok`、MuMu 配置哈希一致、两个 Git 仓库能打开历史、SSH 公私钥成对。

## 14. 重装后的恢复顺序

1. Windows 更新、芯片组/网卡/NVIDIA/MuMu 虚拟显示驱动、PowerShell、Git。
2. 先恢复密码管理器或离线介质中的 `id_ed25519`，验证其指纹，再克隆本 Private 仓库。
3. 依据 `docs/installed-apps-2026-08-14.md` 安装 Node/Python/Java/.NET/Go/Rust、Build Tools、Android SDK、编辑器与日常应用。
4. 运行本仓库 `setup.ps1` 恢复 Claude/Codex/OpenCode/Orca 等脱敏配置模板。
5. 逐账号重新登录 GitHub、Microsoft、Google、Grok、QQ、浏览器和 AI Agent。
6. 如仍需要 Docker/WSL，安装全新环境，不导入旧卷/VHDX/Ubuntu。
7. 新部署 grok2api，解密并分别导入三个 provider JSON，核对总数 3,532。
8. 安装 MuMu 与助手 APK，恢复加密包中的配置并核对 QQ `1601647237`。
9. 恢复 Git 工作树与 C 盘项目，确认 untracked/stash 数量。
10. 恢复浏览器同步、Passkey/2FA、Wi-Fi；普通缓存最后重建。

## 15. 恢复后验收

- `git --version`、`gh auth status`、`ssh -T git@github.com`
- `node -v`、`npm -v`、`pnpm -v`、`bun -v`、`deno --version`
- `py -0p`、`uv python list --only-installed`、`conda env list`
- `java -version`、`mvn -v`、`dotnet --info`、`go version`、`rustc -V`
- `age --version`；用恢复后的 SSH 私钥解密三个归档并核对 SHA-256。
- grok2api：总数 3,532；`grok_web` 1,579、`grok_console` 1,477、`grok_build` 476；实际推理请求成功。
- grok-register：基础账号 197、别名 782、`PRAGMA integrity_check` 返回 `ok`。
- MuMu：助手版本 711.0、QQ `1601647237`、两个配置文件 SHA-256 一致。
- 如重新安装 Docker/WSL，只验证新环境本身，不检查旧卷或旧发行版数据。
- Chrome/Edge/Firefox：书签、密码、扩展、同步状态与关键站点登录。

## 16. 已知异常与本次审计副作用

- pnpm 全局 bin 不在 PATH。
- Pi、mcpr 当前缺失。
- Ollama 有安装痕迹但命令不可用。
- Gemini CLI 当前 OAuth 客户端不再受支持，需要升级或重新登录。
- 9router 当前数据库有 SQLite 一致性警告，应在重装前另行修复/重建副本。
- 为导出 grok2api 可移植账号临时启动了 Docker Desktop；导出、加密、解密校验后已停止 `grok2api` 和 Docker Desktop。
- 在 WSL 中查询 `code --version` 时意外触发了一次 VS Code Server 更新；未回滚，其余审计操作为只读。

## 附录 A：VS Code 扩展

```text
aaron-bond.better-comments@3.0.2
adpyke.codesnap@1.3.4
anthropic.claude-code@2.1.226
bierner.markdown-mermaid@1.32.1
charliermarsh.ruff@2026.70.0
christian-kohler.path-intellisense@2.10.0
coastermcgee.word-theme@1.3.6
danielpinto8zz6.c-cpp-compile-run@1.0.92
dracula-theme.theme-dracula@2.25.1
eamodio.gitlens@18.3.0
esbenp.prettier-vscode@12.4.0
firefox-devtools.vscode-firefox-debug@2.15.0
formulahendry.code-runner@0.12.2
formulahendry.dotnet-test-explorer@0.7.8
franneck94.c-cpp-runner@9.5.0
github.vscode-github-actions@0.32.3
golang.go@0.56.0
gruntfuggly.todo-tree@0.0.226
kevinrose.vsc-python-indent@1.21.0
lurek-st.vscode-docx-editor@1.2.3
mechatroner.rainbow-csv@3.24.1
mescius.spreadjs-xlsx-editor@19.1.5
mhutchie.git-graph@1.30.0
ms-azuretools.vscode-containers@2.4.5
ms-azuretools.vscode-docker@2.0.0
ms-ceintl.vscode-language-pack-zh-hans@1.118.2026052020
ms-dotnettools.csdevkit@3.20.199
ms-dotnettools.csharp@2.140.9
ms-dotnettools.vscode-dotnet-runtime@3.1.0
ms-kubernetes-tools.vscode-kubernetes-tools@1.4.1
ms-python.debugpy@2026.6.0
ms-python.python@2026.4.0
ms-python.vscode-pylance@2026.3.1
ms-toolsai.jupyter@2025.9.1
ms-toolsai.jupyter-keymap@1.1.2
ms-toolsai.jupyter-renderers@1.3.0
ms-toolsai.vscode-jupyter-cell-tags@0.1.9
ms-toolsai.vscode-jupyter-slideshow@0.1.6
ms-vscode-remote.remote-containers@0.466.0
ms-vscode-remote.remote-wsl@0.104.3
ms-vscode.cmake-tools@1.23.52
ms-vscode.cpp-devtools@0.5.13
ms-vscode.cpptools@1.33.6
ms-vscode.cpptools-extension-pack@1.5.1
ms-vscode.cpptools-themes@2.0.0
ms-vscode.powershell@2025.4.0
mtxr.sqltools@0.28.6
nilssoderman.batch-runner@1.4.0
njpwerner.autodocstring@0.6.1
openai.chatgpt@26.803.41515
pkief.material-icon-theme@5.37.0
redhat.vscode-yaml@1.24.0
ritwickdey.liveserver@5.7.10
shd101wyy.markdown-preview-enhanced@0.8.30
streetsidesoftware.code-spell-checker@4.5.6
tomoki1207.pdf@1.2.2
usernamehw.errorlens@3.28.0
vadimcn.vscode-lldb@1.12.2
vue.volar@3.3.9
yzhang.markdown-all-in-one@3.6.3
zhuangtongfa.material-theme@3.19.0
```
