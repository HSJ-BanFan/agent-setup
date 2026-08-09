# 执行规则 (RULES)

AI agent 在本仓库执行配置任务时必须遵守以下规则。

## 安全规则

1. **绝不提交密钥**:仓库内所有密钥字段用 `YOUR_*_KEY_HERE` 占位。真实密钥只写入用户本机文件
   (`~/.codex/auth.json`、`~/.cc-switch/cc-switch.db`、`infra/cliproxy/config.yaml` 等)。
2. **先备份再覆盖**:修改用户已有配置前,先复制为 `<file>.bak-<yyyyMMdd-HHmmss>`。
3. **最小干预**:不修改与本任务无关的配置;不删除用户数据。
4. **不确定就问**:涉及密钥来源、供应商选择、端口占用、付费服务时,先询问用户。

## 来源规则

5. **官方源优先**:工具一律从 `skill/tool-index.md` / `sources.json` 登记的官方源仓库安装。
6. **不用山寨源**:禁止使用未经验证的第三方镜像、非官方 npm 包名、来路不明的安装脚本。
7. **版本可追溯**:记录安装的版本号(`npm ls -g` / `docker ps` 确认)。

## 顺序规则

8. **先工具后配置**:先安装 CLI 本体,再复制配置,最后填密钥。
9. **先基础设施后 agent 配置**(若用户要求部署):先起 Docker 网关(9router/grok2api/kiro-rs/cli-proxy-api),
   确认端口可用,再配置各 agent 指向这些端点。
10. **配置 → 验证闭环**:每步完成后验证(`--version`、`curl` 端口、`/reload` 生效)。

## 平台规则

11. **Windows**:
    - 符号链接 `mklink /D` 需要管理员或开发者模式;无权限时退化为 `Copy-Item -Recurse`
    - Git Bash 下 node 路径用 `which node` 获取(如 `/e/Program Files/nodejs/node`)
12. **Linux/macOS**:
    - 符号链接用 `ln -s`;注意 `~/.claude/skills` 等目录需先创建
13. **国内网络**:GitHub 拉取失败时,提示用户设置代理(`export HTTPS_PROXY=http://127.0.0.1:7897`),
    而不是改用未经验证的镜像。

## 交互规则

14. **密钥引导**:填密钥时给出获取路径(GitHub Tokens 页面、供应商控制台等),不替用户编造。
15. **结果汇报**:完成后给出验证清单(见 `SKILL.md` 第 4 节),逐项打勾说明。
16. **失败处理**:某步骤失败时,给出具体错误与修复建议,不静默跳过、不伪造成功。
