# Context Economics Quick Reference

Token costs, compliance metrics, and context thresholds for informed decisions about AI-assisted development.

**Last updated:** March 2026. Prices change frequently — verify at each provider's pricing page before budgeting.

---

## Token Costs by Model (March 2026)

### Anthropic (Claude)

| Model | Input $/MTok | Output $/MTok | Context Window | Best For |
|-------|-------------|--------------|----------------|----------|
| **Opus 4.6** | $5 | $25 | 1M tokens | Complex reasoning, architecture, multi-file changes |
| **Sonnet 4.6** | $3 | $15 | 1M tokens | Most coding tasks; best cost/quality balance |
| **Haiku 4.5** | $1 | $5 | 200k tokens | Simple edits, classification, quick completions |

Batch API: 50% discount on all tokens. Prompt caching: 0.1x input on cache hits.

Source: platform.claude.com/docs/en/about-claude/pricing (accessed 2026-03-17)

### OpenAI

| Model | Input $/MTok | Output $/MTok | Context Window | Best For |
|-------|-------------|--------------|----------------|----------|
| **GPT-5.4** | $2.50 | $15 | 1.05M tokens | Flagship; agentic, coding, professional workflows |
| **GPT-5.4 Pro** | $30 | $180 | 1.05M tokens | Premium deep-reasoning tier |
| **GPT-5.2** | $0.875 | $7 | 400k tokens | Mid-tier; good cost/quality balance |
| **GPT-5-mini** | $0.125 | $1 | 400k tokens | Budget with large context |
| **GPT-5 Nano** | $0.05 | $0.40 | 400k tokens | Ultra-cheap for high-volume |
| **GPT-4.1** | $2 | $8 | 1M tokens | Great value with 1M context |
| **GPT-4.1 Mini** | $0.20 | $0.80 | 1M tokens | Budget 1M context |
| **o3** | $2 | $8 | 200k tokens | Reasoning model |
| **o4-mini** | $1.10 | $4.40 | 200k tokens | Budget reasoning |

Long context surcharge: GPT-5.4 input doubles to $5/MTok beyond 272k tokens.

Source: developers.openai.com/api/docs/pricing, pricepertoken.com (accessed 2026-03-17)

### Google (Gemini)

| Model | Input $/MTok | Output $/MTok | Context Window | Notes |
|-------|-------------|--------------|----------------|-------|
| **Gemini 2.5 Pro** | $1.25 | $10 | 1M tokens | Best value for large context |
| **Gemini 2.5 Flash** | $0.30 | $2.50 | — | Budget option |
| **Gemini 3.1 Pro Preview** | $2 | $12 | — | Newest; preview pricing |

Long context surcharge: >200k tokens = 2x input pricing for most models.

Source: ai.google.dev/gemini-api/docs/pricing (accessed 2026-03-17)

### DeepSeek

| Model | Input $/MTok | Output $/MTok | Context Window | Notes |
|-------|-------------|--------------|----------------|-------|
| **DeepSeek V3.2** | $0.28 | $0.42 | 128k tokens | Chat and reasoning; 90% discount on cache hits |
| **DeepSeek R1** (via OpenRouter) | $0.70 | $2.50 | 64k tokens | Third-party premium over direct API |

Source: api-docs.deepseek.com/quick_start/pricing (accessed 2026-03-17)

### Quick Comparison (coding-tier models)

**Flagship tier** (best quality):

| Provider | Model | Input $/MTok | Output $/MTok | Context |
|----------|-------|-------------|--------------|---------|
| Anthropic | Opus 4.6 | $5 | $25 | 1M |
| OpenAI | GPT-5.4 | $2.50 | $15 | 1.05M |
| Anthropic | Sonnet 4.6 | $3 | $15 | 1M |
| Google | Gemini 2.5 Pro | $1.25 | $10 | 1M |

**Budget tier** (best value):

| Provider | Model | Input $/MTok | Output $/MTok | Context |
|----------|-------|-------------|--------------|---------|
| OpenAI | GPT-5-mini | $0.125 | $1 | 400k |
| Anthropic | Haiku 4.5 | $1 | $5 | 200k |
| Google | Gemini 2.5 Flash | $0.30 | $2.50 | — |
| DeepSeek | V3.2 | $0.28 | $0.42 | 128k |
| OpenAI | GPT-5 Nano | $0.05 | $0.40 | 400k |

---

## Typical Session Costs

A typical agentic coding session (10-20 tool calls, ~50k tokens total):

| Model tier | Approx. cost per session |
|-----------|------------------------|
| Nano/budget (GPT-5 Nano, DeepSeek V3.2, Gemini Flash) | < $0.02 |
| Mid-tier (Haiku 4.5, GPT-5-mini, Gemini 2.5 Pro) | $0.05-$0.25 |
| Coding-tier (Sonnet 4.6, GPT-5.4, GPT-4.1) | $0.15-$0.75 |
| Premium (Opus 4.6, GPT-5.4 Pro) | $0.50-$2.00 |
| Multi-agent (3 agents, coding-tier) | $0.50-$3.00 |

---

