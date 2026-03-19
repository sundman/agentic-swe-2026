> **Principle**: Verification is a design problem, not an afterthought

> **WISC strategy**: All strategies — guardrails protect every context engineering approach. Write: rules and hooks must be written down to take effect. Isolate: permissions scope what agents can touch. Select: settings control which tools and context are active. Compress: hooks prevent runaway cost accumulation.

> **You will**:
> - Analyze real production failures to extract prevention principles
> - Design permission rules for a realistic team scenario
> - Build an automated guardrail using Claude's hook system
> - Calibrate task autonomy levels using the HITL/HOTL/HOOTL framework

> **Reference cards**: [Named Failure Patterns](../../reference/failure-patterns.md) · [Delegation Decision Tree](../../reference/delegation-decision-tree.md)

> **Time**: ~50 minutes

> **Recommended model:** `sonnet` at medium effort (`/model sonnet`)

---

## The Challenge

Two real production incidents caused measurable harm that could have been prevented with controls Claude Code already supports. Your challenge: identify what guardrails would have prevented each incident, design permission rules for your own team scenario, implement one as an automated hook, and classify 5 tasks by appropriate autonomy level. By the end of this lab you should have a working hook that blocks at least one dangerous operation, a `.claude/settings.json` you could plausibly commit to a real project, and a clear framework for deciding when to keep humans in, on, or out of the loop.

---

## Suggested Approach

1. Production failure autopsy. For each incident below, identify what permissions were missing or too permissive, what hook could have prevented it, and which WISC failure was the root cause. Write your analysis before moving on — the pattern recognition matters more than the implementation.

   **Replit incident**: During database maintenance, a Claude agent running with broad bash permissions executed `DROP TABLE` on a production database. A code freeze notice existed in the repository but was not in the agent's active context window at the time.

   **GetOnStack incident**: A multi-agent setup allowed agents to spawn help requests to other agents without a depth limit. Two agents entered a recursive help-request loop that ran continuously for several hours, accumulating $47,000 in API costs before a billing alert triggered a manual shutdown.

   For each incident, answer:
   - What permissions were missing or too permissive?
   - What hook could have intercepted the dangerous operation?
   - Which WISC failure occurred (Write / Isolate / Select / Compress)?

2. Design permission rules for this scenario: "Your team of 5 engineers deploys to production from this repo. A new developer joins tomorrow. What should Claude be allowed to do Always / Ask First / Never?" Create your own `.claude/settings.json` with these rules. Use the Osmani three-tier system (Always / Ask First / Never) as your framework. Do not copy-paste from examples — the thinking is the point.

After writing your rules, run `/permissions` to see all active permission rules and which settings file each comes from. This shows how user, project, and local settings merge — and whether your new rules are actually in effect.

> **Implementation note:** Claude Code's `permissions` system is binary: `allow` and `deny`. There is no explicit "Ask First" key. The "Ask First" tier is implemented by *omitting* an action from both lists — Claude will prompt you interactively for anything not explicitly allowed or denied. So: "Always" = add to `allow`, "Never" = add to `deny`, "Ask First" = leave it off both lists.

> **Critical gotcha: Deny rules have a blind spot.** Claude Code's `deny Read(".env")` rule only blocks Claude's built-in Read tool — it does NOT prevent `cat .env` via the Bash tool. The same applies to all Read/Edit deny rules: they follow gitignore-style patterns but only apply to Claude's native file tools, not to shell commands. To truly protect a file, you need BOTH a Read/Edit deny rule AND a Bash deny rule (e.g., `deny Bash("cat .env*")`), or use **sandboxing** (see below) which enforces restrictions at the OS level for all processes.

3. Write a `PreToolUse` hook that blocks at least one dangerous operation. Use the exit code pattern: exit 0 = allow, exit 2 = block (stderr feeds back to Claude as correction guidance). Non-zero codes other than 2 are treated as non-blocking errors and may be ignored — so always use exit 2 when you want to actually stop a dangerous operation. Candidates: block `rm -rf`, DROP TABLE/DATABASE statements in bash commands, or force-push commands.

**Important: Hooks require two steps.**

1. **Write the hook script** (e.g., `.claude/hooks/guardrails.sh`) and make it executable (`chmod +x`).
2. **Register the hook in `.claude/settings.json`** under the `hooks` key. Without this step, the script exists but is never called.

Example registration in `.claude/settings.json`:
```json
{
  "hooks": {
    "PreToolUse": [
      {
        "matcher": "Bash",
        "hooks": [
          {
            "type": "command",
            "command": "bash .claude/hooks/guardrails.sh"
          }
        ]
      }
    ]
  }
}
```

Test by asking Claude to attempt the blocked operation. If the hook doesn't fire, check: Is the script executable? Is it registered in `settings.json`? Does the `matcher` match the tool name?

### Built-in Security Review

Before writing custom hooks, check what Claude Code already provides:

```
/security-review
```

This command analyzes your recent changes for potential security vulnerabilities — SQL injection, XSS, missing input validation, unsafe deserialization, and more. Run it now on the bug fixes from Exercise 2. Did it find anything your manual review missed?

For a verification workflow: `/diff` to see what changed → `/security-review` to check for vulnerabilities → your hook to enforce project-specific rules. Three layers, from general to specific.

