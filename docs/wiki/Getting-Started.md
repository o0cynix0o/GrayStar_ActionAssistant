# Getting Started

## Requirements

- Python 3
- A modern browser
- The project files from the repository

Install Python dependencies from the project folder:

```powershell
python -m pip install -r .\requirements.txt
```

## Start The App

From PowerShell:

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

## Basic Play Flow

1. Start the local server.
2. Open the assistant page from `localhost`.
3. Create or load your Grey Star character.
4. Read the book in the left pane.
5. Use the assistant on the right for inventory, stats, combat, rolls, notes, saves, and achievements.
6. Click book section links normally. The assistant follows your current section.
7. Use the assistant panels when the book calls for inventory changes, stat changes, rolls, combat, notes, or saves.

## Choose A Play Mode

Use the small white dot in the upper-right of the assistant panel to switch modes.

- **Auto** is the normal helper mode with section effects, roll helpers, loot helpers, combat presets, and achievements.
- **Manual** keeps the sheet and saves, but turns off the audited section helpers so you can handle the book math yourself.
- **CLI** opens the terminal assistant inside the web page and uses the same save data.

## Important Browser Note

Use the local server URL. Opening `assistant.html` directly as a file can make the book open but leave the assistant disconnected.

Correct:

```text
http://localhost:8797/assistant.html
```

Risky:

```text
opening assistant.html directly from the file system
```

## Autosave

The app autosaves state during normal play. This is intentional. It prevents the most frustrating failure mode: reaching a later section and discovering your sheet, inventory, or combat state is old.

## Moving Saves

Use the **Saves** tab if you need to move or protect your campaign:

- **Export Current Save** downloads the current character.
- **Backup All Saves** downloads every local save in one ZIP.
- **Import Selected Save** loads an exported save JSON into this installation.
