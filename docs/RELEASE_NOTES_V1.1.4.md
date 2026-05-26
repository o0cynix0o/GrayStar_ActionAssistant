# Grey Star Action Assistant v1.1.4 Release Notes

This release tightens the play surface around route math, Manual Mode advice, local map support, and safer browser startup.

## Added

- Choices-card route checks for audited branch math such as `CS + WP`, `END + WP`, current-stat thresholds, and final-score checks.
- A data-driven route-check file so future book audits can add route math without custom UI code.
- Route-check support in the terminal `choices` view.
- A Map card on the Sheet dashboard using the local Project Aon Book 1 map when the book files are installed.
- Manual Mode advice receipts for section effects, rolls, loot, Willpower costs, combat presets, and combat auto-resolve.
- A Nobles control panel on the Inventory tab so Manual Mode advice has a real place to point for Noble changes.
- Direct `file:///` loading protection for `assistant.html`, with a clear localhost startup message.

## Changed

- The Choices card now includes route checks alongside loot, Willpower costs, combat presets, status flags, and section rolls.
- The book audit workflow now requires a route-check pass for stat math, thresholds, and roll-plus-stat branches.
- The PowerShell launcher no longer uses PowerShell's automatic `$args` variable for launcher arguments.
- The old GUI work planning file was removed after the GUI work moved into the app and docs.

## Notes

Some route checks intentionally wait until a section effect is applied first. If the book says to lose 3 Willpower and then check `WP + END`, the assistant asks you to apply or record that loss before it highlights the legal route.

Project Aon book files are still not included in the release package.

## Verified

- JSON validation passed for `data/book-route-checks.json`.
- Python compile check passed.
- Route-check probes passed for Book 2 section 18, Book 3 section 247, and Book 4 section 310.
- Entry-effect-gated route check passed for Book 2 section 169.
- Headless Chrome smoke test loaded the assistant and reported no JavaScript exceptions.
- Book 1 playtest: 26 passed, 0 warnings, 0 failures.
- Book 2 playtest: 20 passed, 0 warnings, 0 failures.
- Book 3 playtest: 23 passed, 0 warnings, 0 failures.
- Book 4 playtest: 24 passed, 0 warnings, 0 failures.
- Campaign story run: 11 passed, 0 warnings, 0 failures.
- Achievement 100% run: 7 passed, 0 warnings, 0 failures.
