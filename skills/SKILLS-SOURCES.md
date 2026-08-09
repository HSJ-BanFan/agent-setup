# 技能来源索引 (SKILLS-SOURCES)

本仓库 `skills/` 下的技能大多来自开源仓库,本文件标注每个技能的**上游来源**,
便于溯源、更新与致谢。状态:✅ 已确认(内容比对一致)| 🟡 推断(特征匹配)| ⚪ 待确认。

## emilkowalski/skills — 设计工程师技能集(6 个)

https://github.com/emilkowalski/skills

> Emil Kowalski(知名设计师)的设计与动效技能集,通过 `npx skills add https://github.com/emilkowalski/skills` 安装。

| 技能 | 状态 |
|---|---|
| animation-vocabulary | ✅ 内容一致 |
| apple-design | ✅ 内容一致 |
| emil-design-eng | ✅ 内容一致 |
| find-animation-opportunities | ✅ 内容一致 |
| improve-animations | ✅ 内容一致 |
| review-animations | ✅ 内容一致 |

## greensock/gsap-skills — GSAP 官方技能(8 个)

https://github.com/greensock/gsap-skills

> GSAP(GreenSock)官方发布的 AI 技能,教 agent 正确使用 GSAP 动画库。

| 技能 | 状态 |
|---|---|
| gsap-core / gsap-frameworks / gsap-performance | ✅ 官方 |
| gsap-plugins / gsap-react / gsap-scrolltrigger | ✅ 官方 |
| gsap-timeline / gsap-utils | ✅ 官方 |

## mattpocock/skills — 真实工程师技能集(约 25 个)

https://github.com/mattpocock/skills

> Matt Pocock 的工程技能集("Skills for Real Engineers"),覆盖规格/分诊/教学/代码评审等工程流程。

| 技能 | 状态 |
|---|---|
| ask-matt、setup-matt-pocock-skills | ✅ 内容一致 |
| code-review、codebase-design、diagnosing-bugs、domain-modeling | ✅ 内容一致 |
| grill-me、grill-with-docs、grilling | ✅ 内容一致 |
| implement、improve-codebase-architecture、prototype、research | ✅ 内容一致 |
| resolving-merge-conflicts、spec-workflow、tdd、teach | ✅ 内容一致 |
| to-questionnaire、to-spec、to-tickets、triage | ✅ 内容一致 |
| wait-what、wayfinder、wizard、writing-for-agents | ✅ 内容一致 |

## fengshao1227/ccg-workflow — CCG 附带技能(7 个)

https://github.com/fengshao1227/ccg-workflow

> CCG 工作流引擎随附的 Git/文档技能。注:用户已卸载 CCG 引擎本身,仅保留这些独立技能。

| 技能 | 状态 |
|---|---|
| git-commit、git-rollback、git-worktree、git-clean-branches | ✅ 内容一致 |
| doc-context、doc-init、doc-sync | ✅ 内容一致 |

## stablyai/orca — Orca 编排工具技能(4 个)

https://github.com/stablyai/orca

> Orca(agent 编排 ADE)随附的技能:桌面控制、CLI、编排、交接。

| 技能 | 状态 |
|---|---|
| computer-use | ✅ 内容一致 |
| orca-cli | ✅ 内容一致 |
| orchestration | ✅ 内容一致 |
| handoff | ✅ 内容一致 |

## vercel-labs/skills — Vercel 技能(1 个)

https://github.com/vercel-labs/skills

| 技能 | 状态 |
|---|---|
| find-skills | ✅ 内容一致 |

## CC-Switch 技能市场同步(12 个,上游待确认)

以下技能经 **CC-Switch 技能市场**(`~/.cc-switch/skills/`,基于 skills.sh 生态)安装,
原始上游仓库未在 SKILL.md 内标注,建议按需在 https://skills.sh 搜索同名技能溯源:

| 技能 | 状态 |
|---|---|
| agentic-engineering、agent-harness-construction、agent-introspection-debugging | ⚪ 上游待确认 |
| ai-regression-testing、code-tour、deep-research、docker-patterns | ⚪ 上游待确认 |
| e2e-testing、enterprise-agent-ops、github-ops、prompt-optimizer、security-review | ⚪ 上游待确认 |

## 待确认技能

| 技能 | 状态 |
|---|---|
| writing-great-skills | 🟡 可能属 mattpocock/skills,待比对 |

## 更新维护

- 新增技能时同步在本文件登记来源
- 发现上游更新时:对比内容 → 更新本仓库副本 → 记录新版本
- 安装方式统一:`npx skills add <repo> --skill <name>`(skills.sh CLI)
