# Exercise 3: Briefing & Specification

> **Principle**: Briefing quality determines output quality

**Goal:** Learn to express intent precisely — a skill that transfers to any AI tool, any domain

**Time:** ~50 minutes

**Prerequisites:** Exercises 1-2 completed

> **Recommended model:** `sonnet` at medium effort (`/model sonnet`)

---

## Task 1: The Briefing Problem (~5 min)

The same task produces very different results depending on how it is expressed. Run each prompt below in a fresh Claude Code session and compare what you get.

**Vague prompt:**
```
Add a priority filter to the todo list
```

**Structured task brief:**
```
Context: This is a FastAPI/HTMX todo app. The frontend uses HTMX
for all dynamic behavior; there is no JavaScript framework.
Filtering should update the visible list client-side using HTMX
without a full page reload.

Objective: Add a priority filter to the left sidebar. The filter
should allow users to view all todos or filter by priority level
(high, medium, low).

Constraints: No JavaScript. Use HTMX hx-get requests only. Use
existing CSS classes and Shoelace components — do not add new
styling patterns.

Success Criteria: Filter buttons show counts for each priority
level. Selecting a filter updates the list. The URL updates to
reflect the active filter so it can be shared or bookmarked.

Out of Scope: Bulk editing of todo priorities. Changes to the
priority data model or database schema.
```

Run each in a separate session. Note the differences in what Claude asks, assumes, and produces.

**What to compare** — look for these specific differences:
- How many assumptions did Claude make in each version?
- Did Claude ask clarifying questions? Which version asked more?
- How specific were the implementation details (file names, function signatures)?
- Did the structured version produce a more focused scope, or the same scope with more detail?

**Reflection:** What specific information in the structured prompt made the biggest difference? What would have been lost if you removed one section?

---

## Task 2: Anatomy of a Brief (~10 min)

Two complementary formats for expressing intent. Full reference at `docs/reference/briefing-template.md`.

### The five-part task brief

