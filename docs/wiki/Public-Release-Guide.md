# Public Release Guide

This is the short version for a fresh install.

## Start

From the project folder:

```powershell
.\Launch-GreyStar.ps1
```

Then open:

```text
http://localhost:8797/assistant.html
```

## Keep Your Progress Safe

The app autosaves during play. You can also use the **Saves** tab for three useful release-ready tools:

- **Export Current Save** downloads the current character as one JSON file.
- **Backup All Saves** downloads a ZIP of your local save files and UI layout preferences.
- **Import Selected Save** loads a previously exported save JSON into this installation.

Use **Backup All Saves** before moving the app to another folder or computer.

## UI Layouts

Card sizes, card order, and closed cards are stored in `data/ui-preferences.json`. They should survive server restarts. If the layout gets strange, open **Settings** and use **Reset All Card Layouts**.

## Package A Release

For maintainers:

```powershell
.\tools\Make-Release.ps1
```

The release ZIP appears in `dist/`. It contains the app and docs, not personal saves.

## Credits Note

The included book pages are Project Aon editions and keep their original copyright notices and Project Aon links in the HTML. The assistant is an unofficial local companion for playing those books.
