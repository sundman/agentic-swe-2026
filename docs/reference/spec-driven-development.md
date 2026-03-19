# Spec-Driven Development (SDD)

Write a spec before implementing. The agent executes from the spec, not from conversation. The spec survives context resets, session boundaries, and agent handoffs.

---

## The Core Principle

SDD is the practice of writing a detailed specification *before* letting an agent write code. The spec becomes the source of truth — not the conversation, not the developer's memory. Every SDD tool implements the same loop:

```
  ┌───────────┐     ┌───────────┐     ┌───────────┐     ┌───────────┐
  │   ELICIT  │────▶│   WRITE   │────▶│ IMPLEMENT │────▶│ VALIDATE  │
  │           │     │  spec to  │     │ from spec │     │  against  │
  │  require- │     │   file    │     │  (agent)  │     │   spec    │
  │   ments   │     │           │     │           │     │           │
  └───────────┘     └───────────┘     └───────────┘     └───────────┘
      human             human             agent             human
```

Thoughtworks calls SDD "one of 2025's key new AI-assisted engineering practices." The overhead varies by tool (from ~250 lines per change to full multi-epic planning). The question is always: **is the spec overhead worth it for THIS task?**

---

## SDD Tools Landscape (March 2026)

| Tool | Origin | Scope | Overhead | Best For |
|------|--------|-------|----------|----------|
| **Claude Code Plan Mode** | Anthropic (built-in) | Lightweight | Minimal | Any task; always available |
| **AndThen FIS** | AndThen plugin | Single feature | ~1 page FIS | Feature work with validation |
| **GSD** | TÂCHES (open source) | Full SDLC | Medium (15 agents, automated) | Solo devs wanting max automation |
| **OpenSpec** | Fission-AI (YC-backed) | Change-scoped | ~250 lines/change | Brownfield codebases |
| **GitHub Spec Kit** | GitHub | Feature-scoped | ~800 lines/feature | Agent-agnostic teams |
| **BMAD Method** | Community | Full SDLC | Large (19 personas, 34+ workflows) | Enterprise/team scale |
| **Kiro** | Amazon | Full SDLC | IDE-integrated | Spec-driven IDE workflow |
| **feature-dev plugin** | claude-plugins-official | Single feature | ~1 page (7-phase guided) | Medium-complexity features |
| **PRP** | Cole Medin (open source) | Single feature | ~1 page PRP | Implementation blueprints |

---

## When SDD Overhead Is Worth It

| Situation | SDD Worth It? | Why |
|-----------|--------------|-----|
| One-sentence change ("fix the typo") | No | Briefing cost exceeds implementation |
| Exploratory spike | No | You don't know the spec yet |
| Multi-file feature (3+ files) | Yes | Spec prevents drift across files |
| Autonomous run >35 minutes | Yes | Agent needs a persistent reference |
| Ambiguous requirements | Yes | Spec elicitation surfaces unknowns |
| Team review needed | Yes | Spec is the reviewable artifact |
| Multi-session work | Yes | Spec survives context resets |

---

## How They Compare

### Claude Code Plan Mode (built-in, zero overhead)

Shift+Tab → agent explores, produces a plan, you review, then implement in fresh context. The lightest SDD approach — always available, no plugins needed.

Anthropic's recommended pattern: "I want to build [feature]. Interview me using AskUserQuestion... then write a complete spec to SPEC.md."

### AndThen (plugin, single-feature SDD)

Skills (prefix `andthen.`): `andthen.clarify` → `andthen.spec` → `andthen.exec-spec` → `andthen.review-gap`. Produces a Feature Implementation Specification (FIS). The FIS is the process's primary written artifact — equivalent to a PRP but with automated elicitation and gap review.

### PRP (open source, artifact format)

Cole Medin's Product Requirements Prompt: write `INITIAL.md` → `/generate-prp` → `/execute-prp`. The PRP contains: context, implementation blueprints, validation commands, error patterns, confidence checklist. PRP is an *artifact format* (what the spec contains); FIS/Spec Kit are *processes* (how to arrive at a spec). They're complementary.

