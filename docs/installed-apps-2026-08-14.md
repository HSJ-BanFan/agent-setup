# 已安装应用与开发工具清单

生成时间：2026-08-14 21:12:00 +08:00（Asia/Shanghai）

数据源：WinGet 结构化清单、Windows 卸载注册表、开始菜单/桌面快捷方式、VS Code、Conda、npm。

> 用途：Windows 重装后对照下载和恢复。本文不包含许可证密钥、密码、Token、Cookie 或会话数据。版本只是重装前快照；重装时优先安装官方最新稳定版，只有兼容性需要时才固定旧版本。

## 汇总

- WinGet/ARP/MSIX/Steam 识别记录：315
- 注册表额外记录：62
- 开始菜单/桌面有效快捷方式目标：242
- VS Code 扩展：61
- Conda 环境：8
- npm 全局包：33

## 建议优先恢复的开发软件

| 应用 | 当前版本 | 包 ID / 来源 |
|---|---|---|
| Anaconda3 | 2025.06-0 | `Anaconda.Anaconda3` / winget |
| Apifox | 2.8.40 | `Ruihu.Apifox` / winget |
| Bun | Unknown | `ARP\User\X64\Bun` / 传统安装器 |
| Bun | 1.3.13 | `Oven-sh.Bun` / winget |
| Burp Suite | 2026.6 | `PortSwigger.BurpSuite` / winget |
| CC Switch | 3.19.2 | `farion1231.CC-Switch` / winget |
| Charles Proxy | 5.0.3.1 | `XK72.Charles` / winget |
| ChatGPT | 26.803.10989.0 | `MSIX\OpenAI.Codex_26.803.10989.0_x64__2p2nqsd0c76g0` / MSIX/Store |
| Clash Verge | 2.5.2 | `ARP\Machine\X64\Clash Verge` / 传统安装器 |
| Claude | 1.10628.2.0 | `Anthropic.Claude` / winget |
| Claude Code | 2.1.147 | `Anthropic.ClaudeCode` / winget |
| CMake | 4.1.0 | `Kitware.CMake` / winget |
| Cockpit Tools | 0.24.12 | `ARP\User\X64\Cockpit Tools` / 传统安装器 |
| cURL | 8.15.0.4 | `cURL.cURL` / winget |
| DBeaver | 26.1.3 | `DBeaver.DBeaver.Community` / winget |
| Deno | 2.6.4 | `DenoLand.Deno` / winget |
| Docker Desktop | 4.78.0 | `Docker.DockerDesktop` / winget |
| FFmpeg for yt-dlp | N-121938-g2456a39581-20251130 | `yt-dlp.FFmpeg` / winget |
| Git | 2.54.0 | `Git.Git` / winget |
| GitHub CLI | 2.87.3 | `GitHub.cli` / winget |
| Go Programming Language | 1.25.4 | `GoLang.Go` / winget |
| ImageMagick Q16-HDRI | 7.1.2.21 | `ImageMagick.ImageMagick` / winget |
| jq | 1.8.1 | `jqlang.jq` / winget |
| Microsoft .NET SDK 10.0 | 10.0.100 | `Microsoft.DotNet.SDK.10` / winget |
| Microsoft .NET SDK 8.0 | 8.0.423 | `Microsoft.DotNet.SDK.8` / winget |
| Microsoft .NET SDK 9.0.302 (x64) from Visual Studio | 9.3.225.31907 | `ARP\Machine\X64\{118C0ABF-1A67-42FC-AE66-7453FA3C86A2}` / 传统安装器 |
| Microsoft Build of OpenJDK with Hotspot 21 | 21.0.10.7 | `Microsoft.OpenJDK.21` / winget |
| Microsoft Visual Studio 2010 Tools for Office Runtime | 10.0.60833 | `Microsoft.VSTOR` / winget |
| Microsoft Visual Studio Code | 1.119.0 | `Microsoft.VisualStudioCode` / winget |
| Microsoft Visual Studio Installer | 4.7.25.22189 | `ARP\Machine\X64\{6F320B93-EE3C-4826-85E0-ADF79F8D4C61}` / 传统安装器 |
| MSYS2 | 20250622 | `ARP\User\X64\{f0665201-936e-4822-b65d-90a43cccc5ff}` / 传统安装器 |
| Node.js (LTS) | 24.14.1 | `OpenJS.NodeJS.LTS` / winget |
| Orca | 1.4.180 | `StablyAI.Orca` / winget |
| PowerShell | 7.6.4.0 | `Microsoft.PowerShell` / winget |
| Python 3.12 | 3.12.10 | `Python.Python.3.12` / winget |
| Python Launcher | 3.12.10 | `Python.Launcher` / winget |
| Rustup: the Rust toolchain installer | 1.29.0 | `Rustlang.Rustup` / winget |
| Ubuntu 20.04 LTS | 2004.6.17.0 | `Canonical.Ubuntu.2004` / winget |
| Visual Studio 生成工具 2026 | 18.5.0 | `ARP\Machine\X86\173ec20e` / 传统安装器 |
| Visual Studio BuildTools 2022 | < 17.14.37 | `Microsoft.VisualStudio.2022.BuildTools` / winget |
| Visual Studio Code | 1.0.118.1 | `MSIX\Microsoft.VisualStudioCode_1.0.118.1_neutral__8wekyb3d8bbwe` / MSIX/Store |
| Visual Studio Community 2022 | 17.14.10 | `Microsoft.VisualStudio.2022.Community` / winget |
| Windows Subsystem for Linux | 2.7.3.0 | `Microsoft.WSL` / winget |
| Windows Subsystem for Linux Update | 5.10.16 | `ARP\Machine\X64\{36EF257E-21D5-44F7-8451-07923A8C465E}` / 传统安装器 |
| Windows Terminal | 1.24.11911.0 | `Microsoft.WindowsTerminal` / winget |
| WinSCP 6.5.3 | 6.5.3 | `ARP\User\X64\winscp3_is1` / 传统安装器 |
| YARA | 4.5.5 | `VirusTotal.YARA` / winget |
| yt-dlp | 2025.12.08 | `yt-dlp.yt-dlp` / winget |
| Zed | 1.0.0.0 | `MSIX\ZedIndustries.Zed_1.0.0.0_neutral__japxn1gcva8rg` / MSIX/Store |
| Zed | 1.13.1 | `ZedIndustries.Zed` / winget |

安装顺序建议：Git/PowerShell/Terminal → 语言运行时与包管理器 → 编译工具链 → 编辑器/数据库/API 工具 → AI Agent 与代理工具。Docker/WSL 只需重装软件本体，不恢复旧数据盘或发行版数据。

## 可能需要重新登录的应用

- 百度网盘（8.3.10）
- 豆包（2.20.9）
- 适用于 Game Bar 的 Microsoft Edge（1.0.4019.0）
- 网易云音乐（3.1.37.205354）
- 微信输入法（2.1.1.8）
- Apifox（2.8.40）
- CC Switch（3.19.2）
- ChatGPT（26.803.10989.0）
- Claude（1.10628.2.0）
- Claude Code（2.1.147）
- DBeaver（26.1.3）
- Docker Desktop（4.78.0）
- GitHub CLI（2.87.3）
- Google Chrome（151.0.7922.138）
- Microsoft 365 Copilot（19.2607.61021.0）
- Microsoft Edge（151.0.4129.78）
- Microsoft Office LTSC 专业增强版 2024 - zh-cn（16.0.17932.20910）
- Microsoft OneDrive（26.139.0720.0007）
- Microsoft Visual Studio 2010 Tools for Office Runtime（10.0.60833）
- Mozilla Firefox (x64 zh-CN)（153.0.3）
- OneDrive（26139.720.7.0）
- Orca（1.4.180）
- QQ（9.9.31.49738）
- QQExtension（1.0.0.0）
- Steam（2.10.91.91）
- XBOX（2608.1001.17.0）
- Xbox 主机小帮手（48.104.4001.0）
- Xbox Game Bar Plugin（1.54.4001.0）
- Xbox Game Speech Window（1.21.13002.0）
- Xbox Identity Provider（12.130.16001.0）
- Xbox TCUI（1.24.10001.0）

浏览器、聊天软件、云盘、AI 客户端和开发平台应在重装后逐个登录并检查 2FA；不要依赖复制旧 Cookie 或 DPAPI 加密文件。

## 全部已识别应用

