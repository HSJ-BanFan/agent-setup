---
name: context-md
description: Initialize CLAUDE.md and AGENTS.md for the current workspace. Explores the codebase, interviews for gaps, and writes structured context files so every agent starts fully oriented.
argument-hint: [overwrite]
---

# 📋 Context MD

You are a workspace orienteer. Your job is to read this codebase, interview the user for what code alone cannot reveal, and write context files that give any future agent full orientation in a single read.

**Args:** {{args}}

Track every phase below with the `todo_write` tool. Set up dependencies so each phase is blocked by the previous one. Mark each phase `in_progress` when you start and `completed` when done.


## Advisor

When uncertain about structure or content decisions, stuck after 2 failed attempts, or about to commit to a significant interpretation, ask the user directly with `ask_user_question`.



**Shell.** The snippets below assume a POSIX shell (`bash`/`zsh`/`sh`). On Windows / PowerShell, translate as needed: `2>/dev/null` becomes `2>$null`, `/tmp/...` becomes `$env:TEMP\...`, `test -f` becomes `Test-Path`. Run via the Bash tool (Git Bash on Windows) when POSIX syntax is required.


## Phase 0: Bootstrap

**Detect existing context files:**

```bash
test -f CLAUDE.md && echo "HAS_CLAUDE_MD" || echo "NO_CLAUDE_MD"
test -f AGENTS.md && echo "HAS_AGENTS_MD" || echo "NO_AGENTS_MD"
```

**If any context file exists AND `{{args}}` does NOT contain `overwrite`:**
- Read the existing file(s) and display a summary of what sections they contain
- Tell the user: "Context file(s) already exist. Run `/context-md overwrite` to replace them, or `/context-md-update` to update stale sections."
- Stop here. Do not proceed.

**If any context file exists AND `{{args}}` contains `overwrite`:** continue - you will replace all context files.

**If neither exists:** continue normally - you will create both.

**Detect shell environment:**

```bash
echo "CODEX=${CODEX:-false}"
echo "CODEX_SANDBOX=${CODEX_SANDBOX:-}"
```

**Detect git:**

```bash
test -d .git && echo "HAS_GIT" || echo "NO_GIT"
```

**Detect greenfield** (nearly empty workspace):

```bash
ls -A 2>/dev/null | grep -cvE '^(\.git|\.claude|README\.md|LICENSE|\.gitignore|\.env\.example)$'
```

If the count is 3 or fewer (only boilerplate files), set `GREENFIELD=true`. In greenfield mode:
- Skip all explore subagents
- Go directly to Phase 2 (interview)
- Require the user to provide the project description, planned tech stack, and key agent guidelines before proceeding

Record in working memory: `GREENFIELD`, `HAS_GIT`, `OVERWRITE`, `HAS_CLAUDE_MD`, `HAS_AGENTS_MD`.


## Phase 1: Explore

*Skip if `GREENFIELD=true` - go directly to Phase 2.*

Spawn **4-5 parallel subagents** to map the workspace. Each subagent returns: what it found, what is notable, and any surprises.

**Subagent 1 - Directory structure:**
Map the top-level layout and identify the key source directories.

```bash
ls -la

find . -maxdepth 2 -type d | sort | \
  grep -vE '(node_modules|\.git|dist|build|\.next|__pycache__|\.venv|\.turbo|\.cache|coverage|\.svelte-kit)'
```

**Subagent 2 - Package and dependencies:**
Identify the language, framework, package manager, and key libraries.

```bash
cat package.json 2>/dev/null

ls package-lock.json yarn.lock pnpm-lock.yaml bun.lockb bun.lock 2>/dev/null

cat pyproject.toml 2>/dev/null || cat requirements.txt 2>/dev/null

cat go.mod 2>/dev/null

cat Cargo.toml 2>/dev/null
```

**Subagent 3 - Config and environment:**
Find required environment variables, linting setup, test framework, and deployment config.

```bash
cat .env.example 2>/dev/null || cat .env.sample 2>/dev/null || cat .env.template 2>/dev/null

ls tsconfig.json biome.json .eslintrc.js .eslintrc.json jest.config.ts vitest.config.ts 2>/dev/null

ls Dockerfile docker-compose.yml docker-compose.yaml 2>/dev/null
ls .github/workflows/ 2>/dev/null
```

**Subagent 4 - Existing documentation:**
Read any existing README, CLAUDE.md, AGENTS.md, or changelog.

```bash
cat README.md 2>/dev/null || cat readme.md 2>/dev/null
cat AGENTS.md 2>/dev/null
cat CLAUDE.md 2>/dev/null
cat CHANGELOG.md 2>/dev/null | head -60
```

**Subagent 5 - Source structure:**
Understand main source directories and identify the primary language.

```bash
for dir in src app lib packages server api; do
  test -d "$dir" && echo "=== $dir ===" && ls "$dir" && echo
done

for ext in ts tsx js jsx py go rs java swift kt; do
  count=$(find . -name "*.$ext" 2>/dev/null | \
    grep -cvE 'node_modules|dist|build|\.next|__pycache__|\.venv')
  [ "$count" -gt 0 ] && echo "$ext: $count files"
done
```

After all subagents return, synthesize findings. For each area, mark **Resolved** (code gave a clear answer) or **Still open** (needs user input):

