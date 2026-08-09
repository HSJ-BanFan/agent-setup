# Agent 配置复刻脚本 - Windows (PowerShell)
# 用法: .\setup.ps1
# 说明: 将本仓库配置复制到当前用户的 agent 配置目录,不包含 API keys(需手动填入)

$ErrorActionPreference = "Stop"
$REPO = $PSScriptRoot
$HOME_DIR = $env:USERPROFILE

Write-Host "=== Agent 配置复刻 (Windows) ===" -ForegroundColor Cyan

# ---------- 1. Claude Code ----------
Write-Host "`n[1/5] Claude Code..." -ForegroundColor Yellow
New-Item -ItemType Directory -Force -Path "$HOME_DIR\.claude" | Out-Null
if (Test-Path "$HOME_DIR\.claude\settings.json") {
    Copy-Item "$HOME_DIR\.claude\settings.json" "$HOME_DIR\.claude\settings.json.bak-$(Get-Date -Format yyyyMMdd-HHmmss)" -Force
}
Copy-Item "$REPO\claude-code\settings.json" "$HOME_DIR\.claude\settings.json" -Force
Write-Host "  ✓ settings.json (原文件已备份)"

# ---------- 2. Codex ----------
Write-Host "`n[2/5] Codex..." -ForegroundColor Yellow
New-Item -ItemType Directory -Force -Path "$HOME_DIR\.codex" | Out-Null
if (Test-Path "$HOME_DIR\.codex\config.toml") {
    Copy-Item "$HOME_DIR\.codex\config.toml" "$HOME_DIR\.codex\config.toml.bak-$(Get-Date -Format yyyyMMdd-HHmmss)" -Force
}
Copy-Item "$REPO\codex\config.toml" "$HOME_DIR\.codex\config.toml" -Force
Write-Host "  ✓ config.toml (原文件已备份)"
Write-Host "  ⚠ 请手动配置 API key: 运行 codex login 或编辑 $HOME_DIR\.codex\auth.json"

# ---------- 3. Pi ----------
Write-Host "`n[3/5] Pi..." -ForegroundColor Yellow
New-Item -ItemType Directory -Force -Path "$HOME_DIR\.pi\agent\extensions" | Out-Null
if (Test-Path "$HOME_DIR\.pi\agent\settings.json") {
    Copy-Item "$HOME_DIR\.pi\agent\settings.json" "$HOME_DIR\.pi\agent\settings.json.bak-$(Get-Date -Format yyyyMMdd-HHmmss)" -Force
}
Copy-Item "$REPO\pi\settings.json" "$HOME_DIR\.pi\agent\settings.json" -Force
Copy-Item "$REPO\pi\agent\extensions\*.ts" "$HOME_DIR\.pi\agent\extensions\" -Force
Copy-Item "$REPO\pi\open-tui.json" "$HOME_DIR\.pi\agent\open-tui.json" -Force
if (-not (Test-Path "$HOME_DIR\.pi\agent\auth.json")) {
    Copy-Item "$REPO\pi\auth.example.json" "$HOME_DIR\.pi\agent\auth.json" -Force
    Write-Host "  ⚠ 已创建 auth.json 模板,请填入 opencode-go 的 API key"
}
if (-not (Test-Path "$HOME_DIR\.pi\agent\mcp.json")) {
    Copy-Item "$REPO\pi\mcp.example.json" "$HOME_DIR\.pi\agent\mcp.json" -Force
}
Write-Host "  ✓ settings.json + 扩展 + open-tui + auth/mcp 模板"
if (-not (Test-Path "$HOME_DIR\.pi\agent\models.json")) {
    Copy-Item "$REPO\pi\models.example.json" "$HOME_DIR\.pi\agent\models.json" -Force
    Write-Host "  ✓ models.json (模板,请填入 apiKey)"
} else {
    Write-Host "  - models.json 已存在,跳过(手动填入 key)"
}

# ---------- 4. OpenCode ----------
Write-Host "`n[4/5] OpenCode..." -ForegroundColor Yellow
New-Item -ItemType Directory -Force -Path "$HOME_DIR\.config\opencode" | Out-Null
Copy-Item "$REPO\opencode\opencode.jsonc" "$HOME_DIR\.config\opencode\opencode.jsonc" -Force
Write-Host "  ✓ opencode.jsonc"

# ---------- 5. 共享技能 ----------
Write-Host "`n[5/5] 共享技能库..." -ForegroundColor Yellow
New-Item -ItemType Directory -Force -Path "$HOME_DIR\.agents\skills" | Out-Null
Copy-Item "$REPO\skills\*" "$HOME_DIR\.agents\skills\" -Recurse -Force
Write-Host "  ✓ $((Get-ChildItem "$HOME_DIR\.agents\skills" -Directory).Count) 个技能已复制到 ~/.agents/skills"

# 为 Claude Code 创建符号链接(需要管理员或开发者模式)
Write-Host "`n为 Claude Code 创建技能符号链接..." -ForegroundColor Yellow
New-Item -ItemType Directory -Force -Path "$HOME_DIR\.claude\skills" | Out-Null
$linked = 0
Get-ChildItem "$HOME_DIR\.agents\skills" -Directory | ForEach-Object {
    $target = "$HOME_DIR\.claude\skills\$($_.Name)"
    if (-not (Test-Path $target)) {
        try {
            New-Item -ItemType SymbolicLink -Path $target -Target $_.FullName -ErrorAction Stop | Out-Null
            $linked++
        } catch {
            # 无权限时退回复制
            Copy-Item $_.FullName $target -Recurse -Force
            $linked++
        }
    }
}
Write-Host "  ✓ $linked 个技能链接/复制完成"

# ---------- 完成 ----------
Write-Host "`n=== 完成! ===" -ForegroundColor Green
Write-Host "还需要手动完成:"
Write-Host "  1. Codex: 填入 ~/.codex/auth.json 的 API key"
Write-Host "  2. Pi: 填入 ~/.pi/agent/models.json 的 apiKey(如用本地代理)"
Write-Host "  3. Claude Code: 按需配置模型端点(见 claude-code/README.md)"
Write-Host "  4. 安装 claude-hud: claude plugin marketplace add jarrodwatts/claude-hud"
Write-Host "  5. CC-Switch: 重新添加供应商(见 cc-switch/README.md)"
