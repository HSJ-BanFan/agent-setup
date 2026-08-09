# 共享技能库

本目录是跨 agent 共享的技能库(64 个技能,约 800KB),从 `~/.agents/skills/` 复制并补充了通用技能。

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
setup-matt-pocock-skills spec-workflow           tdd
teach                    to-questionnaire        to-spec
to-tickets               triage                  wait-what
wayfinder                wizard                  writing-for-agents
writing-great-skills
```

**新增通用技能(适合 agent 搭配使用)**:

```
agentic-engineering       agent-harness-construction   agent-introspection-debugging
ai-regression-testing     code-tour                    deep-research
docker-patterns           e2e-testing                  enterprise-agent-ops
github-ops                prompt-optimizer             security-review
```

> 更多通用技能(官方 pdf/docx/xlsx/pptx、webapp-testing 等)可从
> https://github.com/anthropics/skills 获取并加入本目录。

## 来源索引

每个技能的上游开源仓库见 **[`SKILLS-SOURCES.md`](SKILLS-SOURCES.md)**:

| 上游仓库 | 技能数 | 说明 |
|---|---|---|
| [emilkowalski/skills](https://github.com/emilkowalski/skills) | 6 | 设计/动效(Emil Kowalski) |
| [greensock/gsap-skills](https://github.com/greensock/gsap-skills) | 8 | GSAP 官方 |
| [mattpocock/skills](https://github.com/mattpocock/skills) | ~25 | 工程流程(Matt Pocock) |
| [fengshao1227/ccg-workflow](https://github.com/fengshao1227/ccg-workflow) | 7 | Git/文档(CCG 附带) |
| [stablyai/orca](https://github.com/stablyai/orca) | 4 | 编排/桌面控制 |
| [vercel-labs/skills](https://github.com/vercel-labs/skills) | 1 | 技能发现 |
| CC-Switch 市场同步 | 12 | 上游待确认(skills.sh) |

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
