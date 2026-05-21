# Grey Star Assistant

This is a standalone Python web app fork of the local Lone Wolf assistant for the four Grey Star books.

It supports the full four-book Grey Star set, including book flow, section automation, combat, achievements, saves, and player-facing strategy documentation.

## Run

```powershell
python .\launch_greystar.py
```

On Windows, this convenience wrapper also works:

```powershell
.\Launch-GreyStar.ps1
```

The main reader opens the book on the left and a web GUI assistant on the right. Clicking book section links updates the assistant state, and using the section controls updates the book frame.

The assistant has button-driven screens for Sheet, Inventory, Magicks, Sections, Combat, Saves, and Notes. The older CLI assistant is still available by running `greystar.py` directly.

Default ports:

- Library: `http://localhost:8797`
- Web app/API: `http://localhost:8797`

## Files

- `greystar.py`: Python Grey Star rules assistant
- `app_server.py`: Python HTTP server for the web app and JSON API
- `ws_server.py`: legacy Python WebSocket terminal bridge
- `launch_greystar.py`: Python launcher for the web app server
- `books/gs`: copied Grey Star books
- `saves`: runtime-created character saves; ignored by git so local play state stays private
- `data/ui-preferences.json`: runtime-created UI layout preferences; ignored by git
- `tools/Make-Release.ps1`: creates a public release ZIP from the current git commit
- `data/crt.json`: Combat Results Table

## Saves And Backups

Use the Saves tab in the web assistant for:

- Export Current Save
- Import Selected Save
- Backup All Saves

These are the safest way to move a character between installs or make a copy before a replay.

## Release Package

From the project folder:

```powershell
.\tools\Make-Release.ps1
```

The ZIP is created in `dist/`. Local saves and UI preference files are not included.

Before publishing, run through `docs/PUBLIC_RELEASE_CHECKLIST.md`.

## Notice

This is an unofficial local play aid. The bundled book HTML files are Project Aon editions and retain their original copyright notices and links inside the book pages. See `NOTICE.md`.

## Dependencies

```powershell
python -m pip install -r .\requirements.txt
```

`pywinpty` is only needed for the legacy browser terminal bridge. The assistant itself can also be run directly:

```powershell
python .\greystar.py
```