- Project purpose and target users
- Tech stack (language, framework, database, package manager)
- Development commands (run, build, test, lint)
- Directory structure and what each area contains
- Architecture (how the pieces connect - only if non-trivial)
- Conventions (naming patterns, tooling rules, things easy to get wrong)
- Environment variables and setup
- Agent guidelines (things to always or never do in this codebase)


## Phase 2: Interview

For each still-open area, ask the user **one question at a time**. One answer often resolves several areas - re-evaluate after each reply.

Priority order:
1. **Project purpose** - "What does this project do, and who are the main users?"
2. **Agent guidelines** - "Any rules for agents working here? Things they should always do, or never do?"
3. **Architecture** - "How do the main pieces connect?" (only if non-obvious from code)
4. **Conventions** - "Any naming rules or patterns agents must follow?" (only if not visible from code)

**Loop cap.** After 6 questions total, stop asking. Record remaining unknowns as "Assumptions" in the generated files.

**Do not proceed to Phase 3 without at minimum: project purpose, tech stack, and development commands.**


## Phase 3: Generate Context Files

Mark Generate `in_progress`.

Write content using this structure. Include only sections that have real content - do not pad with "N/A" or empty bullets. Keep each section tight: a context file agents can scan in 10 seconds beats one they must read for a minute.

```markdown
# <Project Name>

<1-2 sentence description of what this project does and who uses it.>

## Tech Stack

- **Language:** <primary language(s)>
- **Framework:** <main framework>
- **Database:** <if applicable>
- **Package manager:** <bun / npm / pnpm / pip / go / etc.>
- **Key libraries:** <notable ones worth naming>

## Development

\`\`\`bash
# Install
<install command>

# Run
<dev server or main entry command>

# Test
<test command>

# Build
<build command>

# Lint / format
<lint command>
\`\`\`

## Directory Structure

\`\`\`
<key directories with 1-line descriptions, 4-10 entries>
\`\`\`

## Architecture

<1-3 sentences on how the major pieces connect. Include only when non-trivial. Skip for single-file or simple projects.>

## Conventions

<Bullet list of patterns, naming rules, or tooling decisions agents must follow. Include only items that are non-obvious or easy to get wrong. Skip entirely if there is nothing notable.>

## Environment

<List required env vars without values. Skip entirely if no .env file was found.>

\`\`\`
VARIABLE_NAME    # what it is for
\`\`\`

See \`.env.example\` for defaults.

## Agent Guidelines

**Always:**
- <rule>

**Never:**
- <rule>

<!-- context.md last-updated: <YYYY-MM-DD> -->
```

**Write the files:**

Write the content to whichever files are appropriate:
- If `HAS_CLAUDE_MD=false` OR `OVERWRITE=true`: write `CLAUDE.md`
- If `HAS_AGENTS_MD=false` OR `OVERWRITE=true`: write `AGENTS.md`
- If both already existed and `OVERWRITE=true`: replace both with the same content

The content is identical in both files. The only difference is the filename.

**Writing rules:**
- Use the actual project name as the H1 heading, not "Project Name"
- Keep the description factual - not marketing copy
- Only include `## Architecture` if the connections are non-obvious
- Only include `## Conventions` if there are clear, specific rules - not generic "write clean code" statements
- Only include `## Environment` if a `.env` file or template was found
- Always include `## Agent Guidelines` - even a minimal list prevents common agent mistakes
- The HTML comment `<!-- context.md last-updated: YYYY-MM-DD -->` must be the last line in every file - `/context-md-update` uses it to detect staleness


## Phase 4: Verify

Show the user the full content of the generated file(s). Ask: "Does this look right? Any sections to add, change, or remove?"

Apply requested changes directly. Re-show affected sections after each edit.

Do not mark Verify `completed` without at least one round of user review.


## Phase 5: Auto-Update Hook (Optional)

After the user confirms the context files, offer the auto-update hook:

> "Want me to add a reminder hook that prompts you to run `/context-md-update` at the end of every Claude Code session? This keeps the context fresh without manual effort."

If the user says yes, use the `update-config` skill to add a Stop hook:

```
Skill({ skill: "update-config", args: "add Stop hook: echo 'Context may be stale. Run /context-md-update to refresh CLAUDE.md and AGENTS.md.'" })
```

If `update-config` is not installed, write to `.claude/settings.json` directly (create the file if it does not exist, merge if it does):

```json
{
  "hooks": {
    "Stop": [
      {
        "matcher": "",
        "hooks": [
          {
            "type": "command",
            "command": "echo 'Context may be stale. Run /context-md-update to refresh CLAUDE.md / AGENTS.md.'"
          }
        ]
      }
    ]
  }
}
```

Tell the user the hook was added and confirm where (global `~/.claude/settings.json` or project `.claude/settings.json`).

If the user declines, skip silently.


## Completion Report

- **Files written:** list each file and line count
- **Sections included:** which sections made it in
- **Sections skipped:** any optional sections omitted and why
- **Assumptions:** anything left open that was filled with a best guess
- **Auto-update hook:** added or skipped

**context-md-update upsell.** Check if context-md-update is installed:

```bash
ls ~/.claude/skills/context-md-update.md .claude/skills/context-md-update.md 2>/dev/null && echo "INSTALLED" || echo "NOT_INSTALLED"
```

- **Installed:** "Run `/context-md-update` any time the codebase changes to refresh these files."
- **Not installed:** "Tip: `npx skills add -g amajorai/context.md` installs both `/context-md` and `/context-md-update` together."