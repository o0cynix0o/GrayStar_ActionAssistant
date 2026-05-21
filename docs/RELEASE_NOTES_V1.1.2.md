# Grey Star Action Assistant v1.1.2 Release Notes

This release is a polish pass for the first public build: cleaner card controls, better player-facing help, and a smoother potion/combat workflow.

## Added

- Collapsible assistant cards. Use the triangle on a card to shrink it to a one-line title without fully closing it.
- Persistent collapsed-card preferences, saved with the rest of the UI layout.
- Guided Karmo Potion support: use the potion, apply the Book 2 side-effect roll, and finish the potion after combat.
- More visible item-use buttons for supported potions, herbs, meals, and item flags.
- Expanded user FAQ covering startup, cards, potions, combat fields, death recovery, saves, achievements, and audit oddities.

## Changed

- Closed-card restore behavior now lives in Settings instead of cluttering the assistant menu.
- Card close buttons now hide the selected card immediately and can be restored from Settings.
- Landing page branding now reads Grey Star Action Assistant.
- The landing tagline is more story-flavored and less technical.
- Project Aon book download guidance is now linked from the README, install guide, local install page, and wiki.

## Fixed

- Closed cards not actually disappearing when selected.
- Closed tabs/cards missing from the Settings restore list.
- Karmo Potion usability from the Herb Pouch.
- Small GUI polish around card controls and card menu spacing.

## Notes

The release package still does not include Project Aon book files. Download the standard Grey Star HTML ZIPs directly from Project Aon for personal use, then extract them into `books\gs`.

## Verified

- Python compile check passed.
- Release package guard confirms `books/gs` is not tracked.
- Book 1 playtest: 26 passed, 0 warnings, 0 failures.
- Book 2 playtest: 20 passed, 0 warnings, 0 failures.
- Book 3 playtest: 23 passed, 0 warnings, 0 failures.
- Book 4 playtest: 24 passed, 0 warnings, 0 failures.
- Campaign story run: 11 passed, 0 warnings, 0 failures.
- Achievement 100% run: 7 passed, 0 warnings, 0 failures.
