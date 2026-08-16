# DSH(DeepSeek Harness)配置

本目录固化当前工作机的 **DSH Web 界面完整配置**,新机/工作机可直接复刻:

| 文件 | 内容 |
|---|---|
| [install.ps1](install.ps1) | **一键安装**:配置 + 技能同步 + 预设安装 + 手动项指引 |
| [skills.ps1](skills.ps1) | 技能同步脚本(仓库 29 + packaged 4 + git 源 16 = 49 个) |
| [skills-manifest.json](skills-manifest.json) | 外部技能来源清单(机器可读) |
| [settings.yaml](settings.yaml) | 用户设置:LLM provider(opencode-go)、权限预设、默认模型 |
| [cordis.patch.yml](cordis.patch.yml) | web profile 补丁:3 个 MCP 服务器(playwright / github / devtools) |
| [presets/](presets/) | Agent 预设(router-standard / anchored-standard,直接拷入 `~/.dsh/.agent-presets/`) |
| [packaged-skills/](packaged-skills/) | 已做 DSH 适配的第三方技能(4 个) |

## 新机安装

```powershell
# 1. 安装并初始化 DSH(首次会创建 web profile)
npx @deepseek-ai/dsh web        # 浏览器打开 http://127.0.0.1:3080 后 Ctrl+C

# 2. 克隆本仓库并安装
git clone https://github.com/HSJ-BanFan/agent-setup.git
cd agent-setup
.\dsh\install.ps1
```

安装脚本会:
1. 备份并写入 ~/.dsh/settings.yaml(provider 声明,密钥走环境变量引用)
2. 备份并写入 ~/.dsh/profiles/web/cordis.patch.yml(MCP 配置)
3. 同步 49 个技能到 ~/.agents/skills(热加载,无需重启)
4. 安装预设到 ~/.dsh/.agent-presets/(router-standard / anchored-standard)
5. 输出手动项清单(API keys / GITHUB_TOKEN)

## 手动项(密钥不入库,按脚本指引)

| 项 | 方式 |
|---|---|
| OPENCODE_GO_API_KEY / DEEPSEEK_API_KEY | dsh web → 设置 → Models 页写入 |
| GITHUB_TOKEN | gh auth login → setx GITHUB_TOKEN (gh auth token)(系统环境变量) |

## MCP 服务器(由 cordis.patch.yml 声明)

| serverName | 工具前缀 | 包 | 用途 |
|---|---|---|---|
| playwright | mcp__playwright__* | @playwright/mcp | 浏览器自动化 / E2E |
| github | mcp__github__* | @modelcontextprotocol/server-github | PR / issue / 代码搜索 |
| devtools | mcp__devtools__* | chrome-devtools-mcp | 网络抓包 / 性能分析 |

> ⚠️ **宿主 HMR 在 web profile 被禁用**(官方 TODO):修改 cordis.patch.yml 后必须**重启 dsh web 进程**才生效。

## 技能构成(49 个)

- 仓库内置 29 个(../skills/,mattpocock + orca)
- packaged 4 个:claude-md-improver / claude-md-revise / context-md / context-md-update(Anthropic 官方 CLAUDE.md 管理 + amajorai/context.md,已适配 DSH 工具命名)
- git 源 16 个:emilkowalski 动效设计 6 + greensock gsap 8 + vercel find-skills + frontend-design

## 更新配置到本目录

```powershell
Copy-Item $HOME\.dsh\settings.yaml .\dsh\settings.yaml
Copy-Item $HOME\.dsh\profiles\web\cordis.patch.yml .\dsh\cordis.patch.yml
# 预设(已安装副本才是修复后最新版):
Remove-Item .\dsh\presets\* -Recurse -Force
Copy-Item $HOME\.dsh\.agent-presets\* .\dsh\presets\ -Recurse -Force
# 技能 packaged:
Copy-Item $HOME\.agents\skills\claude-md-* .\dsh\packaged-skills\ -Recurse -Force
Copy-Item $HOME\.agents\skills\context-md* .\dsh\packaged-skills\ -Recurse -Force
git add dsh && git commit -m "同步:DSH 配置" && git push
```