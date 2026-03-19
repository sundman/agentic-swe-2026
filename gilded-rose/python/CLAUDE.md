# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Commands

```bash
# Run all tests
uv run pytest tests/ -v

# Run a single test
uv run pytest tests/test_gilded_rose.py::GildedRoseTest::test_foo -v

# Run approval tests only
uv run pytest tests/test_gilded_rose_approvals.py -v

# Run the text fixture (simulate N days)
uv run python texttest_fixture.py 10
```

## Architecture

This is the Gilded Rose refactoring kata. The codebase has two files:

- **`gilded_rose.py`** — contains `GildedRose` (shop logic) and `Item` (data class). `Item` must **not** be modified (goblin owns it). Only `GildedRose.update_quality()` should be refactored.
- **`texttest_fixture.py`** — runs the shop for N days with a fixed set of items; used as the approval test input.

### Item update rules

| Item | Behavior |
|------|----------|
| Normal | quality decreases by 1/day; by 2 after sell_in < 0 |
| Aged Brie | quality increases by 1/day; by 2 after sell_in < 0 |
| Sulfuras | never changes (quality always 80, sell_in never decrements) |
| Backstage passes | +1 quality normally, +2 when sell_in ≤ 10, +3 when sell_in ≤ 5, drops to 0 after concert |
| Conjured (to implement) | degrades twice as fast as normal items |

Quality is always clamped 0–50 (except Sulfuras = 80).

### Tests

- **`tests/test_gilded_rose.py`** — unit tests (the initial `test_foo` is intentionally broken as a starting point).
- **`tests/test_gilded_rose_approvals.py`** — approval test using `approvaltests` library; runs `texttest_fixture.py` for 30 days and compares against `tests/approved_files/test_gilded_rose_approvals.test_gilded_rose_approvals.approved.txt`. To update the approved file after intentional changes, rename the `.received.txt` file.
