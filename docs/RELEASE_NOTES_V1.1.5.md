# Grey Star Action Assistant v1.1.5 Release Notes

This release fixes the Book 3 to Book 4 campaign handoff so the player chooses the Higher Magicks instead of the assistant filling them in silently.

## Fixed

- The Book 3 completion screen now shows a Higher Magicks picker when continuing into Book 4.
- The Book 4 handoff requires exactly five Higher Magicks before it advances.
- The backend now rejects missing, duplicate-short, or invalid Higher Magick handoff data instead of defaulting to the first five powers.
- The book receipt now includes the Higher Magicks selected for the Book 4 start.

## Notes

Book 4 begins with five Higher Magicks. That is a player choice, so the assistant now stops at the Book 3 ending and asks for those choices directly.

Project Aon book files are still not included in the release package.

## Verified

- Python compile check passed.
- Book 3 to Book 4 handoff rejects zero Higher Magicks.
- Book 3 to Book 4 handoff rejects four Higher Magicks.
- Book 3 to Book 4 handoff accepts exactly five Higher Magicks and preserves the selected list.
- The affected local campaign save was reset to Book 3 section 350 so the handoff can be replayed with the new picker.
