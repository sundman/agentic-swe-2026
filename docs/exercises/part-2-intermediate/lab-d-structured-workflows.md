# Lab D: Structured Workflows

**Time:** ~60 minutes

**Prerequisites:** Lab C completed, AndThen plugin installed (Exercise 3)

> **Recommended model:** `sonnet` at medium effort (`/model sonnet`)

---

> **Principle**: Structured workflows have overhead — evaluate the trade-off consciously

> **WISC strategy**: WRITE — spec files serve as persistent session handoffs, surviving context resets and enabling parallel work. SELECT — load only the relevant context per workflow phase, rather than carrying everything through every step.

> **You will**:
> - Run a full structured workflow cycle on a real feature
> - Compare it directly against a quick-implement path
> - Use the workflow itself to improve the workflow

> **Reference cards**: [Briefing Template](../../reference/briefing-template.md) · [PIV Loop](../../reference/piv-loop.md)

---

## The Challenge

Build the "Quick Notes" feature for the todo app — the ability to add timestamped notes to any todo item, with a collapsible note history in the edit dialog — using the full AndThen structured workflow: clarify → spec → exec-spec → review-gap. This is Spec-Driven Development; Thoughtworks calls it "Waterfall in 15 minutes" when AI accelerates each phase.

Then build a second, similarly-scoped feature using the `quick-implement` path. Compare both approaches across four dimensions: time taken, output quality, bugs discovered, and your confidence in the result. Finally, ask Claude what your spec was missing — use its answer to improve the spec.

---

## Suggested Approach

1. Start with `andthen.clarify` for the Quick Notes feature. Answer Claude's clarifying questions thoroughly — these questions reveal what your spec needs. Notice which questions you hadn't considered before being asked.

> **Technical note:** Adding a new `TodoNote` model doesn't require a migration. This project uses `Base.metadata.create_all()` which automatically creates new tables on app startup. Just define the model and restart the server.

2. Run `andthen.spec` to generate a Feature Implementation Specification. Review it carefully before proceeding. Is the scope right? Are the acceptance criteria testable? Is anything wrong or missing? The spec file is the WRITE artifact — a fresh session could pick it up.

3. Run `andthen.exec-spec` to implement. Watch the implementation and validation loops. Then run `andthen.review-gap` to compare implementation against spec. Address any gaps surfaced.

4. Now compare: run `andthen.quick-implement "Add a 'pin todo to top' feature"` — a similarly-scoped feature. How does the result compare to your spec-driven implementation?

5. "Harvest the Feedback": ask Claude — "What was missing from my spec that made implementation harder or required more iterations?" Use the answer to revise your spec or your process.

> **💡 Plugin tip: feature-dev** — For comparison, try the `feature-dev` plugin (`/plugin install feature-dev@claude-plugins-official`) which implements its own 7-phase structured workflow (Discovery → Exploration → Questions → Architecture → Implementation → Review → Summary). Compare its approach to AndThen's clarify → spec → exec-spec → review-gap cycle — what trade-offs does each make?

---

## Reflection

1. For this lab's feature, was the full workflow worth the overhead? What is the threshold of task complexity or risk where you would switch from quick-implement to the full cycle?

2. The spec file served as a WRITE artifact. Could a fresh session — or a different Claude instance — have implemented from just the spec? What does that suggest about context engineering and session handoffs?

3. Compare the review-gap output to the quick-implement result. What categories of issues showed up in one but not the other?

---

## Stretch

- After building the Quick Notes feature, challenge Claude: "Add comprehensive error handling, improve test coverage to above 90%, and add accessibility attributes — treating these as free improvements." ([Willison](https://simonwillison.net/guides/agentic-engineering-patterns/)'s principle: AI should help us produce *better* code, not just *faster* code.)
- Try `andthen.e2e-test` to run browser-based end-to-end validation of your feature. How does automated end-to-end feedback compare to manual verification?
- Design a structured workflow for your actual team: what phases would you include? Which steps would be automated vs. human-reviewed? What would your spec template look like?
