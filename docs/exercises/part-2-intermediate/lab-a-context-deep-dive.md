# Lab A: Context Deep Dive

**Time:** ~60 minutes | **Prerequisites:** Part 1 completed

> **Recommended model:** `sonnet` at medium effort (`/model sonnet`)

---

> **Principle**: Context is probabilistic infrastructure — manage it deliberately

> **WISC strategy**: SELECT (load context just-in-time) + WRITE (externalize memory to files)

> **You will**:
> - Audit your context window and identify what's consuming tokens
> - Experience the performance difference between overloaded and minimal context
> - Build a feature using [Willison's recombination pattern](https://simonwillison.net/guides/agentic-engineering-patterns/hoard-things-you-know-how-to-do/)
> - Induce context rot and practice recovery techniques

> **Reference cards**: [Context Economics](../../reference/context-economics.md) · [Failure Patterns](../../reference/failure-patterns.md) (context rot entry)

---

## The Challenge

Build a small feature for the todo app using deliberately managed context. Start by auditing what's currently in your context window — what percentage is used, and what's consuming it? Then build the same small feature twice: once with all tools and context loaded, once with only the minimum needed. Compare quality, speed, and token cost. Next, try Willison's recombination pattern: identify two existing patterns in the codebase and combine them to build something new. Finally, run a long session until you observe context rot symptoms, then practice recovery.

---

## Suggested Approach

1. Use `/context` to inspect your context window. Look at the breakdown: how many tokens are from system context (CLAUDE.md, rules files)? How many are from conversation history? Which files appear in the system tokens? This tells you what's "always on" versus what accumulates during work. Note the token count and what's consuming the most tokens. Use the token-based thresholds from the reference card as benchmarks: < ~50K normal, ~100K precision drops, ~150K+ erratic behavior.

> **💡 Plugin tip: claude-md-management** — The `claude-md-improver` skill from this plugin audits your CLAUDE.md against the live codebase. Use it during Activity 1 to see how much of your context setup actually maps to what the project needs.

2. Pick a small feature (e.g., "add a created-at timestamp display to each todo"). Build it once with everything loaded. Start a fresh session, load only the files directly relevant, and build the same feature. Compare the outputs.

> **💡 Plugin tip: playground** — Try the `playground` plugin (`/plugin install playground@claude-plugins-official`) to create an interactive architecture explorer for the todo-app. Ask Claude to build a playground showing component relationships (routes → services → models → templates) with toggleable layers. Building this forces you to articulate the architecture — a powerful WRITE strategy artifact.

3. [Willison's recombination](https://simonwillison.net/guides/agentic-engineering-patterns/hoard-things-you-know-how-to-do/): find two existing patterns in the codebase (e.g., an API endpoint and a template pattern). Ask Claude to build something new by combining them. Tip: use the Read tool or `/add <filepath>` to load raw file content when you need Claude to see the full source, not just summaries.

4. Practice context management recovery. By this point in the lab, you've consumed significant context through Activities 1-3. Run `/context` to check your current usage. Practice `/compact` with a specific focus instruction — for example: `/compact` then tell Claude: "Summarize focusing on the created-at feature implementation and context audit findings." Compare your context usage before and after. Then create a `HANDOFF.md` file using the template below — this is the WRITE artifact that survives a context reset:

```markdown
# Session Handoff

## Current State
[What's working, what's broken, what's in progress]

## Key Decisions Made
[Architecture choices, patterns selected, tradeoffs accepted]

## Files Changed
[List of modified files and what changed in each]

## What's Next
[Remaining work, in priority order]

## Key Constraints
[Non-obvious constraints discovered during this session]

## Context to Preserve
[Insights that would be lost if starting fresh without this file]
```

Start a fresh session and use only the HANDOFF.md to resume work. How much was preserved? What was lost?

---

## Reflection

1. "How much of your context was actually useful vs noise? If you could keep only 20% of what was loaded, what would it be?"

2. "Did fewer tools and less context produce better or worse results? Did it surprise you?"

3. "Which WISC strategy (WRITE or SELECT) was most valuable for this lab? In what situation would the other be more important?"

---

## Stretch

- Spotify challenge: "The more tools you have, the more dimensions of unpredictability you introduce." Remove all MCP servers except one. Can you still build the feature? What do you trade?

- Context infrastructure audit: In a production codebase, context infrastructure (CLAUDE.md + rules + skills + hooks) consumed 24.2% of the entire codebase. Estimate: what percentage of the todo-app project is now "context infrastructure"? Is that the right ratio?
