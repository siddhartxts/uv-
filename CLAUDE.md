# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

**neway** is a Python 3.12 web service project using FastAPI and Flask. The project is in early stages with minimal implementation.

## Development Setup

### Initial Setup
```bash
# Install dependencies using uv (UV package manager is faster than pip)
uv sync

# Activate the virtual environment
source .venv/bin/activate
```

### Environment
- Python version: 3.12 (see `.python-version`)
- Package manager: uv (see `uv.lock` for lock file)
- Virtual environment: `.venv/`

## Running the Project

```bash
# Run the main script
python main.py

# If running a web service (FastAPI/Flask server):
# uvicorn main:app --reload  # For FastAPI
# python -m flask run        # For Flask (if configured)
```

## Common Commands

```bash
# Install/update dependencies
uv add <package_name>      # Add a new dependency
uv sync                    # Sync dependencies from pyproject.toml
uv pip install <package>   # Direct pip-style install if needed

# Development
python main.py             # Run main script
python -m pytest           # Run tests (once test suite is added)
python -m mypy .           # Type checking (if mypy is added)
```

## Project Structure

- `main.py` — Entry point for the application
- `pyproject.toml` — Project metadata and dependency declarations
- `uv.lock` — Locked dependency versions (auto-generated)
- `.python-version` — Python version specification (3.12)
- `skills/` — Custom Claude Code skills directory
  - `git-quick-commit/` — Skill for quick git commits (structure prepared, agents not yet implemented)
- `.venv/` — Python virtual environment (created by `uv sync`)

## Development Notes

- The project uses **uv** for dependency management, which is significantly faster than traditional pip. Always use `uv` commands for package operations.
- Dependencies are defined in `pyproject.toml`; the lock file (`uv.lock`) should be committed to version control.
- As the project develops with FastAPI and/or Flask, ensure:
  - Routes are well-structured and documented
  - Environment variables are managed appropriately (use `.env` files with python-dotenv if needed)
  - Database models and migrations are set up (if applicable)
  - Error handling and validation are implemented at API boundaries
