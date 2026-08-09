---
name: git-rollback
description: 交互式 Git 回滚:安全回滚分支到历史版本,reset/revert 双模式,默认 dry-run 预览,列出最近 20 个版本(含 reflog)。Use when the user says rollback, 回滚, 撤销提交, 退回版本, 恢复误删 commit. 与 CCG 的 /ccg:rollback 同思路。
---

# Git Rollback — 安全回滚

安全地将分支回滚到指定历史版本。**默认 dry-run:先预览,确认后执行。**

## 流程

### 阶段 1:同步
- `git fetch` 确认远端状态(仅本地分支可跳过)
- 记录当前 HEAD hash(回滚反悔用)

### 阶段 2:列版本
- `git log --oneline -20`:最近 20 个版本,标注分支/tag
- 误删恢复场景:`git reflog` 找丢失的提交

### 阶段 3:选目标
- 用户指定 target(commit hash / tag / 分支名);不指定则从列表选

### 阶段 4:预览(dry-run,默认)
展示将执行的命令与影响:
```bash
git reset --hard <target>   # 本地丢弃历史,工作区同步,不可逆,慎用
git revert <target>         # 生成反向提交,保留历史,适合已推送
```
明确说明:目标之后的所有提交会被丢弃(reset)或反向抵消(revert)。

### 阶段 5:确认执行
- 展示完整命令,等用户明确确认(可选 `--yes` 跳过)
- 支持 `--mode reset|revert` 强制指定模式、`--branch <branch>` 指定分支、`--depth <n>` 调整列出版本数

### 阶段 6:报告
- 回滚结果 + 后续影响:是否需要推送、工作区状态、涉及的分支

## 规则
- 永远默认 dry-run,先展示再执行
- 已推送分支优先 revert;reset 需用户显式确认,且用户需知道可能 force-push
- 绝不跳过确认直接执行破坏性命令(除非用户明确 --yes 且已看过预览)
