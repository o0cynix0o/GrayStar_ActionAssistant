# Campaign Story Run

Generated: 2026-05-22T08:05:51

## Summary

- Passed: 11
- Warnings: 0
- Failures: 0
- Scope: brand-new character creation, Book 1 to Book 4 flow, same-character handoffs, completion screens, and final campaign state.
- Save safety: dry-run only; the live save pointer is not touched.

## Character Creation

- Name: QA Story Grey Star
- Starting book: 1
- Deterministic rolls: CS +9, WP +9, END +9
- Starting sheet: CS 19, END 29/29, WP 29
- Lesser Magicks chosen: Sorcery, Enchantment, Elementalism, Alchemy, Prophecy
- Shianti gift: Jewelled Dagger

## Book Flow

- Book 1 (Grey Star the Wizard): 141 route stops, ended at section 350, completed=True, END 13/29, WP 0.
- Book 2 (The Forbidden City): 63 route stops, ended at section 310, completed=True, END 2/29, WP -5.
- Book 3 (Beyond the Nightmare Gate): 58 route stops, ended at section 350, completed=True, END 12/29, WP 38.
- Book 4 (War of the Wizards): 45 route stops, ended at section 360, completed=True, END 58/59, WP 93.

## Final State

- Character: QA Story Grey Star
- Current book: 4
- Current section: 360
- Completed books: 1, 2, 3, 4
- Achievements unlocked during story run: 51/102
- Active death state: False

## Passed

- Fresh character creation produced the expected deterministic Book 1 sheet.
- Story run completed Book 1: Grey Star the Wizard.
- Continue flow advanced from Book 1 to Book 2.
- Story run completed Book 2: The Forbidden City.
- Continue flow advanced from Book 2 to Book 3.
- Story run completed Book 3: Beyond the Nightmare Gate.
- Continue flow advanced from Book 3 to Book 4.
- Story run completed Book 4: War of the Wizards.
- The same character name was preserved through the whole campaign.
- CompletedBooks contains all four books at the end of the story run.
- No active death or failed-mission state remained after the story run.

## Warnings

- None

## Failures

- None
