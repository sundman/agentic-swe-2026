# Exercise 2: Bug Solutions

Reference solutions for the 5 bugs (4 planted + 1 regression introduced by Claude). Try to solve them with Claude Code first!

---

## Bug 1: Missing Default Priority

**File:** `todo-app/src/app/routes/todos.py` — `create_todo` function

**Problem:** The `Todo()` constructor doesn't set a default priority.

**Fix:** Add `priority="low"` when creating the todo:

```python
todo = Todo(
    list_id=list_id,
    title=title.strip(),
    position=new_pos,
    priority="low",  # Add this line
)
```

---

## Bug 2: Due Dates Not Saving

**File:** `todo-app/src/app/routes/todos.py` — `update_todo` function

**Problem:** The date format string doesn't match what HTML date inputs send.

HTML `<input type="date">` sends `"2024-01-15"` (YYYY-MM-DD), but the code expects `"%Y-%m-%dT%H:%M"` (datetime-local format). The `except ValueError: pass` silently swallows the mismatch.

**Fix:** Change the format string:

```python
# Before (broken):
todo.due_date = datetime.strptime(due_date, "%Y-%m-%dT%H:%M")

# After (fixed):
todo.due_date = datetime.strptime(due_date, "%Y-%m-%d")
```

---

## Bug 3: Sidebar Count Not Updating on Delete

**File:** `todo-app/src/app/routes/todos.py` — `delete_todo` function

**Problem:** The function returns a plain `Response(status_code=200)` without an OOB (Out-of-Band) swap to update the sidebar count. Compare with `toggle_todo` which correctly returns an OOB update.

**Fix:** Return an HTML response with the updated count. The function needs to:
1. Store the `list_id` before deleting
2. Delete the todo
3. Get the updated count
4. Return an HTML response with an OOB swap

```python
@router.delete("/{todo_id}")
async def delete_todo(
    request: Request,
    todo_id: str,
    user_id: Annotated[str, Depends(get_current_user_id)],
    db: Session = Depends(get_db),
):
    """Delete a todo item."""
    todo = db.query(Todo).filter(Todo.id == todo_id).first()
    if not todo:
        return Response(status_code=404)

    list_obj = _verify_list_access(db, todo.list_id, user_id)
    if not list_obj:
        return Response(status_code=403)

    list_id = todo.list_id
    db.delete(todo)
    db.commit()

    # Get updated count for OOB swap
    count = _get_list_todo_count(db, list_id)

    return templates.TemplateResponse(
        request=request,
        name="partials/todo_item_with_oob.html",
        context={"todo": None, "list": list_obj, "count": count},
    )
```

> Note: The exact implementation may vary. The key is returning an OOB swap with the updated count, similar to how `toggle_todo` handles it.

---

## Bug 4: Overdue Styling Wrong

**File:** `todo-app/src/app/utils.py` — `is_overdue` and `is_due_today` functions

**Problem:** Comparing full `datetime` objects (with time) instead of just dates.

- `is_overdue`: `todo.due_date < now` — a todo due today at midnight is "overdue" at 1am
- `is_due_today`: `todo.due_date == now` — exact datetime match is essentially impossible

**Fix:** Compare `.date()` parts only:

```python
def is_overdue(todo: "Todo") -> bool:
    """Return True if due_date < today AND not completed."""
    if todo.is_completed or not todo.due_date:
        return False
    today = date.today()
    return todo.due_date.date() < today


def is_due_today(todo: "Todo") -> bool:
    """Return True if due_date == today."""
    if not todo.due_date:
        return False
    today = date.today()
    return todo.due_date.date() == today
```

---

## Bug 5: Silent Data Loss on Due Date Clearing

**File:** `todo-app/src/app/routes/todos.py` — `update_todo` function

**Problem:** When a user clears the due date field, the browser sends `due_date=""` (empty string). The `except ValueError: pass` block catches the parse failure on an empty string and silently does nothing — the existing due date is never cleared.

Result: once a due date is set on a todo, it can never be removed.

**Why Claude misses it:** Claude focuses on fixing the date format parsing (the presented symptom in Bug 2) and doesn't test the "clear" case. The `except ValueError: pass` pattern looks like correct defensive error handling, so it passes a superficial review. The regression is only visible by testing the clear action after applying the Bug 2 fix.

**Fix:** Check for empty string before attempting to parse:

```python
if due_date == "":
    todo.due_date = None
elif due_date:
    todo.due_date = datetime.strptime(due_date, "%Y-%m-%d")
```

**Failure pattern:** Plausible-but-wrong (pattern #8). The fix for Bug 2 is correct for the presented symptom, but incomplete — it doesn't handle the related clearing case. The `except ValueError: pass` makes the incompleteness invisible.

**Teaching point:** This is the 29.6% stat made concrete. Claude's fix for Bug 2 is syntactically correct, passes the existing tests, and addresses the stated problem. It still introduces a regression for a case that was never explicitly described. Review is not optional.