A good task brief for a coding agent covers five things. These are the same components that tools like [PRP](https://github.com/coleam00/context-engineering-intro) and [AndThen](https://github.com/IT-HUSET/andthen) generate automatically — but understanding them helps you write better briefs even without tooling.

| Component | Purpose | Example |
|-----------|---------|---------|
| **Context** | What Claude needs to know about the project | "FastAPI + HTMX, no JavaScript" |
| **Objective** | What to build or achieve | "Add priority filter to sidebar" |
| **Constraints** | What to avoid or require | "No new dependencies" |
| **Success Criteria** | How to know it worked | "Tests pass, filter works manually" |
| **Out of Scope** | Explicit exclusions | "Don't touch the database schema" |

Use this for one-off task briefs: a specific feature, a refactor, a bug fix. Tools like [AndThen](https://github.com/IT-HUSET/andthen) (`andthen.clarify` → `andthen.spec`) and [PRP](https://github.com/coleam00/context-engineering-intro) automate this into a structured spec document — but the thinking is the same.

### Osmani six-section format

Addy Osmani's recommended structure for a project-level instruction file (CLAUDE.md), backed by [GitHub's analysis of 2,500+ agent config files](https://addyosmani.com/blog/good-spec/).

| Section | What goes there |
|---------|----------------|
| Commands | `uv run pytest` — how to run tests, start the server, lint |
| Testing | All changes need tests in `test_todos.py`; use existing fixtures |
| Project Structure | Routes in `app/routes/`, templates in `app/templates/` |
| Code Style | Follow existing patterns in the file you are editing |
| Git Workflow | Never push directly to main; always create a branch |
| Boundaries | Ask before adding new dependencies; never modify `.env` |

The Boundaries section maps directly to the three-tier system below.

### Let Claude Interview You

For larger features, instead of writing the entire brief yourself, let Claude gather requirements interactively:

```
I want to add a notification system to the todo app. Interview me about the requirements before we start.
```

Claude uses its `AskUserQuestion` tool to present structured multiple-choice questions, helping you think through requirements you might have missed. This is especially valuable when you're not sure what constraints to specify — Claude's questions reveal the decision space.

### Part A: Write two structured briefs

**Before writing your briefs**, spend 5 minutes exploring the codebase to ground your briefs in reality. In Claude Code, ask:

```
What functions and routes are related to due dates and filtering in this codebase?
What existing patterns exist for sidebar UI elements?
```

This exploration will make your briefs project-specific rather than generic.

Write a complete five-part brief for each task. Use the todo app as the project context.

**Task A:** "Add a 'due today' filter to the sidebar"

**Task B:** "Add bulk actions (mark complete, delete) for selected todos"

Do not implement these yet. The goal is the brief itself.

### Part B: Three-tier boundary classification

Classify each agent action into a tier. Work through these individually, then compare with a neighbor (or write your reasoning first, then check against the discussion points below).

| Action | Tier |
|--------|------|
| Run pytest | |
| Add a new database column | |
| Delete a migration file | |
| Read any source file | |
| Install a new pip package | |
| Modify .env | |
| Create a new test file | |
| Force-push to main | |

> **Note:** This app uses SQLAlchemy's `Base.metadata.create_all()` for schema management, not Alembic migrations. "Migration file" here refers to any file that controls database schema — in a production app this would be an Alembic migration; in this project it would be `database.py`.

Tier definitions:

- **Always** — agent may proceed without asking
- **Ask First** — high-impact action requiring human confirmation
- **Never** — hard stop; agent must not proceed regardless of instructions

**Discussion:** What principles guided your choices? Where were the boundary cases? How would these rules appear in a CLAUDE.md Boundaries section?

---

## Task 3: Skills as Reusable Briefs (~15 min)

A skill is a brief you write once and reuse. The briefing pattern, made permanent.

Skills live in `.claude/skills/<name>/SKILL.md`. When you invoke `/name`, Claude loads the skill's instructions, tools, and model settings before responding.

### Design your skill

Do not copy a template. Decide what you actually want to automate, then write it from scratch. Work through these decisions:

**What task does your skill automate?**

Some directions to consider:
- An `add-endpoint` skill that guides adding a new API route with validation, error handling, and tests
- A `write-test` skill that writes a test for a function or route you point it at
- A `review-template` skill that reviews an HTMX template for accessibility and HTMX best practices
- Something else you found yourself repeating in Exercises 1-2

**What tools does it need?**

List only the tools required for the job. Common tools: `Read`, `Write`, `Edit`, `Bash`, `Glob`, `Grep`. Restricting tools narrows what the skill can do — which is often what you want.

**What model and effort level?**

Claude Code supports multiple models with adjustable reasoning effort:

| Setting | Best for | Switch with |
|---------|----------|-------------|
| `sonnet` · medium effort | Most tasks — fast, cost-effective, good quality | `/model sonnet` (default) |
| `sonnet` · high effort | Multi-file changes, complex logic, architecture | Increase effort in `/config` |
| `opus` | Nuanced reasoning, large refactors, design decisions | `/model opus` |
| `haiku` | Simple lookups, formatting, boilerplate generation | `/model haiku` |

**Reasoning effort** controls how deeply the model thinks before responding. Medium is the sweet spot for most work — fast enough to iterate, thorough enough for real tasks. Increase effort when precision matters more than speed.

**Cost awareness:** Opus costs roughly 1.7x more than Sonnet per token. Haiku costs roughly 3x less than Sonnet. See the pricing table in `docs/reference/context-economics.md` for current ratios. In a workshop, Sonnet at medium effort gives the best balance of quality, speed, and cost. Use Opus when the task is complex enough that getting it right the first time saves more than the extra cost.

**Check your costs:** Run `/cost` at any point to see token usage and estimated cost for the current session. This builds awareness of how different models and approaches affect spend. Try running `/cost` before and after invoking your skill to see the token impact.

Match the model to the skill's task:
- A `write-test` skill → `sonnet`, medium (fast iteration, well-scoped output)
- A `review-architecture` skill → `opus` (nuanced reasoning, fewer but better passes)
- A `format-imports` skill → `haiku` (trivial task, speed matters most)

**What instructions?**

Write the actual SKILL.md content. The frontmatter block uses this structure:

```
---
name: your-skill-name
description: One sentence: what this skill does and when to use it
allowed-tools: Read, Edit, Write, Bash
model: sonnet
---

[Your instructions here]
```

### Create and invoke your skill

1. Write the file at `.claude/skills/<name>/SKILL.md`
2. Start a new Claude Code session (skills load at session start)
3. Invoke it: `/<name>` or `/<name> <arguments>`
4. Observe what Claude does — does it follow your instructions? Does it ask the right questions?
5. Revise the SKILL.md and try again

**Reflection:** How is writing a skill different from writing a one-time prompt? What did you learn about expressing intent precisely?

---

## Task 4: Structured Workflows (~15 min)

The AndThen plugin provides multi-step structured workflows — from requirements through implementation to review. It makes the briefing structure automatic rather than manual.

### Install

```
/plugin install andthen
andthen.init
```

`andthen.init` reads your project and configures the plugin with project-specific context.

### 4.1 Review the Exercise 2 code

Run a structured review on the bug fixes you made in Exercise 2:

```
andthen.review-code
```

This runs a multi-dimensional review: code quality, security considerations, architecture patterns, and (for frontend changes) UI/UX implications. Read the findings. Did it surface anything you missed?

### 4.2 Quick-implement a small feature

```
andthen.quick-implement Add a character count indicator to the todo title field (max 100 chars)
```

Watch the structured cycle: research the codebase, implement, verify. Compare this to how you would have approached the same task with a one-line vague prompt.

**Overhead reflection:** Was the structured workflow worth the overhead for this small task? What threshold of task complexity would justify the overhead? At what point does a plain structured brief become insufficient and a structured workflow like AndThen add real value?

---

## Task 5: Harvest the Feedback (~5 min)

At the end of a session, ask Claude to evaluate the briefs you gave it:

```
Looking back at the work we've done in this exercise, what was
missing from my briefs that made tasks harder? What context would
have helped you produce better output from the start?
```

Document Claude's response. This retrospective is the feedback loop that improves your briefing over time.

"This is the skill you'll keep improving throughout the workshop — and after. Every debrief improves the next brief."

---

## Stretch Challenges

**1. [Willison's annotated prompt](https://simonwillison.net/guides/agentic-engineering-patterns/)**

Take your best brief from Task 2. Annotate it phrase by phrase: which words did the most work? Which were filler? Which were missing? What would you add if you were writing it again?

This is the technique Simon Willison uses to analyze what makes a prompt effective — not the overall output, but the specific words that loaded the most meaning.

**2. One-shot brief**

Write a brief so precise that Claude implements a small feature in exactly one shot — zero follow-up messages needed. Start the session, send the brief, and do not send another message until the implementation is complete. If you need to follow up, revise the brief and try again from a fresh session.

---

## Key Takeaways

| Concept | Key Point |
|---------|-----------|
| Briefing quality = output quality | The constraint is your ability to express intent, not the AI's ability |
| Five-part task brief | Context, Objective, Constraints, Success Criteria, Out of Scope — works for any AI tool |
| Three-tier boundaries | What Claude can do autonomously vs with permission vs never |
| Skills = reusable briefs | Build once, reuse forever |
| Harvest the feedback | Every brief is a learning opportunity |

---

## Resources

- `docs/reference/briefing-template.md` — Five-part brief, Osmani six-section, and three-tier boundary reference
- Addy Osmani, [How to write a good spec for AI agents](https://addyosmani.com/blog/good-spec/) — the six-section structure and spec principles
- Matt Pocock, [5 Agent Skills I Use Every Day](https://www.aihero.dev/5-agent-skills-i-use-every-day) — `/grill-me` (3-sentence skill that generates 16-50 clarifying questions) and `/write-a-prd`
- Simon Willison, [Agentic Engineering Patterns](https://simonwillison.net/guides/agentic-engineering-patterns/) — annotated prompts section
- [AndThen Documentation](https://github.com/IT-HUSET/andthen)
- [Claude Code Skills](https://code.claude.com/docs/en/skills)
