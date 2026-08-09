# 共享技能库

本目录是跨 agent 共享的技能库(29 个技能),从 `~/.agents/skills/` 复制。
**只保留两个系列**:Matt Pocock 工程技能(25)+ Orca 技能(4)。

> CCG(git-*/doc-*)与前端设计(gsap-*/apple-design/emil-* 等)系列已按用户要求完全移除。

## 技能清单

### Matt Pocock 工程技能(25 个) — https://github.com/mattpocock/skills

```
ask-matt                  # 技能路由入口:询问哪个技能/流程适合当前情况
code-review               # 提交/分支/PR 双轴审查(标准 + 规格)
codebase-design           # 深模块设计词汇
diagnosing-bugs           # 硬 bug 诊断循环
domain-modeling           # 领域模型打磨
grill-me / grill-with-docs / grilling  # 需求拷问
implement                 # 工程实现流程
improve-codebase-architecture  # 架构改进扫描
prototype                 # 一次性原型
research                  # 高信任源研究
resolving-merge-conflicts # 冲突解决
setup-matt-pocock-skills  # 技能集初始化配置
spec-workflow             # 变更文档闭环(OpenSpec 风格)
tdd                       # 测试驱动开发
teach                     # 教学
to-questionnaire / to-spec / to-tickets  # 会话转问卷/规格/工单
triage                    # 问题分诊
wait-what                 # 质疑
wayfinder                 # 路径导航
wizard                    # 交互式向导
writing-for-agents        # 面向 agent 的文档写作
```

### Orca 技能(4 个) — https://github.com/stablyai/orca

```
computer-use    # 桌面/浏览器 UI 操作(Orca CLI)
orca-cli        # Orca CLI 使用指南
orchestration   # Orca 多代理编排
handoff         # 会话交接文档
```

## 安装到新机器

技能统一放在 `~/.agents/skills/`(各 agent 通过符号链接引用):

```bash
# Windows (PowerShell)
Copy-Item skills/* "$env:USERPROFILE\.agents\skills\" -Recurse

# Linux/macOS
mkdir -p ~/.agents/skills && cp -r skills/* ~/.agents/skills/
```

### 为各 agent 建符号链接

```bash
# Linux/macOS
mkdir -p ~/.claude/skills ~/.codex/skills
for d in ~/.agents/skills/*/; do
  ln -s "$d" ~/.claude/skills/"$(basename "$d")"
  ln -s "$d" ~/.codex/skills/"$(basename "$d")"
done
```

> Windows 用 `setup.ps1` 自动处理(符号链接失败时退化为复制)。
> Pi 通过 `settings.json` 的 `skills` 数组指向 `~/.claude/skills`、`~/.codex/skills` 复用。
