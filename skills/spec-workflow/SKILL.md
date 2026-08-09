---
name: spec-workflow
description: 变更文档闭环(OpenSpec 风格):为功能/修复创建 specs.md + design.md + tasks.md 工件,按「计划→实现→验证→归档」四阶段驱动开发,verify 阶段校验实现是否匹配文档。Use when the user wants to start a new change, write a spec, plan with design docs and task lists, verify implementation matches docs, or archive a completed change. 与 CCG 的 spec-plan/impl/review 同思路。
---

# Spec Workflow — 变更工件驱动开发

把"想做什么"变成可验证的工件链,实现阶段变成纯机械执行。灵感来自 OpenSpec 与 CCG 的 `/ccg:spec-plan|impl|review`。

## 工件结构

```
changes/<kebab-case-name>/      # 如 changes/add-jwt-auth/
├── specs.md       # 需求规格:目标、非目标、验收标准(每条可测试)
├── design.md      # 设计决策:方案对比、取舍、接口、数据流
├── tasks.md       # 任务清单(- [ ] X.Y 勾选格式)
└── review.md      # 验证结果:逐条核对,通过/失败 + 证据
```

## 四阶段

### 1. new — 创建变更
- 从用户描述提取 kebab-case 名称;描述不清就先问清楚
- 写 specs.md:目标 / 非目标 / 验收标准——每条验收标准必须可测试,优先写成性质或不变量(Property-Based)

### 2. plan — 消除歧义(零决策计划)
- **核心哲学**:消除所有决策点,让实现变成纯机械执行
- 每个模糊点解析为明确约束,未解决前**禁止进入实现**
- 关键取舍写入 design.md(方案对比、选中理由、否掉的方案)
- tasks.md 全用 `- [ ] X.Y 描述` 勾选格式,拆到可机械执行的粒度
- 复杂变更可派 subagent 并行做 research(探索)与 review(交叉审查)

### 3. impl — 机械执行
- 按 tasks.md 逐条勾选完成,一次只做一件事
- 改动 >30 行或跨模块时,先自查再继续
- **阶段边界**:plan 阶段不写代码,impl 阶段不改规格

### 4. verify — 校验实现匹配文档
- 逐条核对 specs 验收标准与 tasks 完成项是否**真实满足**(看代码与测试输出,不信口头)
- 结果写入 review.md:每项 ✅/❌ + 证据(文件/行号/命令输出)
- 发现不匹配 → 开修复任务回到 impl;确属规格错误则修订 specs.md 并记录修订理由

### 5. archive — 归档
- 合并工件为单个文档放入 `docs/changes/<name>.md`(含结论与遗留事项)
- 从 changes/ 移除,更新 changes/README.md 索引
- 同步触发的文档(README、模块文档)交给 doc-sync skill

## 规则
- 与 openspec CLI 兼容:tasks.md 保持 `- [ ] X.Y` 格式(openspec 解析依赖它)
- 用户指引只说本技能阶段名(/spec:new、/spec:plan、/spec:impl、/spec:verify、/spec:archive),不暴露底层细节
