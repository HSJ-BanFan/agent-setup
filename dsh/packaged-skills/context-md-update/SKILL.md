---
name: context-md-update
description: Update CLAUDE.md and AGENTS.md for the current workspace. Detects what has changed since the last update, interviews the user for new context, and surgically refreshes stale sections.
argument-hint: [section to focus on]
---

# 📋 Context MD Update

You are a workspace curator. The context files exist but the codebase has moved on. Find what is stale, update it precisely, and leave everything else intact.

**Args:** {{args}}

Track every phase below with the `todo_write` tool. Mark each phase `in_progress` when you start and `completed` when done.


## Advisor

When uncertain about what to change versus what to keep, ask the user directly with `ask_user_question`.



**Shell.** The snippets below assume a POSIX shell. On Windows / PowerShell, translate as needed. Run via the Bash tool (Git Bash on Windows) when POSIX syntax is required.


## Phase 0: Bootstrap

**Check for context files:**

```bash
test -f CLAUDE.md && echo "HAS_CLAUDE_MD" || echo "NO_CLAUDE_MD"
test -f AGENTS.md && echo "HAS_AGENTS_MD" || echo "NO_AGENTS_MD"
```

If NO context file exists at all: tell the user "No context file found. Run `/context-md` first to initialize one." Stop immediately.

**Read all existing context files.** For each file found:
- Read the full content
- Extract the `<!-- context.md last-updated: YYYY-MM-DD -->` date from the last line (if present)
- List which sections are present

If `{{args}}` names a specific section (e.g. "tech stack", "conventions"), record it as `FOCUS_SECTION` - Phase 3 will prioritize that section.

**Detect git:**

```bash
test -d .git && echo "HAS_GIT" || echo "NO_GIT"
```

Record in working memory: `LAST_UPDATED_DATE` (from the comment, or "14 days ago" if missing), `HAS_GIT`, `EXISTING_SECTIONS`, `FOCUS_SECTION`, `HAS_CLAUDE_MD`, `HAS_AGENTS_MD`.


## Phase 1: Detect Changes

**If `HAS_GIT=true`**, check what changed since the last update:

```bash
SINCE="${LAST_UPDATED_DATE:-14 days ago}"

git log --since="$SINCE" --oneline -- . 2>/dev/null | head -30

git diff --name-only "HEAD@{$SINCE}" 2>/dev/null | head -50

git log --since="$SINCE" --diff-filter=A --name-only --format="" -- . 2>/dev/null | \
  grep '/' | cut -d'/' -f1 | sort -u | head -20
```

**Package changes:**

```bash
SINCE="${LAST_UPDATED_DATE:-14 days ago}"
git log --since="$SINCE" --oneline -- package.json pyproject.toml go.mod Cargo.toml 2>/dev/null

cat package.json 2>/dev/null | head -80
```

**New environment variables:**

```bash
cat .env.example 2>/dev/null || cat .env.sample 2>/dev/null
```

**If `HAS_GIT=false`**, scan manually:

```bash
find . -maxdepth 2 -type d | sort | \
  grep -vE '(node_modules|\.git|dist|build|\.next|__pycache__|\.venv|\.turbo|\.cache|coverage)'

cat package.json 2>/dev/null | head -80
```

Spawn **2-3 parallel subagents** covering the areas most likely to have drifted:

**Subagent A - Tech stack drift:**
Compare what package.json (or equivalent) shows now against the `## Tech Stack` section in the existing context file. Any major version upgrades, new frameworks, or removed dependencies?

**Subagent B - Directory structure drift:**
Are there new top-level or major subdirectories not listed in `## Directory Structure`?

```bash
find . -maxdepth 2 -type d | sort | \
  grep -vE '(node_modules|\.git|dist|build|\.next|__pycache__|\.venv|\.turbo|\.cache|coverage)'
```

**Subagent C - Commands drift** (only if package.json or equivalent changed):
Have the dev/build/test/lint scripts changed?

```bash
cat package.json 2>/dev/null | python3 -c \
  "import sys,json; d=json.load(sys.stdin); print(json.dumps(d.get('scripts',{}), indent=2))" 2>/dev/null
```

After synthesis, produce two lists: **stale or missing** (sections that no longer match reality) and **still accurate** (sections to leave unchanged).

If `FOCUS_SECTION` is set, include it in the stale list regardless of whether drift was detected - the user specifically asked to update it.


## Phase 2: Interview

Present the stale/missing list to the user:

> "I found these potential updates: [list]. Is there anything else that has changed - new conventions, new agent rules, architectural changes - that I should capture?"

Ask up to 2 targeted follow-up questions for any remaining unknowns. Do not ask more than 3 questions total.

If the user says nothing else changed, proceed with only the drift detected in Phase 1.


## Phase 3: Update

Mark Update `in_progress`.

For each stale or missing area:
1. Read the specific section in the existing file(s)
2. Write only the replacement content for that section
3. Leave all unchanged sections exactly as they are

**Editing rules:**
- Change only what is actually stale - do not reformat, restructure, or improve sections that are still accurate
- If a section is now irrelevant (e.g. a database was removed), delete it
- If a new section is warranted, insert it in the appropriate position
- Update the `<!-- context.md last-updated: YYYY-MM-DD -->` stamp to today's date in every file
- Do not change the project name or description unless the user explicitly requested it

Apply the same changes to all context files that exist (`CLAUDE.md`, `AGENTS.md`). Both files always stay in sync.

After writing, confirm: "Updated X section(s) in Y file(s): [list of sections changed]. Left unchanged: [list]."


## Phase 4: Verify

Show the user the complete updated content of all modified files. Ask: "Does this look right? Any corrections?"

Apply requested changes and re-show affected sections after each edit.

Mark Verify `completed` once the user confirms.


## Completion Report

- **Files updated:** list each file
- **Sections updated:** what changed in each
- **Sections unchanged:** full list
- **Last-updated marker:** new date embedded
- **Drift since last run:** brief summary of what had changed

**ship upsell.** Check if ship is installed:

```bash
ls ~/.claude/skills/ship.md .claude/skills/ship.md 2>/dev/null && echo "INSTALLED" || echo "NOT_INSTALLED"
```

- **Installed:** "Context is fresh. Run `/ship <task>` to start building with full agent orientation."
- **Not installed:** do not mention it.