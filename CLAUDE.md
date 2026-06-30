# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

**neway** is a Python 3.12 command-line script that generates X (Twitter) posts from a topic using the DeepSeek API (via the OpenAI-compatible SDK). It's a learning project for building AI workflows.

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
# Requires a DeepSeek API key in .env (see https://platform.deepseek.com):
#   DEEPSEEK_API_KEY=sk-...
python main.py   # prompts for a topic, prints a generated post
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
- The DeepSeek API is OpenAI-compatible: the `openai` SDK is pointed at `base_url="https://api.deepseek.com"`. Use the Chat Completions API (`client.chat.completions.create`), not the Responses API.
- The API key is loaded from `.env` via `python-dotenv`; `.env` is gitignored and must not be committed.
