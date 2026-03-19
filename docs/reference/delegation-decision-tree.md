# Delegation Decision Tree

Frameworks for deciding what to delegate to Claude Code and how.

---

## HITL / HOTL / HOOTL Framework

Match autonomy level to task risk and reversibility.

| Level | Name | Definition | When Appropriate | Example Tasks |
|-------|------|-----------|-----------------|---------------|
| **HITL** | Human In The Loop | Human approves every action before execution | Unfamiliar codebase; irreversible operations; high-stakes changes | Schema migrations, production deploys, security changes |
| **HOTL** | Human On The Loop | Agent acts autonomously; human monitors and can intervene | Routine feature work in known codebase; tests catch regressions | Feature implementation, refactoring, test writing |
| **HOOTL** | Human Out Of The Loop | Agent runs to completion without human review | Well-specified, reversible, fully tested tasks | Dependency updates, linting fixes, doc generation |

Source: Agentic SWE community taxonomy; used in Anthropic documentation (2025)

---

## IndyDevDan's Mechanism Selection

| Mechanism | Load Method | Best For | Context Efficiency |
|-----------|-------------|---------|-------------------|
| **Skills** | Agent loads automatically | Repeatable autonomous behaviors (spec, review, plan) | Highest — loaded on demand |
| **Commands** | Human triggers with /slash | Manual one-off tasks; human-initiated workflows | High — only when invoked |
| **Subagents** | Spawned by orchestrator | Parallelizable, isolated work; independent subtasks | High — separate context window |
| **MCP servers** | Configured in .mcp.json | Multi-client tool integrations (GitHub, Jira, databases) | Medium — persistent connection overhead |
| **CLI scripts** | Called as tools | Automation that wraps external systems | Medium |

Context efficiency hierarchy: **Skills > CLI/Scripts > MCP**

Source: IndyDevDan, "Claude Code: The Full Guide" (2025), youtube.com/@IndyDevDan

---

## AndThen Plugin Skills

AndThen adds structured-workflow skills to Claude Code (prefix: `andthen.`). Skills are auto-invoked by the agent or triggered by name — they orchestrate sub-agents, tool calls, and validation loops internally.

| Skill | When to Use |
|-------|-------------|
| `andthen.clarify` | Starting a non-trivial feature — surfaces ambiguities before committing to a spec |
| `andthen.spec` | Writing a persistent Feature Implementation Specification (FIS) |
| `andthen.exec-spec` | Implementing from a written FIS with automated validation loops |
| `andthen.review-gap` | Checking that implementation matches the original spec |
| `andthen.quick-implement` | Small tasks where spec overhead isn't justified |
| `andthen.exec-plan` | Multi-story implementation plans — full pipeline per story |
| `andthen.review-code` | Structured code review (quality, security, architecture) |
| `andthen.e2e-test` | Browser-based end-to-end validation |

Install: `/plugin install andthen` → `andthen.init`

---

## [Böckeler's "Who Loads Context" Taxonomy](https://martinfowler.com/articles/exploring-gen-ai/context-engineering-coding-agents.html)

| Loader | Mechanism | Claude Code Feature | Example |
|--------|-----------|-------------------|---------|
| **LLM** | Agent decides when to use | Skills (`.claude/skills/`) | Agent invokes `/spec` when it detects a feature request |
| **Human** | Person triggers manually | Commands (`/slash-commands`) | Developer runs `/review-code` before a PR |
| **Agent Software** | System injects automatically | Hooks (`.claude/hooks/`) | `reinject-context.sh` runs after every compaction event |

Source: [Birgitta Böckeler, "Context Engineering for Coding Agents"](https://martinfowler.com/articles/exploring-gen-ai/context-engineering-coding-agents.html) — on martinfowler.com (2026)

---

## The Orchestration Decision Tree

```
    Needs external tools or data?
    │
    ├── NO ── Single-turn question?
    │         ├── YES ─▶ Inline prompt
    │         └── NO ──▶ Conversation thread
    │
    └── YES ── Modifies code or files?
              │
              ├── NO ───▶ Tool call (read-only)
              │           search, fetch, query
              │
              └── YES ── Can run independently of main context?
                         │
                         ├── YES ─▶ Sub-agent
                         │          Isolated context window.
                         │          Use for: research, parallel work,
                         │          exploration that would pollute context.
                         │
                         └── NO ──▶ Inline with tool use
                                    Needs full conversation history.
```

Rule of thumb: if you'd open a new terminal tab for it, use a sub-agent.

When in doubt: if you'd open a new terminal tab for it, use a sub-agent.

---

## Sources

- IndyDevDan, "Claude Code: The Full Guide" — youtube.com/@IndyDevDan (2025)
- [Birgitta Böckeler, "Context Engineering for Coding Agents"](https://martinfowler.com/articles/exploring-gen-ai/context-engineering-coding-agents.html) — martinfowler.com (2026)
- Anthropic, "Building Effective Agents" — docs.anthropic.com (2025)
- Community orchestration patterns — gathered from Claude Code Discord (2025-2026)
