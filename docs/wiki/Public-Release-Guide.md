# Public Release Guide

This is the short version for a fresh install.

## Start

From the project folder:

```powershell
.\Launch-GreyStar.ps1
```

Then open:

```text
http://127.0.0.1:8897/assistant.html
```

## Install The Books

The release ZIP does not include Project Aon book files.

Download the standard Grey Star HTML ZIPs from Project Aon for personal use, then extract them into `books\gs`.

Use the local guide page:

```text
http://127.0.0.1:8897/install-books.html
```

Or read:

```text
docs\INSTALL_PROJECT_AON_BOOKS.md
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

The release ZIP appears in `dist/`. It contains the app and docs, not personal saves and not Project Aon book files.

## Credits Note

Project Aon provides the Grey Star Internet Editions from its own site. This assistant is an unofficial local companion for playing those books after the user has downloaded them for personal use.
