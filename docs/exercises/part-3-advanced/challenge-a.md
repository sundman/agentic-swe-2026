# Challenge A: Greenfield Capstone

> **Goal**: Build a working application from scratch, applying all workshop principles without step-by-step guidance.

> **Constraints**:
> - Must include CLAUDE.md + at least one rules file.
> - Must use at least one structured workflow approach (PIV loop, TDD, or AndThen cycle — your choice).
> - Must include automated tests.
> - Must document your decisions.

> **Success criteria**:
> - Application runs and passes its own tests.
> - Your CLAUDE.md would be useful to a new developer joining the project.
> - You can explain every significant architectural decision.
> - Your linear walkthrough accurately describes what the code does.

> **Time**: ~90 minutes

> **Recommended model:** `sonnet` at high effort, or `opus` — greenfield builds benefit from stronger reasoning for architecture decisions (`/model opus`)

---

## The Brief

You've spent the workshop working with an existing codebase and a ready-made context setup. Now you start from zero. Choose one of the project ideas below — or propose your own — set up the context engineering foundations yourself, and build a working first version. The hard part isn't the code: it's deciding what context Claude needs to do good work on your specific project, and choosing a workflow approach that fits how you think. There is no prescribed workflow here; that's the point. Choose the approach that makes sense for you, and be ready to explain why you chose it. When you're done, you'll have a project you built under your own judgment, using the full range of techniques from the workshop.

---

## Project Options

### Option A: Bookmark Manager

Save URLs with tags and notes, searchable.

### Option B: Habit Tracker

Daily habits with streaks and completion history.

### Option C: Recipe Book

Recipes with ingredients, steps, and meal planning.

### Option D: Your Own Idea

3-5 core features, CRUD operations, and a simple UI.

---

> **💡 Plugin tip: frontend-design** — The `frontend-design` skill (`/plugin install frontend-design@claude-plugins-official`) generates distinctive, production-grade frontend interfaces — not generic AI aesthetics. Use it to rapidly prototype your UI, then iterate on the design. This can dramatically accelerate the visual side of your greenfield app.

---

## Deliverables

1. Working application (code, tests passing).
2. CLAUDE.md + at least one rules file.
3. Decision log: for each significant decision (architecture, tech choices, workflow approach), record what you asked AI, what you retained, and why.
4. Linear walkthrough: ask Claude to produce a file-by-file explanation of your code — save it as `WALKTHROUGH.md`. Review it: does it accurately describe what you built?
5. One named pattern: document one repeatable pattern you discovered during this build (a la Willison's living guide). Give it a name, describe the problem it solves, and write the key prompt.

---

## Final Reflection

1. Which WISC strategies did you use naturally? Which did you consciously choose, and which emerged from necessity?
2. What was your biggest learning about working with AI agents on a full-stack project?
3. Did your approach change as the project progressed? What triggered the change?
4. Looking at your decision log: what percentage of decisions came from AI, and what percentage were yours? Does that feel right?
5. If you could give one piece of advice to someone starting with agentic engineering tomorrow, what would it be?
