> **Principle**: Orchestration is choosing the right isolation level for each task

> **WISC strategy**: ISOLATE — sub-agents keep your main context clean by doing work in a separate context window, returning only a summary

> **You will**:
> - Design a custom sub-agent for a real research problem
> - Run an isolation experiment comparing main session vs sub-agent, measuring the context impact of each
> - Classify real scenarios using IndyDevDan's decision framework to develop orchestration intuition
> - Use a git worktree to experiment with a risky change without touching your main branch

> **Reference cards**: [Delegation Decision Tree](../../reference/delegation-decision-tree.md) · [Context Economics](../../reference/context-economics.md)

> **Recommended model:** `sonnet` at medium effort (`/model sonnet`) — sub-agents can use different models; experiment with `haiku` for simple research agents

---

## The Challenge

Design and deploy a sub-agent that answers a codebase research question of your choosing, then produce a direct comparison: what happens to your main context when you answer the same question in the main session versus via the sub-agent? Your comparison should be concrete — note the context impact, the answer quality, and whether the isolation was worth the overhead.

Alongside the experiment, classify five real orchestration scenarios to develop judgment about when to use each isolation tool. Then use a git worktree to safely explore a change you wouldn't want to commit yet, and decide whether to keep it or discard it.

---

## Suggested Approach

1. Classify the five scenarios below before doing anything else. For each, decide: use `/btw`, spawn a sub-agent, handle in the main session, use a worktree, or run parallel sub-agents? Write down your reasoning — you'll revisit it in reflection.
   - "I need to understand how the HTMX `hx-boost` attribute works"
   - "I want to refactor the database layer while keeping the feature work going"
   - "I need to research 3 different authentication approaches for the API"
   - "I have a quick question about the current branch name"
   - "I want to try a risky refactoring without breaking my current work"

2. Design a custom sub-agent for a codebase research task you care about. The agent lives in `.claude/agents/`.

> **Note:** Create the directory first if it doesn't exist: `mkdir -p .claude/agents`

Decisions you need to make: which tools does it actually need (Read? Grep? Glob? Bash?)? What model makes sense for this task? What `maxTurns` limit is appropriate? Key constraint to keep in mind: sub-agents receive a single comprehensive prompt — they have no conversation history from the main session. Your prompt must be self-contained.

**How to use your sub-agent:** After creating the agent file at `.claude/agents/auth-auditor.md` (or whatever you named it), invoke it from your main Claude Code session by asking: *"Use the agent defined in .claude/agents/auth-auditor.md to answer: [your research question]"*. Claude spawns it as an isolated sub-agent with its own context window and returns only the summary to your main session. The sub-agent cannot see your conversation history — it works from the prompt alone.

3. Run the isolation experiment. Pick a complex codebase question. Run `/context` before posing your research question. Note the token count. Ask the question in the main session. Run `/context` again — the delta is your context cost. Then start a fresh session, send the same question to your sub-agent via the agent file, and run `/context` to see the main-session impact (it should be minimal — just the summary). Compare: how much context did each approach consume? Was the sub-agent's answer sufficient? What was the overhead cost — and was it worth it?

4. Create a git worktree for an experimental change: `git worktree add ../todo-experiment feature/experiment`. Make a change you wouldn't want to commit to your main branch yet — something you want to evaluate first.

> If the branch `feature/experiment` already exists, use: `git worktree add ../todo-experiment-2 -b feature/experiment-2` or choose a different branch name.

Assess: does it work well enough to merge, or should you discard it? When you're done evaluating, clean up the worktree:
```bash
git worktree remove ../todo-experiment
git branch -d feature/experiment
```
Forgetting this step leaves dangling worktrees that can cause confusion later.

> **💡 Plugin tip: feature-dev** — The `feature-dev` plugin (`/plugin install feature-dev@claude-plugins-official`) is a real-world example of multi-agent orchestration. It launches parallel `code-explorer` agents, then feeds their findings into a `code-architect` agent, then runs a `code-reviewer`. Study its structure in `.claude/plugins/feature-dev/` to see how production-grade agent orchestration is designed.

---

## Reflection

1. How much context did the sub-agent save versus the main session approach? In what situations would the saving matter — and in what situations would it not be worth the overhead?

2. For the five scenarios above, was any classification surprising? Are there cases where two approaches are both valid? What criterion would you use to choose between them?

3. IndyDevDan's hierarchy ranks context efficiency as: Skills > CLI/Scripts > MCP. When would you deliberately choose a less efficient option, and why?

---

## Stretch

- Run three parallel sub-agents researching different parts of the todo-app architecture simultaneously. Compare the total token cost against doing the same research sequentially. How does the quality of the combined output compare? Reference point: multi-agent approaches have been measured at 90.2% quality improvement relative to single-agent, but at roughly 15x the token cost. Does your experiment match that pattern?

- Design a "scout" pattern: a lightweight sub-agent that explores a problem space before the main session commits to an approach. What does the scout need to report back for the main session to make a good decision? Try it on a real decision in the todo-app.
