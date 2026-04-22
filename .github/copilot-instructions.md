# GitHub Copilot Workspace Instructions

## What this project is

This repository is a simple Telegram bot built with `aiogram`.
- `main.py` is the bot entrypoint and starts polling.
- `config_data/config.py` loads `BOT_TOKEN` and `ADMIN_IDS` from `.env` using `environs`.
- `handlers/handlers.py` defines `aiogram` router handlers for commands and button flows.
- `keyboards/` contains keyboard and markup helper functions.
- `lexicon/lexicon.py` stores message text and button labels.

## Key conventions

- Use `aiogram` router decorators in `handlers/handlers.py`.
- The bot is configured with `Bot`, `Dispatcher`, and `MemoryStorage` in `main.py`.
- Commands are mapped through `CommandStart`, `Command`, and `F.text` filters.
- Text content is centralized in `LEXICON` and `LEXICON_COMMANDS`.
- The `.env` file is expected at project root with variables `BOT_TOKEN` and `ADMIN_IDS`.

## How to run this project

1. Install dependencies.
2. Create `.env` with:
   - `BOT_TOKEN=<your telegram token>`
   - `ADMIN_IDS=123456789,987654321`
3. Run the bot with:
   - `python main.py`

## Useful files

- `main.py` — bot startup, logging, menu registration, router inclusion.
- `config_data/config.py` — configuration loader and dataclasses.
- `handlers/handlers.py` — Telegram message handlers and bot flow.
- `keyboards/kb_utils.py` — helper functions for creating keyboards.
- `keyboards/main_menu.py` — main menu setup.
- `lexicon/lexicon.py` — static bot text and button label definitions.

## What to edit here

- Update bot flow and commands in `handlers/handlers.py`.
- Add or change message text in `lexicon/lexicon.py`.
- Adjust keyboard layout in `keyboards/kb_utils.py` and `keyboards/main_menu.py`.
- Change environment config behavior in `config_data/config.py` if needed.

## Example Copilot prompts

- "Help me add a new `/info` command to this bot that sends a detailed info message."
- "Refactor `handlers/handlers.py` to avoid duplicate function names and improve handler clarity."
- "Explain how `main.py` initializes the bot and where I should add a new router."
- "Add a fallback handler for unknown text messages in `handlers/handlers.py`."

## Notes for AI assistance

- Prefer making minimal changes in the existing `aiogram` architecture.
- Keep user-facing strings in `lexicon/lexicon.py` rather than inline in handler code.
- Do not assume there is already a `README.md`; the repo currently has no project documentation.
