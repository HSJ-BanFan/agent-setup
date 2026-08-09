# 共享技能库

本目录是跨 agent 共享的技能库(52 个技能,共 666KB),从 `~/.agents/skills/` 复制。

## 技能清单

```
animation-vocabulary     apple-design            ask-matt
code-review              codebase-design         computer-use
diagnosing-bugs          doc-context             doc-init
doc-sync                 domain-modeling         emil-design-eng
find-animation-opportunities  find-skills        git-clean-branches
git-commit               git-rollback            git-worktree
grill-me                 grill-with-docs         grilling
gsap-core                gsap-frameworks         gsap-performance
gsap-plugins             gsap-react              gsap-scrolltrigger
gsap-timeline            gsap-utils              handoff
implement                improve-animations      improve-codebase-architecture
orca-cli                 orchestration           prototype
research                 resolving-merge-conflicts  review-animations
setup-matt-pocock-skills tdd                     teach
to-questionnaire         to-spec                 to-tickets
triage                   wait-what               wayfinder
wizard                   writing-for-agents
```

## 安装到新机器

技能统一放在 `~/.agents/skills/`(各 agent 通过符号链接引用):

```bash
# 1. 复制技能到共享位置
# Windows (PowerShell)
Copy-Item skills/* "$env:USERPROFILE\.agents\skills\" -Recurse

# Linux/macOS
mkdir -p ~/.agents/skills && cp -r skills/* ~/.agents/skills/
```

### 2a. Claude Code(符号链接)

```bash
# Linux/macOS
mkdir -p ~/.claude/skills
for d in ~/.agents/skills/*/; do
  ln -s "$d" ~/.claude/skills/"$(basename "$d")"
done

# Windows(需管理员/开发者模式)
# 用 setup.ps1 自动处理,或:
# cmd /c mklink /D "%USERPROFILE%\.claude\skills\<name>" "%USERPROFILE%\.agents\skills\<name>"
```

### 2b. Codex

```bash
# Codex 直接读取 ~/.codex/skills/,可复制或软链
ln -s ~/.agents/skills/* ~/.codex/skills/
```

### 2c. Pi

Pi 在 `~/.pi/agent/settings.json` 的 `skills` 数组里配置路径:

```json
"skills": [
  "~/.claude/skills",   // 通过符号链接复用
  "~/.codex/skills"
]
```

## 说明

- 技能来源:Claude 官方、社区(ask-matt、gsap 官方、emil-kowalski 设计技能等)及本地自建
- 每个技能目录含 `SKILL.md` 入口,被 agent 自动发现
- 个别技能可能依赖环境(如 `computer-use` 需要 Orca CLI),见技能内 README
