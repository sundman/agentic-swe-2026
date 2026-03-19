# Exercise 2: Bug Hunt & Trust Calibration

> **Core principle**: Trust Calibration
> AI output requires verification, not acceptance. 29.6% of plausible fixes introduce regressions.

**Goal:** Find and fix **5** planted bugs using Claude Code for AI-assisted debugging

**Time:** ~50 minutes

**Prerequisites:** Exercise 1 completed, todo app running

> **Recommended model:** `sonnet` at medium effort (`/model sonnet`)

---

## Setup

Make sure the todo app is running:

```bash
cd todo-app
uv run uvicorn app.main:app --reload
```

Open http://localhost:8000 and log in with `demo@example.com` / `demo123`.

Create a test list and add a few todos to work with.

84% of developers use AI tools. Fewer than 50% review AI code before committing. (Stack Overflow 2025.) In this exercise, you'll practice being in the review-first 50%.

Keep `docs/reference/failure-patterns.md` open alongside this exercise. As you work through each bug, identify which named pattern you're seeing.

> **The challenge:** Describe the *symptom* to Claude Code, not the solution. Let the AI do the detective work. The better you describe what you observe, the faster Claude will find the root cause.

---

## Bug 1: Missing Default Priority

**Symptom:** Quick-add todos have no priority set.

**Reproduce:**
1. Type a todo title in the "Quick add" field and press Enter
2. Click the edit button on the new todo
3. Notice: the priority dropdown is empty or unset

**Your task:** Describe this bug to Claude Code. Focus on what you observe, not on what you think the fix should be.

```
I noticed that when I add a todo using the quick-add field, it doesn't
have a default priority. When I edit it, the priority is empty.
Can you find and fix this?
```

<details>
<summary>Stuck? Here's a hint</summary>

Look at `todo-app/src/app/routes/todos.py` — the `create_todo` function.
When creating a `Todo` object, no `priority` is specified.
The fix: add `priority="low"` to the `Todo()` constructor.
</details>

**Verify:** Create a new quick-add todo. Edit it — priority should show "low".

Which failure pattern was this? How would you have caught it without running tests?

---

## Bug 2: Due Dates Not Saving

**Symptom:** Setting a due date in the edit dialog doesn't persist.

**Reproduce:**
1. Edit a todo and set a due date
2. Save and close the dialog
3. Edit the same todo again — the due date is gone

**Your task:** Describe what you see happening.

```
When I set a due date on a todo and save, the date doesn't persist.
After reopening the edit dialog, the due date field is empty again.
Find and fix the issue.
```

<details>
<summary>Stuck? Here's a hint</summary>

File: `todo-app/src/app/routes/todos.py` — `update_todo` function.

HTML date inputs send dates in `"2024-01-15"` format (YYYY-MM-DD).
The code tries to parse with `"%Y-%m-%dT%H:%M"` (datetime-local format).
Since the format doesn't match, the `except ValueError: pass` silently swallows the error.

Fix: Change the format string to `"%Y-%m-%d"`.
</details>

**Verify:** Set a due date, save, reopen — the date should persist.

Claude's fix looks clean. Before accepting it, what edge cases should you check? (Hint: what happens when the field is empty?)

---

## Bug 3: Sidebar Count Not Updating on Delete

**Symptom:** Deleting a todo doesn't update the sidebar count.

**Reproduce:**
1. Create a list with 3+ incomplete todos
2. Note the count shown in the sidebar
3. Delete one todo
4. The sidebar count stays the same (only updates on page refresh)

**Your task:** This involves HTMX Out-of-Band (OOB) swaps — a pattern where a response updates multiple parts of the page. Describe what you observe.

```
When I delete a todo, the sidebar count doesn't update. It still shows
the old number until I refresh the page. Other operations like toggling
completion do update the count. Find and fix this.
```

<details>
<summary>Stuck? Here's a hint</summary>

File: `todo-app/src/app/routes/todos.py` — `delete_todo` function.

The function returns a plain `Response(status_code=200)` without an OOB swap to update the sidebar count. Compare with `toggle_todo` which returns `todo_item_with_oob.html` including the updated count.

Fix: Make `delete_todo` return an HTML response with an OOB swap, similar to `toggle_todo`.

**Tip:** Check if there's already a template for this — look at the `partials/` directory for an existing `todo_deleted_oob.html` template that may already have what you need.
</details>

**Verify:** Delete a todo — sidebar count should update immediately.

This was the hardest bug. Would Claude have found it on its own if you'd just said "fix the sidebar"? Why or why not?

---

## Bug 4: Overdue Styling Wrong

**Symptom:** Overdue/due-today styling appears on the wrong todos.

**Reproduce:**
1. Create three todos with due dates: yesterday, today, and tomorrow
2. Check the styling:
   - Yesterday's todo should be red (overdue)
   - Today's todo should be amber/orange (due today)
   - Tomorrow's should be normal
3. Instead: today's todo shows as overdue, and "due today" styling never appears

**Your task:** This is a datetime comparison bug. Describe what you observe.

```
The overdue styling is wrong. Todos due today are showing as overdue
(red), and the "due today" styling (amber) never appears. I created
todos with yesterday, today, and tomorrow due dates to test.
Can you find the date comparison issue?
```

<details>
<summary>Stuck? Here's a hint</summary>

File: `todo-app/src/app/utils.py` — `is_overdue` and `is_due_today` functions.

The bug: comparing full `datetime` (with time) instead of just dates.
- `is_overdue`: compares `todo.due_date < now` — since `now` includes the current time, a todo due "today" at midnight is considered overdue at 1am.
- `is_due_today`: compares `todo.due_date == now` — exact datetime match will essentially never be true.

