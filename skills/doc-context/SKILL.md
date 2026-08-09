---
name: doc-context
description: 决策日志管理:维护 .context/ 目录(session.log → uncommit.md → history/commits.md),提交时自动从 git diff 分析决策并归档,支持压缩、查看历史、合并记录。Use when the user mentions recording decisions, context management, decision log, viewing session history, or wants a decision audit trail. 与 CCG 的 /ccg:context 同思路。
---

# Doc Context — 决策日志与审计链

维护 `.context/` 目录,为项目提供**与代码绑定**的可追溯决策审计链。与 claude-mem 互补:claude-mem 记会话记忆,本技能沉淀"为什么这么写"——每个决策都挂到具体提交上。

## 目录结构

```
.context/
├── session.log          # 追加式工作日志(原始流水)
├── uncommit.md          # 压缩后的待归档决策(手动预览用)
└── history/
    └── commits.md       # 按提交归档的正式决策记录(只增不改)
```

## 用法

| 子命令 | 说明 |
|---|---|
| init | 初始化 `.context/` 结构(每个项目执行一次) |
| log <msg> | 手动追加一条 session.log 备注 |
| show | 查看当前分支的 session.log |
| compress | 把 session.log 压缩为决策条目写入 uncommit.md |
| history | 查看 history/commits.md |
| squash <ids> | 合并多条 history 记录(配合 git squash) |

**核心用法**:init 一次,之后只管开发。`git-commit` skill 提交时自动分析 diff 并归档决策;`log` 仅在需要手动补充备注时使用。

## 归档规范(每次提交后执行)

1. 从 `git diff`(本次提交)提取与代码绑定的决策:为什么这样改、放弃过什么方案、影响范围
2. 每条决策记:时间 / 提交 hash / 决策 / 理由 / 备选(被否掉的)
3. 追加到 history/commits.md;同一次提交的多条记录合并为一个条目(可 squash)
4. session.log 中已归档内容标记 `[archived <hash>]`

## 决策条目模板

```markdown
## <hash7> <时间> <主题>
- 决策:<做了什么>
- 理由:<为什么>
- 备选:<考虑过但否掉的,及原因>
- 影响:<涉及模块>
```

## 规则
- 归档只追加、不修改历史条目(审计链完整性)
- 找不到明确决策的纯机械改动(格式化、重命名)不必硬编决策
