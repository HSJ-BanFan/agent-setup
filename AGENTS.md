# AGENTS.md — 仓库指令(平台中立)

本仓库是 **AI 开发环境配置技能包**:任何 AI 编码 agent(Claude Code、Codex、Pi、
OpenCode、Cursor、Cline 等)读取本文件后,即可在陌生机器上引导用户复刻完整环境。

## 仓库是什么

- **配置模板**:4 个 agent(Claude Code / Codex / Pi / OpenCode)+ CC-Switch 的脱敏配置
- **共享技能库**:`skills/`(64 个跨 agent 技能)
- **基础设施说明**:`infra/`(9router / grok2api / kiro-rs / cli-proxy-api / CPA Manager Plus / NapCat / Watchtower)
- **配置技能**:`SKILL.md` + `skill/`(tool-index / routing / sources)+ `RULES.md`

## 作为 agent 如何工作

1. 用户请求环境配置时,先读 `SKILL.md` 了解工作流程
2. 需要工具来源时读 `skill/tool-index.md`(所有源仓库地址)
3. 需要路由时读 `skill/routing.md`(任务 → 文件映射)
4. 执行时遵守 `RULES.md`(安全/来源/顺序/平台规则)
5. 用 `setup.ps1`(Windows)或 `setup.sh`(Linux/macOS)一键复刻,或按各目录 README 分步执行

## 本仓库已在配置中包含的技能(供 agent 使用)

`skills/` 下技能可在配置完成后继续使用,包括:
- 开发工作流:tdd、code-review、diagnosing-bugs、implement、spec-workflow、triage
- 设计与动效:apple-design、gsap-*(8 个)、animation-vocabulary、emil-design-eng
- 研究:research、deep-research、find-skills
- Agent 工程:agentic-engineering、agent-harness-construction、enterprise-agent-ops
- 运维:github-ops、docker-patterns、e2e-testing、security-review
- 其他:computer-use、wizard、prototype、orchestration 等

## 维护约定

- 配置变更:更新对应目录文件并提交
- 新增工具:同步更新 `skill/tool-index.md` 与 `skill/sources.json`
- 密钥永不入库(用 `YOUR_*_KEY_HERE` 占位)
