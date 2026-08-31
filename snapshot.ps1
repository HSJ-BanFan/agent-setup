# 反向导出:把本机当前 Pi 配置同步回本仓库(改了配置/装了新包后运行)
# 永不触碰: auth.json、sessions、missions、run-history、各类缓存
# 用法: pwsh snapshot.ps1
$ErrorActionPreference = 'Stop'
$repo = $PSScriptRoot
$piAgent = Join-Path $HOME '.pi\agent'

function Mirror($src, $dst) {
    if (-not (Test-Path $src)) {
        if (Test-Path $dst) { Remove-Item $dst -Recurse -Force }
        Write-Host "跳过不存在的源: $src (已清空 $dst)"
        return
    }
    robocopy $src $dst /MIR /NFL /NDL /NJH /NJS | Out-Null
    if ($LASTEXITCODE -ge 8) { throw "robocopy 失败: $src -> $dst (exit $LASTEXITCODE)" }
}

# 1. 配置文件
$configs = 'settings.json', 'mcp.json', 'open-tui.json', 'claude-code-style.json', 'models-store.json'
foreach ($f in $configs) {
    if (-not (Test-Path "$piAgent\$f")) { throw "缺少 $piAgent\$f，请确认路径" }
}
Copy-Item ($configs | ForEach-Object { "$piAgent\$_" }) "$repo\pi\" -Force
# Pi 自动维护的版本号是运行时元数据，不同步到仓库
$settingsPath = Join-Path $repo 'pi\settings.json'
$settings = Get-Content $settingsPath -Raw | ConvertFrom-Json
$settings.PSObject.Properties.Remove('lastChangelogVersion')
$settings | ConvertTo-Json -Depth 10 | Set-Content $settingsPath -Encoding utf8
Mirror "$piAgent\extensions" "$repo\pi\extensions"
Mirror "$piAgent\skills" "$repo\pi\skills"

# 2. 共享技能
Mirror "$HOME\.agents\skills" "$repo\agents-skills"
if (Test-Path "$HOME\.agents\browser-qa.md") { Copy-Item "$HOME\.agents\browser-qa.md" "$repo\" -Force }

# 3. 安全检查:仓库里不允许出现密钥
$hit = Get-ChildItem $repo -Recurse -File |
    Where-Object { $_.FullName -notmatch '[\\/]\.git[\\/]' } |
    Select-String -Pattern 'sk-[A-Za-z0-9]{20}' -List
if ($hit) { Write-Warning "疑似密钥，禁止提交: $($hit.Path)" }

Write-Host '已导出。核对后提交:'
git -C $repo status --short

