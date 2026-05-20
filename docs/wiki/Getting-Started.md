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
.\Launch-GrayStar.ps1
```

Or:

```powershell
python .\launch_graystar.py
```

Then open:

```text
http://localhost:8797/assistant.html
```

## Basic Play Flow

1. Start the local server.
2. Open the assistant page from `localhost`.
3. Create or load your Gray Star character.
4. Read the book in the left pane.
5. Use the assistant on the right for inventory, stats, combat, rolls, notes, saves, and achievements.
6. Click book section links normally. The assistant follows your current section.
7. Use the assistant panels when the book calls for inventory changes, stat changes, rolls, combat, notes, or saves.

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
