# Challenge D: Plugin from Workshop Work

> **Goal**: Package your best workshop artifacts into a shareable, installable plugin.

> **Constraints**:
> - Must include at least one skill and one hook or agent, plus a manifest.
> - Must curate from your own workshop work — not create new content specifically for the plugin.
> - Must document what you included, excluded, and why.
> - Must be tested by a partner.
>   (Working solo? Test your plugin by installing it in a fresh project directory and verifying each component works outside the workshop context.)

> **Success criteria**:
> - Plugin installs successfully in a partner's Claude Code session.
> - Partner can use at least one component.
> - You can explain every inclusion/exclusion decision.
> - Partner feedback reveals at least one insight you did not expect.

> **Time**: ~60 minutes

> **Recommended model:** `sonnet` at medium effort (`/model sonnet`)

---

## The Brief

Spend 10 minutes reviewing everything you've built during this workshop — skills, agents, hooks, slash commands, CLAUDE.md rules, briefing templates. The question isn't "did you build a lot?" It's "did you build the right things?" Choose the components worth sharing. Package them into a plugin with proper directory structure and a manifest. Then swap with a partner: install each other's plugins, actually use them, and give honest feedback. This is the "Contribute a Named Pattern" moment — not just for code, but for workflows.

---

> **💡 Plugin tip: plugin-dev** — The `plugin-dev` plugin (`/plugin install plugin-dev@claude-plugins-official`) is purpose-built for this challenge. Its `/plugin-dev:create-plugin` command runs an 8-phase guided workflow for creating plugins, and includes specialist skills for hooks, commands, agents, and MCP integration. Install it first to scaffold your plugin structure.

---

## Deliverables

1. Plugin directory with proper structure and manifest.json.
2. At least one skill, one hook or agent — your own work, curated and polished for sharing.
3. Design decision log: for each component included, why? For at least two components you built but excluded, why not?
4. Partner feedback notes: what did they use? What confused them? What would they change?

---

## Plugin Structure Reference

A Claude Code plugin follows this directory structure:

```
my-plugin/
├── manifest.json          # Plugin metadata and configuration
├── skills/               # Skill definitions
│   └── my-skill/
│       └── SKILL.md
├── agents/               # Agent definitions
│   └── my-agent.md
├── hooks/                # Hook scripts
│   └── my-hook.sh
└── README.md             # Documentation
```

The `manifest.json` contains:

```json
{
  "name": "my-plugin",
  "version": "1.0.0",
  "description": "What this plugin does",
  "skills": ["skills/my-skill"],
  "hooks": {
    "PreToolUse": [
      {
        "matcher": "Bash",
        "hooks": [
          {
            "type": "command",
            "command": "bash hooks/my-hook.sh"
          }
        ]
      }
    ]
  }
}
```

> **Tip:** Ask Claude to help you create the manifest — describe what components you want to include and let it generate the structure. Then review and adjust.

> **Note:** The plugin manifest format may evolve. Check the [Claude Code plugin documentation](https://code.claude.com/docs/en/plugins) for the current format before structuring your manifest.

---

## Final Reflection

1. What made a component worth packaging vs leaving as a local artifact? What was the deciding factor?
2. Did your partner use the plugin differently than you intended? What does that tell you about building tools for others vs for yourself?
3. Looking across everything you built during this workshop: what's the ratio of "for you" vs "for Claude" vs "for your team"? Does that feel like the right balance?
4. Willison: "Coding agents mean we only ever need to figure out a useful trick once." Which trick from this workshop would you most want to share with the entire agentic engineering community? Why?
5. What's the one component you wish you had built but didn't?
