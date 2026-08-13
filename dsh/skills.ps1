# dsh/skills.ps1 — 同步全部技能到 ~/.agents/skills
# 用法:
#   .\dsh\skills.ps1                 # 同步到默认位置 ~/.agents/skills
#   .\dsh\skills.ps1 -Target D:\x    # 指定目标目录
#   .\dsh\skills.ps1 -GitOnly        # 只同步 git 源技能(跳过仓库内置与 packaged)
# 幂等:重复执行安全;git 源用稀疏检出,只拉取所需目录。
param(
  [string]$Target = (Join-Path $HOME ".agents\skills"),
  [switch]$GitOnly,
  [switch]$SkipGit
)
$ErrorActionPreference = "Stop"
$RepoRoot = Split-Path -Parent $PSScriptRoot
$Manifest = Get-Content (Join-Path $PSScriptRoot "skills-manifest.json") -Raw | ConvertFrom-Json
New-Item $Target -ItemType Directory -Force | Out-Null
$count = 0

if (-not $GitOnly) {
  # --- 1) 仓库内置技能(skills/ 下 29 个)---
  $repoSkills = Join-Path $RepoRoot "skills"
  if (Test-Path $repoSkills) {
    Get-ChildItem $repoSkills -Directory | ForEach-Object {
      Copy-Item $_.FullName (Join-Path $Target $_.Name) -Recurse -Force
      $count++
    }
    Write-Host "[skills] 仓库内置: $count 个"
  }
  # --- 2) packaged 适配技能(4 个)---
  $pkgDir = Join-Path $PSScriptRoot "packaged-skills"
  if (Test-Path $pkgDir) {
    Get-ChildItem $pkgDir -Directory | ForEach-Object {
      Copy-Item $_.FullName (Join-Path $Target $_.Name) -Recurse -Force
      $count++
    }
    Write-Host "[skills] packaged 适配: $count 个(累计)"
  }
}

if (-not $SkipGit) {
  # --- 3) git 源技能(16 个,稀疏检出)---
  $tmp = Join-Path $env:TEMP "dsh-skills-sync"
  New-Item $tmp -ItemType Directory -Force | Out-Null
  foreach ($src in $Manifest.git) {
    $repoName = $src.id
    $cloneDir = Join-Path $tmp $repoName
    Write-Host "[skills] 同步 $repoName ..."
    if (-not (Test-Path (Join-Path $cloneDir ".git"))) {
      Remove-Item $cloneDir -Recurse -Force -ErrorAction SilentlyContinue
      git clone --quiet --depth 1 --filter=blob:none --sparse $src.repo $cloneDir
      if ($LASTEXITCODE -ne 0) { throw "git clone 失败: $($src.repo)" }
    }
    $sparse = $src.skills | ForEach-Object { "$($src.prefix)/$_" }
    git -C $cloneDir sparse-checkout set $sparse
    if ($LASTEXITCODE -ne 0) { throw "sparse-checkout 失败: $repoName" }
    foreach ($skill in $src.skills) {
      $srcPath = Join-Path $cloneDir ($src.prefix -replace "/", "\")
      $skillSrc = Join-Path $srcPath $skill
      if (Test-Path $skillSrc) {
        Copy-Item $skillSrc (Join-Path $Target $skill) -Recurse -Force
        $count++
      } else {
        Write-Warning "[skills] 未找到 $($src.repo) 的 $skill"
      }
    }
  }
  Remove-Item $tmp -Recurse -Force -ErrorAction SilentlyContinue
}

Write-Host "[skills] 完成: 共 $count 个技能已同步到 $Target"
Write-Host "[skills] 目标总数应为 49(仓库 29 + packaged 4 + git 16);DSH 技能目录热加载,无需重启"