## Context Utilization Thresholds

Quality degrades based on **absolute token volume**, not percentage of window capacity. The thresholds below apply regardless of whether your model has a 200K or 1M context window — the degradation is driven by attention dilution and positional effects, not by how full the window is.

| Token Usage | Observed Behavior | Action |
|-------------|-------------------|--------|
| < ~50K | Normal operation | Continue |
| ~100K | Precision begins to drop; agent starts missing instructions | Consider `/compact` |
| ~150K+ | Hallucination rate increases; behavior becomes erratic | Use `/compact` with specific focus, or start a new session (write HANDOFF.md first) |

![The 1M Context Window — showing system prompts, MCP tools, memory files, and messages filling the window from left to right, with Optimal, Caution, and Danger zones](../../assets/context-window-diagram.png)

The lower end of each range applies to smaller context windows; larger windows with better positional encoding may tolerate slightly more. But a 1M window at 200K tokens used will perform worse than a fresh session — more context is not always better context.

Source: Practitioner guidance informed by the "Lost in the Middle" paper (Liu et al., 2023), which established that LLM accuracy degrades when relevant information is buried in long contexts, regardless of total window size.

---

## Instruction File Design — What the Research Shows

How instruction file design affects agent behavior:

**Instruction count degrades compliance.** [Jaroslawicz et al. (2025)](https://arxiv.org/abs/2507.11538) measured 20 LLMs on the IFScale benchmark (500 instructions). Claude Sonnet dropped from ~100% compliance at 10 instructions to ~53% at 500. The relationship is roughly linear for Claude models — more instructions means lower compliance per instruction.

**Context files can hurt if poorly written.** [ETH Zurich (2026)](https://arxiv.org/html/2602.11988v1) tested context files (AGENTS.md) across 300 SWE-bench Lite tasks. LLM-generated context files *reduced* performance by ~2% and increased cost 20%. Human-written files improved performance by ~4%. Quality matters more than quantity.

**Practical guidance** (broad community experience, not rigorous measurement):

| Design choice | Effect |
|---|---|
| Fewer, focused rules (< ~15) | Higher compliance per rule |
| Imperative phrasing ("Do X", "Never Y") | Stronger adherence than descriptive ("X is preferred") |
| Shorter files (< ~200 lines) | Better than long files — consistent with Jaroslawicz instruction-count findings |
| Multiple focused files | Better than one monolithic file — allows selective loading |

Key takeaway: **Short + imperative + selective loading = best results.** Anthropic's own documentation treats CLAUDE.md as context, not enforcement — there are no compliance guarantees.

Sources:
- Jaroslawicz et al., ["How Many Instructions Can LLMs Follow at Once?"](https://arxiv.org/abs/2507.11538) — arXiv (July 2025)
- ETH Zurich, ["Evaluating AGENTS.md"](https://arxiv.org/html/2602.11988v1) — arXiv 2602.11988 (February 2026)
- Practitioner observations from Claude Code community (2025-2026)

---

## Multi-Agent Cost vs. Quality

| Metric | Single Agent | Multi-Agent | Delta |
|--------|-------------|-------------|-------|
| Output quality score | baseline | +90.2% | Significant improvement |
| Token consumption | 1x | ~15x | Substantial cost increase |

ROI is positive for complex, parallelizable tasks. ROI is negative for simple tasks where coordination overhead dominates. At March 2026 mid-tier pricing (~$3/$15 per MTok), a 3-agent session on a medium feature costs roughly $2-5 total.

Source: Anthropic multi-agent research benchmarks (2025)

---

## When Human Work Is Cheaper

A rough decision heuristic (recalibrated for March 2026 pricing):

- **Task takes a human < 2 minutes**: at current pricing, even the cheapest agent call may not save time (context loading + verification overhead)
- **Task is repetitive across many files**: multi-agent ROI improves sharply; automation wins decisively
- **Task requires judgment calls every step**: human-in-the-loop beats full automation
- **Task output is hard to verify**: add verification cost to the total
- **DeepSeek/Haiku tier**: at < $0.05 per session, the cost barrier has effectively disappeared — the question is quality, not price

Rule of thumb: if you can't describe the success criteria in one sentence, the briefing cost may exceed the token cost.

---

## Sources

- Anthropic pricing — platform.claude.com/docs/en/about-claude/pricing (accessed 2026-03-17)
- OpenAI pricing (via OpenRouter) — openrouter.ai/openai (accessed 2026-03-17)
- Google Gemini pricing — ai.google.dev/gemini-api/docs/pricing (accessed 2026-03-17)
- DeepSeek pricing — api-docs.deepseek.com/quick_start/pricing (accessed 2026-03-17)
- Anthropic, context window guidance — engineering blog (2025)
- Jaroslawicz et al., "How Many Instructions Can LLMs Follow at Once?" — arXiv (July 2025)
- ETH Zurich, "Evaluating AGENTS.md" — arXiv 2602.11988 (February 2026)
- Anthropic, multi-agent quality benchmarks — engineering blog (2025)
- Nelson et al., "Lost in the Middle" — Transactions of ACL (2023)
