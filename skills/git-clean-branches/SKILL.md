---
name: git-clean-branches
description: 清理 Git 分支:识别并安全清理已合并或长期未更新(默认超 30 天)的分支,默认 dry-run 预览。Use when the user says 清理分支, 删除过期分支, 整理分支, clean branches. 与 CCG 的 /ccg:clean-branches 同思路。
---

# Git Clean Branches — 分支清理

安全识别并清理已合并或长期未更新的分支。**默认 dry-run:先预览,确认后删除。**

## 流程

### 阶段 1:预检
- 确认当前分支、base 分支(`--base <branch>`,默认 main/master,不存在则问用户)
- 确认是否有 worktree 引用待删分支

### 阶段 2:收集候选
- 已合并:`git branch --merged <base>`(排除 base 与当前分支)
- 过期:`git branch -v` 按最后提交时间过滤,超 `--stale <days>`(默认 30)天未更新的

### 阶段 3:预览(dry-run,默认)
列出将删除的分支 + 最后提交时间;明确标注**未合并**的候选(删除需 `--force`,有数据丢失风险)。

### 阶段 4:确认执行
- 展示删除清单,等用户确认(可选 `--yes` 跳过)
- `--remote` 时同步删除远程分支(共享仓库须二次确认)
- `--force` 才允许删除未合并分支

### 阶段 5:收尾
- 报告删除结果;如有 worktree 引用已删分支,一并提示处理

## 安全规则
- 永不删除:当前分支、base 分支、最近 7 天内有活动的分支、用户指定保留的分支
- 未合并且无 `--force` 的分支一律跳过
- 删除远程分支前必须二次确认
