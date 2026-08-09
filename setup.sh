#!/usr/bin/env bash
# Agent 配置复刻脚本 - Linux/macOS
# 用法: ./setup.sh
set -euo pipefail

REPO="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
HOME_DIR="$HOME"
TS=$(date +%Y%m%d-%H%M%S)

echo "=== Agent 配置复刻 (Linux/macOS) ==="

# ---------- 1. Claude Code ----------
echo -e "\n[1/5] Claude Code..."
mkdir -p "$HOME_DIR/.claude"
if [ -f "$HOME_DIR/.claude/settings.json" ]; then
  cp "$HOME_DIR/.claude/settings.json" "$HOME_DIR/.claude/settings.json.bak-$TS"
fi
cp "$REPO/claude-code/settings.json" "$HOME_DIR/.claude/settings.json"
echo "  ✓ settings.json (原文件已备份)"

# ---------- 2. Codex ----------
echo -e "\n[2/5] Codex..."
mkdir -p "$HOME_DIR/.codex"
if [ -f "$HOME_DIR/.codex/config.toml" ]; then
  cp "$HOME_DIR/.codex/config.toml" "$HOME_DIR/.codex/config.toml.bak-$TS"
fi
cp "$REPO/codex/config.toml" "$HOME_DIR/.codex/config.toml"
echo "  ✓ config.toml (原文件已备份)"
echo "  ⚠ 请手动配置 API key: 运行 codex login"

# ---------- 3. Pi ----------
echo -e "\n[3/5] Pi..."
mkdir -p "$HOME_DIR/.pi/agent/extensions"
if [ -f "$HOME_DIR/.pi/agent/settings.json" ]; then
  cp "$HOME_DIR/.pi/agent/settings.json" "$HOME_DIR/.pi/agent/settings.json.bak-$TS"
fi
cp "$REPO/pi/settings.json" "$HOME_DIR/.pi/agent/settings.json"
cp "$REPO/pi/agent/extensions/"*.ts "$HOME_DIR/.pi/agent/extensions/"
echo "  ✓ settings.json + 扩展"
if [ ! -f "$HOME_DIR/.pi/agent/models.json" ]; then
  cp "$REPO/pi/models.example.json" "$HOME_DIR/.pi/agent/models.json"
  echo "  ✓ models.json (模板,请填入 apiKey)"
fi

# ---------- 4. OpenCode ----------
echo -e "\n[4/5] OpenCode..."
mkdir -p "$HOME_DIR/.config/opencode"
cp "$REPO/opencode/opencode.jsonc" "$HOME_DIR/.config/opencode/opencode.jsonc"
echo "  ✓ opencode.jsonc"

# ---------- 5. 共享技能 ----------
echo -e "\n[5/5] 共享技能库..."
mkdir -p "$HOME_DIR/.agents/skills" "$HOME_DIR/.claude/skills" "$HOME_DIR/.codex/skills"
cp -r "$REPO/skills/"* "$HOME_DIR/.agents/skills/"
# 符号链接(Claude Code / Codex / Pi 复用)
for d in "$HOME_DIR/.agents/skills/"*/; do
  name=$(basename "$d")
  [ -e "$HOME_DIR/.claude/skills/$name" ] || ln -s "$d" "$HOME_DIR/.claude/skills/$name"
  [ -e "$HOME_DIR/.codex/skills/$name" ] || ln -s "$d" "$HOME_DIR/.codex/skills/$name"
done
echo "  ✓ $(( $(ls -d "$HOME_DIR/.agents/skills"/*/ | wc -l) )) 个技能已复制并链接"

# ---------- 完成 ----------
echo -e "\n=== 完成! ==="
echo "还需要手动完成:"
echo "  1. Codex: 填入 ~/.codex/auth.json 的 API key"
echo "  2. Pi: 填入 ~/.pi/agent/models.json 的 apiKey(如用本地代理)"
echo "  3. Claude Code: 按需配置模型端点(见 claude-code/README.md)"
echo "  4. 安装 claude-hud: claude plugin marketplace add jarrodwatts/claude-hud"
echo "  5. CC-Switch: 重新添加供应商(见 cc-switch/README.md)"
