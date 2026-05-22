# Grey Star Action Assistant v1.1.3 Release Notes

This release adds expandable notification receipts to the web assistant, making the app more transparent about what it just changed and why.

## Added

- Expandable bottom-bar receipts for section automation, item use, Karmo controls, loot choices, combat actions, death recovery, book completion, achievements, rolls, and assistant notices.
- Before/after detail rows for common state changes such as Endurance, Willpower, Combat Skill, Nobles, inventory, position, and important automation flags.
- Combat receipts that show round number, roll, ratio, END loss, Staff WP spend, and current combat totals.
- Death recovery receipts that explain Repeat vs Rewind and show the restored checkpoint.
- Documentation for the receipt drawer in the README and wiki FAQ.

## Changed

- Achievement unlock toasts still appear, but they no longer overwrite the bottom notification text. Achievement details are now folded into the receipt for the action that caused them.
- Manual Mode blocked-action messages now use the same expandable receipt system.
- Save-import warnings and connection errors now use receipts instead of plain text.

## Notes

The receipt drawer is intentionally brief until clicked. The collapsed line stays out of the way during play, while the expanded view gives the "what changed, why, and how" explanation when you want to inspect it.

Project Aon book files are still not included in the release package.

## Verified

- Python compile check passed.
- Headless Chrome smoke test loaded the assistant, expanded a sample receipt, and reported no JavaScript exceptions.
- Release package guard confirms `books/gs` is not tracked.
- Book 1 playtest: 26 passed, 0 warnings, 0 failures.
- Book 2 playtest: 20 passed, 0 warnings, 0 failures.
- Book 3 playtest: 23 passed, 0 warnings, 0 failures.
- Book 4 playtest: 24 passed, 0 warnings, 0 failures.
- Campaign story run: 11 passed, 0 warnings, 0 failures.
- Achievement 100% run: 7 passed, 0 warnings, 0 failures.