| 应用名称 | 当前版本 | 标识 | 安装来源 | 可用更新 |
|---|---|---|---|---|
| “开始体验”应用 | 1.380.2.0 | `MSIX\Microsoft.StartExperiencesApp_1.380.2.0_x64__8wekyb3d8bbwe` | MSIX/Store | — |
| 3D 查看器 | 1.0.125.0 | `MSIX\Microsoft.Microsoft3DViewer_1.0.125.0_x64__8wekyb3d8bbwe` | MSIX/Store | — |
| 百度网盘 | 8.3.10 | `Baidu.BaiduNetdisk` | winget | 有：8.7.0 |
| 百度网盘 | 7.17.5.6 | `MSIX\BaiduNetdisk.DesktopSyncClient_7.17.5.6_neutral__r5kxaep58dem0` | MSIX/Store | — |
| 崩溃大陆 | Unknown | `ARP\Machine\X64\Steam App 391730` | Steam | — |
| 边境开拓者 | Unknown | `ARP\Machine\X64\Steam App 2346410` | Steam | — |
| 边缘世界 RimWorld | Unknown | `ARP\Machine\X64\Steam App 294100` | Steam | — |
| 编程农场 | Unknown | `ARP\Machine\X64\Steam App 2060160` | Steam | — |
| 冰汽时代 | Unknown | `ARP\Machine\X64\Steam App 323190` | Steam | — |
| 电脑管家 | 3.22.3.0 | `MSIX\Microsoft.MicrosoftPCManager_3.22.3.0_x64__8wekyb3d8bbwe` | MSIX/Store | — |
| 电影和电视 | 10.26061.10051.0 | `MSIX\Microsoft.ZuneVideo_10.26061.10051.0_x64__8wekyb3d8bbwe` | MSIX/Store | — |
| 东方夜雀食堂 - Touhou Mystia's Izakaya | Unknown | `ARP\Machine\X64\Steam App 1584090` | Steam | — |
| 豆包 | 2.20.9 | `ByteDance.Doubao` | winget | 有：2.23.7 |
| 反馈中心 | 2.2606.703.0 | `MSIX\Microsoft.WindowsFeedbackHub_2.2606.703.0_x64__8wekyb3d8bbwe` | MSIX/Store | — |
| 放松时光:与你共享Lo-Fi故事 | Unknown | `ARP\Machine\X64\Steam App 3548580` | Steam | — |
| 画图 | 11.2605.71.0 | `MSIX\Microsoft.Paint_11.2605.71.0_x64__8wekyb3d8bbwe` | MSIX/Store | — |
| 画图 3D | 6.1907.29027.0 | `MSIX\Microsoft.MSPaint_6.1907.29027.0_x64__8wekyb3d8bbwe` | MSIX/Store | — |
| 混合现实门户 | 2000.21051.1282.0 | `MSIX\Microsoft.MixedReality.Portal_2000.21051.1282.0_x64__8wekyb3d8bbwe` | MSIX/Store | — |
| 火绒安全软件 | 6.0.11.1 | `ARP\Machine\X64\HuorongSysdiag` | 传统安装器 | — |
| 获取帮助 | 10.2409.42092.0 | `MSIX\Microsoft.GetHelp_10.2409.42092.0_x64__8wekyb3d8bbwe` | MSIX/Store | — |
| 饥荒联机版 | Unknown | `ARP\Machine\X64\Steam App 322330` | Steam | — |
| 截图工具 | 11.2602.49.0 | `MSIX\Microsoft.ScreenSketch_11.2602.49.0_x64__8wekyb3d8bbwe` | MSIX/Store | — |
| 快速助手 | 2.0.29.0 | `MSIX\MicrosoftCorporationII.QuickAssist_2.0.29.0_x64__8wekyb3d8bbwe` | MSIX/Store | — |
| 来自设备制造商的 HEVC 视频扩展 | 2.5.10.0 | `MSIX\Microsoft.HEVCVideoExtension_2.5.10.0_x64__8wekyb3d8bbwe` | MSIX/Store | — |
| 罗马拓荒录 | Unknown | `ARP\Machine\X64\Steam App 1805320` | Steam | — |
| 猫娘计划 - N.E.K.O. | Unknown | `ARP\Machine\X64\Steam App 4099310` | Steam | — |
| 梦幻魔法公主 | Unknown | `ARP\Machine\X64\Steam App 3562120` | Steam | — |
| 命令面板 | 0.3.1871.0 | `MSIX\Microsoft.CommandPalette_0.3.1871.0_x64__8wekyb3d8bbwe` | MSIX/Store | — |
| 奈斯启示录 Necesse | Unknown | `ARP\Machine\X64\Steam App 1169040` | Steam | — |
| 欧路词典 | 26.4.0.0 | `EuSoft.Eudic` | winget | 有：26.8.1.0 |
| 潜水员戴夫 DAVE THE DIVER | Unknown | `ARP\Machine\X64\Steam App 1868140` | Steam | — |
| 缺氧 | Unknown | `ARP\Machine\X64\Steam App 457140` | Steam | — |
| 日本語 ローカル エクスペリエンス パック | 26100.174.273.0 | `MSIX\Microsoft.LanguageExperiencePackja-JP_26100.174.273.0_neutral__8wekyb3d8bbwe` | MSIX/Store | — |
| 适用于 Game Bar 的 Microsoft Edge | 1.0.4019.0 | `MSIX\Microsoft.Edge.GameAssist_1.0.4019.0_x64__8wekyb3d8bbwe` | MSIX/Store | — |
| 手机连接 | 1.26062.145.0 | `MSIX\Microsoft.YourPhone_1.26062.145.0_x64__8wekyb3d8bbwe` | MSIX/Store | — |
| 搜图神器 | 0.12.18.0 | `MSIX\59134yyx.38291988B71E1_0.12.18.0_x64__gebjtwgs32d54` | MSIX/Store | — |
| 逃离鸭科夫 | Unknown | `ARP\Machine\X64\Steam App 3167020` | Steam | — |
| 土豆兄弟(Brotato) | Unknown | `ARP\Machine\X64\Steam App 1942280` | Steam | — |
| 网易有道翻译 | 11.3.14.0 | `Youdao.YoudaoTranslate` | winget | 有：11.3.16.0 |
| 网易云音乐 | 3.1.37.205354 | `NetEase.CloudMusic` | winget | — |
| 微信输入法 | 2.1.1.8 | `XPFFFP686NDRDZ` | msstore | — |
| 小丸工具箱 | 236 | `ARP\Machine\X86\{7EEB2DD0-264B-4340-B6BE-F05D99066D3C}` | 传统安装器 | — |
| 虚拟桌宠模拟器 | Unknown | `ARP\Machine\X64\Steam App 1920960` | Steam | — |
| 移动设备 | 1.26062.105.0 | `MSIX\MicrosoftWindows.CrossDevice_1.26062.105.0_x64__cw5n1h2txyewy` | MSIX/Store | — |
| 英特尔(R) 无线 Bluetooth(R) | 22.200.0.2 | `ARP\Machine\X86\{00000200-0220-2052-84C8-B8D95FA3C8C3}` | 传统安装器 | — |
| 邮件和日历 | 16005.14326.22342.0 | `MSIX\microsoft.windowscommunicationsapps_16005.14326.22342.0_x64__8wekyb3d8bbwe` | MSIX/Store | — |
| 原始图像扩展 | 2.5.24.0 | `MSIX\Microsoft.RawImageExtension_2.5.24.0_x64__8wekyb3d8bbwe` | MSIX/Store | — |
| 云枢 | 2.80 | `ARP\Machine\X86\YunShu` | 传统安装器 | — |
| 战地风云TM 6 | Unknown | `ARP\Machine\X64\Steam App 2807960` | Steam | — |
| 中文(简体)本地体验包 | 26100.163.263.0 | `MSIX\Microsoft.LanguageExperiencePackzh-CN_26100.163.263.0_neutral__8wekyb3d8bbwe` | MSIX/Store | — |
| 资讯 | 4.56.21872.0 | `MSIX\Microsoft.BingNews_4.56.21872.0_x64__8wekyb3d8bbwe` | MSIX/Store | — |
| Anaconda3 | 2025.06-0 | `Anaconda.Anaconda3` | winget | 有：2025.12-2 |
| Apex Legends | Unknown | `ARP\Machine\X64\Steam App 1172470` | Steam | — |
| Apifox | 2.8.40 | `Ruihu.Apifox` | winget | 有：2.8.42 |
| App Installer | 1.29.280.0 | `Microsoft.AppInstaller` | winget | — |
| AV1 Video Extension | 2.0.24.0 | `MSIX\Microsoft.AV1VideoExtension_2.0.24.0_x64__8wekyb3d8bbwe` | MSIX/Store | — |
| AVC 编码器视频扩展 | 1.1.23.0 | `MSIX\Microsoft.AVCEncoderVideoExtension_1.1.23.0_x64__8wekyb3d8bbwe` | MSIX/Store | — |
| BaiduNetdiskService | 1.0.18.0 | `MSIX\3AD8A913.49937325EFC59_1.0.18.0_x64__j4r74wbqry4cc` | MSIX/Store | — |
| Bun | Unknown | `ARP\User\X64\Bun` | 传统安装器 | — |
| Bun | 1.3.13 | `Oven-sh.Bun` | winget | 有：1.3.14 |
| Burp Suite | 2026.6 | `PortSwigger.BurpSuite` | winget | 有：2026.7.3 |
| CC Switch | 3.19.2 | `farion1231.CC-Switch` | winget | — |
| Charles Proxy | 5.0.3.1 | `XK72.Charles` | winget | 有：5.2.1.2 |
| ChatGPT | 26.803.10989.0 | `MSIX\OpenAI.Codex_26.803.10989.0_x64__2p2nqsd0c76g0` | MSIX/Store | — |
| Clash Verge | 2.5.2 | `ARP\Machine\X64\Clash Verge` | 传统安装器 | — |
| Claude | 1.10628.2.0 | `Anthropic.Claude` | winget | 有：1.30096.1 |
| Claude Code | 2.1.147 | `Anthropic.ClaudeCode` | winget | 有：2.1.229 |
| CMake | 4.1.0 | `Kitware.CMake` | winget | 有：4.4.2 |
| Cockpit Tools | 0.24.12 | `ARP\User\X64\Cockpit Tools` | 传统安装器 | — |
| Control Center Service | 5.1.50.36 | `ARP\Machine\X64\{6ea3ce12-b991-4b65-9f8d-b148eaaecd87}_is1` | 传统安装器 | — |
| Craft The World | Unknown | `ARP\Machine\X64\Steam App 248390` | Steam | — |
| cURL | 8.15.0.4 | `cURL.cURL` | winget | 有：8.21.0.6 |
| Darkest Dungeon® | Unknown | `ARP\Machine\X64\Steam App 262060` | Steam | — |
| DBeaver | 26.1.3 | `DBeaver.DBeaver.Community` | winget | 有：26.1.4 |
| Deno | 2.6.4 | `DenoLand.Deno` | winget | 有：2.9.5 |
| DingTalk | 8.3.45-Release.260720005 | `Alibaba.DingTalk.Mainland` | winget | — |
| Docker Desktop | 4.78.0 | `Docker.DockerDesktop` | winget | 有：4.86.0 |
| EarTrumpet | 2.3.0.0 | `MSIX\40459File-New-Project.EarTrumpet_2.3.0.0_x86__1sdd7yawvg6ne` | MSIX/Store | — |
| Euro Truck Simulator 2 | Unknown | `ARP\Machine\X64\Steam App 227300` | Steam | — |
| EZ CD Audio Converter | 2024.6.28 | `ARP\Machine\X86\EZ CD Audio Converter` | 传统安装器 | — |
| Fast Node Manager | 1.39.0 | `Schniz.fnm` | winget | — |
| Feishu | 7.73.9 | `ByteDance.Feishu` | winget | — |
| FFmpeg for yt-dlp | N-121938-g2456a39581-20251130 | `yt-dlp.FFmpeg` | winget | 有：N-125875-g5d4d3bdc61-20260731 |
| Game Bar | 7.326.6011.0 | `MSIX\Microsoft.XboxGamingOverlay_7.326.6011.0_x64__8wekyb3d8bbwe` | MSIX/Store | — |
| GamingCenter3_Cross | 5.1.50.36 | `MSIX\ControlCenter3_5.1.50.36_x64__wrbgcf7aesyd8` | MSIX/Store | — |
| Git | 2.54.0 | `Git.Git` | winget | 有：2.55.0.3 |
| GitHub CLI | 2.87.3 | `GitHub.cli` | winget | 有：2.97.0 |
| Go Programming Language | 1.25.4 | `GoLang.Go` | winget | 有：1.26.5 |
| Google Chrome | 151.0.7922.138 | `ARP\Machine\X86\Google Chrome` | 传统安装器 | — |
| Handle | 5.0 | `Microsoft.Sysinternals.Handle` | winget | — |
| HEIF 图像扩展 | 1.2.36.0 | `MSIX\Microsoft.HEIFImageExtension_1.2.36.0_x64__8wekyb3d8bbwe` | MSIX/Store | — |
| hi | 1.30.5 | `ARP\User\X64\hi` | 传统安装器 | — |
| HireMe AI 0.3.44 | 0.3.44 | `ARP\User\X64\a676006a-3c40-5f43-8014-e2ee3598d8ac` | 传统安装器 | — |
| HRContextMenu | 1.0.0.0 | `MSIX\HRContextMenu_1.0.0.0_neutral__m6ed0pe7fcjg8` | MSIX/Store | — |
| IDA Pro v7.0 and Hex-Rays Decompiler (ARM64,ARM,x64,x86) | Unknown | `ARP\Machine\X64\IDA Pro_7.0_is1` | 传统安装器 | — |
| IIS 10.0 Express | 10.0.10007 | `ARP\Machine\X64\{0F4F67F8-21E1-422D-B31C-B3800F4D6E36}` | 传统安装器 | — |
| ImageConverter | 1.5.2.0 | `ARP\Machine\X64\ImageConverter_is1` | 传统安装器 | — |
| ImageMagick Q16-HDRI | 7.1.2.21 | `ImageMagick.ImageMagick` | winget | 有：7.1.2.29 |
| Ink.Handwriting.Main.zh-Hans.1.0 | 0.1248.2215.0 | `MSIX\Microsoft.Ink.Handwriting.Main.zh-Hans.1.0_0.1248.2215.0_x64__8wekyb3d8bbwe` | MSIX/Store | — |
| Ink.Handwriting.zh-Hans.1.0 | 0.1248.2215.0 | `MSIX\Microsoft.Ink.Handwriting.zh-Hans.1.0_0.1248.2215.0_x64__8wekyb3d8bbwe` | MSIX/Store | — |
| Ink.Handwriting.zh-Hans.1.0 | 0.1248.2215.0 | `MSIX\Microsoft.Ink.Handwriting.zh-Hans.1.0_0.1248.2215.0_x86__8wekyb3d8bbwe` | MSIX/Store | — |
| Intel(R) Chipset Device Software | 10.1.19199.8340 | `ARP\Machine\X86\{e6ecf35a-b1bb-4e59-9d90-4c98fde2ffa8}` | 传统安装器 | — |
| Intel(R) Innovation Platform Framework | 2.0.10200.8 | `ARP\Machine\X86\{1F2F557C-7559-4376-9347-1C6ACFAD35C2}` | 传统安装器 | — |
| Intel(R) Management Engine Components | 2242.3.34.0 | `ARP\Machine\X64\{1CEAC85D-2590-4760-800F-8DE5E91F3700}` | 传统安装器 | — |
| Java 8 | 8.0.4810.10 | `Oracle.JavaRuntimeEnvironment` | winget | 有：8.0.5010.8 |
| Java(TM) SE Development Kit 17 | 11.0.28.0 | `Oracle.JDK.17` | winget | 有：17.0.12.0 |
| jq | 1.8.1 | `jqlang.jq` | winget | 有：1.8.2 |
| Left 4 Dead 2 | Unknown | `ARP\Machine\X64\Steam App 550` | Steam | — |
| Lossless Scaling | Unknown | `ARP\Machine\X64\Steam App 993090` | Steam | — |
| lx-music-desktop | 2.12.2 | `lyswhut.lx-music-desktop` | winget | — |
| Microsoft .NET Framework 1.1 | Unknown | `ARP\Machine\X86\Microsoft .NET Framework 1.1  (1033)` | 传统安装器 | — |
| Microsoft .NET Framework 1.1 Security Update (KB2698023) | Unknown | `ARP\Machine\X86\M2698023` | 传统安装器 | — |
| Microsoft .NET Framework 1.1 Security Update (KB2833941) | Unknown | `ARP\Machine\X86\M2833941` | 传统安装器 | — |
| Microsoft .NET Framework 1.1 Security Update (KB971108) | Unknown | `ARP\Machine\X86\M971108` | 传统安装器 | — |
| Microsoft .NET Framework 1.1 Security Update (KB979906) | Unknown | `ARP\Machine\X86\M979906` | 传统安装器 | — |
| Microsoft .Net Native Framework Package 1.7 | 1.7.27413.0 | `MSIX\Microsoft.NET.Native.Framework.1.7_1.7.27413.0_x64__8wekyb3d8bbwe` | MSIX/Store | — |
| Microsoft .Net Native Framework Package 1.7 | 1.7.27413.0 | `MSIX\Microsoft.NET.Native.Framework.1.7_1.7.27413.0_x86__8wekyb3d8bbwe` | MSIX/Store | — |
| Microsoft .Net Native Framework Package 2.2 | 2.2.29512.0 | `MSIX\Microsoft.NET.Native.Framework.2.2_2.2.29512.0_x64__8wekyb3d8bbwe` | MSIX/Store | — |
| Microsoft .Net Native Framework Package 2.2 | 2.2.29512.0 | `MSIX\Microsoft.NET.Native.Framework.2.2_2.2.29512.0_x86__8wekyb3d8bbwe` | MSIX/Store | — |
| Microsoft .NET Native Runtime | 2.2.28604.0 | `Microsoft.DotNet.Native.Runtime` | winget | — |
| Microsoft .Net Native Runtime Package 1.7 | 1.7.27422.0 | `MSIX\Microsoft.NET.Native.Runtime.1.7_1.7.27422.0_x64__8wekyb3d8bbwe` | MSIX/Store | — |
| Microsoft .Net Native Runtime Package 1.7 | 1.7.27422.0 | `MSIX\Microsoft.NET.Native.Runtime.1.7_1.7.27422.0_x86__8wekyb3d8bbwe` | MSIX/Store | — |
| Microsoft .NET SDK 10.0 | 10.0.100 | `Microsoft.DotNet.SDK.10` | winget | 有：10.0.400 |
| Microsoft .NET SDK 8.0 | 8.0.423 | `Microsoft.DotNet.SDK.8` | winget | 有：8.0.424 |
| Microsoft .NET SDK 9.0.302 (x64) from Visual Studio | 9.3.225.31907 | `ARP\Machine\X64\{118C0ABF-1A67-42FC-AE66-7453FA3C86A2}` | 传统安装器 | — |
| Microsoft .NET Windows Desktop Runtime 6.0 | 6.0.25 | `Microsoft.DotNet.DesktopRuntime.6` | winget | 有：6.0.36 |
| Microsoft .NET Windows Desktop Runtime 8.0 | 8.0.19 | `Microsoft.DotNet.DesktopRuntime.8` | winget | 有：8.0.30 |
| Microsoft 365 Copilot | 19.2607.61021.0 | `MSIX\Microsoft.MicrosoftOfficeHub_19.2607.61021.0_x64__8wekyb3d8bbwe` | MSIX/Store | — |
| Microsoft 必应 | 1.1.43.0 | `MSIX\Microsoft.BingSearch_1.1.43.0_x64__8wekyb3d8bbwe` | MSIX/Store | — |
| Microsoft 便笺 | 4.0.6104.0 | `MSIX\Microsoft.MicrosoftStickyNotes_4.0.6104.0_x64__8wekyb3d8bbwe` | MSIX/Store | — |
| Microsoft 人脉 | 10.2202.100.0 | `MSIX\Microsoft.People_10.2202.100.0_x64__8wekyb3d8bbwe` | MSIX/Store | — |
| Microsoft 照片 | 2026.11060.2004.0 | `MSIX\Microsoft.Windows.Photos_2026.11060.2004.0_x64__8wekyb3d8bbwe` | MSIX/Store | — |
| Microsoft AppLocale | 1.0.0 | `ARP\Machine\X86\{394BE3D9-7F57-4638-A8D1-1D88671913B7}` | 传统安装器 | — |
| Microsoft Build of OpenJDK with Hotspot 21 | 21.0.10.7 | `Microsoft.OpenJDK.21` | winget | 有：21.0.12.8 |
| Microsoft Clipchamp | 4.5.10920.0 | `MSIX\Clipchamp.Clipchamp_4.5.10920.0_x64__yxz26nhyzhsrt` | MSIX/Store | — |
| Microsoft Edge | 151.0.4129.78 | `Microsoft.Edge` | winget | — |
| Microsoft Edge | 151.0.4129.78 | `MSIX\Microsoft.MicrosoftEdge.Stable_151.0.4129.78_neutral__8wekyb3d8bbwe` | MSIX/Store | — |
| Microsoft Engagement Framework | 10.0.23012.0 | `MSIX\Microsoft.Services.Store.Engagement_10.0.23012.0_x64__8wekyb3d8bbwe` | MSIX/Store | — |
| Microsoft Engagement Framework | 10.0.23012.0 | `MSIX\Microsoft.Services.Store.Engagement_10.0.23012.0_x86__8wekyb3d8bbwe` | MSIX/Store | — |
| Microsoft Family | 0.2.40.0 | `MSIX\MicrosoftCorporationII.MicrosoftFamily_0.2.40.0_x64__8wekyb3d8bbwe` | MSIX/Store | — |
| Microsoft ODBC Driver 17 for SQL Server | 17.10.6.1 | `Microsoft.msodbcsql.17` | winget | 有：17.11.1.1 |
| Microsoft Office LTSC 专业增强版 2024 - zh-cn | 16.0.17932.20910 | `ARP\Machine\X64\ProPlus2024Volume - zh-cn` | 传统安装器 | — |
| Microsoft OneDrive | 26.139.0720.0007 | `Microsoft.OneDrive` | winget | — |
| Microsoft PowerToys | 0.92.1 | `XP89DCGQ3K6VLD` | msstore | 有：0.100.2 |
| Microsoft Silverlight | 5.1.50918.0 | `ARP\Machine\X64\{89F4137D-6C26-4A84-BDB8-2E5A4BB71E00}` | 传统安装器 | — |
| Microsoft SQL Server 2019 LocalDB | 15.0.4382.1 | `ARP\Machine\X64\{E5B3A478-C4C3-49E3-8384-A12D4B2008D4}` | 传统安装器 | — |
| Microsoft Store | 22606.1401.13.0 | `MSIX\Microsoft.WindowsStore_22606.1401.13.0_x64__8wekyb3d8bbwe` | MSIX/Store | — |
| Microsoft Store 体验主机 | 22606.1401.2.0 | `MSIX\Microsoft.StorePurchaseApp_22606.1401.2.0_x64__8wekyb3d8bbwe` | MSIX/Store | — |
| Microsoft System CLR Types for SQL Server 2019 | 15.0.2000.5 | `Microsoft.CLRTypesSQLServer.2019` | winget | — |
| Microsoft Teams | 1.0.0.0 | `Microsoft.Teams` | winget | 有：26198.304.4946.9672 |
| Microsoft To Do | 0.176.7601.0 | `MSIX\Microsoft.Todos_0.176.7601.0_x64__8wekyb3d8bbwe` | MSIX/Store | — |
| Microsoft Update Health Tools | 3.74.0.0 | `Microsoft.UpdateHealthTools` | winget | 有：5.69 |
| Microsoft Visual C++ 2005 Redistributable (x64) | 8.0.61186 | `ARP\Machine\X64\{ad8a2fa1-06e7-4b0d-927d-6e54b3d31028}` | 传统安装器 | — |
| Microsoft Visual C++ 2005 Redistributable (x86) | 8.0.61187 | `Microsoft.VCRedist.2005.x86` | winget | — |
| Microsoft Visual C++ 2008 Redistributable - x64 | 9.0.30729.7523 | `Microsoft.VCRedist.2008.x64` | winget | — |
| Microsoft Visual C++ 2008 Redistributable - x64 9.0.30729.17 | 9.0.30729 | `ARP\Machine\X64\{8220EEFE-38CD-377E-8595-13398D740ACE}` | 传统安装器 | — |
| Microsoft Visual C++ 2008 Redistributable - x86 | 9.0.30729.7523 | `Microsoft.VCRedist.2008.x86` | winget | — |
| Microsoft Visual C++ 2010 x64 Redistributable | 10.0.40219 | `Microsoft.VCRedist.2010.x64` | winget | — |
| Microsoft Visual C++ 2010 x86 Redistributable | 10.0.40219 | `Microsoft.VCRedist.2010.x86` | winget | — |
| Microsoft Visual C++ 2012 Redistributable (x64) | 11.0.61135.400 | `Microsoft.VCRedist.2012.x64` | winget | — |
| Microsoft Visual C++ 2012 Redistributable (x86) | 11.0.61135.400 | `Microsoft.VCRedist.2012.x86` | winget | — |
| Microsoft Visual C++ 2013 Redistributable (x64) | 12.0.40664.0 | `Microsoft.VCRedist.2013.x64` | winget | — |
| Microsoft Visual C++ 2013 Redistributable (x86) | 12.0.40664.0 | `Microsoft.VCRedist.2013.x86` | winget | — |
| Microsoft Visual C++ 2015 UWP Desktop Runtime Package | 14.0.33728.0 | `Microsoft.VCLibs.Desktop.14` | winget | — |
| Microsoft Visual C++ 2015 UWP Runtime Package | 14.0.33519.0 | `Microsoft.VCLibs.14` | winget | — |
| Microsoft Visual C++ v14 Redistributable (x64) | 14.51.36247.0 | `Microsoft.VCRedist.2015+.x64` | winget | — |
| Microsoft Visual C++ v14 Redistributable (x86) | 14.51.36247.0 | `Microsoft.VCRedist.2015+.x86` | winget | — |
| Microsoft Visual F# 2.0 Runtime | 10.0.40219 | `ARP\Machine\X86\{85467CBC-7A39-33C9-8940-D72D9269B84F}` | 传统安装器 | — |
| Microsoft Visual Studio 2010 Tools for Office Runtime | 10.0.60833 | `Microsoft.VSTOR` | winget | — |
| Microsoft Visual Studio Code | 1.119.0 | `Microsoft.VisualStudioCode` | winget | 有：1.132.0 |
| Microsoft Visual Studio Installer | 4.7.25.22189 | `ARP\Machine\X64\{6F320B93-EE3C-4826-85E0-ADF79F8D4C61}` | 传统安装器 | — |
| Microsoft Web Deploy | 10.0.9419 | `Microsoft.WebDeploy` | winget | — |
| Microsoft Windows Application Compatibility Database | Unknown | `ARP\Machine\X64\{deb7008b-681e-4a4a-8aae-cc833e8216ce}.sdb` | 传统安装器 | — |
| Microsoft XNA Framework Redistributable Refresh | 4.0.30901.0 | `Microsoft.XNARedist` | winget | — |
| Microsoft.UI.Xaml | 7.2409.9001.0 | `Microsoft.UI.Xaml.2.7` | winget | — |
| Microsoft.UI.Xaml | 8.2511.26001.0 | `Microsoft.UI.Xaml.2.8` | winget | — |
| Microsoft.UI.Xaml.2.0 | 2.1810.18004.0 | `MSIX\Microsoft.UI.Xaml.2.0_2.1810.18004.0_x64__8wekyb3d8bbwe` | MSIX/Store | — |
| Microsoft.UI.Xaml.2.3 | 2.32002.13001.0 | `MSIX\Microsoft.UI.Xaml.2.3_2.32002.13001.0_x64__8wekyb3d8bbwe` | MSIX/Store | — |
| Microsoft.UI.Xaml.2.3 | 2.32002.13001.0 | `MSIX\Microsoft.UI.Xaml.2.3_2.32002.13001.0_x86__8wekyb3d8bbwe` | MSIX/Store | — |
| Microsoft.UI.Xaml.2.4 | 2.42007.9001.0 | `MSIX\Microsoft.UI.Xaml.2.4_2.42007.9001.0_x64__8wekyb3d8bbwe` | MSIX/Store | — |
| Microsoft.UI.Xaml.2.4 | 2.42007.9001.0 | `MSIX\Microsoft.UI.Xaml.2.4_2.42007.9001.0_x86__8wekyb3d8bbwe` | MSIX/Store | — |
| Mozilla Firefox (x64 zh-CN) | 153.0.3 | `ARP\Machine\X64\Mozilla Firefox` | 传统安装器 | — |
| Mozilla Maintenance Service | 146.0.1 | `ARP\Machine\X64\MozillaMaintenanceService` | 传统安装器 | — |
| MPEG-2 视频扩展 | 1.2.13.0 | `MSIX\Microsoft.MPEG2VideoExtension_1.2.13.0_x64__8wekyb3d8bbwe` | MSIX/Store | — |
| MSN 天气 | 4.54.63045.0 | `MSIX\Microsoft.BingWeather_4.54.63045.0_x64__8wekyb3d8bbwe` | MSIX/Store | — |
| MSYS2 | 20250622 | `ARP\User\X64\{f0665201-936e-4822-b65d-90a43cccc5ff}` | 传统安装器 | — |
| Multica | 0.4.4 | `Multica.MulticaDesktop` | winget | 有：0.4.25 |
| MuMu模拟器 | 6.5.1.0 | `ARP\Machine\X64\MuMuPlayer` | 传统安装器 | — |
| MySQL | 8.0.43 | `Oracle.MySQL` | winget | 有：8.4.9 |
| Node.js (LTS) | 24.14.1 | `OpenJS.NodeJS.LTS` | winget | 有：24.19.0 |
| Noita | Unknown | `ARP\Machine\X64\Steam App 881100` | Steam | — |
| Notepad4 | 26.05r6166 | `zufuliu.notepad4` | winget | 有：26.07r6234 |
| Notion | 7.9.0 | `Notion.Notion` | winget | 有：7.30.0 |
| Npcap | 1.85 | `ARP\Machine\X86\NpcapInst` | 传统安装器 | — |
| NSSM | 2.24-101-g897c7ad | `NSSM.NSSM` | winget | — |
| NVIDIA 图形驱动程序 581.80 | 581.80 | `ARP\Machine\X64\{B2FE1952-0186-46C3-BAEC-A80AA35AC5B8}_Display.Driver` | 传统安装器 | — |
| NVIDIA App 11.0.6.383 | 11.0.6.383 | `ARP\Machine\X64\{B2FE1952-0186-46C3-BAEC-A80AA35AC5B8}_Display.NvApp` | 传统安装器 | — |
| NVIDIA Control Panel | 8.1.969.0 | `MSIX\NVIDIACorp.NVIDIAControlPanel_8.1.969.0_x64__56jybvy8sckqj` | MSIX/Store | — |
| NVIDIA FrameView SDK 1.5.11821.36727370 | 1.5.11821.36727370 | `ARP\Machine\X64\{B2FE1952-0186-46C3-BAEC-A80AA35AC5B8}_FrameViewSdk` | 传统安装器 | — |
| NVIDIA HD 音频驱动程序 1.4.5.0 | 1.4.5.0 | `ARP\Machine\X64\{B2FE1952-0186-46C3-BAEC-A80AA35AC5B8}_HDAudio.Driver` | 传统安装器 | — |
| NVIDIA PhysX System Software | 9.23.1019 | `Nvidia.PhysX` | winget | — |
| Obsidian | 1.12.4 | `Obsidian.Obsidian` | winget | 有：1.13.7 |
| Ollama | 0.10.1 | `Ollama.Ollama` | winget | 有：0.32.11 |
| OneDrive | 26139.720.7.0 | `MSIX\Microsoft.OneDriveSync_26139.720.7.0_neutral__8wekyb3d8bbwe` | MSIX/Store | — |
| OneNote for Windows 10 | 16.14326.22589.0 | `MSIX\Microsoft.Office.OneNote_16.14326.22589.0_x64__8wekyb3d8bbwe` | MSIX/Store | — |
| OpenSSL Light | 3.6.1 | `ShiningLight.OpenSSL.Light` | winget | 有：4.0.1 |
| Orca | 1.4.180 | `StablyAI.Orca` | winget | 有：1.4.181 |
| Outlook for Windows | 1.2026.520.0 | `MSIX\Microsoft.OutlookForWindows_1.2026.520.0_x64__8wekyb3d8bbwe` | MSIX/Store | — |
| Palworld / 幻兽帕鲁 | Unknown | `ARP\Machine\X64\Steam App 1623730` | Steam | — |
| Pandoc | 3.8.2 | `JohnMacFarlane.Pandoc` | winget | 有：3.10.2 |
| PasteMD 版本 0.1.5.7 | 0.1.5.7 | `ARP\Machine\X64\{4f3f2b18-55a3-4f40-98f6-d01a3e3e0220}}_is1` | 传统安装器 | — |
| PixPin 版本 3.4.3.2 | 3.4.3.2 | `ARP\User\X64\{506270E7-E3B5-4157-B53A-3BFFE8E418DB}_is1` | 传统安装器 | — |
| PixPinContextMenu | 1.0.0.0 | `MSIX\PixPinContextMenu_1.0.0.0_x64__9mnqdg1kkwem8` | MSIX/Store | — |
| PostgreSQL 18 | 18.1-2 | `PostgreSQL.PostgreSQL.18` | winget | 有：18.6-1 |
| PotPlayer | 26.07.01.0 | `XP8BSBGQW2DKS0` | msstore | 有：210428 |
| Power Automate | 1.0.2117.0 | `MSIX\Microsoft.PowerAutomateDesktop_1.0.2117.0_x64__8wekyb3d8bbwe` | MSIX/Store | — |
| PowerShell | 7.6.4.0 | `Microsoft.PowerShell` | winget | — |
| PowerToys FileLocksmith Context Menu | 0.92.1.0 | `MSIX\Microsoft.PowerToys.FileLocksmithContextMenu_0.92.1.0_neutral__8wekyb3d8bbwe` | MSIX/Store | — |
| PowerToys ImageResizer Context Menu | 0.92.1.0 | `MSIX\Microsoft.PowerToys.ImageResizerContextMenu_0.92.1.0_neutral__8wekyb3d8bbwe` | MSIX/Store | — |
| PowerToys New+ | 0.92.1.0 | `MSIX\Microsoft.PowerToys.NewPlusContextMenu_0.92.1.0_neutral__8wekyb3d8bbwe` | MSIX/Store | — |
| PowerToys PowerRename Context Menu | 0.92.1.0 | `MSIX\Microsoft.PowerToys.PowerRenameContextMenu_0.92.1.0_neutral__8wekyb3d8bbwe` | MSIX/Store | — |
| Python 3.12 | 3.12.10 | `Python.Python.3.12` | winget | — |
| Python Launcher | 3.12.10 | `Python.Launcher` | winget | 有：3.13.5 |
| QQ | 9.9.31.49738 | `Tencent.QQ.NT` | winget | 有：9.9.33.51802 |
| QQExtension | 1.0.0.0 | `MSIX\QQExtension_1.0.0.0_neutral__fv0hcek9q9tbw` | MSIX/Store | — |
| Radmin VPN | 1.4.4642.1 | `Famatech.RadminVPN` | winget | 有：2.0.4899.9 |
| Rapture3D 2.7.4 Game | Unknown | `ARP\Machine\X86\{D2FCA41E-AC01-4DCD-B3A7-DC9E32363065}}_is1` | 传统安装器 | — |
| Realtek Audio Control | 1.1.137.0 | `MSIX\RealtekSemiconductorCorp.RealtekAudioControl_1.1.137.0_x64__dt26b99r8h8gj` | MSIX/Store | — |
| Realtek Ethernet Controller Driver | 11.10.0720.2022 | `ARP\Machine\X86\{8833FFB6-5B0C-4764-81AA-06DFEED9A476}` | 传统安装器 | — |
| Redis on Windows | 5.0.14.1 | `ARP\Machine\X64\{0452DA9B-BF9A-4CC6-A40C-6BC2FB04BE81}` | 传统安装器 | — |
| REDpass 1.8.4 | 1.8.4 | `ARP\Machine\X64\54ccf452-3dae-523d-95de-5707b73f6700` | 传统安装器 | — |
| RipGrep MSVC | 15.1.0 | `BurntSushi.ripgrep.MSVC` | winget | 有：15.2.0 |
| Rustup: the Rust toolchain installer | 1.29.0 | `Rustlang.Rustup` | winget | — |
| scrcpy | 4.0 | `Genymobile.scrcpy` | winget | 有：4.1 |
| Simple Sticky Notes | 6.9 | `Simnet.SimpleStickyNotes` | winget | — |
| Slay the Spire | Unknown | `ARP\Machine\X64\Steam App 646570` | Steam | — |
| Slay the Spire 2 | Unknown | `ARP\Machine\X64\Steam App 2868840` | Steam | — |
| Solitaire & Casual Games | 4.26.7290.0 | `MSIX\Microsoft.MicrosoftSolitaireCollection_4.26.7290.0_x64__8wekyb3d8bbwe` | MSIX/Store | — |
| SPlayer | 3.1.1 | `ARP\User\X64\a424861f-5ffe-572b-9a0a-23492faf0f1c` | 传统安装器 | — |
| Stardew Valley | Unknown | `ARP\Machine\X64\Steam App 413150` | Steam | — |
| Stardock Fences 6 | 6.0.2.2 | `ARP\Machine\X86\Stardock Fences 6` | 传统安装器 | — |
| Stardock Fences Desktop Menu | 1.0.0.0 | `MSIX\Stardock.Fences.DesktopMenu_1.0.0.0_neutral__a8b8bqct24ect` | MSIX/Store | — |
| Steam | 2.10.91.91 | `Valve.Steam` | winget | — |
| Tailscale | 1.102.2 | `Tailscale.Tailscale` | winget | — |
| Telegram Desktop | 7.0.1 | `Telegram.TelegramDesktop` | winget | 有：7.0.9 |
| Tencent Meeting | 3.44.10.457 | `Tencent.TencentMeeting` | winget | 有：3.45.2.405 |
| Terraria | Unknown | `ARP\Machine\X64\Steam App 105600` | Steam | — |
| tModLoader | Unknown | `ARP\Machine\X64\Steam App 1281930` | Steam | — |
| ToDesk | 4.8.8.3 | `Youqu.ToDesk` | winget | — |
| Totally Accurate Battle Simulator | Unknown | `ARP\Machine\X64\Steam App 508440` | Steam | — |
| TranslucentTB | 2026.1.0.0 | `CharlesMilette.TranslucentTB` | winget | — |
| Ubuntu 20.04 LTS | 2004.6.17.0 | `Canonical.Ubuntu.2004` | winget | — |
| UltraUXThemePatcher | 4.4.4.0 | `ARP\Machine\X86\UltraUXThemePatcher` | 传统安装器 | — |
| Update for x64-based Windows Systems (KB5001716) | 8.94.0.0 | `ARP\Machine\X64\{B8D93870-98D1-4980-AFCA-E26563CDFB79}` | 传统安装器 | — |
| UU加速器 | 5.78.1.554 | `ARP\Machine\X86\NeteaseGacc` | 传统安装器 | — |
| UU远程 | 4.3.6.4951 | `NetEase.UURemote` | winget | 有：4.37.0.9232 |
| ViGEm Bus Driver | 1.20.432 | `ViGEm.ViGEmBus` | winget | — |
| Visual Basic for Application 7.0.1590 | 7.0.1590 | `ARP\Machine\X86\Visual Basic for Application` | 传统安装器 | — |
| Visual Studio 生成工具 2026 | 18.5.0 | `ARP\Machine\X86\173ec20e` | 传统安装器 | — |
| Visual Studio BuildTools 2022 | < 17.14.37 | `Microsoft.VisualStudio.2022.BuildTools` | winget | 有：17.14.37 |
| Visual Studio Code | 1.0.118.1 | `MSIX\Microsoft.VisualStudioCode_1.0.118.1_neutral__8wekyb3d8bbwe` | MSIX/Store | — |
| Visual Studio Community 2022 | 17.14.10 | `Microsoft.VisualStudio.2022.Community` | winget | 有：17.14.38 |
| VP9 视频扩展 | 1.2.20.0 | `MSIX\Microsoft.VP9VideoExtensions_1.2.20.0_x64__8wekyb3d8bbwe` | MSIX/Store | — |
| vs_CoreEditorFonts | 17.7.40001 | `ARP\Machine\X86\{1851460E-0E63-4117-B5BA-25A2F045801B}` | 传统安装器 | — |
| Wallpaper Engine:壁纸引擎 | Unknown | `ARP\Machine\X64\Steam App 431960` | Steam | — |
| Watt Toolkit | 3.1.2025.0 | `MSIX\4651ED44255E.47979655102CE_3.1.2025.0_x64__k6txddmbb6c52` | MSIX/Store | — |
| Wave | 0.14.5.0 | `CommandLine.Wave` | winget | — |
| Web 媒体扩展 | 2.1.38.0 | `MSIX\Microsoft.WebMediaExtensions_2.1.38.0_x64__8wekyb3d8bbwe` | MSIX/Store | — |
| WebP 映像扩展 | 1.2.14.0 | `MSIX\Microsoft.WebpImageExtension_1.2.14.0_x64__8wekyb3d8bbwe` | MSIX/Store | — |
| WeChat | 4.1.12.26 | `Tencent.WeChat.Universal` | winget | 有：4.1.12.55 |
| Weixin | 1.0.0.0 | `MSIX\WeixinShare_1.0.0.0_neutral__fv0hcek9q9tbw` | MSIX/Store | — |
| WGestures 2.9.1 | 2.9.1 | `ARP\Machine\X64\{85B84769-ADB3-4E16-816F-06E6018F20D0}` | 传统安装器 | — |
| Widgets Platform Runtime | 1.6.19.0 | `MSIX\Microsoft.WidgetsPlatformRuntime_1.6.19.0_x64__8wekyb3d8bbwe` | MSIX/Store | — |
| WinAppRuntime.Main.1.4 | 4000.1309.2056.0 | `MSIX\MicrosoftCorporationII.WinAppRuntime.Main.1.4_4000.1309.2056.0_x64__8wekyb3d8bbwe` | MSIX/Store | — |
| WinAppRuntime.Main.1.8 | 8000.921.1539.0 | `MSIX\MicrosoftCorporationII.WinAppRuntime.Main.1.8_8000.921.1539.0_x64__8wekyb3d8bbwe` | MSIX/Store | — |
| WinAppRuntime.Singleton | 8002.3.1.0 | `MSIX\MicrosoftCorporationII.WinAppRuntime.Singleton_8002.3.1.0_x64__8wekyb3d8bbwe` | MSIX/Store | — |
| Windows 安全中心 | 1000.29628.1000.0 | `MSIX\Microsoft.SecHealthUI_1000.29628.1000.0_x64__8wekyb3d8bbwe` | MSIX/Store | — |
| Windows 地图 | 1.0.65.0 | `MSIX\Microsoft.WindowsMaps_1.0.65.0_x64__8wekyb3d8bbwe` | MSIX/Store | — |
| Windows 计算器 | 11.2606.0.0 | `MSIX\Microsoft.WindowsCalculator_11.2606.0.0_x64__8wekyb3d8bbwe` | MSIX/Store | — |
| Windows 记事本 | 11.2606.15.0 | `MSIX\Microsoft.WindowsNotepad_11.2606.15.0_x64__8wekyb3d8bbwe` | MSIX/Store | — |
| Windows 录音机 | 1.1.119.0 | `MSIX\Microsoft.WindowsSoundRecorder_1.1.119.0_x64__8wekyb3d8bbwe` | MSIX/Store | — |
| Windows 媒体播放器 | 11.2606.19.0 | `MSIX\Microsoft.ZuneMusic_11.2606.19.0_x64__8wekyb3d8bbwe` | MSIX/Store | — |
| Windows 时钟 | 11.2606.11.0 | `MSIX\Microsoft.WindowsAlarms_11.2606.11.0_x64__8wekyb3d8bbwe` | MSIX/Store | — |
| Windows 相机 | 2026.2605.7.0 | `MSIX\Microsoft.WindowsCamera_2026.2605.7.0_x64__8wekyb3d8bbwe` | MSIX/Store | — |
| Windows 应用程序兼容性增强 | 1.2511.9.0 | `MSIX\Microsoft.ApplicationCompatibilityEnhancements_1.2511.9.0_x64__8wekyb3d8bbwe` | MSIX/Store | — |
| Windows Advanced Settings | 0.2100.858.0 | `MSIX\Microsoft.Windows.DevHome_0.2100.858.0_x64__8wekyb3d8bbwe` | MSIX/Store | — |
| Windows App Runtime | 1.3.3 | `Microsoft.WindowsAppRuntime.1.3` | winget | — |
| Windows App Runtime | 1.4.7 | `Microsoft.WindowsAppRuntime.1.4` | winget | — |
| Windows App Runtime 1.5 | 1.5.9 | `Microsoft.WindowsAppRuntime.1.5` | winget | — |
| Windows App Runtime 1.6 | 1.6.9 | `Microsoft.WindowsAppRuntime.1.6` | winget | — |
| Windows App Runtime 1.7 | 1.7.9 | `Microsoft.WindowsAppRuntime.1.7` | winget | — |
| Windows App Runtime 1.8 | > 1.8.9 | `Microsoft.WindowsAppRuntime.1.8` | winget | — |
| Windows App Runtime 2.0 | 2.3.1.0 | `Microsoft.WindowsAppRuntime.2` | winget | — |
| Windows App Runtime DDLM 4000.1049.117.0-x6 | 4000.1049.117.0 | `MSIX\Microsoft.WinAppRuntime.DDLM.4000.1049.117.0-x6_4000.1049.117.0_x64__8wekyb3d8bbwe` | MSIX/Store | — |
| Windows App SDK | 1.1.5 | `Microsoft.WindowsAppRuntime.1.1` | winget | — |
| Windows Package Manager Source (winget-font) V2 | 2025.1016.311.49 | `MSIX\Microsoft.Winget.Fonts.Source_2025.1016.311.49_neutral__8wekyb3d8bbwe` | MSIX/Store | — |
| Windows Package Manager Source (winget) V2 | 2026.814.1259.6 | `MSIX\Microsoft.Winget.Source_2026.814.1259.6_neutral__8wekyb3d8bbwe` | MSIX/Store | — |
| Windows SDK AddOn | 10.1.0.0 | `ARP\Machine\X86\{5E9BF0FA-BD7F-4FBF-886B-7138DAB9F8D3}` | 传统安装器 | — |
| Windows Software Development Kit - Windows 10.0.26100.4188 | 10.1.26100.4188 | `ARP\Machine\X86\{a174f9c3-3990-44e0-9904-1c5218139b20}` | 传统安装器 | — |
| Windows Software Development Kit - Windows 10.0.26100.4188 | 10.0.26100.7705 | `Microsoft.WindowsSDK.10.0.26100` | winget | — |
| Windows Subsystem for Linux | 2.7.3.0 | `Microsoft.WSL` | winget | 有：2.7.11 |
| Windows Subsystem for Linux Update | 5.10.16 | `ARP\Machine\X64\{36EF257E-21D5-44F7-8451-07923A8C465E}` | 传统安装器 | — |
| Windows Terminal | 1.24.11911.0 | `Microsoft.WindowsTerminal` | winget | — |
| Windows Web Experience Pack | 526.17301.80.0 | `MSIX\MicrosoftWindows.Client.WebExperience_526.17301.80.0_x64__cw5n1h2txyewy` | MSIX/Store | — |
| WinSCP 6.5.3 | 6.5.3 | `ARP\User\X64\winscp3_is1` | 传统安装器 | — |
| XBOX | 2608.1001.17.0 | `MSIX\Microsoft.GamingApp_2608.1001.17.0_x64__8wekyb3d8bbwe` | MSIX/Store | — |
| Xbox 主机小帮手 | 48.104.4001.0 | `MSIX\Microsoft.XboxApp_48.104.4001.0_x64__8wekyb3d8bbwe` | MSIX/Store | — |
| Xbox Game Bar Plugin | 1.54.4001.0 | `MSIX\Microsoft.XboxGameOverlay_1.54.4001.0_x64__8wekyb3d8bbwe` | MSIX/Store | — |
| Xbox Game Speech Window | 1.21.13002.0 | `MSIX\Microsoft.XboxSpeechToTextOverlay_1.21.13002.0_x64__8wekyb3d8bbwe` | MSIX/Store | — |
| Xbox Identity Provider | 12.130.16001.0 | `MSIX\Microsoft.XboxIdentityProvider_12.130.16001.0_x64__8wekyb3d8bbwe` | MSIX/Store | — |
| Xbox TCUI | 1.24.10001.0 | `MSIX\Microsoft.Xbox.TCUI_1.24.10001.0_x64__8wekyb3d8bbwe` | MSIX/Store | — |
| YARA | 4.5.5 | `VirusTotal.YARA` | winget | — |
| yt-dlp | 2025.12.08 | `yt-dlp.yt-dlp` | winget | 有：2026.07.04 |
| Zed | 1.0.0.0 | `MSIX\ZedIndustries.Zed_1.0.0.0_neutral__japxn1gcva8rg` | MSIX/Store | — |
| Zed | 1.13.1 | `ZedIndustries.Zed` | winget | — |

