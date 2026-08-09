---
name: git-worktree
description: Git Worktree 管理:add/list/remove/prune/migrate,默认创建在 ../.ccg/<项目名>/ 目录,用于并行开发分支、隔离 agent 工作区。Use when the user says worktree, 工作树, 并行分支, 隔离开发, 迁移工作区. 与 CCG 的 /ccg:worktree 同思路。
---

# Git Worktree — 工作树管理

在结构化目录管理 git worktree,用于并行开发多个分支、给 agent/subagent 隔离工作区、快速验证旧版本。

## 默认约定

- 存放目录:`../.ccg/<项目名>/<分支名>`(相对仓库根;用户可指定其他位置)
- 命名:目录名用项目名(如 `../.ccg/terraria.wiki/feature-x`)

## 子命令

| 命令 | 说明 |
|---|---|
| `add <path>` | 创建新 worktree;`-b <branch>` 同时新建分支;`-o/--open` 创建后用编辑器打开 |
| `list` | 列出所有 worktree(路径 / 分支 / HEAD 提交) |
| `remove <path>` | 删除 worktree(先确保无未提交改动) |
| `prune` | 清理失效的 worktree 引用 |
| `migrate <target>` | 把当前 worktree 内容迁移到目标 worktree |

## 流程(以 add 为例)

1. 确认目标分支未被其他 worktree checkout(`git worktree list` 检查)
2. 确认路径可用(目录不存在或为空)
3. 执行创建并报告路径与分支
4. 需要时用编辑器打开该目录

## 规则

- add 前必查分支占用,避免"branch is already checked out"错误
- remove 前检查未提交改动,有则先提示用户
- 给 subagent 分配隔离工作区时,优先用 agent 原生 worktree 支持(如 Pi subagent 的 `worktree: true`),本 skill 用于人工管理的场景
