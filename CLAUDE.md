# Agentic Software Engineering Workshop 2026

## Project Overview

Educational workshop repository for learning AI-assisted software development with Claude Code.
Contains a full-stack todo application (Python/FastAPI/HTMX) used as the learning vehicle,
plus a Gilded Rose refactoring kata for warmup exercises.

## Tech Stack

- **Backend**: Python 3.11+, FastAPI, SQLAlchemy, SQLite
- **Frontend**: HTMX, Shoelace Web Components, Jinja2 templates
- **Package Manager**: uv (Astral)
- **Testing**: pytest with httpx

## Key Commands

```bash
# Todo app
cd todo-app && uv run uvicorn app.main:app --reload    # Start dev server (port 8000)
cd todo-app && uv run pytest tests/ -v                  # Run tests

# Gilded Rose
cd gilded-rose/python && uv run pytest tests/ -v          # Run tests
```

## Project Structure

```
├── docs/                           # Exercises, reference cards, guidelines
│   ├── exercises/                  # Workshop exercises
│   │   ├── warmup/                 # Gilded Rose kata
│   │   ├── part-1-fundamentals/    # Exercises 1-4 (Phase 1: Guided Foundations)
│   │   ├── part-2-intermediate/    # Labs A-E (Phase 2: Theme Labs)
│   │   ├── part-3-advanced/        # Challenges A-D (Phase 3: Open Challenges)
│   │   └── templates/              # Lab and challenge format templates
│   ├── reference/                  # Quick-reference cards (WISC, PIV loop, failure patterns, etc.)
│   ├── rules/                      # Development guidelines
│   ├── todo-app-requirements/      # App specifications
│   └── misc/                       # Tips and references
│
├── gen-image/                      # Image generation CLI (exercise)
│
├── gilded-rose/                    # Refactoring kata (warmup)
│
└── todo-app/                       # Full-stack todo application
    ├── src/app/                    # FastAPI application
    │   ├── main.py                 # App entry point
    │   ├── database.py             # SQLAlchemy models
    │   ├── utils.py                # Shared utilities
    │   ├── core/deps.py            # Auth dependencies
    │   ├── routes/                 # API endpoints
    │   ├── templates/              # Jinja2 HTML templates
    │   └── static/                 # CSS, JS, images
    └── tests/                      # Test suite
```

## Credentials

Demo login: `demo@example.com` / `demo123`


## Workflow Rules, Guardrails and Guidelines

### Foundational Rules and Guardrails
_Always fully read and understand this file before doing any work:_ @docs/rules/CRITICAL-RULES-AND-GUARDRAILS.md


### Foundational Development Guidelines and Standards
**Always read** relevant guidelines below as _needed_, based on the type of work being done. Review what guidelines are relevant to the task at hand before starting any work that involves coding, code exploration, architecture and solution design, UX/UI, code review, etc.

* docs/rules/DEVELOPMENT-ARCHITECTURE-GUIDELINES.md – when doing development work (coding, architecture, etc.)
* docs/rules/UX-UI-GUIDELINES.md – when doing UX/UI related work
* docs/rules/WEB-DEV-GUIDELINES.md – when doing web development work


## MCP Servers

- **Context7**: Documentation lookup — use for FastAPI, SQLAlchemy, HTMX, Shoelace docs
- **Fetch**: Download web content as markdown
