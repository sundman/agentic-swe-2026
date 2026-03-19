<!--
  CHALLENGE TEMPLATE — Open Challenge Format (Phase 3)
  =====================================================

  PURPOSE
  This template defines the structure for all Phase 3 Open Challenges.
  Students choose one challenge and work on it independently. The format
  gives them a goal and constraints, but no suggested workflow — they
  bring everything they learned in Phases 1 and 2 and apply it their way.

  WHICH EXERCISES USE THIS TEMPLATE
  - Challenge: Greenfield Capstone (choose a project and build it from scratch)
  - Challenge: Alt-Stack Port (port the todo app to a different tech stack)
  - Challenge: Multi-Agent Sprint (design and run a multi-agent workflow)
  - Challenge: Plugin from Workshop Work (package your best workshop artifacts)

  KEY DIFFERENCE FROM THE LAB TEMPLATE
  Labs (Phase 2) include a "Suggested Approach" section — light scaffolding
  for students who need a starting point. Challenges do NOT. Students choose
  their own workflow. This is intentional: Phase 3 is about proving mastery
  by applying principles independently, not following a structure.

  PEDAGOGICAL PRINCIPLES BEHIND THIS FORMAT

  1. Minimal guidance, maximum autonomy
     The challenge gives a goal, constraints, and success criteria. Nothing
     more. Students decide how to approach the work. They may apply WISC
     strategies, structured workflows, agent teams, or none of the above.
     The freedom IS the challenge.

  2. Decision documentation (required for all challenges)
     Students record what they asked the AI, what output they retained, and
     why. This creates accountability and makes tacit judgment explicit.
     It also produces a reflection artifact more valuable than the code itself.
     Include this requirement in every challenge's Deliverables section.

  3. Linear Walkthroughs (Willison pattern)
     After building, students ask Claude to produce a walkthrough of the code
     they created. This combats cognitive debt: students who used AI assistance
     extensively may not fully understand what they built. The walkthrough
     forces comprehension after generation. Include this in every challenge's
     Deliverables section.

  4. "Contribute a Pattern"
     Students document one named pattern they discovered during their challenge
     — something reusable they'd share with the group. This makes tacit
     knowledge explicit and creates workshop-wide sharing. At least one
     challenge should include this as a reflection prompt.

  5. Capstone accountability
     The challenge is the proof. Students should leave with something they
     built under their own judgment, using skills from the whole workshop.
     The Final Reflection questions connect back to the workshop's big ideas,
     not just the challenge's technical requirements.

  HOW TO USE THIS TEMPLATE
  - Replace all bracketed placeholders with actual content
  - Remove this comment block before publishing
  - Keep the section order exactly as specified
  - The header block MUST include Goal, Constraints, Success criteria, and Time
  - Deliverables MUST include decision documentation and linear walkthrough
  - Do NOT add a "Suggested Approach" section — that's what distinguishes
    challenges from labs
  - Constraints should be 2-4 items: specific enough to prevent drift,
    loose enough to allow genuine choice
-->

<!-- ============================================================
  HEADER BLOCK
  Rendered visibly at the top of the challenge.
  Goal is one sentence. Constraints prevent scope drift.
  Success criteria must be observable (a reviewer can check them).
  ============================================================ -->

> **Goal**: [One sentence. What the student is trying to achieve. Should be ambitious but achievable in the time given. Example: "Build a working web application from scratch using Claude Code as your primary development tool." Example: "Port the todo app to a different tech stack while preserving all existing functionality."]

> **Constraints**:
> - [Constraint 1 — what you must include. Example: "Must include a working CLAUDE.md that reflects your stack and project conventions."]
> - [Constraint 2 — what you must include or demonstrate. Example: "Must apply at least two WISC strategies, identified and documented."]
> - [Constraint 3 — what to avoid or what counts as out-of-bounds. Example: "Must not copy-paste code from Phase 1 exercises — all code should be generated fresh."]
> - [Constraint 4 (optional) — a quality or process constraint. Example: "Must produce passing tests before submitting."]

> **Success criteria**:
> - [Criterion 1 — observable outcome. Example: "A working application that meets the project's core requirements."]
> - [Criterion 2 — process artifact. Example: "Decision log documenting at least 5 key choices: what you asked AI, what you retained, and why."]
> - [Criterion 3 — comprehension artifact. Example: "A linear walkthrough produced with Claude that you can explain to a partner."]
> - [Criterion 4 (optional) — reflection quality. Example: "Reflection connects at least one decision to a specific WISC strategy or workshop principle."]

> **Time**: [Suggested duration. Example: "90 minutes." Example: "60 minutes." Challenges range from 45-90 min in the workshop.]

---

## The Brief

