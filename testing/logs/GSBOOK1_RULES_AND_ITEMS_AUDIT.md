# GS Book 1 Rules And Items Audit

Book: Grey Star the Wizard

Status: Step 1 starter audit. Machine sweep is complete; human confirmation begins at front matter and section 1.

Pass 1 baseline:

- `GSBOOK1_PASS1_RULES_BASELINE.md` now records the confirmed setup, inventory, Willpower, Staff, combat, errata, and section 1 findings.
- `powers.htm`, `sage.htm`, and `crsumary.htm` were added to the support-page pass after the starter sweep because they are material to Grey Star rules.

## Source And Support Pages

| File | Exists | Title | Cue Categories |
|---|---|---|---|
| `title.htm` | True | Grey Star the Wizard: Title Page | combat, magick_check |
| `gamerulz.htm` | True | Grey Star the Wizard: The Game Rules | combat, ending, inventory, random, state_gain, state_loss, willpower |
| `powers.htm` | True | Grey Star the Wizard: Magical Powers | combat, inventory, magick_check, state_loss, willpower |
| `equipmnt.htm` | True | Grey Star the Wizard: Equipment | combat, inventory, magick_check, state_loss, willpower |
| `action.htm` | True | Grey Star the Wizard: Action Chart | None |
| `cmbtrulz.htm` | True | Grey Star the Wizard: Rules for Combat | combat, inventory, magick_check, random, state_loss, willpower |
| `crsumary.htm` | True | Grey Star the Wizard: Combat Rules Summary | combat, random, state_loss, willpower |
| `crtable.htm` | True | Grey Star the Wizard: Combat Results Table | combat |
| `random.htm` | True | Grey Star the Wizard: Random Number Table | random |
| `sage.htm` | True | Grey Star the Wizard: Sage Advice | ending, inventory, willpower |
| `footnotz.htm` | True | Grey Star the Wizard: Footnotes | combat, ending, inventory, magick_check, state_gain, state_loss, willpower |
| `errata.htm` | True | Grey Star the Wizard: Errata | combat, inventory, magick_check, random, state_gain, willpower |
| `coming.htm` | True | Grey Star the Wizard: Of the Coming of Grey Star | inventory |
| `toc.htm` | True | Grey Star the Wizard: | combat, random |

## Step 1 Starting Notes

- `title.htm` confirms the audit target as Book 1, Grey Star the Wizard.
- `sect1.htm` is the opening section and branches to sections 202 and 168.
- Section 1 is confirmed as a Magick-gated route choice for Elementalism. No state change is confirmed at section 1.
- Rules support pages must be read before finalizing startup equipment, Magick selection, Willpower behavior, and staff combat assumptions.

## Candidate Section Groups

### inventory

1, 3, 4, 5, 11, 18, 19, 22, 23, 25, 27, 30, 32, 36, 37, 38, 41, 42, 43, 45, 46, 48, 49, 51, 52, 55, 57, 58, 59, 60, 63, 66, 73, 74, 76, 78, 80, 83, 84, 87, 90, 91, 94, 98, 99, 100, 101, 111, 112, 114, 115, 117, 123, 125, 128, 132, 133, 136, 137, 142, 146, 147, 150, 151, 161, 164, 167, 168, 170, 172, 173, 178, 179, 183, 185, 190, 193, 198, 204, 206 ... (+47)

### willpower

4, 5, 11, 12, 15, 19, 22, 30, 31, 38, 46, 48, 49, 52, 53, 56, 57, 58, 59, 64, 66, 70, 76, 78, 81, 84, 85, 87, 88, 91, 92, 94, 95, 96, 98, 101, 102, 107, 109, 111, 114, 115, 116, 117, 120, 123, 124, 132, 139, 143, 149, 150, 158, 159, 162, 165, 172, 175, 179, 181, 183, 185, 191, 193, 201, 202, 204, 211, 215, 226, 229, 235, 236, 239, 242, 248, 254, 257, 259, 265 ... (+19)

### state_loss

2, 3, 5, 6, 42, 47, 52, 56, 59, 66, 68, 74, 78, 79, 97, 102, 104, 118, 150, 153, 162, 165, 168, 187, 196, 202, 210, 256, 259, 268, 270, 272, 281, 283, 287, 293, 295, 297, 298, 303, 308, 314, 319, 323, 328, 329, 341, 342, 343

### state_gain

15, 36, 38, 49, 85, 88, 99, 109, 161, 183, 189, 195, 199, 201, 203, 205, 226, 242, 243, 245, 259, 270, 303, 308, 309

### magick_check

1, 3, 10, 18, 19, 22, 23, 34, 38, 40, 42, 43, 49, 53, 54, 55, 56, 58, 70, 73, 74, 82, 87, 90, 91, 92, 95, 98, 101, 105, 112, 114, 116, 124, 128, 136, 137, 142, 149, 150, 151, 153, 157, 159, 161, 170, 172, 175, 176, 178, 187, 191, 193, 199, 200, 211, 214, 215, 221, 251, 275, 278, 280, 286, 292, 305, 332, 338, 350

### random

49, 286

### combat

2, 3, 5, 6, 9, 12, 15, 30, 38, 43, 47, 50, 57, 58, 59, 66, 68, 78, 79, 85, 88, 94, 96, 99, 101, 107, 109, 117, 118, 119, 120, 128, 133, 143, 148, 149, 150, 154, 161, 165, 168, 172, 183, 189, 193, 197, 201, 203, 204, 205, 210, 215, 224, 226, 229, 231, 242, 243, 244, 246, 248, 255, 256, 257, 259, 260, 265, 266, 268, 270, 272, 279, 281, 283, 284, 287, 293, 294, 295, 298 ... (+17)

### ending

14, 17, 31, 44, 67, 69, 155, 216, 220, 237, 271, 310, 312

## Starter Findings

- Book 1 has all expected 350 section files present.
- Support pages and errata are present locally.
- The sweep found many Willpower and inventory references, so Book 1 likely needs more than generic manual controls to feel complete.
- Sections 110 and 342 have no incoming section links in the initial parser output and need human route verification. Section 110 is footnote-linked from section 264; section 342 may be reached by a nonstandard reference or parser gap.
