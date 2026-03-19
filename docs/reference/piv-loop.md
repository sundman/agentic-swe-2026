# The PIV Loop

Plan -> Implement -> Validate — the fundamental agentic engineering workflow.

---

## The PIV Loop

```
    ┌──────────┐      ┌─────────────┐      ┌────────────┐
    │          │      │             │      │            │
    │   PLAN   │─────▶│  IMPLEMENT  │─────▶│  VALIDATE  │
    │  (Human) │      │   (Agent)   │      │  (Human)   │
    │          │      │             │      │            │
    └──────────┘      └─────────────┘      └─────┬──────┘
         ▲                                       │
         │            iterate if needed          │
         └───────────────────────────────────────┘
```

**Plan**: Define the outcome before writing a line of code. Write specs, acceptance criteria, and constraints to a file — not just in conversation. Identify ambiguities and resolve them with the agent before implementation begins. Output: a written spec or task list the agent will execute from.

**Implement**: Agent executes from the written plan. Human stays out of the loop (HOTL or HOOTL depending on risk). The agent reads context from files, not from memory of the conversation. Long or complex implementation may use sub-agents for parallel subtasks.

**Validate**: Human verifies output against the original success criteria — not just "does it look right?" Run the tests. Check edge cases. Confirm the spec was followed. If validation fails, the next Plan phase incorporates what was learned; the loop does not restart from scratch.

---

## The Sandwich Principle

> "Humans own planning (P) and validation (V). Agents own implementation (I)."
>
> — Cole Medin

The sandwich pattern prevents the most common failure modes: agents that plan poorly (scope creep, wrong assumptions) and agents that validate their own work (test sabotage, plausible-but-wrong).

---

## Boris Tane's Workflow

Boris Tane (Anthropic engineer) described his personal workflow in three phases:

| Phase | Description | Key Practice |
|-------|-------------|--------------|
| **Research** | Agent explores the codebase, reads relevant files, maps dependencies | Uses sub-agents; exploration noise stays isolated |
| **Planning** | Annotation cycle — agent produces a plan, human annotates and refines, repeat | 1-6 rounds; plan is written to a file before execution begins |
| **Implementation** | Agent executes from the annotated plan | Fresh context loaded from the plan file, not from conversation history |

Source: Boris Tane, Anthropic engineering team (2025)

---

## System Evolution Mindset

When an agent fails, the instinct is to fix that instance. The better response is to ask: what system change would prevent this class of failure?

- Agent ignored a constraint -> add it to CLAUDE.md or a rules file
- Agent forgot context -> add a hook to reinject it
- Agent produced low-quality output -> write a skill with a better prompt
- Agent ran too long -> add a checkpoint or compaction instruction

Each failure is a signal that the system (CLAUDE.md, commands, skills, hooks) needs updating — not just that the prompt needed to be better.

Source: Cole Medin, "Building Durable Agentic Systems" (2025)

---

## AndThen: The PIV Loop as a Plugin

The [AndThen plugin](https://github.com/andthen/andthen) makes the PIV loop executable as Claude Code skills (prefix: `andthen.`). Each phase maps directly:

| PIV Phase | AndThen Skill | What It Does |
|-----------|---------------|--------------|
| **Plan** | `andthen.clarify` | Asks structured clarifying questions, surfaces ambiguities |
| **Plan** | `andthen.spec` | Produces a Feature Implementation Specification (FIS) — the written plan |
| **Implement** | `andthen.exec-spec` | Implements from the FIS with validation loops |
| **Validate** | `andthen.review-gap` | Compares implementation against the original spec |

For smaller tasks: `andthen.quick-implement` compresses Plan+Implement into a single step (skip when spec persistence matters).

For orchestrated multi-story work: `andthen.exec-plan` runs an entire implementation plan through the full pipeline.

Install: `/plugin install andthen`, then `andthen.init`

---

## Connection to WISC

The PIV loop and the WISC framework address the same problems from different angles:

| PIV Phase | WISC Support |
|-----------|-------------|
| **Plan** | WRITE — specs and handoffs persist the plan across sessions |
| **Implement** | ISOLATE — sub-agents keep exploration noise out of the main context |
| **Validate** | SELECT + COMPRESS — focused context and clean sessions produce reliable output to verify against |

---

## Sources

- Cole Medin, "Claude Code Best Practices" — youtube.com/@ColeMedin (2025)
- Boris Tane, Anthropic engineering workflow — shared at Anthropic developer event (2025)
- Anthropic, "Agentic AI Patterns" — docs.anthropic.com (2025)
