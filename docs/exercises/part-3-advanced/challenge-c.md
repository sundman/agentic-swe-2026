# Challenge C: Multi-Agent Sprint

> **Goal**: Design and execute a multi-agent feature implementation, measuring the cost/quality tradeoff.

> **Constraints**:
> - Must decompose the task BEFORE launching agents — the design document comes first, code comes second.
> - Must estimate token cost before starting and compare it to the actual cost afterward.
> - Must design the decomposition to avoid file conflicts — each agent owns specific files.
> - Must reference the Anthropic multi-agent anti-patterns in your design: agents with unclear scope boundaries, agents that assume shared state, agents with no cost limit, agents that modify the same files, and orchestrators without error handling.

> **Success criteria**:
> - Feature works correctly with passing tests.
> - Your cost estimate was within 2× of actual (use `/cost` or session statistics).
> - No file conflicts occurred during execution.
> - You can explain why you chose your specific agent architecture — parallel sub-agents, sequential sub-agents, Agent Teams (multiple agents coordinating on a shared task with defined roles and handoff protocols), or a hybrid — and what the tradeoff was versus running a single agent.

> **Time**: ~90 minutes

> **Recommended model:** `sonnet` at high effort, or `opus` for orchestration design — multi-agent coordination benefits from stronger reasoning (`/model opus`)

---

## The Brief

Choose a medium-complexity feature for the todo app. Suggested: "Tags" — a system where todos can have multiple tags, with the ability to filter the todo list by tag. Or choose your own feature of similar scope: something that touches the data model, the API, and the UI, and could plausibly be decomposed into independently-ownable work. Before you write a single line of code or spawn a single agent, design your orchestration: how many agents, what each one does, which files each agent touches, where dependencies force sequencing, and where true parallelism is possible. Only after you have written that design should you execute.

The Anthropic multi-agent anti-patterns to avoid are: agents with unclear scope boundaries, agents that assume shared state, agents with no cost limit, agents that modify the same files, and orchestrators without error handling. Your design document should address each of these explicitly — either explaining how you avoided the anti-pattern or documenting a conscious tradeoff.

When you are done, you will have a working feature, a design document written before a line was generated, a cost comparison, and a clear account of whether the multi-agent approach was worth it.

> **If using Agent Teams:** Use `/tasks` to manage the shared task list — create tasks, assign to teammates, track progress. Press **Shift+Down** to cycle between teammates in in-process mode, or use split panes (tmux/iTerm2) to see them working simultaneously. Monitor with `/cost` to track token spend across the team.

---

## Deliverables

- Working feature with passing tests, demonstrable in the browser.
- Task decomposition document written BEFORE execution: agent names, responsibilities, files owned, dependencies, estimated token budget per agent. Include your architecture decision rationale — why this architecture (parallel, sequential, Agent Teams, hybrid) vs single-agent.
- Cost comparison: your pre-execution estimate vs. actual (use `/cost` or session statistics).
- Decision log with at least 5 entries: what you asked, what the agent produced, what you retained or rejected, and why. Include a narrative walkthrough of the final feature.

---

## Final Reflection

1. Was the multi-agent approach worth the cost? Anthropic's data puts the quality improvement at 90.2% with a 15× token cost increase. Did you see a quality improvement that justified the cost, or did the overhead eat the gain?
2. At what task size or complexity does multi-agent parallelism start to pay off? Based on what you observed today, where is the breakpoint — and what factors matter most (task independence, file boundaries, time pressure)?
3. What would you change about your decomposition after seeing how it actually executed? Where did your pre-execution design hold up, and where did it break down?
4. Where did sequencing dependencies limit your parallelism more than you expected? What does that suggest about how to scope agent tasks differently next time?
5. What is the most important guardrail to have in place before running autonomous multi-agent tasks on a real codebase?