<!-- ============================================================
  THE BRIEF
  3-5 sentences describing what to build or do. This is the
  narrative version of the goal — it gives context and stakes,
  not instructions.

  WHAT GOOD CONTENT LOOKS LIKE
  - Concrete scenario or framing, not abstract description
  - Establishes WHY this challenge exists and what it tests
  - Mentions the source materials or starting point
  - Does NOT describe steps or workflow
  - Ends with what the student will have when they're done

  EXAMPLE (Greenfield Capstone)
  "You've spent the day working on an existing codebase with a
  ready-made context setup. Now you start from zero. Choose one
  of the project ideas below (or propose your own), set up the
  context engineering foundations yourself — CLAUDE.md, rules,
  structure — and build a working first version. The hard part
  isn't the code: it's deciding what context Claude needs to do
  good work on your specific project. When you're done, you'll
  have a project you built under your own judgment, using the
  full stack of techniques from the workshop."

  COMMON MISTAKES
  - Including workflow hints: "Start by setting up CLAUDE.md,
    then..." → That's a suggested approach. Remove it.
  - Being too vague: "Build something interesting." → Students
    won't know what's in scope
  - Being too prescriptive: "Use FastAPI and SQLite." → That's
    a constraint, put it in the header block
  ============================================================ -->

[3-5 sentences. Describe the challenge scenario, what the student is working with, why this tests meaningful skills, and what they'll have produced at the end. No step-by-step instructions.]

---

## Deliverables

<!-- ============================================================
  DELIVERABLES
  What the student must produce to complete the challenge.
  Should be concrete and checkable.

  REQUIRED FOR ALL CHALLENGES
  All challenges must include:
  1. Decision documentation — what they asked AI, what they
     retained, and why. This makes judgment explicit and creates
     accountability for AI-assisted work.
  2. Linear Walkthrough (Willison pattern) — after building,
     students ask Claude to produce a narrative walkthrough of
     what they created. Students should be able to explain the
     walkthrough to a partner. This combats cognitive debt.

  WHAT GOOD CONTENT LOOKS LIKE
  - 3-5 bullet items
  - Mix of primary artifact (the thing they built) and
    reflection artifacts (decision log, walkthrough, pattern)
  - Each item is specific enough to be checkable
  - "Contribute a Pattern" included where relevant

  EXAMPLE (Greenfield Capstone)
  "- A working application meeting your chosen project's core
    requirements (demonstrable in a browser or terminal)
  - A decision log: at least 5 entries recording what you asked
    Claude, what you retained, and why you made that choice
  - A linear walkthrough: ask Claude to produce a narrative
    explanation of what you built — review it and be ready to
    explain it to a partner
  - Your CLAUDE.md and any rules files, with a brief note on
    what each rule is for
  - (Optional) A named pattern you discovered — something
    reusable you'd share with the group"

  COMMON MISTAKES
  - Omitting decision documentation → Students produce code but
    develop no reflective capacity
  - Omitting linear walkthrough → Students may not understand
    what they built
  - Making deliverables too vague: "Show your work" → Not
    checkable
  ============================================================ -->

- [Primary deliverable — the thing they built or produced. Example: "A working application meeting the core requirements, demonstrable in a browser or terminal."]
- [Decision log — required for all challenges. Example: "A decision log with at least 5 entries: what you asked Claude, what you retained from the output, and why you made that choice."]
- [Linear walkthrough — required for all challenges. Example: "A linear walkthrough produced with Claude: ask Claude to explain what you built, section by section. Be ready to explain it to a partner in your own words."]
- [Challenge-specific deliverable (optional). Example: "Your CLAUDE.md and any rules files, with a brief note on what each rule is for."]
- [(Optional) Contribute a Pattern — Example: "A named pattern you discovered during this challenge — something reusable you'd share with the group."]

---

## Final Reflection

<!-- ============================================================
  FINAL REFLECTION
  Capstone questions connecting back to the workshop's big ideas.
  These are different from lab reflection questions — they're
  not about the challenge's specific topic, but about the student's
  overall development as an agentic engineer.

  WHAT GOOD CONTENT LOOKS LIKE
  - 2-4 questions
  - At least one connects to the WISC framework or a named
    principle from the workshop
  - At least one asks the student to compare their approach
    to what they would have done at the start of the day
  - At least one is forward-looking: what will you do differently?
  - Questions that can generate real disagreement between partners

  EXAMPLE (Greenfield Capstone)
  "1. Which WISC strategies did you use, and which would you
      have used differently knowing what you know now?
  2. At what point in the project did you feel most confident
      in what Claude was producing? At what point were you most
      skeptical? What changed?
  3. What's one thing you would do differently on the next
      greenfield project?
  4. What pattern did you discover that you'd want to share
      with an engineer who wasn't at this workshop?"

  COMMON MISTAKES
  - Questions that are too challenge-specific: "Was the
    Bookmark Manager the right choice?" → Not transferable
  - Questions that have obvious answers → Not discussable
  - Skipping the forward-looking question → Students leave
    without a concrete next action
  ============================================================ -->

1. [Reflection question 1 — connects to WISC or a core workshop principle. Example: "Which WISC strategies did you use in this challenge? Which would you use differently?"]
2. [Reflection question 2 — trust calibration or verification. Example: "At what point did you feel most uncertain about Claude's output? How did you resolve that uncertainty?"]
3. [Reflection question 3 — forward-looking. Example: "What's one thing you'll do differently in your own work next week because of this workshop?"]
4. [Reflection question 4 (optional) — transfer and sharing. Example: "What named pattern did you discover that you'd want to share with an engineer who wasn't here?"]
