# Exercise 4: Building a Feature

**Goal:** Complete the full Plan → Implement → Verify cycle using Claude Code, MCP servers, and git workflows

**Time:** ~50 minutes (stretch challenges are extra)

**Prerequisites:** Exercise 3 completed, AndThen plugin installed

> **Recommended model:** `sonnet` at medium effort (`/model sonnet`)

---

> **Core principle**: Plan → Implement → Verify (the PIV Loop)
> Humans own planning and validation. Agents own implementation. This is "The Sandwich Principle."
> See `docs/reference/piv-loop.md`

---

## The Feature: Priority Filter Buttons

You'll add filter buttons above the todo list that let users filter by priority: **All**, **Low**, **Medium**, **High**.

This touches backend (route), frontend (template + HTMX attributes), and styling — a realistic full-stack feature.

---

## Before You Start: The Engineer's Workflow

An Anthropic engineer's actual process: Research → annotation cycle (1-6 rounds reviewing the plan with Claude) → implementation. [Boris Tane](https://x.com/boristane)'s rule: "Never let Claude write code until you've reviewed and approved a written plan." This is the Sandwich Principle in practice.

The three phases below follow this pattern exactly.

---

## Phase 1: Plan (~10 min)

### 1.1 Enter Plan Mode

Press **Shift+Tab** twice to enter Plan mode (or start a new session with `--permission-mode plan`).

### 1.2 Research and Plan

```
I want to add priority filter buttons to the todo list. The buttons should
appear above the todo list: All, Low, Medium, High. Clicking a button should
filter the visible todos. The "All" button should be active by default.

Analyze the current codebase and create a detailed implementation plan.
Consider:
- How the current todo list rendering works
- Where to add the filter UI
- Whether to filter client-side or server-side
- How to maintain filter state across interactions
```

> **Architecture note:** The todo list is currently server-rendered via Jinja `{% include %}` tags — there is no separate API endpoint that returns filtered todos. Your plan will need to either add a new endpoint that returns filtered HTML, or modify the existing rendering to accept a filter parameter. This is a design decision worth discussing in your plan.

### 1.3 Use MCP for Documentation

Claude Code has MCP servers configured for documentation lookup. While in Plan mode, ask:

```
Look up the HTMX documentation for hx-get and how to implement
active button state. Use the Context7 MCP server.
```

<details>
<summary>What's happening here?</summary>

MCP (Model Context Protocol) servers extend Claude Code with external tools. The project has two configured in `.mcp.json`:

- **Context7**: Looks up library documentation (FastAPI, HTMX, SQLAlchemy, etc.)
- **Fetch**: Downloads web content as markdown

Claude automatically uses these when it needs documentation. You can also explicitly ask it to use them.
</details>

### 1.4 Review the Plan

Read Claude's plan carefully. Does it make sense? Would you approach it differently?

### 1.5 Save the Plan

Before leaving Plan mode, save the plan to a file:

```
Write this plan to a file called PLAN.md in the project root.
```

This is critical: when you start a fresh context for implementation (Phase 2), the plan will be lost unless it's written to a file. This follows Boris Tane's rule and the PIV Loop workflow in `docs/reference/piv-loop.md`.

Switch back to Normal mode: press **Shift+Tab**.

---