说明：`ARP` 是传统安装器注册项，`MSIX` 通常来自 Microsoft Store/系统包，`Steam App` 可由 Steam 库恢复。带 winget/msstore ID 的项目可优先尝试 `winget install --id <ID> -e`。

## 注册表补充项

以下程序存在于卸载注册表，但未按完全相同名称出现在 WinGet 结构化结果中；可能是驱动组件、Visual Studio 子组件、旧版运行库或厂商工具。

| 名称 | 版本 | 发布者 | 范围 |
|---|---|---|---|
| 钉钉 | 8.3.45-Release.260720005 | Alibaba (China) Network Technology Co.,Ltd. | Machine-32 |
| 放松时光：与你共享Lo-Fi故事 | — | Nestopi Inc. | Machine-64 |
| 飞书 | 7.73.9 | Beijing Feishu Technology Co., Ltd. | User |
| 腾讯会议 | 3.44.10.457 | 腾讯科技(深圳)有限公司 | Machine-64 |
| 微信 | 4.1.12.26 | 腾讯科技(深圳)有限公司 | Machine-32 |
| 战地风云™ 6 | — | Battlefield Studios | Machine-64 |
| Anaconda3 2025.06-0 (Python 3.13.5 64-bit) | 2025.06-0 | Anaconda, Inc. | User |
| Apifox 2.8.40 | 2.8.40 | Apifox Team | User |
| Burp Suite 2026.6 | 2026.6 | PortSwigger Web Security | Machine-64 |
| DBeaver 26.1.3 (current user) | 26.1.3 | DBeaver Corp | User |
| Go Programming Language amd64 go1.25.4 | 1.25.4 | https://go.dev | Machine-64 |
| ImageMagick 7.1.2-21 Q16-HDRI (64-bit) (2026-04-21) | 7.1.2.21 | ImageMagick Studio LLC | Machine-64 |
| Java 8 Update 481 | 8.0.4810.10 | Oracle Corporation | Machine-32 |
| Java 8 Update 481 (64-bit) | 8.0.4810.10 | Oracle Corporation | Machine-64 |
| Java(TM) SE Development Kit 11.0.28 (64-bit) | 11.0.28.0 | Oracle Corporation | Machine-64 |
| lx-music-desktop 2.12.2 | 2.12.2 | lyswhut | User |
| Microsoft .NET SDK 10.0.100 (x64) | 10.1.25.52411 | Microsoft Corporation | Machine-32 |
| Microsoft .NET SDK 8.0.423 (x64) | 8.4.2326.32602 | Microsoft Corporation | Machine-32 |
| Microsoft Build of OpenJDK  21.0.10+7 (x64) | 21.0.10.7 | Microsoft | Machine-64 |
| Microsoft Visual C++ 2005 Redistributable | 8.0.61187 | Microsoft Corporation | Machine-32 |
| Microsoft Visual C++ 2008 Redistributable - x64 9.0.30729.7523 | 9.0.30729.7523 | Microsoft Corporation | Machine-64 |
| Microsoft Visual C++ 2008 Redistributable - x86 9.0.30729.7523 | 9.0.30729.7523 | Microsoft Corporation | Machine-32 |
| Microsoft Visual C++ 2010  x64 Redistributable - 10.0.40219 | 10.0.40219 | Microsoft Corporation | Machine-64 |
| Microsoft Visual C++ 2010  x86 Redistributable - 10.0.40219 | 10.0.40219 | Microsoft Corporation | Machine-32 |
| Microsoft Visual C++ 2012 Redistributable (x64) - 11.0.61135 | 11.0.61135.400 | Microsoft Corporation | Machine-32 |
| Microsoft Visual C++ 2012 Redistributable (x86) - 11.0.61135 | 11.0.61135.400 | Microsoft Corporation | Machine-32 |
| Microsoft Visual C++ 2013 Redistributable (x64) - 12.0.30501 | 12.0.30501.0 | Microsoft Corporation | Machine-32 |
| Microsoft Visual C++ 2013 Redistributable (x64) - 12.0.40664 | 12.0.40664.0 | Microsoft Corporation | Machine-32 |
| Microsoft Visual C++ 2013 Redistributable (x86) - 12.0.30501 | 12.0.30501.0 | Microsoft Corporation | Machine-32 |
| Microsoft Visual C++ 2013 Redistributable (x86) - 12.0.40664 | 12.0.40664.0 | Microsoft Corporation | Machine-32 |
| Microsoft Visual C++ v14 Redistributable (x64) - 14.51.36247 | 14.51.36247.0 | Microsoft Corporation | Machine-32 |
| Microsoft Visual C++ v14 Redistributable (x86) - 14.51.36247 | 14.51.36247.0 | Microsoft Corporation | Machine-32 |
| Microsoft Visual Studio 2010 Tools for Office Runtime (x64) | 10.0.60833 | Microsoft Corporation | Machine-64 |
| Microsoft Visual Studio Code (User) | 1.119.0 | Microsoft Corporation | User |
| Microsoft Web Deploy 4.0 | 10.0.9419 | Microsoft Corporation | Machine-64 |
| Microsoft Windows Desktop Runtime - 6.0.25 (x64) | 6.0.25.33020 | Microsoft Corporation | Machine-32 |
| Microsoft Windows Desktop Runtime - 8.0.19 (x64) | 8.0.19.35118 | Microsoft Corporation | Machine-32 |
| Microsoft Windows Desktop Runtime - 8.0.6 (x86) | 8.0.6.33720 | Microsoft Corporation | Machine-32 |
| Microsoft XNA Framework Redistributable 1.0 Refresh | 1.1.10405.0 | Microsoft Corporation | Machine-32 |
| Microsoft XNA Framework Redistributable 2.0 | 2.0.11128.1 | Microsoft Corporation | Machine-32 |
| Microsoft XNA Framework Redistributable 3.0 | 3.0.11010.0 | Microsoft Corporation | Machine-32 |
| Microsoft XNA Framework Redistributable 3.1 | 3.1.10527.0 | Microsoft Corporation | Machine-32 |
| Microsoft XNA Framework Redistributable 4.0 Refresh | 4.0.30901.0 | Microsoft Corporation | Machine-32 |
| Multica 0.4.4 | 0.4.4 | Multica | User |
| MySQL Installer | 1.6.15.0 | Oracle Corporation | Machine-32 |
| MySQL Server 8.0 | 8.0.43 | Oracle Corporation | Machine-64 |
| Node.js | 24.14.1 | Node.js Foundation | Machine-64 |
| Notion 7.9.0 | 7.9.0 | Notion Labs, Inc | User |
| NVIDIA PhysX 系统软件 9.23.1019 | 9.23.1019 | NVIDIA Corporation | Machine-64 |
| Ollama version 0.10.1 | 0.10.1 | Ollama | User |
| OpenSSL 3.6.1 Light (64-bit) | 3.6.1 | OpenSSL Win64 Installer Team | Machine-64 |
| Pandoc 3.8.2 | 3.8.2 | John MacFarlane | Machine-64 |
| PostgreSQL 18 | 18.1-2 | PostgreSQL Global Development Group | Machine-64 |
| PotPlayer-64 bit | 26.07.01.0 | Kakao Corp. | Machine-64 |
| PowerToys (Preview) x64 | 0.92.1 | Microsoft Corporation | User |
| Python 3.12.10 (64-bit) | 3.12.10150.0 | Python Software Foundation | User |
| Python 3.9.12 (64-bit) | 3.9.12150.0 | Python Software Foundation | User |
| Radmin VPN 1.4.1 | 1.4.4642.1 | Famatech | Machine-32 |
| Simple Sticky Notes 6.9 | 6.9 | Simnet Ltd. | Machine-32 |
| Visual Studio 生成工具 2022 | 17.14.35 | Microsoft Corporation | Machine-32 |
| Wallpaper Engine：壁纸引擎 | — | Wallpaper Engine Team | Machine-64 |
| Windows Software Development Kit - Windows 10.0.26100.7705 | 10.1.26100.7705 | Microsoft Corporation | Machine-32 |