Fix: Compare `.date()` parts only:
```python
today = date.today()
return todo.due_date.date() < today   # is_overdue
return todo.due_date.date() == today  # is_due_today
```
</details>

**Verify:** Yesterday = red (overdue), today = amber (due today), tomorrow = normal.

What verification approach would have caught this fastest — reading the code, running tests, or manual testing?

---

## Bug 5: The Silent Data Loss Bug

**Bug 5 is different.** You've been trusting Claude's fixes for the last four bugs. This time, Claude's first suggestion will look correct — but it introduces a subtle regression. Your job is to catch it before accepting.

**Background:** Bug 2's fix changed the date format string so that dates save correctly. But there's a second issue lurking in the same function: what happens when a user *clears* a due date?

**Symptom:** After fixing Bug 2, try clearing a due date — set a due date on a todo, save it, then edit again and delete the date value. Save. The due date is still there.

**Reproduce:**
1. Edit a todo and set a due date
2. Save — confirm the date appears
3. Edit the same todo again and clear the due date field (delete the value)
4. Save — the due date is still there

**What's happening:** When the due date field is cleared, the browser sends `due_date=""` (empty string). The `except ValueError: pass` block catches the parse failure for this empty string and silently does nothing — the old date remains. This bug was hidden by Bug 2: when the format string was wrong, ALL date operations failed silently, so you couldn't tell that clearing was also broken.

**Your task:**
1. Make sure Bug 2 is fixed first — this bug is only visible once date saving works.
2. Review Claude's fix carefully — does it handle an empty string `due_date`?
3. Test it: create a todo with a due date, then try to clear it. Does it clear?
4. If not, instruct Claude to fix the clearing case explicitly:

```
The due date fix works for saving dates, but there's another case:
when a user clears the due date field (sends an empty string),
the date should be removed. Right now it stays set.
The fix: if due_date == "", set todo.due_date = None.
```

<details>
<summary>Stuck? Here's a hint</summary>

File: `todo-app/src/app/routes/todos.py` — `update_todo` function.

The fix needs to handle empty string before attempting to parse:

```python
if due_date == "":
    todo.due_date = None
elif due_date:
    todo.due_date = datetime.strptime(due_date, "%Y-%m-%d")
```

The `except ValueError: pass` block is what hid this — it looks like correct error handling, but it swallows the empty-string case along with genuine parse errors.
</details>

**Verify:** Set a due date, save. Edit again, clear the date field, save. The due date should be gone.

What failure pattern is this? (Plausible-but-wrong.) How could you have caught it earlier? What does this teach about the 29.6% stat?

---

## Quick Check — Slopsquatting Awareness (~2 min)

Look at the imports in the files you've been working with. Does every `import` reference a real, installed package? Check `pyproject.toml`. "Slopsquatting" — hallucinated package names — is a real supply chain attack vector.

---

## Final Check

Run the test suite to confirm your fixes don't break anything:

```
Run all the tests in the todo app and show me the results.
```

Or in a separate terminal:
```bash
cd todo-app
uv run pytest tests/ -v
```

All tests should pass.

> **💡 Plugin tip: pyright-lsp** — With the Python LSP plugin installed (`/plugin install pyright-lsp@claude-plugins-official`), Claude gets real-time type diagnostics. Some of the planted bugs (like the missing default priority) surface more clearly through type checking. This demonstrates how tool augmentation improves trust calibration.

## Review Your Fixes

Use Claude Code's built-in review tools to inspect what you changed:

### Interactive Diff
```
/diff
```

This opens an interactive diff viewer showing all file changes. Review each change — does it match what you intended?

### Security Review
```
/security-review
```

This analyzes your changes for potential security vulnerabilities. For a todo app, it might flag things like missing input validation or unsafe date parsing. Even if it finds nothing critical, building the habit of running `/security-review` before committing is valuable.

---

## Bonus: Investigate with Plan Mode

If you have extra time, try using Plan mode to investigate one of the bugs before fixing it:

1. Press **Shift+Tab** twice to enter Plan mode
2. Describe a symptom
3. Watch Claude trace through the code without making changes
4. Switch back to Normal mode and apply the fix

This is a great workflow for complex bugs — investigate first, then fix.

---

## Stretch Challenge

Find a 6th bug that ISN'T planted. Review `utils.py` and `deps.py` for real issues.

---

## Key Takeaways

| Concept | Remember |
|---------|----------|
| Trust calibration | Verify before accepting — 29.6% of plausible fixes introduce regressions (Kent Beck: *"TDD is a superpower when working with AI agents"*) |
| Symptom-first | Describe what you observe, not what you think the fix is |
| Silent failures | Watch for `except: pass` — errors vanish silently |
| Date/time bugs | Compare `.date()` not full datetime with time component |
| HTMX OOB swaps | Multiple page sections can update from a single response |
| Default values | Set defaults explicitly, don't assume the DB handles it |
| Named failure patterns | Shared vocabulary for diagnosing what went wrong |
| Tests pass ≠ it works | "If the code has never been executed it's pure luck if it actually works" (Willison) |
| Plan mode | Great for investigating before fixing |

---

## Resources

- [HTMX OOB Swaps](https://htmx.org/docs/#oob_swaps)
- [Python datetime](https://docs.python.org/3/library/datetime.html)
- [FastAPI Form Data](https://fastapi.tiangolo.com/tutorial/request-forms/)
- `docs/reference/failure-patterns.md` — Named failure patterns reference card
- Kent Beck, [TDD, AI agents and coding](https://newsletter.pragmaticengineer.com/p/tdd-ai-agents-and-coding-with-kent) — why tests are "an unambiguous, executable specification" for AI
- Robert C. Martin, [Clean AI: Agentic Discipline](https://cleancoders.com/episode/agentic-discipline-1) — testing + refactoring as the two essential disciplines
