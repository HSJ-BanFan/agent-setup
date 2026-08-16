# dsh/install.ps1 — 新机一键复刻 DSH(DeepSeek Harness)配置
# 用法:
#   .\dsh\install.ps1                 # 完整安装(配置 + 技能)
#   .\dsh\install.ps1 -SkipSkills     # 只装配置
#   .\dsh\install.ps1 -DryRun         # 只打印将要做什么
#
# 遵循 RULES.md:先备份再覆盖;密钥不入库,只做指引。
param(
  [switch]$SkipSkills,
  [switch]$DryRun
)
$ErrorActionPreference = "Stop"
$DshHome = if ($env:DSH_HOME) { $env:DSH_HOME } else { Join-Path $HOME ".dsh" }
$ProfileDir = Join-Path $DshHome "profiles\web"
$Stamp = Get-Date -Format "yyyyMMdd-HHmmss"

function Backup-IfExists($path) {
  if (Test-Path $path) {
    $bak = "$path.bak-$Stamp"
    Copy-Item $path $bak -Force
    Write-Host "[dsh] 备份: $bak"
  }
}

Write-Host "==== DSH 配置复刻 ===="
Write-Host "DSH_HOME = $DshHome"

# 0) 检查 dsh
$dsh = Get-Command dsh -ErrorAction SilentlyContinue
if (-not $dsh) {
  Write-Host "[dsh] 未找到 dsh 命令。请先安装并启动一次 Web 界面:"
  Write-Host "      npx @deepseek-ai/dsh web   (首次运行会自动初始化 web profile)"
  Write-Host "      或: npm i -g @deepseek-ai/dsh"
  if (-not $DryRun) { Write-Host "[dsh] 中止安装(配置目录可能尚未初始化)" }
}

# 1) settings.yaml(模型 provider / 权限预设 / agent 默认模型)
$targetSettings = Join-Path $DshHome "settings.yaml"
$srcSettings = Join-Path $PSScriptRoot "settings.yaml"
if ($DryRun) {
  Write-Host "[dsh] 将写入: $targetSettings"
} else {
  Backup-IfExists $targetSettings
  Copy-Item $srcSettings $targetSettings -Force
  Write-Host "[dsh] settings.yaml 已写入(无密钥,仅 provider 声明 + apiKeyEnv 引用)"
}

# 2) cordis.patch.yml(web profile 的 MCP 服务器配置)
$targetPatch = Join-Path $ProfileDir "cordis.patch.yml"
if ($DryRun) {
  Write-Host "[dsh] 将写入: $targetPatch"
} else {
  New-Item $ProfileDir -ItemType Directory -Force | Out-Null
  Backup-IfExists $targetPatch
  Copy-Item (Join-Path $PSScriptRoot "cordis.patch.yml") $targetPatch -Force
  Write-Host "[dsh] cordis.patch.yml 已写入(MCP: playwright / github / devtools)"
  Write-Host "[dsh] 注意: web profile 的宿主 HMR 被禁用,修改此文件后必须重启 dsh web"
}

# 3) 技能同步
if (-not $SkipSkills -and -not $DryRun) {
  Write-Host "[dsh] 同步技能库 ..."
  & (Join-Path $PSScriptRoot "skills.ps1")
}

# 4) 预设安装(router-standard / anchored-standard → ~/.dsh/.agent-presets)
$presetRoot = Join-Path $DshHome ".agent-presets"
$srcPresets = Join-Path $PSScriptRoot "presets"
if (Test-Path $srcPresets) {
  Write-Host "[dsh] 同步预设到 $presetRoot ..."
  New-Item $presetRoot -ItemType Directory -Force | Out-Null
  Get-ChildItem $srcPresets -Directory | ForEach-Object {
    $target = Join-Path $presetRoot $_.Name
    if ($DryRun) {
      Write-Host "[dsh] 将写入预设: $target"
    } else {
      if (Test-Path $target) {
        $bak = "$target.bak-$Stamp"
        Move-Item $target $bak -Force
        Write-Host "[dsh] 备份旧预设: $bak"
      }
      Copy-Item $_.FullName $target -Recurse -Force
      Write-Host "[dsh] 预设已装: $($_.Name)"
    }
  }
} else {
  Write-Host "[dsh] 未找到 presets/ 目录,跳过预设安装" -ForegroundColor Yellow
}

# 5) 凭据与环境变量指引(密钥不入库)
Write-Host ""
Write-Host "==== 需要手动完成 ===="
Write-Host "1. API keys: 启动 dsh web 后,在 设置 → Models 页面写入(对应 apiKeyEnv):"
Write-Host "   - OPENCODE_GO_API_KEY"
Write-Host "   - DEEPSEEK_API_KEY (web 搜索/模型)"
Write-Host "2. GitHub Token(供 MCP github 服务器与 gh CLI 使用):"
Write-Host "   gh auth login   # 然后:"
Write-Host "   setx GITHUB_TOKEN (gh auth token)   # 或系统设置 → 环境变量"
Write-Host "3. 重启 dsh web 进程使 MCP 与 GITHUB_TOKEN 生效"
Write-Host ""
Write-Host "==== 验证清单 ===="
Write-Host "[] dsh web 启动正常 (默认 http://127.0.0.1:3080)"
Write-Host "[] 新会话预设可选: Router Standard (experimental) / Anchored Standard (experimental)"
Write-Host "[] 新会话中可见 mcp__playwright__* / mcp__github__* / mcp__devtools__* 工具"
Write-Host "[] skill 目录加载 49 个技能 (可用 / 菜单或直接触发)"