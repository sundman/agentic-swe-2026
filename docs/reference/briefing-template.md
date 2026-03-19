# Briefing Template Reference

Quick reference for writing structured prompts and specifications.

---

## The Five-Part Task Brief

Five-component structure for any non-trivial task brief. These are the same components that spec-driven tools like [AndThen](https://github.com/IT-HUSET/andthen) (`andthen.clarify` → `andthen.plan`) and [PRP](https://github.com/coleam00/context-engineering-intro) generate automatically — formalizing what good engineering briefs have always contained.

| Component | Purpose | Example |
|-----------|---------|---------|
| **Context** | Background the agent needs to understand the situation | "This is a FastAPI app using HTMX for frontend; no JavaScript frameworks." |
| **Objective** | The specific outcome required | "Add a due-date filter to the todo list endpoint." |
| **Constraints** | What must not change or be violated | "Do not modify the database schema; stay within existing routes." |
| **Success Criteria** | How you will verify completion | "All 58 tests pass; filter works for past/today/future." |
| **Out of Scope** | Explicit exclusions to prevent scope creep | "Do not add UI; backend only for now." |

---

## [Osmani Six-Section CLAUDE.md Format](https://addyosmani.com/blog/good-spec/)

Structure for a project-level instruction file, based on [GitHub's analysis of 2,500+ agent config files](https://addyosmani.com/blog/good-spec/). Each section controls a different aspect of agent behavior.

| Section | What to Put There |
|---------|-------------------|
| **Commands** | How to run, test, lint, and build the project; one-liners the agent should use verbatim |
| **Testing** | Test framework, how to run a single test, what passing looks like, coverage expectations |
| **Project Structure** | Directory layout, where new files go, naming conventions |
| **Code Style** | Formatting rules, linting tools, style preferences (e.g., "prefer early return over nested if") |
| **Git Workflow** | Branch naming, commit message format, PR conventions, what NOT to commit |
| **Boundaries** | Three-tier permission system (see below); what the agent may never do autonomously |

Source: [Addy Osmani, "How to write a good spec for AI agents"](https://addyosmani.com/blog/good-spec/) (2025)

---

## Three-Tier Boundary System

Explicit permission tiers eliminate ambiguity about when the agent should act vs. ask.

| Tier | Definition | Example Actions |
|------|-----------|-----------------|
| **Always** | Agent may proceed without asking | Edit source files, run tests, create branches, write docs |
| **Ask First** | High-impact actions requiring confirmation | Deploy to staging, modify CI config, delete files, add dependencies |
| **Never** | Hard stops — agent must not proceed regardless of instructions | Run in production, drop databases, push to main, expose credentials |

Place the Never tier prominently in CLAUDE.md. Agents respect explicit prohibitions more reliably than implicit ones.

---

## AndThen Structured Briefing Workflow

The [AndThen plugin](https://github.com/IT-HUSET/andthen) automates the structured brief into a workflow via skills (prefix: `andthen.`):

1. **`andthen.clarify`** — agent asks structured clarifying questions. Your answers become the input to the next step.
2. **`andthen.plan`** — discovers requirements and creates a PRD with implementation plan and story breakdown. Can start from a clarify session, an existing PRD, or from scratch. Detailed specs are created just-in-time per story.
3. **`andthen.spec`** — produces a Feature Implementation Specification (FIS) for a single story or feature: scope, acceptance criteria, architecture decision, implementation tasks, and validation checklist. This is a formalized structured brief — machine-readable and session-persistent.
4. **`andthen.exec-spec`** — implements from the FIS; the spec file replaces the conversation as the source of truth.
5. **`andthen.review-gap`** — compares implementation against the original FIS.

The FIS serves as the written artifact that survives context resets — equivalent to PRP but with a defined format. Choose AndThen when you want the spec to persist across sessions or agents.

For larger work, **`andthen.exec-plan`** executes an entire plan through a pipeline (spec → exec-spec → review-gap per story), so you don't have to run each step manually.

Quick path (no FIS generated): **`andthen.quick-implement`** — useful for simple, self-contained changes.

---

## Persistent Spec Patterns (Spec-Driven Development)

The core principle: **write a persistent spec to a file before implementing.** The spec survives context resets, session boundaries, and agent handoffs. Multiple approaches exist — they are layers, not alternatives.

### How the layers relate

```
  ┌───────────────────────────────────────────────────┐
  │  WISC  Context management                         │
  │  "What enters the window and when?"               │
  │                                                   │
  │  ┌─────────────────────────────────────────────┐  │
  │  │  PIV Loop  Workflow rhythm                  │  │
  │  │  Plan --> Implement --> Validate            │  │
  │  │                                             │  │
  │  │  ┌───────────────────────────────────────┐  │  │
  │  │  │  Spec Artifact (PRP, FIS, SPEC.md)    │  │  │
  │  │  │  "What does the agent need to         │  │  │
  │  │  │   execute this feature?"              │  │  │
  │  │  └───────────────────────────────────────┘  │  │
  │  └─────────────────────────────────────────────┘  │
  └───────────────────────────────────────────────────┘
```

### PRP (Product Requirements Prompt)

Cole Medin's PRP is the most widely adopted **artifact format** for agent-readable implementation specs. The flow: write `INITIAL.md` (feature description + context pointers) → run `/generate-prp INITIAL.md` → agent produces a structured PRP → run `/execute-prp`. The PRP contains: context, implementation blueprints, validation commands, error patterns, and a confidence checklist.

PRP is an artifact format, not a process. It complements (not competes with) the AndThen FIS workflow: FIS is the *elicitation process* that produces a spec; PRP is one structured *format* that spec could follow.

Source: Cole Medin, context-engineering-intro — github.com/coleam00/context-engineering-intro (12.8k stars, updated March 2026)

### Anthropic's SPEC.md Pattern

Anthropic's official equivalent (unnamed): "I want to build [brief description]. Interview me using AskUserQuestion... then write a complete spec to SPEC.md." Structurally identical to PRP but without the named framework. Used in Claude Code best practices documentation.

Source: Anthropic, "Claude Code Best Practices" — code.claude.com/docs/en/best-practices (2026)

### GSD (Get Shit Done)

A full-SDLC spec-driven system (31.5k stars) that installs as slash commands via `npx get-shit-done-cc@latest`. Core innovation: **context rot prevention** — every agent spawns with a fresh 200K context window, keeping the orchestrator lean. Plans execute in dependency-analyzed parallel waves with atomic commits. 15 specialized agents, model profiles (quality/balanced/budget), and a quick path (`/gsd:quick`) for ad-hoc tasks. Targets solo developers wanting maximum automation with minimum ceremony.

Source: GSD — github.com/gsd-build/get-shit-done (31.5k stars, March 2026)

### BMAD Method

A full project-management orchestration system using 12+ specialized agent personas and 34+ workflows. Targets larger-scale work than PRP: multi-epic planning, persona-driven architecture, scale-adaptive planning. Worth knowing exists, but heavier than needed for single-feature work.

Source: BMAD Method — github.com/bmadcode/BMAD-METHOD (41k stars, v6.2.0 March 2026)

---

## Sources

- Addy Osmani, "AI-Assisted Engineering" — osmani.dev (2025)
- Cole Medin, context-engineering-intro — github.com/coleam00/context-engineering-intro (2025-2026)
- Cole Medin, "My COMPLETE Agentic Coding Workflow" — youtube.com/@ColeMedin (Feb 2026)
- Anthropic, "Claude Code Best Practices" — code.claude.com/docs/en/best-practices (2026)
- GSD — github.com/gsd-build/get-shit-done (2025-2026)
- BMAD Method — github.com/bmadcode/BMAD-METHOD (2025-2026)
- Community CLAUDE.md patterns — github.com/anthropics/claude-code (2025-2026)
