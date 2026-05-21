# Grey Star Action Assistant

Grey Star Action Assistant is a local browser-based play aid for the four *Grey Star* gamebooks. It pairs the Project Aon book text with a companion assistant that handles character bookkeeping, section support, combat tracking, saves, achievements, and strategy-guide material.

The app is built to run locally from your machine. It does not require a hosted account or cloud save service.

Current public release: **v1.1.0**

## What It Includes

- Complete support for Books 1-4.
- Split view with the book reader on the left and the assistant on the right.
- Character sheet with Endurance, Willpower, Combat Skill, Nobles, Magicks, and completed books.
- Inventory tracking for Weapons, Backpack Items, Special Items, Herb Pouch items, and stored/confiscated gear.
- Audited section helpers for book effects, rolls, loot, Willpower costs, gear loss/return, and book completion.
- Grey Star combat tracking with Staff use, modifiers, evasion, death handling, repeat/rewind recovery, and combat history.
- Achievements with unlock notifications and replay support.
- Save export, save import, and full save backup.
- Persistent card layout and size preferences.
- Three play modes: Auto, Manual, and CLI.
- Player-facing wiki and strategy guides.

## Quick Start

Install dependencies from the project folder:

```powershell
python -m pip install -r .\requirements.txt
```

Start the app:

```powershell
.\Launch-GreyStar.ps1
```

Or:

```powershell
python .\launch_greystar.py
```

Then open:

```text
http://localhost:8797/assistant.html
```

Use the `localhost` page. Opening `assistant.html` directly from the file system can make the book pane load while leaving the assistant disconnected.

## Play Modes

Use the small white dot in the upper-right of the assistant panel to switch modes.

- **Auto Mode** is the normal helper mode. Section effects, section-aware rolls, loot helpers, combat presets, saves, death recovery, and achievements are available.
- **Manual Mode** keeps the sheet, saves, inventory, notes, and achievements, but disables audited section automation. Use it when you want to do the book math yourself.
- **CLI Mode** replaces the normal assistant body with the terminal assistant inside the web page. It uses the same save data as the web GUI.

Default ports:

- Library and web app: `http://localhost:8797`
- Embedded CLI bridge: `ws://localhost:8798`

## Basic Play Flow

1. Start the app from PowerShell.
2. Open the assistant page from `localhost`.
3. Create or load a Grey Star character.
4. Read the book in the left pane.
5. Click book section links normally; the assistant follows your current section.
6. Use the assistant panels for inventory, stats, combat, rolls, notes, saves, and achievements.
7. When a book ends, use the completion screen to continue, repeat the book, or review the summary.

## Saves And Backups

Use the **Saves** tab for:

- **Export Current Save**: download the current character as JSON.
- **Import Selected Save**: load an exported save into this install.
- **Backup All Saves**: download every local save in one ZIP.

Runtime save data is intentionally local and ignored by git:

- `saves/`
- `current-position.json`
- `data/last-save.txt`
- `data/ui-preferences.json`

## Documentation

Project docs live in `docs/`.

Useful starting points:

- `docs/PUBLIC_RELEASE_CHECKLIST.md`
- `docs/BOOK_AUDIT_WORKFLOW.md`
- `docs/BOOK_SOURCE_MAP.md`
- `docs/RELEASE_NOTES_V1.1.0.md`

Wiki source pages live in `docs/wiki/` and are mirrored to the GitHub wiki. Player-facing pages include:

- Getting Started
- Game Modes
- Combat Guide
- Inventory and Item Rules
- Book 1-4 Strategy Guides
- Full Campaign Story Run
- Achievement 100 Percent Guide

## Testing

Run the release checks from the project folder:

```powershell
python -m py_compile app_server.py greystar.py launch_greystar.py ws_server.py
python .\testing\playtest_book1.py
python .\testing\playtest_book2.py
python .\testing\playtest_book3.py
python .\testing\playtest_book4.py
python .\testing\playtest_campaign.py
```

The playtest reports are written to `testing/logs/`.

## Release Package

Create a release ZIP from the current git commit:

```powershell
.\tools\Make-Release.ps1
```

The ZIP is written to `dist/`. Runtime saves, UI preferences, and other local files are not included.

## Project Layout

- `assistant.html`: web assistant UI.
- `index.html`: local book library entry page.
- `app_server.py`: HTTP server and JSON API for the web assistant.
- `greystar.py`: terminal assistant and shared Grey Star rules logic.
- `greystar.ps1`: PowerShell entry point for the terminal assistant.
- `ws_server.py`: WebSocket bridge for embedded CLI mode.
- `launch_greystar.py`: Python launcher for the web app and CLI bridge.
- `Launch-GreyStar.ps1`: Windows convenience launcher.
- `books/gs/`: bundled Project Aon Grey Star book HTML.
- `data/crt.json`: Combat Results Table.
- `testing/`: route, automation, combat, campaign, and achievement checks.
- `tools/Make-Release.ps1`: release ZIP builder.

## Notice

This is an unofficial local play aid. The bundled book HTML files are Project Aon editions and retain their original copyright notices and links inside the book pages. See `NOTICE.md`.
