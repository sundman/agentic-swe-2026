# Where Claude Code Runs

Quick reference for Claude Code's three execution environments.

---

## Three Environments at a Glance

| | Local CLI | Remote Control | Claude Code on the Web |
|---|---|---|---|
| **Code runs on** | Your machine | Your machine | Anthropic cloud VM |
| **You interact via** | Terminal | Terminal + browser + mobile | Browser + mobile |
| **Start with** | `claude` | `claude --rc` or `/rc` | `claude --remote "task"` or claude.ai/code |
| **Local filesystem** | Full access | Full access | No — GitHub repo clone only |
| **MCP servers** | Available | Available | Not available |
| **Hooks** | All (user + repo) | All (user + repo) | Repo-committed only |
| **CLAUDE.md** | All (user + repo) | All (user + repo) | Repo-committed only |
| **User settings** | `~/.claude/settings.json` | `~/.claude/settings.json` | Not carried over |
| **Network** | Unrestricted | Unrestricted (your machine) | Proxied, configurable allowlist |
| **Parallelism** | One session | `--spawn worktree` for multiple | Multiple independent sessions |
| **Session persistence** | Tied to terminal | Auto-reconnects on network drop | Persists even if laptop closes |

---

## When to Use Each

| Use case | Best environment |
|----------|-----------------|
| Daily interactive development | **Local CLI** |
| Continue local work from phone/browser | **Remote Control** |
| Fire-and-forget tasks while you do other work | **Web** |
| Repos you don't have cloned locally | **Web** |
| Multiple parallel tasks (bug fixes, refactors) | **Web** |
| Tasks needing local MCP servers or custom tools | **Local CLI** or **Remote Control** |
| CI/CD automation | **Local CLI** (`claude -p`) or **Web** (`claude --remote`) |

---

## Key Commands

### Remote Control

```bash
# Start a dedicated server (waits for remote connections)
claude remote-control
claude remote-control --name "My Project" --spawn worktree

# Start interactive session with remote access
claude --rc
claude --rc "My Project"

# Enable from inside an existing session
/rc
```

Press spacebar in server mode to show a QR code for your phone.

### Claude Code on the Web

```bash
# Send a task to run in the cloud
claude --remote "Fix the flaky test in auth.spec.ts"

# Run multiple tasks in parallel
claude --remote "Update API documentation"
claude --remote "Refactor logger to structured output"

# Check progress
/tasks

# Pull a cloud session back to your terminal
claude --teleport        # interactive picker
claude --teleport <id>   # specific session
/teleport                # from inside Claude Code
```

---

## Context Engineering Implications

The most important thing about these environments: **where code runs determines what context Claude can see.**

| Context source | Local | Remote Control | Web |
|---------------|-------|---------------|-----|
| Your local files | Yes | Yes | No (only what's in git) |
| `~/.claude/settings.json` | Yes | Yes | No |
| `.claude/settings.json` (in repo) | Yes | Yes | Yes |
| CLAUDE.md (in repo) | Yes | Yes | Yes |
| MCP servers | Yes | Yes | No |
| Setup scripts (cloud config) | N/A | N/A | Yes |
| SessionStart hooks (in repo) | Yes | Yes | Yes |

**Takeaway:** If you want your context artifacts to work everywhere — including cloud sessions — commit them to the repo. This means:
- Keep CLAUDE.md up to date (it's your context that travels)
- Commit `.claude/settings.json` with hooks and permission rules
- Use SessionStart hooks (not user-level settings) for setup that should run in all environments

---

## Requirements

- **Remote Control:** Pro/Max/Team/Enterprise plan, claude.ai OAuth (`/login`), Claude Code v2.1.51+
- **Web:** Pro/Max/Team/Enterprise plan, GitHub account connected, Claude GitHub app installed on repos
- **API keys are not supported** for either feature — both require claude.ai authentication

---

## Further Reading

- Remote Control docs: https://code.claude.com/docs/en/remote-control
- Claude Code on the Web docs: https://code.claude.com/docs/en/claude-code-on-the-web