> **Alternative: Red/Green TDD path** (optional)
>
> Instead of planning, write failing tests for the priority filter first. Confirm they fail.
> Then prompt Claude: "Make these tests pass."
> Two-word shortcut: "Build the priority filter. Use red/green TDD."
>
> This forces specification-before-implementation and makes your expectations explicit.
>
> ([Willison](https://simonwillison.net/guides/agentic-engineering-patterns/): "Despite previously hating test-first TDD as a human practice, I use it with agents because tests are effectively free now.")
>
> If you take this path, skip to Phase 2 — your failing tests are the plan.

---

## Phase 2: Implement (~20 min)

### 2.1 Session Management & Fresh Context

Before exiting your planning session, name it so you can find it later:

```
/rename priority-filter-planning
```

Now exit and start a fresh session for implementation:

```
# Press Ctrl+D to exit
claude
```

Why start fresh? Plan mode fills the context with research. A fresh session gives Claude more room for implementation details. But naming the session means you can return to it:

```bash
# Resume most recent session
claude --continue

# Browse all sessions — press P to preview, R to rename, B to filter by branch
claude --resume
```

You can also **fork** a conversation with `/branch` — this creates a copy you can take in a different direction while preserving the original.

And remember: **Esc Esc** (double escape) opens the rewind menu within any session, letting you restore code, conversation, or both from any previous checkpoint.

**When to resume vs start fresh:**
- **Resume** when you need the full conversation context (e.g., returning to a complex debugging session mid-investigation)
- **Fresh + HANDOFF.md** when the old context would be stale or distracting (e.g., moving from planning to implementation — a clean slate is the point)

Both are valid. The PIV loop recommends fresh context for implementation because plan-phase research would dilute the implementation context.

### 2.2 Implement the Feature

Give Claude the implementation instructions based on what the plan identified. For example:

```
Add priority filter buttons to the todo list. Requirements:

1. Add filter buttons (All, Low, Medium, High) above the todo list
2. Use HTMX to fetch filtered todos from the server
3. Add a query parameter ?priority=low|medium|high to the todo list endpoint
4. The "All" button should be active by default
5. Maintain the active button state visually
6. Style the buttons using Shoelace components

Follow the existing patterns in the codebase.
```

> **💡 Plugin tip: pyright-lsp** — If you installed the Python LSP plugin in an earlier exercise, notice how Claude uses type information during implementation. LSP diagnostics catch issues before tests run, tightening the agentic loop.

### 2.3 Watch the Implementation

Notice how Claude:
- Reads relevant files first
- Modifies the backend route to accept a filter parameter
- Updates the template to add filter buttons
- Adds HTMX attributes for dynamic filtering
- Styles the buttons to match the existing UI

### 2.4 Test Manually

Open the app in your browser and test:
1. Do the filter buttons appear?
2. Does clicking "High" show only high-priority todos?
3. Does "All" show everything?
4. Does the active state highlight the selected filter?

If something doesn't work, describe the issue to Claude Code.

> **Known limitation:** The filter buttons sit outside the `#todos-list` HTMX swap target. This means clicking a filter replaces the todo list but doesn't update which button appears active. The active state only works correctly on initial page load. This is a real HTMX scoping challenge — solving it requires either including the buttons inside the swap target or using an `hx-swap-oob` response to update the buttons separately. If you notice this, it's a great learning moment about HTMX swap boundaries.

---

## Phase 3: Verify (~15 min)

### 3.1 Run Existing Tests

```
Run the full test suite to make sure nothing is broken.
```

Check your token usage so far:
```
/cost
```

Note the cost. After writing tests and doing the review, run `/cost` again and compare. This builds intuition for how different activities (planning vs implementing vs testing) consume tokens differently.

> **💡 Plugin tip: code-simplifier** — After implementation, try running the `code-simplifier` plugin (`/plugin install code-simplifier@claude-plugins-official`). It autonomously reviews recently modified code for clarity, redundancy, and naming — demonstrating the annotation cycle (build → review → simplify → commit).

### 3.2 Add Tests for the New Feature

```
Write tests for the priority filter feature:
- Filter returns only todos with matching priority
- "All" filter returns all todos
- Filter works with empty results
- Invalid priority parameter is handled gracefully
```

### 3.3 Manual Verification with curl

Tests pass, but does it actually work? Make sure the dev server is running (`uv run uvicorn app.main:app --reload` in the `todo-app/` directory). Then instruct Claude:

```
Use curl to test the priority filter with:
1. A valid priority filter (e.g., ?priority=high)
2. An invalid filter value (e.g., ?priority=invalid)
3. Filtering when no todos match (e.g., ?priority=urgent when none exist)
```

Compare actual responses vs expected. Willison: "Never assume that code generated by an LLM works until that code has been executed."

### 3.4 Code Review

Use AndThen for a thorough review:

```
andthen.review-code
```

Address any findings.

### 3.5 Writer/Reviewer Pattern (Optional)

For higher-stakes changes, use two separate sessions: one writes code, another reviews with fresh context. The reviewer has no knowledge of the implementation journey — only the code itself. This mimics how human code review works and catches assumptions that accumulated during implementation.

Try it: start a new Claude Code session and ask it to review the priority filter changes without any context about how they were built:

```
Review the recent changes to the todo list filtering. Focus on edge cases, error handling, and HTMX best practices.
```

Compare this review to the one from `andthen.review-code`. Did the fresh-context reviewer catch anything the in-session reviewer missed?

### 3.6 Clean Up

Once the feature is implemented and verified, delete `PLAN.md` — it served its purpose as a handoff artifact between planning and implementation sessions.

### 3.7 Write a PR Description

Write a PR description for the priority filter feature you just built (this is a writing exercise — no actual PR required):

- **Intent**: What did you build and why? (1-2 sentences)
- **Proof**: What tests pass? What did you manually verify?
- **Risk tier**: Low / Medium / High — and your reasoning
- **Needs review**: Specific areas where you want human eyes

This is Willison's anti-pattern in reverse: "Don't file pull requests with code you haven't reviewed yourself." Writing this PR description forces you to take that review step seriously.

### 3.8 Create a Git Commit

```
Create a git commit for the priority filter feature.
Write a descriptive commit message.
```

### 3.9 Create a Pull Request (Bonus)

If your repo is connected to GitHub:

```
Create a pull request for this feature. Include a summary
of what was added and how to test it.
```

---

## Harvest the Feedback

Ask Claude:

```
Looking at the plan we created together — what was missing from it that
made implementation harder? What context would have helped you implement
this feature faster or with fewer iterations?
```

Use the answer to improve how you write plans next time.

---

## Stretch Challenges

These are independent of the main exercise — pick any that interest you.

- **Count badges**: Add a count of todos per priority level next to each filter option in the sidebar
- **localStorage persistence**: Remember the selected filter across page reloads
- **Keyboard shortcuts**: Add keyboard shortcuts (`h`, `m`, `l` for high/medium/low) to switch filters
- **URL query state**: Reflect the current filter in the URL (`?priority=high`) so it's bookmarkable and shareable
- **Red/Green TDD**: If you used the standard path above, try one of these stretch features using red/green TDD instead
- **Headless mode**: Run `claude -p "List all TODO comments in the codebase" --output-format json` from your terminal. This is how you use Claude Code in shell scripts, CI/CD pipelines, and automation. Try piping output: `claude -p "Generate test data for the todo app" | python -c "import sys; print(sys.stdin.read()[:500])"`

---

## Understanding MCP Servers

During this exercise, you used MCP servers for documentation. Here's how they work:

### What's Configured

Check `.mcp.json` in the project root:

```json
{
  "mcpServers": {
    "context7": {
      "command": "npx",
      "args": ["-y", "@upstash/context7-mcp@latest"]
    },
    "fetch": {
      "command": "uvx",
      "args": ["mcp-server-fetch"]
    }
  }
}
```

### MCP Scopes

| Scope | File | Shared? |
|-------|------|---------|
| Project | `.mcp.json` | Yes (git) |
| User | `~/.claude.json` | No, all projects |
| Local | `~/.claude.json` (project section) | No, this project |

### Managing MCP Servers

```bash
# Add a new server
claude mcp add context7 -- npx -y @upstash/context7-mcp@latest

# List configured servers
claude mcp list

# Remove a server
claude mcp remove context7
```

### Common MCP Servers

| Server | Purpose |
|--------|---------|
| Context7 | Library documentation lookup |
| Fetch | Download web content as markdown |
| GitHub | Issues, PRs, repository management |
| Postgres/SQLite | Direct database access |
| Playwright | Browser automation and testing |

> **Key insight**: MCP servers are how Claude Code connects to external tools and data sources. Exercise 5 covers this in depth.

---

## Key Takeaways

| Concept | Remember |
|---------|----------|
| PIV Loop | Plan → Implement → Verify (The Sandwich Principle) — see `docs/reference/piv-loop.md` |
| Fresh context | Start new session for implementation after planning |
| "Tests pass" ≠ "it works" | Always manually verify — run the code, use curl, test edge cases |
| PR Contract | Intent + proof + risk tier + review areas before committing |
| Red/Green TDD | Two-word shortcut: "Use red/green TDD" — tests are effectively free now |
| MCP servers | External tools configured in `.mcp.json` |
| Code review | Use `andthen.review-code` (or ask Claude directly) before committing |

---

## Resources

- [MCP Servers Documentation](https://code.claude.com/docs/en/mcp)
- [HTMX Documentation](https://htmx.org/docs/)
- [FastAPI Query Parameters](https://fastapi.tiangolo.com/tutorial/query-params/)
- PIV Loop reference: `docs/reference/piv-loop.md`
