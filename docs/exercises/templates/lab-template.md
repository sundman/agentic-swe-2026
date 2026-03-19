<!--
  LAB TEMPLATE — Theme Lab Format (Phase 2)
  ==========================================

  PURPOSE
  This template defines the structure for all Phase 2 Theme Labs (Labs A through E).
  It establishes a consistent, outcome-focused format that replaces step-by-step
  feature tours with principle-driven practice.

  WHICH EXERCISES USE THIS TEMPLATE
  - Lab A: Context Deep Dive (converted from Exercise 5)
  - Lab B: Agent Orchestration (converted from Exercise 6)
  - Lab C: Verification & Security (converted from Exercise 7)
  - Lab D: Structured Workflows (converted from Exercise 8)
  - Lab E: Tool Building (converted from Exercise 9)

  PEDAGOGICAL PRINCIPLES BEHIND THIS FORMAT

  1. Outcome-focused, not step-by-step
     "The Challenge" section describes WHAT to achieve, not HOW. Students decide
     the approach. This develops judgment, not procedural memory.

  2. Productive struggle
     Students should have to think. The "Suggested Approach" provides light
     scaffolding for those who need it, but doesn't remove the need to make
     decisions. The point is the thinking, not the execution.

  3. Generation-then-comprehension
     Students attempt the task before receiving explanation. This is the
     generation effect: struggling with a problem first makes subsequent
     instruction more memorable. The reflection questions consolidate learning
     after the attempt.

  4. WISC as a connecting thread
     Every lab is anchored to one or two WISC strategies (Write, Isolate, Select,
     Compress). This connects the lab to the context engineering framework from
     the slides and gives students a vocabulary for what they're practicing.

  5. Partner work
     The reflection questions are designed for two people. Learning is social.
     Students who work alone should at minimum write answers before moving on.

  HOW TO USE THIS TEMPLATE
  - Replace all bracketed placeholders with actual content
  - Remove this comment block before publishing
  - Keep the section order exactly as specified — students will develop pattern
    recognition across labs
  - The "Suggested Approach" should be 3-4 steps, high-level, not prescriptive
  - Reference card links go in docs/reference/ — use relative paths
-->

<!-- ============================================================
  HEADER BLOCK
  This is a blockquote, rendered visibly at the top of the lab.
  Keep it brief — this is orientation, not instruction.
  ============================================================ -->

> **Principle**: [One sentence capturing the transferable idea this lab teaches. Should be true beyond Claude Code — a principle the student can apply with any AI coding tool. Example: "Controlling what an agent can see is more powerful than controlling what it can do." Example: "Isolation is the cheapest way to prevent context pollution."]

> **WISC strategy**: [Which strategy (or strategies) this lab primarily practices. One of: Write, Isolate, Select, Compress. Example: "SELECT — choosing what context to provide and what to withhold." Example: "ISOLATE — running tasks in a clean context to prevent cross-contamination." If two strategies apply, list both with a brief note on each.]

> **You will**:
> - [Outcome statement 1 — start with a verb, describe something the student will do or experience. Example: "Audit a live context window and identify what's consuming the most space."]
> - [Outcome statement 2 — Example: "Induce context rot and observe how output quality degrades."]
> - [Outcome statement 3 — optional. Example: "Recover a session using a recombination prompt."]

> **Reference cards**: [Links to relevant reference materials in docs/reference/. Example: "[Context Economics](../../reference/context-economics.md) · [Delegation Decision Tree](../../reference/delegation-decision-tree.md)". Only link cards that students will actually need during this lab.]

---

## The Challenge

<!-- ============================================================
  THE CHALLENGE
  This is the heart of the lab. Describe the END STATE the
  student should reach, not the steps to get there.

  WHAT GOOD CONTENT LOOKS LIKE
  - 2-4 sentences describing the outcome
  - Concrete and specific — students should know when they've
    succeeded (or failed)
  - Tool-agnostic where possible — describes WHAT, not HOW
  - Avoids verbs like "open", "run", "type", "navigate to"
  - Does use verbs like "demonstrate", "produce", "compare",
    "show", "measure", "design", "document"

  EXAMPLE (Lab A: Context Deep Dive)
  "Using your todo-app session from Phase 1, produce a before/
  after comparison showing how context window composition affects
  output quality. Your final session should demonstrate tool
  minimalism: the same task completed with at least 30% fewer
  active context tokens. Document what you removed and why."

  COMMON MISTAKES
  - Writing "Step 1: Open Claude Code. Step 2: Run /context."
    → That's a tutorial, not a challenge.
  - Being so vague that students don't know when they're done
    → Add a concrete deliverable or success signal
  - Describing the journey instead of the destination
    → Reframe from "you will explore X" to "you will produce Y"
  ============================================================ -->

