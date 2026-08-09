---
name: git-commit
description: 智能 Git 提交:分析工作区改动生成 Conventional Commit 信息,支持拆分建议、amend、signoff、emoji、scope、type。Use when the user says commit, 提交, 提交信息, or wants a smart conventional commit. 提交后自动归档决策(配合 doc-context)。与 CCG 的 /ccg:commit 同思路。
---

# Git Commit — 智能提交

## 流程

1. **检查状态**:`git status` + `git diff --stat`;有未暂存改动先展示给用户
2. **分析归类**:按改动内容判定类型——
   - `feat` 新功能 / `fix` 修复 / `refactor` 重构 / `docs` 文档 / `test` 测试 / `chore` 杂项
3. **生成信息**:Conventional Commit 格式,示例:
   ```bash
   feat(weapons): 新增微光武器合成配方
   fix(crafting): 修复工作台配方缺失
   refactor(api): 统一错误处理中间件
   ```
4. **用户选项**:
   | 选项 | 说明 |
   |---|---|
   | `--all` | 暂存所有改动 |
   | `--amend` | 修补上次提交 |
   | `--signoff` | 附加 Signed-off-by |
   | `--emoji` | 信息带 emoji 前缀 |
   | `--scope <x>` | 指定作用域(模块名) |
   | `--type <x>` | 强制指定类型 |
   | `--no-verify` | 跳过 git 钩子 |
5. **拆分建议**:改动混合多个关注点(feat+docs、多模块混改)时,列出拆分方案,用户确认后**分批提交**
6. **提交后归档**:按 doc-context skill 的归档规范,从本次 diff 提取决策写入 `.context/history/commits.md`

## 规则
- type 用英文标准词,描述用中文
- 不确定的改动先问,不猜;有未跟踪文件时先问是否纳入
- 钩子校验失败时如实报告原因,不擅自 `--no-verify`
