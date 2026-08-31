# 在全新 Windows 机器上一键复刻 Pi 环境（除账号登录外的一切）
# 用法: pwsh setup.ps1
$ErrorActionPreference = 'Stop'
$repo = $PSScriptRoot

function Mirror($src, $dst) {
    if (-not (Test-Path $src)) {
        if (Test-Path $dst) { Remove-Item $dst -Recurse -Force }
        Write-Host "跳过不存在的源: $src (已清空 $dst)"
        return
    }
    robocopy $src $dst /MIR /NFL /NDL /NJH /NJS | Out-Null
    if ($LASTEXITCODE -ge 8) { throw "robocopy 失败: $src -> $dst (exit $LASTEXITCODE)" }
}

# 1. node / npm
if (-not (Get-Command node -ErrorAction SilentlyContinue)) {
    Write-Host '未检测到 node，通过 winget 安装 LTS...'
    winget install --id OpenJS.NodeJS.LTS -e --accept-source-agreements --accept-package-agreements
}
if (-not (Get-Command npm -ErrorAction SilentlyContinue)) {
    throw 'npm 仍不可用，请重开终端后重新运行本脚本'
}

# 2. Pi 本体
npm install -g '@earendil-works/pi-coding-agent'

# 3. ~/.pi/agent 配置（settings.json 中的扩展包会在首次启动 pi 时自动安装）
$piAgent = Join-Path $HOME '.pi\agent'
New-Item -ItemType Directory -Force -Path "$piAgent\extensions", "$piAgent\skills", "$HOME\.agents\skills" | Out-Null
Copy-Item "$repo\pi\*.json" $piAgent -Force
Mirror "$repo\pi\extensions" "$piAgent\extensions"
Mirror "$repo\pi\skills" "$piAgent\skills"

# 4. 共享技能 ~/.agents/
if (Test-Path "$repo\browser-qa.md") { Copy-Item "$repo\browser-qa.md" "$HOME\.agents\" -Force }
Mirror "$repo\agents-skills" "$HOME\.agents\skills"

Write-Host ''
Write-Host '✅ 复刻完成。唯一剩余的手动步骤:'
Write-Host '   运行 pi → /login 登录账号（auth.json 不入库，无法代劳）'
Write-Host '   首次启动会自动安装 settings.json 里的扩展包（约 360MB，需网络）。'

