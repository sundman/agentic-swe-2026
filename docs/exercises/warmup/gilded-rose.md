# Warmup: Gilded Rose Kata

> **Core principle**: Human-AI Collaboration Patterns
> Your first interaction with an AI coding agent establishes habits you'll use throughout the workshop.

**Goal:** Get comfortable with Claude Code through a refactoring exercise

**Time:** ~30 minutes

**Prerequisites:** Claude Code installed, `gilded-rose/` directory available

> **Recommended model:** `sonnet` at medium effort (`/model sonnet`)

---

## Overview

The Gilded Rose is a classic refactoring kata. You'll use Claude Code as your pair programmer to understand, test, and refactor legacy code — learning key features along the way.

## Setup

First, set up the Python environment:
```bash
cd gilded-rose/python
uv sync
```

Then start Claude Code:
```bash
claude
```

When Claude Code starts, initialize the project:
```
/init
```

This analyzes your project structure and gives Claude deep understanding of the codebase.

> You may be prompted for file access permissions. Accept them for this session.

> **Note:** If you see errors about missing `pytest`, run `uv sync` in the `gilded-rose/python` directory to install dependencies.

---

## The Agentic Loop (~2 min)

Before you start, understand what Claude Code is doing under the hood. Every interaction follows the same cycle:

**Gather Context → Think → Act → Observe → Repeat**

1. **Gather**: Claude reads files, searches code, checks git state
2. **Think**: Claude reasons about what it found and what to do next
3. **Act**: Claude edits files, runs commands, creates tests
4. **Observe**: Claude checks the results — did tests pass? Did the build succeed?
5. **Repeat**: Based on results, Claude course-corrects and continues

This loop runs automatically. You can interrupt at any point with **Esc**. You'll see this cycle play out in every exercise — watch for it.

---

> **Expect 2–3 iterations, not 1**
>
> Your first interaction with Claude won't produce the final answer — it builds shared context. Expect 2-3 iterations before you have a direction worth pursuing. This is the process, not a failure.
>
> — Vincent Quigley, Sanity

---

## Part 1: Understand the Code

### 1.1 First Run the Tests

Open Claude Code in the `gilded-rose/python` directory. Start with four words: **"First run the tests."**