Source: github.com/coleam00/context-engineering-intro (12.8k stars, updated March 2026)

### GitHub Spec Kit (agent-agnostic CLI)

Released September 2025 by GitHub. Works with Claude Code, Copilot, Gemini CLI, Cursor, Windsurf. Workflow: write a `constitution.md` → `/specify` → `/plan` → `/tasks` → `/implement`. Heavier than FIS/PRP (~800 lines per feature) but designed for team environments where multiple people review specs.

Source: github.blog (Sept 2, 2025)

### GSD — Get Shit Done (solo dev, full automation)

The fastest-growing SDD framework (31.5k stars, launched Dec 2025). Installs as slash commands via `npx get-shit-done-cc@latest`. Six-step loop: new-project → discuss → plan → execute → verify → complete. Quick path: `/gsd:quick` for ad-hoc tasks.

GSD's core architectural insight: **context rot** — quality degrades as the context window fills. Every executor, planner, and checker spawns as a sub-agent with a **fresh 200K context**, so the orchestrator never accumulates heavy state. Plans are dependency-analyzed into **parallel waves** — independent tasks execute concurrently.

15 specialized agents, XML-structured plans, atomic commits per task, model profiles (quality/balanced/budget). Explicitly anti-enterprise-ceremony: targets solo developers who want automation without sprint rituals.

Notable features: Nyquist auditor (test coverage validation), persistent debug knowledge base, multi-runtime support (6 runtimes), UI design pipeline.

Source: github.com/gsd-build/get-shit-done (31.5k stars, March 2026)

### OpenSpec (brownfield-focused)

YC-backed, released January 2026. Designed for existing codebases. Change-scoped (~250 lines per change vs Spec Kit's 800). Connected to the intent-driven.dev community.

Source: ycombinator.com/launches/Pdc-openspec

### BMAD Method (enterprise scale)

"Breakthrough Method for Agile AI-Driven Development." 19 specialized agent personas, 34+ workflows, full SDLC orchestration. Key innovation: "sharding" — atomic story files reduce token consumption ~90%. Much larger scope than single-feature SDD; closer to a full project management system.

Source: github.com/bmad-code-org/BMAD-METHOD (41k stars, v6.2.0 March 2026)

---

## The SDD Critique

[Birgitta Böckeler](https://martinfowler.com/articles/exploring-gen-ai/sdd-3-tools.html) (Martin Fowler's blog, October 2025) provides the sharpest critique:

- **Problem-size mismatch**: SDD works best for medium tasks; too heavy for small, too rigid for truly complex
- **Specification decay**: specs become stale during implementation — the agent follows the original even when the terrain changes
- **False sense of control**: a detailed spec doesn't guarantee a good outcome
- **Historical parallel**: Model-Driven Development (MDD) failed for similar reasons — the specification becomes its own maintenance burden

The counter-argument: SDD overhead is falling as tools improve. The key is matching tool weight to task size.

---

## Sources

- Thoughtworks, "Spec-Driven Development" — thoughtworks.com (Dec 5, 2025)
- [Birgitta Böckeler, "SDD Tools"](https://martinfowler.com/articles/exploring-gen-ai/sdd-3-tools.html) — martinfowler.com (Oct 15, 2025)
- GitHub, "Spec Kit launch" — github.blog (Sept 2, 2025)
- Cole Medin, context-engineering-intro — github.com/coleam00/context-engineering-intro (2025-2026)
- OpenSpec — ycombinator.com/launches/Pdc-openspec (Jan 2026)
- GSD — github.com/gsd-build/get-shit-done (2025-2026)
- BMAD Method — github.com/bmad-code-org/BMAD-METHOD (2025-2026)
- Anthropic, "Claude Code Best Practices" — code.claude.com (2026)