## 便携程序与快捷方式补充

这些条目来自桌面和开始菜单；它们可能与上表重复，但可帮助发现便携软件、厂商启动器或安装目录。

| 快捷方式 | 目标 | 位置 |
|---|---|---|
| 百度网盘 | `E:\BaiduNetdisk\BaiduNetdisk.exe` | Desktop |
| 哔哩哔哩 (゜-゜)つロ 干杯~-bilibili | `C:\Program Files\Google\Chrome\Application\chrome_proxy.exe` | Desktop |
| 钉钉 | `E:\04_Toolbox\DingDing\DingtalkLauncher.exe` | Machine Start Menu |
| 豆包 | `E:\04_Toolbox\Doubao\Doubao.exe` | User Start Menu |
| 飞书 | `E:\04_Toolbox\Feishu\Feishu.exe` | User Start Menu |
| 飞书 | `E:\04_Toolbox\Feishu\Feishu.exe` | Desktop |
| 关于 Java | `C:\Program Files\Java\jre1.8.0_481\bin\javacpl.exe` | Machine Start Menu |
| 火绒安全软件 | `C:\Program Files\Huorong\Sysdiag\bin\HipsMain.exe` | Machine Start Menu |
| 火绒日志 | `C:\Program Files\Huorong\Sysdiag\bin\HipsLog.exe` | Machine Start Menu |
| 极客战记.bat | `E:\githubitem\极客战记\codecombat-win\极客战记.bat` | Desktop |
| 检查更新 | `C:\Program Files\Java\jre1.8.0_481\bin\javacpl.exe` | Machine Start Menu |
| 墨将助手 | `F:\games_gongjv\BIGBIG WON\BigBigWonAssistant.exe` | User Start Menu |
| 您的 Chrome - Chrome | `C:\Program Files\Google\Chrome\Application\chrome.exe` | Desktop |
| 欧路词典 eudic | `E:\04_Toolbox\eudic\eudic.exe` | Machine Start Menu |
| 配置 Java | `C:\Program Files\Java\jre1.8.0_481\bin\javacpl.exe` | Machine Start Menu |
| 软件教程 | `D:\Material_processing\xiaowan\软件教程.url` | Machine Start Menu |
| 腾讯会议 | `E:\txhy\WeMeet\WeMeetApp.exe` | Machine Start Menu |
| 网易有道翻译 | `E:\04_Toolbox\Dict\YoudaoDict.exe` | Machine Start Menu |
| 网易云音乐 | `F:\Music_player\CloudMusic\cloudmusic.exe` | Machine Start Menu |
| 微信 | `F:\Chat\WeChat\Weixin\Weixin.exe` | Machine Start Menu |
| 微信输入法 | `C:\Program Files\Tencent\WeType\2.1.1.8\wetype_update.exe` | Machine Start Menu |
| 小丸工具箱 | `C:\Windows\Installer\{7EEB2DD0-264B-4340-B6BE-F05D99066D3C}\xiaowan.exe_C91A08E04E3646B7B443E9F9DA0D73A8.exe` | Machine Start Menu |
| 小丸拾色器 | `C:\Windows\Installer\{7EEB2DD0-264B-4340-B6BE-F05D99066D3C}\GetColor.exe_9F12C2F83CE342C3ABE60FE65BFFCB33.exe` | Machine Start Menu |
| 虚拟网络编辑器 | `E:\VMware\VM\vmnetcfg.exe` | Machine Start Menu |
| 学习记录管理器 | `E:\04_Toolbox\eudic\eudic.exe` | Machine Start Menu |
| 自定义 Fences | `C:\Program Files (x86)\Stardock\Fences\Fences.exe` | Desktop |
| Access | `C:\Program Files\Microsoft Office\root\Office16\MSACCESS.EXE` | Machine Start Menu |
| Administrative Tools | `C:\WINDOWS\system32\control.exe` | User Start Menu |
| Anaconda Navigator | `E:\gongjv_yilai\anaconda\pythonw.exe` | User Start Menu |
| Anaconda PowerShell Prompt | `C:\Windows\System32\WindowsPowerShell\v1.0\powershell.exe` | User Start Menu |
| Anaconda Prompt | `C:\Windows\System32\cmd.exe` | User Start Menu |
| Android Studio | `E:\gongjv_kai_fa_\apk_nixiang\AndroidStudio\bin\studio64.exe` | Machine Start Menu |
| Apifox | `E:\04_Toolbox\Apifox\Apifox.exe` | User Start Menu |
| Apifox | `E:\04_Toolbox\Apifox\Apifox.exe` | Desktop |
| Application Stack Builder | `C:\Program Files\PostgreSQL\18\bin\stackbuilder.exe` | Machine Start Menu |
| Application Verifier (WOW) | `C:\Windows\SysWOW64\appverif.exe` | Machine Start Menu |
| Application Verifier (X64) | `C:\Windows\System32\appverif.exe` | Machine Start Menu |
| Bandizip.x64 | `E:\香草工具箱\Bandizip-Professional-7.36-All-Portable\Bandizip.x64.exe` | Desktop |
| Burp Suite | `C:\Program Files\BurpSuiteCommunity\BurpSuite.exe` | Machine Start Menu |
| Camoufox Private Browsing | `C:\Users\Meiosis\AppData\Local\camoufox\camoufox\Cache\private_browsing.exe` | User Start Menu |
| CC Switch | `C:\Users\Meiosis\AppData\Local\Programs\CC Switch\cc-switch.exe` | User Start Menu |
| CC Switch | `C:\Users\Meiosis\AppData\Local\Programs\CC Switch\cc-switch.exe` | Desktop |
| Character Map | `C:\WINDOWS\system32\charmap.exe` | Machine Start Menu |
| Cisco Packet Tracer Help | `E:\gongjv_kai_fa_\思科\Cisco Packet Tracer 6.2sv\help\default\index.htm` | Machine Start Menu |
| Cisco Packet Tracer Student | `E:\gongjv_kai_fa_\思科\Cisco Packet Tracer 6.2sv\bin\PacketTracer6.exe` | Machine Start Menu |
| Clash Verge | `C:\Program Files\Clash Verge\clash-verge.exe` | Machine Start Menu |
| CMake (cmake-gui) | `C:\Program Files\CMake\bin\cmake-gui.exe` | Machine Start Menu |
| CMake Documentation | `C:\Program Files\CMake\doc\cmake\html\index.html` | Machine Start Menu |
| Cockpit Tools | `E:\gongjv_guan_li_\Cockpit Tools\cockpit-tools.exe` | User Start Menu |
| Command Prompt | `C:\WINDOWS\system32\cmd.exe` | User Start Menu |
| Component Services | `C:\WINDOWS\system32\comexp.msc` | Machine Start Menu |
| Computer Management | `C:\WINDOWS\system32\compmgmt.msc` | Machine Start Menu |
| DBeaver | `C:\Users\Meiosis\AppData\Local\DBeaver\dbeaver.exe` | User Start Menu |
| Debuggable Package Manager | `C:\Windows\SysWOW64\WindowsPowerShell\v1.0\powershell.exe` | Machine Start Menu |
| Developer Command Prompt for VS | `C:\Windows\System32\cmd.exe` | Machine Start Menu |
| Developer Command Prompt for VS 2022 | `C:\Windows\System32\cmd.exe` | Machine Start Menu |
| Developer PowerShell for VS | `C:\Windows\SysWOW64\WindowsPowerShell\v1.0\powershell.exe` | Machine Start Menu |
| Developer PowerShell for VS 2022 | `C:\Windows\SysWOW64\WindowsPowerShell\v1.0\powershell.exe` | Machine Start Menu |
| dfrgui | `C:\WINDOWS\system32\dfrgui.exe` | Machine Start Menu |
| DingTalk Official Website | `E:\04_Toolbox\DingDing\DingTalk Official Website.url` | Machine Start Menu |
| Disk Cleanup | `C:\WINDOWS\system32\cleanmgr.exe` | Machine Start Menu |
| Docker Desktop | `C:\Program Files\Docker\Docker\Docker Desktop.exe` | User Start Menu |
| Docker Desktop | `C:\Program Files\Docker\Docker\Docker Desktop.exe` | Desktop |
| Documentation for Desktop Apps | `C:\Program Files (x86)\Windows Kits\10\Shortcuts\DesktopAppsDocumentation.url` | Machine Start Menu |
| Documentation for UWP Apps | `C:\Program Files (x86)\Windows Kits\10\Shortcuts\UWPAppsDocumentation.url` | Machine Start Menu |
| Event Viewer | `C:\WINDOWS\system32\eventvwr.msc` | Machine Start Menu |
| Excel | `C:\Program Files\Microsoft Office\root\Office16\EXCEL.EXE` | Machine Start Menu |
| EZ CD Audio Converter | `D:\Material_processing\EZ CD Audio Converter\ezcd.exe` | Machine Start Menu |
| Fences | `C:\Program Files (x86)\Stardock\Fences\Fences.exe` | Machine Start Menu |
| Firefox | `C:\Program Files\Mozilla Firefox\firefox.exe` | Machine Start Menu |
| Firefox 隐私浏览 | `C:\Program Files\Mozilla Firefox\private_browsing.exe` | Machine Start Menu |
| Git Bash | `C:\Program Files\Git\git-bash.exe` | Machine Start Menu |
| Git CMD | `C:\Program Files\Git\git-cmd.exe` | Machine Start Menu |
| Git GUI | `C:\Program Files\Git\cmd\git-gui.exe` | Machine Start Menu |
| Git Release Notes | `C:\Program Files\Git\ReleaseNotes.html` | Machine Start Menu |
| GlaryUtilitiesPortable | `E:\香草工具箱\GlaryUtilities-Pro-v6.28.0.32-Portable\GlaryUtilities\GlaryUtilitiesPortable.exe` | Desktop |
| Google Chrome | `C:\Program Files\Google\Chrome\Application\chrome.exe` | Machine Start Menu |
| Google Chrome (Ubuntu) | `C:\Program Files\WSL\wslg.exe` | User Start Menu |
| GPUView | `C:\Program Files (x86)\Windows Kits\10\Windows Performance Toolkit\gpuview\GPUView.exe` | Machine Start Menu |
| HBuilder X | `E:\duoduankaifa\HBuilderX.4.87.2025121004\HBuilderX\HBuilderX.exe` | Desktop |
| hi | `C:\Users\Meiosis\AppData\Local\hi\REDcity.exe` | User Start Menu |
| hi | `C:\Users\Meiosis\AppData\Local\hi\REDcity.exe` | Desktop |
| HireMe AI | `E:\04_Toolbox\Electron\Electron.exe` | User Start Menu |
| HireMe AI | `E:\04_Toolbox\Electron\Electron.exe` | Desktop |
| Hyper-V Manager | `C:\WINDOWS\System32\mmc.exe` | Machine Start Menu |
| IDA Pro (32-bit) | `E:\gongjv_kai_fa_\IDA 7.0\ida.exe` | Machine Start Menu |
| IDA Pro (32-bit) | `E:\gongjv_kai_fa_\IDA 7.0\ida.exe` | Desktop |
| IDA Pro (64-bit) | `E:\gongjv_kai_fa_\IDA 7.0\ida64.exe` | Machine Start Menu |
| IDA Pro (64-bit) | `E:\gongjv_kai_fa_\IDA 7.0\ida64.exe` | Desktop |
| IDLE (Python 3.11 64-bit) | `C:\Program Files\Python311\pythonw.exe` | Machine Start Menu |
| IDLE (Python 3.12 64-bit) | `C:\Users\Meiosis\AppData\Local\Programs\Python\Python312\pythonw.exe` | User Start Menu |
| IDLE (Python 3.9 64-bit) | `C:\Program Files\Python39\pythonw.exe` | Machine Start Menu |
| ImageConverter | `C:\Program Files\ImageConverter\ImageConverter.exe` | Machine Start Menu |
| ImageConverter | `C:\Program Files\ImageConverter\ImageConverter.exe` | Desktop |
| ImageMagick Web Pages | `C:\Program Files\ImageMagick-7.1.2-Q16-HDRI\index.html` | Machine Start Menu |
| Inno Setup Compiler | `C:\Users\Meiosis\AppData\Local\Temp\ggr-inno-setup-6.7.1\Compil32.exe` | Machine Start Menu |
| Inno Setup Documentation | `C:\Users\Meiosis\AppData\Local\Temp\ggr-inno-setup-6.7.1\ISetup.chm` | Machine Start Menu |
| Inno Setup Documentation (Dark) | `C:\Users\Meiosis\AppData\Local\Temp\ggr-inno-setup-6.7.1\ISetup-dark.chm` | Machine Start Menu |
| Inno Setup Example Scripts | `C:\Users\Meiosis\AppData\Local\Temp\ggr-inno-setup-6.7.1\Examples` | Machine Start Menu |
| Inno Setup FAQ | `C:\Users\Meiosis\AppData\Local\Temp\ggr-inno-setup-6.7.1\isfaq.url` | Machine Start Menu |
| Inno Setup Revision History | `C:\Users\Meiosis\AppData\Local\Temp\ggr-inno-setup-6.7.1\whatsnew.htm` | Machine Start Menu |
| Install Additional Tools for Node.js | `C:\Windows\System32\cmd.exe` | Machine Start Menu |
| iSCSI Initiator | `C:\WINDOWS\system32\iscsicpl.exe` | Machine Start Menu |
| JADX GUI | `C:\ProgramData\chocolatey\lib\jadx\tools\bin\jadx-gui.bat` | Machine Start Menu |
| Jupyter Notebook | `E:\gongjv_yilai\anaconda\python.exe` | User Start Menu |
| Kettle 9.2 | `D:\Kettle-9.2\Start-Kettle.cmd` | Desktop |
| leigod | `F:\LeiGod_Acc\leigod.exe` | Desktop |
| LiveCaptions | `C:\WINDOWS\system32\LiveCaptions.exe` | User Start Menu |
| LX Music | `F:\Music_player\lx_music\lx-music-desktop\lx-music-desktop.exe` | Desktop |
| MAA | `F:\Maa\MAA.exe` | Desktop |
| Magnify | `C:\WINDOWS\system32\magnify.exe` | User Start Menu |
| Maxon | `C:\Program Files\Maxon\App Manager\Maxon.exe` | Machine Start Menu |
| Memory Diagnostics Tool | `C:\WINDOWS\system32\MdSched.exe` | Machine Start Menu |
| Microsoft .NET Framework 1.1 Configuration | `C:\Windows\Microsoft.NET\Framework\v1.1.4322\mscorcfg.msc` | Machine Start Menu |
| Microsoft .NET Framework 1.1 Wizards | `C:\Windows\Microsoft.NET\Framework\v1.1.4322\ConfigWizards.exe` | Machine Start Menu |
| Microsoft Edge | `C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe` | Desktop |
| mkvtoolnix | `D:\Material_processing\MKVToolNix_94.0.0_Green_64Bit\MKVToolNix_94.0.0_Green_64Bit\MKV 处理工具(MKVToolNix)94.0.0.x64中文精简绿色便携版\mkvtoolnix-gui.exe` | Desktop |
| Multica | `C:\Users\Meiosis\AppData\Local\Programs\@multicadesktop\Multica.exe` | User Start Menu |
| MuMu模拟器 | `F:\Emulator\MuMuPlayer\nx_main\MuMuNxMain.exe` | User Start Menu |
| MuMu模拟器 | `F:\Emulator\MuMuPlayer\nx_main\MuMuNxMain.exe` | Desktop |
| MusicLyricApp-v7.1-win-x64 | `D:\Material_processing\MusicLyricApp-v7.1-win-x64\MusicLyricApp-v7.1-win-x64.exe` | Desktop |
| MySQL 8.0 Command Line Client | `C:\Program Files\MySQL\MySQL Server 8.0\bin\mysql.exe` | Machine Start Menu |
| MySQL 8.0 Command Line Client - Unicode | `C:\Program Files\MySQL\MySQL Server 8.0\bin\mysql.exe` | Machine Start Menu |
| MySQL Installer - Community | `C:\Program Files (x86)\MySQL\MySQL Installer for Windows\MySQLInstaller.exe` | Machine Start Menu |
| Narrator | `C:\WINDOWS\system32\narrator.exe` | User Start Menu |
| navicat | `E:\Navicat Premium\Navicat Premium 17\navicat.exe` | Desktop |
| Node.js | `E:\Program Files\nodejs\node.exe` | Machine Start Menu |
| Node.js command prompt | `C:\Windows\System32\cmd.exe` | Machine Start Menu |
| Notion | `C:\Users\Meiosis\AppData\Local\Programs\Notion\Notion.exe` | User Start Menu |
| Notion | `C:\Users\Meiosis\AppData\Local\Programs\Notion\Notion.exe` | Desktop |
| NVIDIA App | `C:\Program Files\NVIDIA Corporation\NVIDIA App\CEF\NVIDIA App.exe` | Machine Start Menu |
| OBS | `C:\feat\obs\bin\64bit\obs64.exe` | Desktop |
| Obsidian | `E:\NoteBook\Obsidian\Obsidian.exe` | User Start Menu |
| Obsidian | `E:\NoteBook\Obsidian\Obsidian.exe` | Desktop |
| ODBC Data Sources (32-bit) | `C:\WINDOWS\syswow64\odbcad32.exe` | Machine Start Menu |
| ODBC Data Sources (64-bit) | `C:\WINDOWS\system32\odbcad32.exe` | Machine Start Menu |
| Office 语言首选项 | `C:\Program Files\Microsoft Office\root\Office16\SETLANG.EXE` | Machine Start Menu |
| On-Screen Keyboard | `C:\WINDOWS\system32\osk.exe` | User Start Menu |
| OneDrive | `C:\Program Files\Microsoft OneDrive\OneDrive.exe` | Machine Start Menu |
| OneNote | `C:\Program Files\Microsoft Office\root\Office16\ONENOTE.EXE` | Machine Start Menu |
| OpenCode | `C:\Users\Meiosis\scoop\apps\opencode\current\opencode.exe` | User Start Menu |
| Orca | `C:\Users\Meiosis\AppData\Local\Programs\orca\Orca.exe` | User Start Menu |
| Orca | `C:\Users\Meiosis\AppData\Local\Programs\orca\Orca.exe` | Desktop |
| Pandoc User’s Guide | `C:\Program Files\Pandoc\Pandoc User's Guide.html` | Machine Start Menu |
| PasteMD | `E:\香草工具箱\PasteMD\PasteMD.exe` | Machine Start Menu |
| Performance Monitor | `C:\WINDOWS\system32\perfmon.msc` | Machine Start Menu |
| pgAdmin 4 | `C:\Program Files\PostgreSQL\18\pgAdmin 4\runtime\pgAdmin4.exe` | Machine Start Menu |
| PixPin | `E:\香草工具箱\PixPin\PixPin.exe` | User Start Menu |
| PixPin | `E:\香草工具箱\PixPin\PixPin.exe` | Desktop |
| Plain Craft Launcher 2 - 快捷方式 | `F:\PCL\PCL 正式版 2.8.12\Plain Craft Launcher 2.exe` | Desktop |
| PotPlayer 64 bit | `D:\PotPlayer\PotPlayerMini64.exe` | Machine Start Menu |
| PowerPoint | `C:\Program Files\Microsoft Office\root\Office16\POWERPNT.EXE` | Machine Start Menu |
| Python 3.11 (64-bit) | `C:\Program Files\Python311\python.exe` | Machine Start Menu |
| Python 3.11 Manuals (64-bit) | `C:\Program Files\Python311\Doc\html\index.html` | Machine Start Menu |
| Python 3.11 Module Docs (64-bit) | `C:\Program Files\Python311\python.exe` | Machine Start Menu |
| Python 3.12 (64-bit) | `C:\Users\Meiosis\AppData\Local\Programs\Python\Python312\python.exe` | User Start Menu |
| Python 3.12 Manuals (64-bit) | `C:\Users\Meiosis\AppData\Local\Programs\Python\Python312\Doc\html\index.html` | User Start Menu |
| Python 3.12 Module Docs (64-bit) | `C:\Users\Meiosis\AppData\Local\Programs\Python\Python312\python.exe` | User Start Menu |
| Python 3.9 (64-bit) | `C:\Program Files\Python39\python.exe` | Machine Start Menu |
| Python 3.9 (64-bit) | `C:\Program Files\Python39\python.exe` | User Start Menu |
| Python 3.9 Module Docs (64-bit) | `C:\Program Files\Python39\python.exe` | Machine Start Menu |
| QQ | `F:\Chat\QQ\QQ.exe` | Machine Start Menu |
| Qt Linguist | `E:\gongjv_kai_fa_\思科\Cisco Packet Tracer 6.2sv\bin\linguist.exe` | Machine Start Menu |
| Radmin Viewer 3 | `C:\Program Files (x86)\Radmin VPN\Radmin.exe` | Machine Start Menu |
| Radmin VPN | `C:\Program Files (x86)\Radmin VPN\RvRvpnGui.exe` | Machine Start Menu |
| Rapture3D - Speaker Layout | `C:\Program Files (x86)\Blue Ripple Sound\UserLayout.exe` | Machine Start Menu |
| Rapture3D - User Guide | `C:\Program Files (x86)\Blue Ripple Sound\Rapture3DGame_UserGuide_v2.7.4.pdf` | Machine Start Menu |
| RecoveryDrive | `C:\WINDOWS\system32\RecoveryDrive.exe` | Machine Start Menu |
| REDpass | `C:\Program Files\REDpass\REDpass.exe` | Machine Start Menu |
| Registry Editor | `C:\WINDOWS\regedit.exe` | Machine Start Menu |
| Reload Configuration | `C:\Program Files\PostgreSQL\18\bin\pg_ctl.exe` | Machine Start Menu |
| Remote Desktop Connection | `C:\WINDOWS\system32\mstsc.exe` | Machine Start Menu |
| Resource Monitor | `C:\WINDOWS\system32\perfmon.exe` | Machine Start Menu |
| Sample Desktop Apps | `C:\Program Files (x86)\Windows Kits\10\Shortcuts\DesktopAppsSamples.url` | Machine Start Menu |
| Sample UWP Apps | `C:\Program Files (x86)\Windows Kits\10\Shortcuts\UWPAppsSamples.url` | Machine Start Menu |
| Saves | `E:\gongjv_kai_fa_\思科\Cisco Packet Tracer 6.2sv\saves` | Machine Start Menu |
| Security Configuration Management | `C:\WINDOWS\system32\secpol.msc` | Machine Start Menu |
| services | `C:\WINDOWS\system32\services.msc` | Machine Start Menu |
| Simple Sticky Notes | `E:\04_Toolbox\Simple Sticky Notes\ssn.exe` | Machine Start Menu |
| Simple Sticky Notes | `E:\04_Toolbox\Simple Sticky Notes\ssn.exe` | Desktop |
| SPlayer | `F:\Music_player\SPlayer\SPlayer.exe` | User Start Menu |
| SPlayer | `F:\Music_player\SPlayer\SPlayer.exe` | Desktop |
| Spreadsheet Compare | `C:\Program Files\Microsoft Office\root\Client\AppVLP.exe` | Machine Start Menu |
| Spyder | `E:\gongjv_yilai\anaconda\pythonw.exe` | User Start Menu |
| SQL Shell (psql) | `C:\Program Files\PostgreSQL\18\scripts\runpsql.bat` | Machine Start Menu |
| Steam | `F:\Steam\Steam.exe` | Machine Start Menu |
| Steam | `F:\Steam\steam.exe` | User Start Menu |
| Steps Recorder | `C:\WINDOWS\system32\psr.exe` | Machine Start Menu |
| STranslate | `E:\04_Toolbox\VanillaToolbox\STranslate-win-Portable\current\STranslate.exe` | User Start Menu |
| System Configuration | `C:\WINDOWS\system32\msconfig.exe` | Machine Start Menu |
| System Information | `C:\WINDOWS\system32\msinfo32.exe` | Machine Start Menu |
| Tailscale | `C:\Program Files\Tailscale\tailscale-ipn.exe` | Machine Start Menu |
| Task Manager | `C:\WINDOWS\system32\taskmgr.exe` | Machine Start Menu |
| Task Scheduler | `C:\WINDOWS\system32\taskschd.msc` | Machine Start Menu |
| Telegram | `C:\Users\Meiosis\AppData\Roaming\Telegram Desktop\Telegram.exe` | User Start Menu |
| Telegram | `F:\Chat\Telegram\Telegram Desktop\Telegram.exe` | User Start Menu |
| Telegram | `F:\Chat\Telegram\Telegram Desktop\Telegram.exe` | Desktop |
| The Interactive Disassembler help | `E:\gongjv_kai_fa_\IDA 7.0\idahelp.chm` | Machine Start Menu |
| ToDesk | `E:\ycapp\Todesk\ToDesk.exe` | Machine Start Menu |
| Tools for Desktop Apps | `C:\Program Files (x86)\Windows Kits\10\Shortcuts\DesktopAppsToolsDocumentation.url` | Machine Start Menu |
| Tools for UWP Apps | `C:\Program Files (x86)\Windows Kits\10\Shortcuts\UWPAppsToolsDocumentation.url` | Machine Start Menu |
| UU加速器 | `F:\Netease\UU\uu_launcher.exe` | Machine Start Menu |
| UU远程 | `E:\ycapp\GameViewer\GameViewer.exe` | Desktop |
| vctl 的命令提示符 | `C:\Windows\System32\cmd.exe` | Machine Start Menu |
| Visual Studio Code | `E:\gongjv_kai_fa_\IDE\Microsoft VS Code\Code.exe` | User Start Menu |
| Visual Studio Code | `E:\gongjv_kai_fa_\IDE\Microsoft VS Code\Code.exe` | Desktop |
| Visual Studio Installer | `C:\Program Files (x86)\Microsoft Visual Studio\Installer\setup.exe` | Machine Start Menu |
| VMCreate | `C:\Program Files\Hyper-V\VMCreate.exe` | Machine Start Menu |
| VMware Workstation 17 Player | `E:\VMware\VM\vmplayer.exe` | Machine Start Menu |
| VMware Workstation Pro | `E:\VMware\VM\vmware.exe` | Machine Start Menu |
| VoiceAccess | `C:\WINDOWS\system32\voiceaccess.exe` | User Start Menu |
| Wave | `E:\waveterm\Wave.exe` | User Start Menu |
| Wave Terminal | `E:\waveterm\Wave.exe` | Desktop |
| WGestures 2 | `C:\Program Files\WGestures 2\WGestures.exe` | Machine Start Menu |
| Win64 OpenSSL Command Prompt | `C:\Program Files\OpenSSL-Win64\start.bat` | Machine Start Menu |
| Windows App Cert Kit | `C:\Program Files (x86)\Windows Kits\10\App Certification Kit\appcertui.exe` | Machine Start Menu |
| Windows Defender Firewall with Advanced Security | `C:\WINDOWS\system32\WF.msc` | Machine Start Menu |
| Windows Fax and Scan | `C:\WINDOWS\system32\WFS.exe` | Machine Start Menu |
| Windows Media Player Legacy | `C:\Program Files (x86)\Windows Media Player\wmplayer.exe` | Machine Start Menu |
| Windows Performance Analyzer | `C:\Program Files (x86)\Windows Kits\10\Windows Performance Toolkit\wpa.exe` | Machine Start Menu |
| Windows Performance Recorder | `C:\Program Files (x86)\Windows Kits\10\Windows Performance Toolkit\WPRUI.exe` | Machine Start Menu |
| Windows PowerShell | `C:\Windows\System32\WindowsPowerShell\v1.0\powershell.exe` | User Start Menu |
| Windows PowerShell (x86) | `C:\Windows\SysWOW64\WindowsPowerShell\v1.0\powershell.exe` | User Start Menu |
| Windows PowerShell ISE | `C:\WINDOWS\system32\WindowsPowerShell\v1.0\PowerShell_ISE.exe` | Machine Start Menu |
| Windows PowerShell ISE (x86) | `C:\WINDOWS\syswow64\WindowsPowerShell\v1.0\PowerShell_ISE.exe` | Machine Start Menu |
| Windows Software Development Kit | `C:\WINDOWS\explorer.exe` | Machine Start Menu |
| WinSCP | `E:\香草工具箱\WinSCP\WinSCP.exe` | Desktop |
| Word | `C:\Program Files\Microsoft Office\root\Office16\WINWORD.EXE` | Machine Start Menu |
| WSL | `C:\WINDOWS\Installer\{0C25A4AA-B7AC-4436-8BCC-017CEDB0E43A}\wsl.ico` | Machine Start Menu |
| WSL Settings | `C:\WINDOWS\Installer\{0C25A4AA-B7AC-4436-8BCC-017CEDB0E43A}\wsl.ico` | Machine Start Menu |
| x64 Native Tools Command Prompt for VS | `C:\Windows\System32\cmd.exe` | Machine Start Menu |
| x64 Native Tools Command Prompt for VS 2022 | `C:\Windows\System32\cmd.exe` | Machine Start Menu |
| x64_x86 Cross Tools Command Prompt for VS | `C:\Windows\System32\cmd.exe` | Machine Start Menu |
| x64_x86 Cross Tools Command Prompt for VS 2022 | `C:\Windows\System32\cmd.exe` | Machine Start Menu |
| x86 Native Tools Command Prompt for VS | `C:\Windows\System32\cmd.exe` | Machine Start Menu |
| x86 Native Tools Command Prompt for VS 2022 | `C:\Windows\System32\cmd.exe` | Machine Start Menu |
| x86_x64 Cross Tools Command Prompt for VS | `C:\Windows\System32\cmd.exe` | Machine Start Menu |
| x86_x64 Cross Tools Command Prompt for VS 2022 | `C:\Windows\System32\cmd.exe` | Machine Start Menu |
| XTerminal | `E:\gongjv_guan_li_\XTerminal\XTerminal.exe` | User Start Menu |
| Zed | `E:\gongjv_kai_fa_\Zed\Zed.exe` | User Start Menu |
| Zed | `E:\gongjv_kai_fa_\Zed\Zed.exe` | Desktop |
| Zutty (Ubuntu) | `C:\Program Files\WSL\wslg.exe` | User Start Menu |