This orients the agent to the project's current state, reveals its complexity, and establishes the testing-first mindset you'll use throughout the workshop. (This is Simon Willison's ["First Run the Tests"](https://simonwillison.net/guides/agentic-engineering-patterns/first-run-the-tests/) pattern.)

### 1.2 Explore the Project

Ask Claude Code to explain what it found:

```
Explain what the Gilded Rose kata is about.
What are the main code quality issues you can see?
```

---

## Part 2: Test-Driven Safety Net

### 2.1 Explore /config

Type `/config` to open the interactive settings panel. This is your quick access to Claude Code's key settings — no JSON editing required.

Take 30 seconds to scan what's available:
- **Rewind code (checkpoints)** — verify this is enabled (it should be by default)
- **Model** and **effort level** — you can change these here or via `/model` and `/effort`
- **Auto-compact** — what happens when context fills up
- **Notifications**, **theme**, and other preferences

You'll use `/config` throughout the workshop to adjust settings on the fly. For project-level or team-shared settings, you'll use `.claude/settings.json` instead (covered in Lab C).

Every prompt creates an automatic checkpoint. You can always rewind if something goes wrong.

### 2.2 Assess Current Tests

```
What test coverage do we currently have?
```

### 2.3 Write Comprehensive Tests

```
Write characterization tests that capture all current behavior:
- Normal items degrading in quality
- Aged Brie increasing in quality
- Backstage passes with their complex rules
- Sulfuras never changing
- Quality bounds (0-50)
- Sell-by date edge cases

Then run the tests to verify they pass.
```

> **Reflection:** What did running the tests first tell you about the codebase that you wouldn't have known otherwise?

---

## Part 3: Refactoring with Rewind Safety

### 3.1 Analyze Quality Issues

```
What are the top 3 code quality issues that make this code hard to maintain?
```

### 3.2 First Refactoring

Before you start: make refactoring decisions yourself. When Claude suggests an approach, articulate WHY you agree or disagree before accepting it. Don't just accept the first suggestion.

```
Extract the logic for each item type into separate methods.
Make the changes and run the tests to ensure they still pass.
```

### 3.3 Experiment Fearlessly

```
Add an additional test case for the item type "Vegemite". Treat it as a normal item.
```

### 3.4 Rewind

Press **Esc twice** (or type `/rewind`) to open the rewind menu. Choose a checkpoint from before the "Vegemite" change and select **Restore code and conversation**.

> **Key insight**: Checkpoints + rewind = fearless experimentation. Try bold refactoring approaches knowing you can always go back.

### 3.5 Add Conjured Items

```
Add support for "Conjured" items that degrade in quality twice as fast as normal items.
Write tests first, then implement, then verify.
```

> **Reflection:** What did Claude get right in its refactoring suggestions? Where did you disagree, and why?

---

## Part 4: Review & Commit

### 4.1 Review Your Work

```
Summarize all the refactoring changes we made.
What improvements did we achieve in code quality?
```

### 4.2 Create a Commit

```
Create a git commit with all our changes. Write a detailed commit message.
```

> **Reflection:** How many iterations did it take? Did the Three-Attempt expectation match your experience?

---

## Key Commands Reference

> Full list: [code.claude.com/docs/en/commands](https://code.claude.com/docs/en/commands) · Keyboard shortcuts: [code.claude.com/docs/en/interactive-mode](https://code.claude.com/docs/en/interactive-mode)

### Setup & Configuration

| Command | Purpose |
|---------|---------|
| `/config` | Interactive settings panel (model, effort, theme, etc.) |
| `/doctor` | Diagnose installation issues |
| `/effort` | Control reasoning depth (low/medium/high) |
| `/init` | Analyze project and create CLAUDE.md |
| `/model` | Switch model (sonnet, opus, haiku) |
| `/terminal-setup` | Configure terminal for optimal experience |

### Context & Memory

| Command | Purpose |
|---------|---------|
| `@filepath` | Add a file to conversation context |
| `/btw <question>` | Quick side question (no tools, ephemeral) |
| `/compact` | Compress conversation to free context |
| `/context` | Show context window usage and token breakdown |
| `/memory` | View/edit auto memory and CLAUDE.md |
| `/plan` | Enter Plan mode (read-only exploration) |

### Session Management

| Command | Purpose |
|---------|---------|
| `/branch` | Fork conversation into a copy |
| `/rename` | Name current session for findability |
| `/resume` or `--resume` | Browse and continue a previous session |
| `/rewind` or `Esc Esc` | Restore code/conversation from checkpoint |

### Review & Verification

| Command | Purpose |
|---------|---------|
| `/copy` | Copy last response to clipboard |
| `/cost` | Show token usage and cost |
| `/diff` | Interactive diff viewer |
| `/insights` | Session analysis report |
| `/security-review` | Analyze changes for vulnerabilities |
| `/usage` | Show plan limits and usage |

### Extensions & Security

| Command | Purpose |
|---------|---------|
| `!command` | Run shell command directly (bash mode) |
| `/help` | List all commands |
| `/mcp` | Manage MCP server connections |
| `/permissions` | View active permission rules |
| `/status` | Session info |
| `/tasks` | Manage task list (useful with Agent Teams) |

## Keyboard Shortcuts

> **macOS note:** Shortcuts using `Alt` (like `Alt+P`) require Option configured as Meta key in your terminal. In iTerm2: Settings → Profiles → Keys → set Option key to "Esc+". Run `/terminal-setup` for guided configuration.

| Action | macOS | Windows/Linux |
|--------|-------|---------------|
| Accept prompt suggestion | `Tab` | `Tab` |
| Background a task | `Ctrl+B` | `Ctrl+B` |
| Cycle permission modes | `Shift+Tab` | `Shift+Tab` |
| Exit session | `Ctrl+D` | `Ctrl+D` |
| Interrupt | `Esc` | `Esc` |
| Navigate history | `Up/Down` arrows | `Up/Down` arrows |
| New line | `Option+Enter` | `Shift+Enter` (varies by terminal) |
| Open in text editor | `Ctrl+G` | `Ctrl+G` |
| Open rewind menu | `Esc Esc` | `Esc Esc` |
| Paste image | `Ctrl+V` or `Cmd+V` (iTerm2) | `Ctrl+V` or `Alt+V` |
| Push-to-talk (voice) | Hold `Space` | Hold `Space` |
| Switch model | `Option+P` | `Alt+P` |
| Toggle task list | `Ctrl+T` | `Ctrl+T` |
| Toggle thinking | `Option+T` | `Alt+T` |

---

> **💡 Plugin tip: pyright-lsp** — Install the Python LSP plugin (`/plugin install pyright-lsp@claude-plugins-official`) to give Claude type-aware refactoring suggestions. With LSP enabled, Claude can use go-to-definition, find-references, and type diagnostics — making the Gilded Rose refactoring noticeably more precise.

---

## Key Takeaways

| Feature | What You Learned |
|---------|-----------------|
| `/init` | Bootstraps project understanding |
| Test-first | "First run the tests" reveals state before you write a line |
| Checkpoints | Automatic snapshots at every prompt |
| `/rewind` | Fearless experimentation and rollback |
| Iteration | 2–3 exchanges to build shared context is normal |