4. Classify these 5 tasks by autonomy level — HITL (Human In The Loop), HOTL (Human On The Loop), or HOOTL (Human Out Of The Loop) — and write one sentence justifying each:
   - Rename a local variable
   - Design the database schema for a new feature
   - Write unit tests for an existing function
   - Deploy to production
   - Refactor a function to reduce complexity

---

## Sandboxing (~10 min)

Permissions control what Claude's tools can do. Sandboxing controls what the **operating system** allows — it restricts all processes Claude spawns, not just the built-in tools.

### Why Sandboxing Matters

Traditional permission-based security leads to **approval fatigue** — repeatedly clicking "approve" means you pay less attention to what's approved. Anthropic's data: sandboxing reduces permission prompts by **84%** while maintaining security.

### 5.1 Enable the Sandbox

Run `/sandbox` to see your current sandboxing status.

Enable sandboxing for this project:

```json
// In .claude/settings.json, add:
{
  "sandbox": {
    "enabled": true,
    "autoAllowBashIfSandboxed": true
  }
}
```

With `autoAllowBashIfSandboxed: true`, Claude can run shell commands without asking — because the sandbox restricts what those commands can actually do.

### 5.2 Test the Sandbox

With sandboxing enabled, ask Claude:

```
Try to read /etc/passwd and write a file to /tmp/test.txt
```

The sandbox should block access outside the project directory. On macOS, this uses Apple's Seatbelt; on Linux, it uses bubblewrap.

### 5.3 Configure Filesystem Rules

Customize what the sandbox allows:

```json
{
  "sandbox": {
    "enabled": true,
    "autoAllowBashIfSandboxed": true,
    "filesystem": {
      "allowWrite": ["./"],
      "denyWrite": [".env", ".claude/settings.json"],
      "denyRead": [".env"]
    }
  }
}
```

Now the sandbox enforces file restrictions at the OS level — unlike permission deny rules, this cannot be bypassed by shell commands.

### 5.4 Network Restrictions (Optional)

For production use, also restrict network access:

```json
{
  "sandbox": {
    "network": {
      "allowedDomains": ["api.anthropic.com", "registry.npmjs.org", "pypi.org"]
    }
  }
}
```

This prevents data exfiltration even if a dependency or script is compromised.

### Sandboxing vs Permissions

| Layer | Scope | Enforcement | Bypass risk |
|---|---|---|---|
| **Permissions** | Claude's built-in tools only | Application-level | Bash commands can bypass Read/Edit rules |
| **Sandboxing** | All OS processes | OS-level (Seatbelt/bubblewrap) | Very low — enforced by kernel |

**Defense in depth:** Use both. Permissions for fine-grained Claude tool control. Sandboxing for OS-level enforcement that catches everything else.

> **Reflection:** How does this change your answer to the Replit incident analysis? Would sandboxing alone have prevented the DROP TABLE? (Hint: consider the difference between filesystem and network restrictions.)

---

## Reflection

1. Which is more important for your team — permission rules (pre-emptive) or hook automation (reactive)? Could you have a secure setup without either?

2. The Replit incident was caused by missing context: the freeze notice was not loaded into the agent's active window. The GetOnStack incident was caused by missing structural guardrails: no depth limit in the orchestration logic. What does this suggest about the relationship between context engineering and security? Are they the same problem?

3. For the 5 tasks above, where did you have doubts? What factors push a task from HOTL to HOOTL — and what would need to change about your confidence or the tooling before you'd make that move?

---

## Advanced: Prompt and Agent Hooks (Optional Extension)

If you finish the main lab early, explore these more powerful hook types:

### Prompt Hooks
A prompt hook uses a single-turn LLM call to evaluate a condition — useful when the check requires understanding, not just pattern matching:

```json
{
  "hooks": {
    "PreToolUse": [
      {
        "matcher": "Bash",
        "hooks": [
          {
            "type": "prompt",
            "prompt": "Evaluate if this Bash command could be destructive. The command is: {{tool_input.command}}. Respond with EXIT_CODE=2 if dangerous, EXIT_CODE=0 if safe."
          }
        ]
      }
    ]
  }
}
```

### Agent Hooks
For complex validation requiring multiple steps, use an agent hook — it gets its own tools and multiple turns:

```json
{
  "hooks": {
    "Stop": [
      {
        "hooks": [
          {
            "type": "agent",
            "prompt": "Verify the completed work: check tests pass, no linting errors, changes are focused.",
            "tools": ["Bash", "Read", "Glob", "Grep"]
          }
        ]
      }
    ]
  }
}
```

### SessionStart Hooks
Inject context at the start of every session — useful for reminders that survive context compaction:

```json
{
  "hooks": {
    "SessionStart": [
      {
        "hooks": [
          {
            "type": "command",
            "command": "echo 'Reminder: Always run tests before committing.'"
          }
        ]
      }
    ]
  }
}
```

These three hook types — command (pattern matching), prompt (LLM judgment), and agent (multi-step verification) — give you a full spectrum from simple rules to complex quality gates.

---

## Stretch

- Design permissions for a CI/CD pipeline that runs Claude Code in `dontAsk` mode (fully autonomous). What changes compared to interactive use? What would you absolutely never allow, even in automation?

- Write a post-mortem template for an AI incident — structured to capture what the agent did, what the human oversight missed, which WISC failure was the root cause, and what the prevention rule is going forward.

- Audit the `.claude/settings.json` in the course repo: what is currently allowed, what is currently denied, and what would you change if this were a production team project? Write the diff and explain each change.