[Outcome description — WHAT to achieve, not HOW. 2-4 sentences. Describe the end state clearly enough that a student knows when they've succeeded. Include a concrete deliverable or comparison where possible.]

---

## Suggested Approach

<!-- ============================================================
  SUGGESTED APPROACH
  Light scaffolding for students who need a starting point.
  This is NOT a walkthrough. It's a sequence of phases, each of
  which requires independent decision-making.

  WHAT GOOD CONTENT LOOKS LIKE
  - 3-4 numbered steps
  - Each step is a phase or decision, not a specific command
  - Leaves the "how" open — students still have to figure it out
  - Written as questions or framing hints, not instructions

  EXAMPLE (Lab A: Context Deep Dive)
  "1. Measure first. Before changing anything, inspect your
      current session — what's in scope? What tools are active?
  2. Form a hypothesis. What do you expect to improve if you
      reduce context? Write it down before testing.
  3. Experiment. Make a change, run the same task, compare.
      Be disciplined: change one thing at a time.
  4. Document. Keep a running log of what you changed, what
      improved, and what surprised you."

  COMMON MISTAKES
  - Prescriptive commands: "Run /context, then copy-paste the
    output to a note." → Too specific. Students stop thinking.
  - Too few steps: Only 1-2 phases → Students have no structure
  - Too many steps: 7+ numbered items → This is now a tutorial

  NOTE ON PHILOSOPHY
  This section exists because students who are stuck will give up
  rather than ask for help. The suggested approach is a safety
  net, not a script. Students who use it should still be making
  real decisions at each step.
  ============================================================ -->

1. [Phase or decision 1 — Example: "Before changing anything, establish a baseline. What does the current state look like? What would success look like?"]
2. [Phase or decision 2 — Example: "Form a hypothesis. Write down what you expect to happen before you test it."]
3. [Phase or decision 3 — Example: "Run the experiment. Be deliberate — change one thing at a time so you can attribute the result."]
4. [Phase or decision 4 (optional) — Example: "Document what you found. Your reflection questions will ask you to explain your results to a partner."]

---

## Reflection

<!-- ============================================================
  REFLECTION
  Questions for students to discuss with a partner after the lab.
  These consolidate learning and connect practice to principle.

  WHAT GOOD CONTENT LOOKS LIKE
  - 2-3 questions
  - Questions that require articulation, not recall
  - At least one question connects to the WISC strategy
  - At least one question asks about transfer ("how would you
    apply this in your own codebase?")
  - Questions that produce interesting disagreement — different
    students may have had different experiences

  EXAMPLE (Lab A: Context Deep Dive)
  "1. What surprised you most about what was consuming your
      context window? Did your hypothesis hold?
  2. When is it worth spending time on context minimalism, and
      when is it not? Where's the break-even point?
  3. What's one change from this lab you'd make permanent in
      your own workflow?"

  COMMON MISTAKES
  - Yes/no questions: "Did you succeed?" → Not discussable
  - Recall questions: "What does /context show?" → Not reflection
  - Too many questions: 5+ → Students rush through all of them
    instead of going deep on 2-3
  ============================================================ -->

1. [Reflection question 1 — connects to the lab's core experience. Example: "What surprised you most about what you found? Did it match your expectations going in?"]
2. [Reflection question 2 — connects to the WISC strategy. Example: "Where in your own work would this strategy help most? What's stopping you from applying it there?"]
3. [Reflection question 3 — transfer question. Example: "If you had to explain this principle to a colleague who'd never used Claude Code, what would you say?"]

---

## Stretch

<!-- ============================================================
  STRETCH
  Optional deepening for fast finishers or students who want
  to go further. Should not be required for the lab to succeed.

  WHAT GOOD CONTENT LOOKS LIKE
  - 2-3 options, not a single path
  - Each option is genuinely optional — different students will
    find different ones interesting
  - Options deepen or extend the lab's principle rather than
    introducing new topics
  - Written as possibilities, not instructions ("try X" or
    "explore Y", not "do steps 1-3 to complete X")

  EXAMPLE (Lab A: Context Deep Dive)
  "- Apply the same minimalism technique to a different task
    type (not feature work). Does the same approach transfer?
  - Try Willison's 'recombination' pattern: end the session,
    start fresh, and reconstruct context from scratch. Compare
    quality to the original session.
  - Measure the token cost of context compression: does a
    tighter context produce faster or cheaper responses?"

  COMMON MISTAKES
  - Making stretch feel like homework → Frame as exploration
  - Adding a stretch that requires setup not covered in the lab
  - Writing a single mandatory-feeling extension
  ============================================================ -->

- [Stretch option 1 — a deeper variation of the core challenge. Example: "Try applying the same approach to a different context — does the principle hold?"]
- [Stretch option 2 — an extension into adjacent territory. Example: "Explore what happens when you push the constraint further than you did in the challenge."]
- [Stretch option 3 (optional) — a reflection-based extension. Example: "Document a named pattern from your work today — something reusable you'd want to share with the group."]
