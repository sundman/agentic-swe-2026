> **Principle**: Build tools FOR AI, not just use AI as a tool.

> **WISC strategy**: SELECT — skills use progressive disclosure (metadata → instructions → full scripts), loading only what's needed when it's needed.

> **You will**:
> - Build a utility that Claude can use
> - Experience the composability moment — you built it, AI runs it
> - Encode a repeated workflow as a reusable command
> - Automate a guardrail with a hook you write yourself

> **Reference cards**: [Agentic Patterns](../../reference/agentic-patterns.md) ([Willison's "Hoard Things"](https://simonwillison.net/guides/agentic-engineering-patterns/hoard-things-you-know-how-to-do/)) · [Failure Patterns](../../reference/failure-patterns.md)

> **Timing**: ~60 minutes

> **Recommended model:** `sonnet` at medium effort (`/model sonnet`)

---

## The Challenge

Build something Claude can use — a CLI tool, a validation script, or a data utility for the todo app. Design its interface for AI invocation: clear help text, predictable exit codes, structured output. Then give Claude a feature request that requires your tool to complete. Experience the composability moment: you built it, AI runs it.

Next, identify one workflow you have repeated during this workshop and encode it as a slash command — "Commandify Everything" (Cole Medin). Finally, write a hook that enforces a guardrail using the exit-code pattern: exit 0 allows the operation, exit 2 sends your stderr message back to Claude for self-correction.

---

## Suggested Approach

1. Choose a tool to build. Ideas: a script that checks todo-app database integrity, a CLI that generates test data for the todo app, a validator that checks HTMX attribute usage in templates, or your own idea. The key design constraint: Claude must be able to understand and invoke it from a short description alone. UV single-file scripts are portable if you want a self-contained approach — add `#!/usr/bin/env -S uv run --script` at the top with embedded dependencies.

2. Build the tool, then prompt Claude: "Use the tool at [path] to [accomplish a task]." The composability moment is when Claude reads your tool's output and integrates it into a larger workflow. If Claude can't figure out how to invoke your tool, that is feedback on the interface — not on Claude.

> **Tip:** Claude Code also works as a unix utility. Try: `claude -p "What does this tool do?" --output-format json < your-tool.py`. This headless mode (`-p` flag) lets you integrate Claude into shell scripts and CI pipelines — another form of composability where Claude uses YOUR tools AND your scripts use Claude.

3. "Commandify Everything": identify a workflow you have repeated during this workshop (for example: run tests, show coverage, commit if passing).

> **Note:** Create the directory first if needed: `mkdir -p .claude/commands`

**Stuck on what to commandify?** Here are workflows you've likely repeated during this workshop:
- Run tests, show results, commit if passing
- Check test coverage for a specific file
- Review a file for HTMX best practices
- Create a new route with its template and test file

Create a slash command in `.claude/commands/<name>.md` that encodes it. Test it with `/name` in the Claude Code prompt.

4. Write a hook. Use the exit-code pattern: exit 0 allows the operation, exit 2 returns your stderr message to Claude as a self-correction signal. A PreToolUse hook that validates something before a tool runs, or a PostToolUse hook that checks output quality, are good starting points. The implementation is yours — do not copy-paste a ready-made script.

**Remember: hooks require two steps** — write the script file AND register it in `.claude/settings.json`. Without registration, the script exists but never fires. See Lab C for the full registration example.

---

## Reflection

1. How is building a tool FOR AI different from building one for yourself? What interface decisions changed? Would a human user want the same thing?

2. Anthropic's principle: "If a human engineer can't definitively say which tool should be used, an AI agent can't be expected to do better." Did you see this play out in the composability exercise?

3. The WISC SELECT strategy is about progressive disclosure — loading only what is needed. How does the Skills mechanism embody this principle differently than CLAUDE.md rules?

---

## Stretch

- Build the full composability loop: CLI tool + slash command that invokes it + hook that validates the output. Three layers, all connected.
- Build a skill with progressive disclosure: a SKILL.md with metadata (description, trigger words) and detailed instructions that only load when the skill activates. Compare how Claude reaches for it versus how it uses a CLAUDE.md rule.
- Build a tool that generates context: a script that, when run, produces a formatted summary of the current project state that Claude can read as a briefing. Measure whether it improves first-turn accuracy on a task.
- Build a CI integration: use `claude -p "query" --output-format json` (headless mode) to run Claude Code as a unix utility. Write a shell script that pipes code into Claude for analysis: `cat src/app/routes/todos.py | claude -p "List all potential security issues in this code" --output-format json`. Then combine it with your tool or hook — for example, a pre-commit hook that runs a security scan via headless Claude. Headless mode is how Claude Code integrates into CI/CD pipelines, automated workflows, and shell scripts. The `--output-format json` flag gives structured output you can parse programmatically.
