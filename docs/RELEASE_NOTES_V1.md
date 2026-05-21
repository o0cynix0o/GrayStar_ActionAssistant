# Grey Star Action Assistant v1 Release Notes

This first public release supports all four Grey Star books.

## Included

- Local browser-based reader and assistant.
- Book 1 through Book 4 section support.
- Character sheet, inventory, Magicks, notes, saves, and achievements.
- Section automation for audited rules, loot, rolls, combat starts, gear loss, and gear return.
- Lone Wolf-style tracked combat adapted for Grey Star rulings.
- Death recovery with Repeat and Rewind.
- Book completion, continue-to-next-book, and repeat-book flow.
- Achievement notifications and completionist support.
- Strategy guide pages and full campaign/achievement playtest guides.
- Persistent card layout preferences.
- Save export, save import, and all-saves backup.

## Local Data

The following are intentionally local and ignored by git:

- `saves/`
- `current-position.json`
- `data/last-save.txt`
- `data/ui-preferences.json`

## Known Notes

- Start the app through `localhost`; opening `assistant.html` directly as a file will not connect the assistant to the server.
- Autosave is always on.
- Book rules override assistant convenience behavior.
