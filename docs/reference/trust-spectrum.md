# The Trust Spectrum

From vibe coding to agentic engineering — where you are and where to go.

---

## The Spectrum

| Level | Name | Characteristics | Key Risk |
|-------|------|----------------|---------|
| 1 | **Vibe coding** | Describe what you want; accept whatever the agent produces; no review | Accumulating code you cannot explain or maintain |
| 2 | **Prompt engineering** | Craft prompts carefully; iterate on wording; still output-focused | Optimizing for generation quality rather than correctness |
| 3 | **Context engineering** | Design what the agent sees (CLAUDE.md, rules, specs); verify output against criteria | Context debt — rules that contradict or instructions that age poorly |
| 4 | **Intent engineering** | Express intent precisely; agent translates to executable plan; human validates plan before implementation | Plan-implementation drift when specs are not machine-readable |
| 5 | **Agentic engineering** | Compose agents, tools, and systems; own the architecture the agent operates within | Orchestration failures; runaway autonomy; trust misalignment |

Source: Community synthesis; Karpathy "vibe coding" coinage (Feb 2025); Jan 2026 follow-up "agentic engineering"

---

## The METR Paradox (and its correction)

**Original finding (July 2025):**

| Metric | Value |
|--------|-------|
| Productivity change (experienced developers with AI tools) | -19% |
| Perceived productivity change (same developers) | +20% |
| Perception gap | ~39 percentage points |

**February 2026 update:** METR is revising the methodology. 30-50% of developers avoided submitting tasks where AI would help most (selection bias). With correction, the new directional estimate: **AI likely speeds developers up by ~18%**, but with wide confidence intervals.

Both data points are valuable for teaching: the original finding illustrates the perception gap; the correction illustrates that **workflow adaptation** — not just tool adoption — determines outcomes. This workshop exists to accelerate that adaptation.

Source: METR, metr.org/blog/2025-07-10 (original) and metr.org/blog/2026-02-24-uplift-update/ (correction)

---

## Trust Gap Data (Stack Overflow 2025)

| Metric | Value |
|--------|-------|
| AI tool adoption | 80% |
| Trust in AI accuracy | 29% (down from 40% year-over-year) |
| Developers who review AI changes before merging | < 50% |
| Time spent fixing near-correct AI output | 66% report increased time |

The gap between adoption (80%) and trust (29%) is the defining tension. Adoption is saturated; quality is the frontier problem. Two-thirds of developers report spending *more* time fixing near-correct AI output than they save.

Source: Stack Overflow Developer Survey 2025, published Dec 29, 2025

---

## The Three-Attempt Framework

Set this expectation before starting any non-trivial task:

| Attempt | Expected Quality | Purpose |
|---------|-----------------|---------|
| **First** | ~5% usable | AI builds context; surfaces hidden constraints and real complexity |
| **Second** | ~50% usable | Nuances absorbed; half still unusable but direction is clear |
| **Third** | Working starting point | Incorporate learnings from attempts 1-2 into a focused brief |

Iteration is not a failure — it is the mechanism. Better briefs compress three attempts toward one.

Source: Vincent Quigley, Staff Engineer at Sanity (2025)

---

## Key Quotes

Andrej Karpathy (Feb 2025, coining "vibe coding"):
> "I just see stuff, say stuff, run stuff, and it mostly works."

Karpathy (Jan 2026, on the transition):
> "Vibe coding is fine for throwaway scripts. For anything in production, you need agentic engineering — you need to own what the agent is doing."

Simon Willison (on the review obligation):
> "I won't commit any code I couldn't explain to a colleague."

---

## Sources

- METR, "Impact of AI Coding Tools on Developer Productivity" — metr.org (Jul 2025; Feb 2026 follow-up)
- Stack Overflow Developer Survey 2025 — stackoverflow.com/survey
- Andrej Karpathy, X/Twitter (Feb 2025; Jan 2026)
- Simon Willison, "Agentic Engineering Patterns" — simonwillison.net (2025-2026)
- Vincent Quigley, Sanity engineering blog (2025)
