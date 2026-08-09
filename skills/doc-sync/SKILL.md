---
name: doc-sync
description: 文档同步门禁:检查 README/DESIGN/模块文档是否随代码改动过时并自动更新,校验模块结构与实现一致。Use when the user asks to update the README, sync documentation, regenerate docs, or after significant code changes (>30 lines, new/removed modules, changed public APIs) and before committing. 与 CCG 的 gen-docs / verify-change 门禁同思路。
---

# Doc Sync — 文档同步门禁

代码改动后保证 README 与设计文档"不撒谎"。触发时机:改动 >30 行、新增/删除模块、公共接口签名变化、用户要求更新文档、提交前。

## 检查清单

1. **README**:快速开始、命令、目录结构是否仍准确;有模块级 CLAUDE.md 的核对模块地图
2. **设计文档**:接口签名、数据流、架构图与代码是否一致
3. **模块结构**:docs/modules/ 与真实模块一一对应(新增模块 → 补文档,删除模块 → 移除或标注 deprecated)
4. **变更工件**:changes/ 下 open 的变更工件是否同步更新
5. **项目文档**:根级 CLAUDE.md 的技术栈、常用命令有无变化

## 执行方式

- **能确定的过时处直接修**(改路径、命令、接口名、目录树)
- **不确定的**(设计意图变了?行为变了?)列出问题问用户,不擅自改写
- 空转时输出一行"文档同步 ✓"即可,不啰嗦
- 修复结果用 `git diff --stat` 汇报改动范围

## 规则
- 文档同步是提交前的常规步骤,与 git-commit 配合使用
- 大 PR 合并后、或用户说"文档过时了"时也可单独触发
