# Grey Star Action Assistant

Grey Star Action Assistant is a local browser-based play aid for the four *Grey Star* gamebooks. It pairs locally installed Project Aon book files with a companion assistant that handles character bookkeeping, section support, combat tracking, saves, achievements, and strategy-guide material.

The app is built to run locally from your machine. It does not require a hosted account or cloud save service.

Current public release: **v1.1.2**

## Book Files Are Not Included

This project does **not** redistribute the Grey Star book HTML files. Project Aon provides the Internet Editions for personal use from its own site, and their license does not allow this release package to include or redistribute the books.

After downloading the app, download the standard Grey Star HTML ZIPs directly from Project Aon and extract them into `books\gs`.

Full walkthrough:

- `docs/INSTALL_PROJECT_AON_BOOKS.md`
- local app page: `http://localhost:8797/install-books.html`

Project Aon links:

- License: https://www.projectaon.org/en/Main/License
- Grey Star the Wizard: https://www.projectaon.org/en/Main/GreyStarTheWizard
- The Forbidden City: https://www.projectaon.org/en/Main/TheForbiddenCity
- Beyond the Nightmare Gate: https://www.projectaon.org/en/Main/BeyondTheNightmareGate
- War of the Wizards: https://www.projectaon.org/en/Main/WarOfTheWizards

Use the **standard** multi-page HTML ZIPs:

| Book | Standard ZIP |
| --- | --- |
| 1. Grey Star the Wizard | https://www.projectaon.org/en/xhtml/gs/01gstw/01gstw.zip |
| 2. The Forbidden City | https://www.projectaon.org/en/xhtml/gs/02tfc/02tfc.zip |
| 3. Beyond the Nightmare Gate | https://www.projectaon.org/en/xhtml/gs/03btng/03btng.zip |
| 4. War of the Wizards | https://www.projectaon.org/en/xhtml/gs/04wotw/04wotw.zip |

Extract those ZIPs into:

```text
books\gs
```

After extraction, these files should exist:

```text
books\gs\01gstw\title.htm
books\gs\02tfc\title.htm
books\gs\03btng\title.htm
books\gs\04wotw\title.htm
```

PowerShell example from the project folder:

```powershell
New-Item -ItemType Directory -Force .\books\gs

Expand-Archive "$env:USERPROFILE\Downloads\01gstw.zip" -DestinationPath .\books\gs -Force
Expand-Archive "$env:USERPROFILE\Downloads\02tfc.zip"  -DestinationPath .\books\gs -Force
Expand-Archive "$env:USERPROFILE\Downloads\03btng.zip" -DestinationPath .\books\gs -Force
Expand-Archive "$env:USERPROFILE\Downloads\04wotw.zip" -DestinationPath .\books\gs -Force
```

## What It Includes

- Complete support for Books 1-4.
- Split view with the book reader on the left and the assistant on the right, once the Project Aon book files are installed locally.
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

If this is a fresh release install, open the book install guide first:

```text
http://localhost:8797/install-books.html
```

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
- `docs/INSTALL_PROJECT_AON_BOOKS.md`
- `docs/BOOK_AUDIT_WORKFLOW.md`
- `docs/BOOK_SOURCE_MAP.md`
- `docs/RELEASE_NOTES_V1.1.2.md`

Wiki source pages live in `docs/wiki/` and are mirrored to the GitHub wiki. Player-facing pages include:

- Getting Started
- Game Modes
- Combat Guide
- Inventory and Item Rules
- FAQ
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
- `books/`: local book install folder. Project Aon book files go under `books/gs/` but are ignored by git and not included in release ZIPs.
- `data/crt.json`: Combat Results Table.
- `testing/`: route, automation, combat, campaign, and achievement checks.
- `tools/Make-Release.ps1`: release ZIP builder.

## Notice

This is an unofficial local play aid. It does not redistribute the Grey Star books. Users download the Project Aon Internet Editions directly from Project Aon for personal use. See `NOTICE.md`.