## VS Code 扩展

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
ms-toolsai.jupyter-keymap@1.1.2
ms-toolsai.jupyter-renderers@1.3.0
ms-toolsai.jupyter@2025.9.1
ms-toolsai.vscode-jupyter-cell-tags@0.1.9
ms-toolsai.vscode-jupyter-slideshow@0.1.6
ms-vscode-remote.remote-containers@0.466.0
ms-vscode-remote.remote-wsl@0.104.3
ms-vscode.cmake-tools@1.23.52
ms-vscode.cpp-devtools@0.5.13
ms-vscode.cpptools-extension-pack@1.5.1
ms-vscode.cpptools-themes@2.0.0
ms-vscode.cpptools@1.33.6
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

恢复命令示例：`code --install-extension publisher.extension`。

## Conda 环境

- `E:\gongjv_yilai\anaconda`
- `E:\gongjv_yilai\anaconda\envs\XianYu`
- `E:\gongjv_yilai\anaconda\envs\astrbot`
- `E:\gongjv_yilai\anaconda\envs\frida17`
- `E:\gongjv_yilai\anaconda\envs\ghidra-mcp`
- `E:\gongjv_yilai\anaconda\envs\hooker39`
- `E:\gongjv_yilai\anaconda\envs\mitmproxy311`
- `E:\gongjv_yilai\anaconda\envs\xhs`

