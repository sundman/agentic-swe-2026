> **Goal**: Port the todo app to a completely different tech stack, proving that well-written requirements are technology-portable.

> **Constraints**:
> - You must use `docs/todo-app-requirements/functional-requirements.md` as your ONLY specification — do NOT read the Python source code for implementation ideas.
> - Must create a CLAUDE.md and at least one rules file for the new stack.
> - Must have passing tests that prove functional equivalence to the original.

> **Success criteria**:
> - App runs with equivalent functionality described in the functional requirements.
> - You can explain every architectural decision.
> - Someone could continue development using only your CLAUDE.md.
> - Your comparison reflection reveals at least 2 patterns that translated and 2 that required different approaches.

> **Time**: ~90 minutes

> **Recommended model:** `sonnet` at high effort, or `opus` — porting to an unfamiliar stack benefits from stronger reasoning (`/model opus`)

> **Scope note:** A full port of all features (auth, lists, search, drag-drop, dark mode) is ambitious for 90 minutes. Focus on core CRUD functionality first — the learning is in the process of translating requirements to a new stack, not in achieving 100% feature parity. A partial port with clean architecture and good tests is a better outcome than a rushed complete port.

---

## The Brief

Choose a tech stack you want to explore: Node.js/Express, Go/Echo, Rust/Axum, Java/Spring Boot, C#/ASP.NET, Ruby/Sinatra, Elixir/Phoenix, or another of your choice. Read the functional requirements document. Set up your context engineering infrastructure for the new stack FIRST — your CLAUDE.md is the most important thing you'll write. Then build. The question isn't "can AI port code?" — it can. The question is: "can YOU specify requirements precisely enough for AI to implement correctly in a stack neither of you knows well?"

---

## Deliverables

- Working application in the chosen stack with passing tests.
- CLAUDE.md and at least one rules file for the new stack, with a brief note on what each rule is for.
- Architectural decision log: why this stack? What framework and library choices? What trade-offs?
- Comparison reflection: what translated directly from the functional requirements? What required different approaches? Where did the functional requirements have gaps you only discovered during porting?
- A linear walkthrough produced with Claude: ask Claude to explain what you built, section by section. Be ready to explain it to a partner in your own words.

---

## Final Reflection

1. What patterns from the Python app translated directly to the new stack? What required completely different approaches?
2. Did the functional requirements document have gaps? Where did you have to make decisions the document didn't specify?
3. How did your CLAUDE.md for the new stack differ from the original? What's universal versus stack-specific?
4. The constraint says "do not read the Python source" — did you follow it? What would have been different if you had?
5. What does this exercise tell you about the relationship between requirements quality and AI output quality?
