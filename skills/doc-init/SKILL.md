---
name: doc-init
description: 初始化或更新项目 AI 上下文文档:四阶段扫描(全仓清点→模块扫描→深度补捞→生成),产出根级 + 模块级 CLAUDE.md(含 Mermaid 结构图与导航面包屑)。Use when the user asks to generate project documentation, initialize docs, scan a project, update CLAUDE.md, or when taking over an unfamiliar codebase.
---

# Doc Init — 项目文档生成

把项目扫描结果沉淀为「根级简明 + 模块级详尽」的文档体系,让任何 agent 或人接手项目都能快速定位。输出采用跨工具通用的 `CLAUDE.md` 约定(Claude Code / Codex / Pi 均识别),与 CCG 的 `/ccg:init` 同思路。

## 输出结构

```
CLAUDE.md                 # 根级:一句话定位 + 技术栈 + 模块地图 + Mermaid 结构图 + 常用命令
docs/
└── modules/
    ├── <module1>.md      # 模块级:职责、入口、接口、依赖、关键文件、测试方式
    └── <module2>.md
```

## 执行流程(严格按四阶段)

### 阶段 A:全仓清点
- 列出根目录结构,按目录/扩展名聚合文件统计
- 识别模块边界(建议 3~10 个,过碎则合并,过大则拆分)
- 记录技术栈(package.json / pyproject.toml / go.mod / Cargo.toml 等)

### 阶段 B:模块优先扫描
对每个模块记录:
- 入口文件、对外接口(函数/类/CLI/API 端点)
- 依赖(内部 + 外部)、测试入口与命令
- 一句话职责描述(3 条以内,写事实不写评价)

### 阶段 C:深度补捞(按需)
仅当出现以下情况才深入:入口指向模糊、接口无文档、存在复杂领域逻辑或核心算法。

### 阶段 D:生成文档
1. 根级 CLAUDE.md:项目定位(1 句)、技术栈表、模块地图(名称+路径+一句话)、Mermaid 结构图、常用命令
2. 每个模块 `docs/modules/<name>.md`:职责、入口、接口清单、依赖、关键文件路径、测试方式
3. 模块文档开头加导航面包屑(返回根级 CLAUDE.md 的链接)

## 规则
- 文档只写**事实**(路径、接口、命令),不写主观评价
- 大项目可用 subagent 工具派发扫描任务并行扫各模块,再汇总成稿
- 更新时先 diff 旧文档,只改过时部分,保留人工补充的内容
- 完成后向用户报告覆盖率(模块数 / 已文档化数)与推荐下一步