环境本身建议用项目的 `environment.yml` / `requirements.txt` 重建，不复制整个环境目录。

## npm 全局包

| 包 | 版本 |
|---|---|
| `@alibaba-group/open-code-review` | 1.8.7 |
| `@anthropic-ai/claude-code` | 2.1.231 |
| `@deepseek-ai/dsh` | 0.1.0-rc.6 |
| `@google/gemini-cli` | 0.49.0 |
| `@jackwener/opencli` | 1.7.4 |
| `@jinzcdev/markmap-mcp-server` | 0.1.1 |
| `@modelcontextprotocol/server-github` | 2025.4.8 |
| `@modelcontextprotocol/server-sequential-thinking` | 2026.7.4 |
| `@musistudio/claude-code-router` | 2.0.0 |
| `@openai/codex` | 0.147.0 |
| `@quasar/cli` | 2.5.0 |
| `@upstash/context7-mcp` | 3.2.1 |
| `@z_ai/coding-helper` | 0.0.6 |
| `9router` | 0.4.27 |
| `better-sqlite3` | 12.6.2 |
| `chrome-devtools-mcp` | 0.12.1 |
| `codewhale` | 0.8.47 |
| `fast-context-mcp` | 1.4.2 |
| `firecrawl-mcp` | 3.20.4 |
| `gemini-cli-chinese` | 0.1.0 |
| `hexo-cli` | 4.3.2 |
| `mcp-chrome-bridge` | 1.0.31 |
| `mcporter` | 0.7.3 |
| `oh-my-codex` | 0.20.1 |
| `opencode-ai` | 1.18.18 |
| `pm2` | 7.0.1 |
| `pnpm` | 11.5.2 |
| `pptxgenjs` | 4.0.1 |
| `token-optimizer-mcp` | 2.17.0 |
| `ui-ux-pro-max-cli` | 2.11.0 |
| `uipro-cli` | 2.2.3 |
| `wrangler` | 4.90.0 |
| `xreach-cli` | 0.3.0 |

恢复时先安装当前 Node.js LTS，再按需要执行 `npm install -g <package>`；不要机械恢复已经废弃或由其他工具托管的全局包。

## 重装核对

- [ ] 从芯片组、显卡、网卡、声卡和 MuMu 虚拟显示驱动开始。
- [ ] 安装 PowerShell、Windows Terminal、Git、GitHub CLI。
- [ ] 安装语言运行时和编译工具链，再恢复编辑器与数据库工具。
- [ ] 安装 AI Agent/代理工具并从脱敏配置模板恢复。
- [ ] 安装 MuMu 模拟器 6.5.1.0 或兼容新版，重建实例 1 后恢复加密的助手配置。
- [ ] 最后安装日常软件和游戏，并逐个验证账号登录。
