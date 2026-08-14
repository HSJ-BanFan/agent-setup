# 私有迁移资料

本目录只适合当前 **Private** 仓库。账号标识文档含真实邮箱和 QQ；`encrypted/` 中的归档还包含密码、Refresh Token、SSO、Cookie 或应用配置，因此禁止将仓库改回 Public。

## 加密接收者

- 算法/工具：`age 1.3.1`
- 接收者：`C:\Users\Meiosis\.ssh\id_ed25519.pub`
- SSH 公钥指纹：`SHA256:3r/wJnK813DZ8H6Poj8y+mXOi9+kyRBwa64aau//ivM`
- 公钥注释：`3330876408@qq.com`

当前对应私钥 `C:\Users\Meiosis\.ssh\id_ed25519` 可用空口令读取。它**没有进入 Git**，但也因此必须在重装前放入可信密码管理器或加密离线介质。私钥一旦丢失，下面的 `.age` 文件无法恢复。

## 加密归档

| 文件 | 内容 | 大小 | SHA-256 |
|---|---|---:|---|
| `grok2api-accounts-2026-08-14.tar.age` | 可重新导入的 grok_web 1,579、grok_console 1,477、grok_build 476，共 3,532 个账号 | 2,221,796 bytes | `ED268F330FC214DCABB066F44CF580D75D100E95F0353EF7CC75BF0A32E48803` |
| `grok-register-credentials-2026-08-14.tar.age` | 一致性备份的 `grok.db`、自动化项目 `.env`、`mail_credentials.txt` 与 `accounts_*.txt` | 1,084,884 bytes | `F0158514C340B942F2807039170EC532CD2463603F801F87ECA81C91DD065D9B` |
| `mumu-coc-assistant-2026-08-14.tar.age` | 部落冲突助手 QQ/580 项配置、脚本包、入口文件和 APK | 47,390,196 bytes | `C66280B4F42CC36A3A51FBE5538711FF9E70A41E145710AD532458C276F6E7FD` |

三个归档均已使用对应 SSH 私钥做过完整解密，并比较了解密前后的 tar SHA-256；临时明文目录已经清除。

## 解密

只在可信机器的空目录中操作：

```powershell
age -d -i "$env:USERPROFILE\.ssh\id_ed25519" `
  -o .\payload.tar `
  .\private\encrypted\grok2api-accounts-2026-08-14.tar.age

tar -tf .\payload.tar
New-Item -ItemType Directory -Path .\private\decrypted -Force
tar -xf .\payload.tar -C .\private\decrypted
```

解密后先核对归档内的 `SHA256SUMS.txt` 与 `MANIFEST.txt`。完成导入后删除 `payload.tar` 和 `private/decrypted`，不要提交它们。

## grok2api 恢复

管理后台的账号导入功能可直接读三个 JSON。先部署一个全新的 grok2api，再按 provider 分别导入，并核对数量：

- `grok_web`：1,579
- `grok_console`：1,477
- `grok_build`：476

这些是便携导出，不依赖旧 Docker 卷或旧 `credentialEncryptionKey`。

## MuMu 恢复

1. 安装 MuMu 和归档内的助手 APK，启动助手一次后退出。
2. 通过 root/ADB 放回 `account-settings.config`、`main.config`、`entry.json` 和脚本包。
3. 恢复正确属主/权限后启动助手。
4. 核对 QQ `1601647237`、切号时间 `30` 与配置文件 SHA-256。
