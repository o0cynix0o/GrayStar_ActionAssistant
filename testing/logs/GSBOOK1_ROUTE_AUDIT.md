# GS Book 1 Route Audit

Generated: 2026-05-20T15:33:09

Book: Grey Star the Wizard

Status: machine route-graph baseline plus first named route-family pass. Endpoint classifications and full dry-run branch coverage still need review.

## Summary

| Metric | Value |
|---|---|
| Expected sections | 350 |
| Existing section files | 350 |
| Missing section files | None |
| Source edges | 542 |
| Bad source links | None |
| Reachable from section 1 | 348/350 |
| Unreachable from section 1 | 110, 342 |
| No incoming links | 110, 342 |
| Endpoint sections | 29 |
| Branch points | 166 |
| Success-capable branch points | 166 |
| Detected success section | 350 |

## Shortest Success Path

- Length: 93 sections
- Path: 1, 202, 140, 280, 100, 121, 300, 289, 150, 348, 187, 230, 291, 178, 93, 258, 62, 36, 201, 172, 124, 333, 259, 296, 41, 349, 245, 292, 199, 31, 75, 3, 85, 18, 190, 21, 39, 55, 70, 156, 215, 2, 24, 10, 51, 102, 149, 165, 192, 276, 52, 227, 29, 54, 184, 325, 136, 61, 111, 266, 330, 256, 107, 307, 249, 282, 148, 49, 210, 74, 219, 294, 319, 43, 118, 268, 8, 19, 59, 65, ... (+13 more)

## Mandatory Success Chokepoints

These sections dominate the detected success endpoint in the source-link graph. They are route-graph chokepoints, not proof that every legal state can pass through them.

- Count: 43
- Sections: 1, 2, 3, 4, 8, 10, 18, 19, 24, 29, 39, 43, 52, 59, 61, 62, 65, 75, 136, 140, 146, 148, 149, 154, 165, 172, 178, 187, 192, 199, 215, 232, 249, 256, 266, 267, 276, 289, 291, 292, 294, 325, 350

## Opening Branches

| Branch | Reachable Sections | Can Reach Success | Reachable Endpoints | Early Merge Examples |
|---|---:|---|---|---|
| 1 -> 202 | 346 | yes | 9, 14, 17, 20, 63, 67, 69, 92, 103, 122, 138, 155, 173, 177, 207, 216, ... (+13 more) | 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17 |
| 1 -> 168 | 346 | yes | 9, 14, 17, 20, 63, 67, 69, 92, 103, 122, 138, 155, 173, 177, 207, 216, ... (+13 more) | 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17 |

## No-Incoming Review Notes

| Section | Route Audit Note |
|---:|---|
| 110 | Hidden correct riddle solution for section 264; the local source has no visible section link into it. |
| 342 | Footnote says no choice leads here and calls it an oversight. Earlier dry-run smoke used this section manually, so that smoke route needs review. |

## Player-Facing Route Families

These names collapse the success-capable branch points into routes a player or tester can reason about. A family is not always a single exclusive path; many branches merge back into the main graph, so these are route themes with important entry sections, state changes, and test hooks.

| Route Family | Entry / Trigger Sections | What It Represents | Route Stakes / Notes | Achievement / App Hooks |
|---|---|---|---|---|
| Opening Elementalism Split | 1 -> 202, 1 -> 168 | The first route split from section 1. | Both opening branches are success-capable and merge into the wider graph early. Keep this as a smoke check that both starts can still reach section 350. | No unique achievement yet; use for route reachability testing. |
| Early Survival And Travel | 2, 3, 58, 59, 78, 168 | Early mainland movement, food pressure, rest, and resource recovery/loss. | This family catches Meal handling, END/WP adjustments, Fresh Laumspur handling, and the early "did the assistant stay in sync?" checks. | Meal automation, Laumspur use/eat controls, WP/END quick controls. |
| Kazim Stone Route | 77, 10, 51, 175, 191, 314, 320, 323 | The optional Kazim Stone arc and its consequences. | Section 77 adds the Stone. Section 10 detects possession. Section 51 removes it. Sections 314/320/323 apply heavy WP/END costs and gated choices. | `gs1_kazim_claimed`, `gs1_kazim_stolen`; item add/remove automation for Kazim Stone; WP can go negative when forced by the book. |
| Shianti / Jnana Blessing Route | 87, 126, 161, 49, 274 | The benevolent-helper route through Jnana and the Silver Charm. | Section 87 can award the Amulet. Section 161 can award Jnana loot. The Silver Charm modifies the section 49 ravine roll and can lead to the section 274 leap result. | `gs1_priests_amulet`, `gs1_jnanas_blessing`, `gs1_leap_of_faith`; loot picker and random-number modifier testing. |
| Alchemy / Yabari / Ezeran Route | 65, 72, 151, 193, 297 | Alchemy supplies, poison/ointment protection, and Ezeran Acid creation. | Section 193 is the main alchemy cache. Sections 65/72 track Yabari protection. Section 151 checks ingredients; section 297 converts ingredients and an empty vial into Ezeran Acid. | `gs1_yabari_ward`, `gs1_alchemy_cache`, `gs1_ezeran_acid`; recipe conversion and ointment in-use flag. |
| Redeemer / Rune Riddle Route | 18, 209, 264, hidden 110 | The Redeemer item route and the hidden riddle answer route. | Section 209 supplies the Medallion and Pink Liquid. Section 264 consumes the liquid and can route to hidden answer section 110, which has no visible source link. | `gs1_redeemers_tokens`; loot picker, item gate, hidden-section route note. |
| Najin Route | 58, 101, 126, 130 | The Najin approach choice and survival fight. | Section 58 presents attack/wait choices. Section 101 is a survival combat that can resolve to 130. Section 126 can lead toward Jnana instead. | `gs1_najin_standoff`; multi-enemy/survival combat testing. |
| Kleasa / Sorcery Shield Route | 90, 139, 149, 165 | The Sorcery shield setup and the Kleasa limited combat. | Section 139 marks the shield active for section 149. Section 149 drains WP every round and drains less END when the shield is active. Section 165 clears the survival gate. | `gs1_kleasa_survivor`, `gs1_shield_raised`, `gs1_no_shield_no_problem`; combat per-round extras and temporary shield flag. |
| Correct Key / Door Route | 142, 159, 170, 205, 214, 235, 286 | The key/door section cluster and its random-number fork. | Section 286 checks Psychomancy first; otherwise it uses an even/odd random result: even to 214, odd to 205. Several routes in this cluster depend on items, Sorcery, or Prophecy. | `gs1_correct_key`; random-number outcome testing and item/Magick gates. |
| Quoku Route | 57, 107, 231, 281, 307, 331, 337 | Quoku encounters, staff attacks, and the large-Quoku threshold fight. | Section 281 is the special one-round fight: after one round, WP >= 10 routes to 331, otherwise 32. Other Quoku sections test combat modifiers and no-evade fights. | `gs1_quoku_breakthrough`; one-round combat, CS modifiers, WP threshold routing. |
| Gear Loss / Recovery Route | Gear loss: 291, 300, 311; recovery: 221, 245; setup: 349 | Backpack/Staff unavailable state and later recovery. | The app must snapshot carried gear when the book removes equipment, keep the unavailable state active, and restore it when section 221 or 245 is reached. | `gs1_gear_taken`, `gs1_gear_recovered`; full inventory snapshot/restore testing. |
| Shan / Tanith Companion Route | 276, 294, 335, 349, 245 | Companion separation, sacrifice, and recovery story beats. | Section 276 records Tanith's sacrifice. Sections 294/335 mark the lone-road state. Section 349 can lead into gear recovery through Tanith. | `gs1_tanith_sacrifice`, `gs1_lone_road`; companion-state notes and final-summary coverage. |
| Final Ascent Route | 340, 298, 350 | The late-game success spine into the Book 1 completion screen. | These sections should remain the canonical completion route family for final save summaries, Book 2 handoff, and repeat-book behavior. | `gs1_final_ascent`, `gs1_complete`; complete-book screen, summary, repeat-book reset. |
| Failure / Death Endpoint Families | 9, 14, 17, 20, 63, 67, 69, 92, 103, 122, 138, 155, 173, 177, 207, 216, 220, 225, 237, 262, 299, 306, 312, 315, 316, 317, 318, 324 | The terminal failure leaves detected by the route graph. | Most are death/failure endpoints; sections 92, 262, 315, and 318 still need human text classification before the report should call them final. | Death screen, rewind/repeat handling, route-family endpoint classification. |
| Source Irregularities | 110, 342 | Sections that need special handling outside normal link traversal. | Section 110 is a hidden riddle solution. Section 342 is called out by the source footnote as unreachable by normal choices, so route tests should not treat it as a legal path unless entered manually for oversight handling. | Hidden-route note for 110; unreachable-section marker for 342. |

## Route Testing Notes

- The named families above should drive playtest scripts: each family needs at least one success-capable dry run and, where practical, one failure/alternate run.
- The old Book 1 success-route smoke is useful for mechanics, but it is not a source-link proof because it used manual jumps through sections such as 342. Rebuild that smoke from this route-family table before using it as route evidence.
- Branches in this book are merge-heavy. A route family can share most of its later path with another family, so coverage should track sections, state changes, achievements, and endpoint behavior rather than only one complete route string.

## Endpoint Inventory

| Section | Classification | Reachable | Tags | Shortest Path |
|---:|---|---|---|---|
| 9 | death_or_failure | yes | leaf | 1, 202, 140, 280, 100, 121, 300, 289, 150, 348, 187, 230, 291, 178, 93, 258, 62, 36, 201, 172, 124, 333, 259, 296, ... (+64 more) |
| 14 | death_or_failure | yes | leaf | 1, 202, 140, 280, 100, 121, 300, 289, 150, 348, 187, 230, 291, 178, 93, 258, 62, 36, 201, 172, 124, 333, 259, 296, ... (+54 more) |
| 17 | death_or_failure | yes | leaf | 1, 202, 140, 280, 100, 121, 300, 289, 150, 348, 187, 230, 291, 178, 93, 258, 62, 36, 201, 172, 124, 333, 259, 296, ... (+54 more) |
| 20 | death_or_failure | yes | leaf | 1, 202, 140, 280, 16, 200, 195, 157, 26, 241, 20 |
| 63 | death_or_failure | yes | leaf | 1, 202, 140, 280, 100, 121, 300, 289, 150, 348, 187, 230, 291, 178, 93, 258, 62, 36, 201, 172, 124, 23, 137, 142, ... (+7 more) |
| 67 | death_or_failure | yes | leaf | 1, 202, 140, 280, 100, 121, 300, 289, 150, 348, 187, 230, 291, 178, 93, 258, 62, 36, 201, 172, 124, 23, 137, 142, ... (+6 more) |
| 69 | death_or_failure | yes | leaf | 1, 202, 140, 280, 100, 121, 300, 289, 150, 348, 187, 230, 291, 178, 93, 258, 62, 36, 201, 172, 124, 333, 259, 296, ... (+21 more) |
| 92 | needs_classification | yes | leaf, magick_check, wp | 1, 202, 140, 280, 100, 121, 300, 289, 150, 348, 187, 230, 291, 178, 93, 258, 62, 36, 201, 172, 124, 23, 92 |
| 103 | death_or_failure | yes | leaf | 1, 202, 140, 280, 100, 121, 300, 289, 150, 348, 187, 230, 291, 178, 93, 258, 62, 36, 201, 172, 124, 333, 259, 296, ... (+68 more) |
| 122 | death_or_failure | yes | leaf | 1, 202, 140, 280, 100, 121, 300, 289, 150, 348, 187, 230, 291, 178, 93, 258, 62, 36, 201, 172, 124, 333, 259, 296, ... (+59 more) |
| 138 | death_or_failure | yes | leaf | 1, 202, 140, 280, 100, 121, 300, 289, 150, 348, 187, 230, 291, 178, 93, 258, 62, 36, 201, 172, 124, 333, 259, 296, ... (+54 more) |
| 155 | death_or_failure | yes | leaf | 1, 202, 140, 112, 84, 196, 50, 155 |
| 173 | death_or_failure | yes | leaf | 1, 202, 140, 280, 100, 121, 300, 289, 150, 348, 187, 230, 291, 178, 93, 258, 62, 36, 201, 172, 124, 333, 259, 296, ... (+3 more) |
| 177 | death_or_failure | yes | leaf | 1, 202, 140, 280, 100, 121, 300, 289, 150, 348, 187, 230, 291, 178, 93, 258, 62, 36, 201, 172, 124, 333, 259, 296, ... (+25 more) |
| 207 | death_or_failure | yes | leaf | 1, 202, 140, 280, 100, 121, 300, 289, 150, 348, 187, 230, 291, 178, 93, 258, 62, 36, 201, 172, 124, 333, 259, 296, ... (+63 more) |
| 216 | death_or_failure | yes | leaf | 1, 202, 140, 280, 100, 121, 300, 289, 150, 348, 187, 230, 291, 178, 93, 258, 62, 36, 201, 172, 124, 333, 259, 296, ... (+35 more) |
| 220 | death_or_failure | yes | leaf | 1, 202, 140, 280, 100, 121, 300, 289, 150, 348, 187, 230, 291, 178, 93, 258, 62, 36, 201, 172, 250, 326, 220 |
| 225 | death_or_failure | yes | leaf | 1, 202, 140, 280, 100, 121, 300, 289, 150, 348, 187, 230, 291, 178, 93, 258, 62, 36, 201, 172, 124, 23, 137, 142, ... (+6 more) |
| 237 | death_or_failure | yes | leaf | 1, 202, 140, 280, 100, 121, 300, 289, 150, 237 |
| 262 | needs_classification | yes | leaf | 1, 202, 140, 280, 100, 121, 300, 289, 150, 348, 187, 230, 291, 178, 93, 258, 62, 36, 201, 172, 124, 333, 259, 296, ... (+35 more) |
| 299 | death_or_failure | yes | leaf, magick_check | 1, 202, 140, 280, 100, 121, 300, 289, 175, 191, 323, 299 |
| 306 | death_or_failure | yes | leaf | 1, 202, 140, 280, 100, 121, 300, 289, 150, 348, 187, 230, 291, 178, 93, 258, 62, 36, 201, 172, 124, 333, 259, 296, ... (+46 more) |
| 312 | death_or_failure | yes | leaf | 1, 202, 140, 280, 100, 121, 300, 289, 150, 348, 187, 230, 291, 178, 93, 258, 62, 36, 201, 172, 124, 23, 137, 142, ... (+4 more) |
| 315 | needs_classification | yes | leaf | 1, 202, 140, 280, 100, 121, 300, 289, 150, 348, 187, 230, 291, 178, 93, 258, 62, 36, 201, 172, 124, 333, 259, 296, ... (+63 more) |
| 316 | death_or_failure | yes | leaf | 1, 202, 140, 280, 100, 121, 300, 289, 150, 348, 187, 230, 291, 178, 93, 258, 62, 36, 201, 172, 124, 333, 259, 296, ... (+55 more) |
| 317 | death_or_failure | yes | leaf | 1, 202, 140, 280, 100, 121, 300, 289, 150, 348, 187, 230, 291, 178, 93, 258, 62, 36, 201, 172, 124, 333, 259, 296, ... (+47 more) |
| 318 | needs_classification | yes | leaf | 1, 202, 140, 280, 100, 121, 300, 289, 150, 348, 187, 230, 291, 178, 93, 258, 62, 36, 201, 172, 124, 333, 259, 296, ... (+53 more) |
| 324 | death_or_failure | yes | leaf | 1, 202, 140, 280, 100, 121, 300, 289, 150, 348, 187, 230, 291, 178, 93, 258, 62, 36, 201, 172, 124, 23, 137, 142, ... (+7 more) |
| 350 | success | yes | leaf, item_gate | 1, 202, 140, 280, 100, 121, 300, 289, 150, 348, 187, 230, 291, 178, 93, 258, 62, 36, 201, 172, 124, 333, 259, 296, ... (+69 more) |

## Success-Capable Branch Points

These are branch sections reachable from section 1 that can still reach the detected success ending.

| Section | Targets | Can Reach Success | Success Targets | Non-success Targets | Tags |
|---:|---|---|---|---|---|
| 1 | 202, 168 | yes | 202, 168 | None | branch, magick_check, item_gate |
| 3 | 85, 275 | yes | 85, 275 | None | branch, item_gate, endurance, meal |
| 8 | 14, 19 | yes | 19 | 14 | branch |
| 10 | 51, 90 | yes | 51, 90 | None | branch, item_gate |
| 11 | 300, 66, 20 | yes | 300, 66 | 20 | branch, wp |
| 16 | 200, 100 | yes | 200, 100 | None | branch, loot |
| 18 | 264, 190, 134 | yes | 264, 190, 134 | None | branch, item_gate |
| 19 | 35, 46, 59 | yes | 35, 46, 59 | None | branch, item_gate, wp |
| 22 | 122, 334 | yes | 334 | 122 | branch, item_gate, wp |
| 23 | 92, 137, 321 | yes | 137, 321 | 92 | branch, magick_check, item_gate |
| 24 | 10, 33 | yes | 10, 33 | None | branch |
| 25 | 77, 129 | yes | 77, 129 | None | branch |
| 26 | 97, 166, 241 | yes | 97, 166, 241 | None | branch |
| 28 | 308, 336 | yes | 308, 336 | None | branch |
| 29 | 54, 104 | yes | 54, 104 | None | branch |
| 32 | 107, 57 | yes | 107, 57 | None | branch |
| 33 | 10, 69 | yes | 10 | 69 | branch |
| 34 | 76, 133 | yes | 76, 133 | None | branch, item_gate |
| 36 | 201, 144 | yes | 201, 144 | None | branch |
| 39 | 55, 208 | yes | 55, 208 | None | branch |
| 40 | 64, 223, 76, 195 | yes | 64, 223, 76, 195 | None | branch, magick_check, item_gate |
| 42 | 216, 262, 119 | yes | 119 | 216, 262 | branch, item_gate |
| 43 | 143, 68, 118 | yes | 143, 68, 118 | None | branch, magick_check, item_gate, endurance, meal, loot |
| 44 | 317, 335 | yes | 335 | 317 | branch |
| 45 | 312, 80 | yes | 80 | 312 | branch |
| 49 | 274, 210 | yes | 210 | 274 | branch, random, item_gate, wp, loot |
| 50 | 40, 155 | yes | 40 | 155 | branch |
| 52 | 152, 227 | yes | 152, 227 | None | branch, wp |
| 54 | 278, 184, 228, 238 | yes | 278, 184, 228, 238 | None | branch, magick_check, item_gate |
| 55 | 70, 81, 99 | yes | 70, 81, 99 | None | branch, magick_check, item_gate |
| 56 | 251, 84 | yes | 251, 84 | None | branch, wp |
| 57 | 307, 182 | yes | 307, 182 | None | branch, item_gate, wp, endurance |
| 58 | 101, 126 | yes | 101, 126 | None | branch, magick_check, item_gate, wp, endurance, meal, loot |
| 60 | 45, 80 | yes | 45, 80 | None | branch |
| 61 | 186, 111, 86 | yes | 186, 111, 86 | None | branch |
| 62 | 7, 36 | yes | 7, 36 | None | branch |
| 65 | 72, 83 | yes | 72, 83 | None | branch |
| 68 | 293, 118 | yes | 293, 118 | None | branch, endurance |
| 70 | 88, 156 | yes | 88, 156 | None | branch, magick_check, wp |
| 73 | 92, 80, 45 | yes | 80, 45 | 92 | branch, magick_check, item_gate, gear_loss |
| 74 | 194, 219 | yes | 194, 219 | None | branch, item_gate |
| 77 | 67, 147 | yes | 147 | 67 | branch |
| 80 | 25, 41 | yes | 25, 41 | None | branch |
| 81 | 99, 145 | yes | 99, 145 | None | branch, wp |
| 82 | 105, 339 | yes | 105, 339 | None | branch, item_gate |
| 83 | 91, 98 | yes | 91, 98 | None | branch |
| 84 | 196, 224 | yes | 196, 224 | None | branch, wp |
| 87 | 125, 137, 212 | yes | 125, 137, 212 | None | branch, magick_check, wp, loot |
| 90 | 139, 123 | yes | 139, 123 | None | branch, magick_check, item_gate |
| 91 | 122, 141 | yes | 141 | 122 | branch, item_gate, wp |
| 95 | 109, 172 | yes | 109, 172 | None | branch, magick_check, item_gate, wp |
| 97 | 241, 89 | yes | 241, 89 | None | branch |
| 98 | 108, 115, 122 | yes | 108, 115 | 122 | branch, item_gate, wp |
| 99 | 88, 94 | yes | 88, 94 | None | branch, combat, endurance, loot |
| 100 | 40, 121 | yes | 40, 121 | None | branch |
| 104 | 248, 179 | yes | 248, 179 | None | branch |
| 105 | 313, 79, 131, 209 | yes | 313, 79, 131, 209 | None | branch, magick_check, item_gate |
| 107 | 307, 182 | yes | 307, 182 | None | branch, item_gate, wp, endurance |
| 109 | 243, 333 | yes | 243, 333 | None | branch, wp, endurance |
| 112 | 84, 56, 28 | yes | 84, 56, 28 | None | branch, magick_check |
| 113 | 138, 188 | yes | 188 | 138 | branch |
| 114 | 92, 80, 45 | yes | 80, 45 | 92 | branch, magick_check, item_gate, wp |
| 116 | 150, 226 | yes | 150, 226 | None | branch, magick_check, wp |
| 118 | 268, 293 | yes | 268, 293 | None | branch, endurance |
| 121 | 265, 300 | yes | 265, 300 | None | branch |
| 124 | 243, 23, 333 | yes | 243, 23, 333 | None | branch, magick_check, wp |
| 125 | 137, 212, 333 | yes | 137, 212, 333 | None | branch, loot |
| 126 | 161, 106 | yes | 161, 106 | None | branch |
| 127 | 50, 40 | yes | 50, 40 | None | branch |
| 128 | 181, 206, 12 | yes | 181, 206, 12 | None | branch, magick_check, item_gate |
| 129 | 67, 147 | yes | 147 | 67 | branch |
| 133 | 27, 71 | yes | 27, 71 | None | branch, combat, endurance |
| 136 | 345, 61 | yes | 345, 61 | None | branch, magick_check, item_gate |
| 137 | 92, 142, 163 | yes | 142, 163 | 92 | branch, magick_check, item_gate |
| 140 | 112, 280 | yes | 112, 280 | None | branch |
| 142 | 286, 159, 170, 163 | yes | 286, 159, 170, 163 | None | branch, item_gate |
| 143 | 68, 118 | yes | 68, 118 | None | branch, wp, endurance |
| 145 | 132, 99, 169 | yes | 132, 99, 169 | None | branch |
| 146 | 158, 232 | yes | 158, 232 | None | branch |
| 147 | 221, 63 | yes | 221 | 63 | branch |
| 148 | 49, 233 | yes | 49, 233 | None | branch |
| 150 | 348, 237 | yes | 348 | 237 | branch, magick_check, wp, endurance |
| 151 | 297, 172 | yes | 297, 172 | None | branch, item_gate |
| 152 | 252, 277, 302 | yes | 252, 277, 302 | None | branch |
| 153 | 185, 198 | yes | 185, 198 | None | branch, magick_check, item_gate |
| 154 | 4, 103 | yes | 4 | 103 | branch, combat, endurance |
| 156 | 215, 120 | yes | 215, 120 | None | branch |
| 157 | 183, 26 | yes | 183, 26 | None | branch, magick_check, item_gate |
| 159 | 114, 170, 163 | yes | 114, 170, 163 | None | branch, magick_check, item_gate, wp |
| 161 | 193, 15 | yes | 193, 15 | None | branch, magick_check, item_gate, endurance, meal |
| 165 | 177, 192 | yes | 192 | 177 | branch, wp, endurance |
| 166 | 241, 11 | yes | 241, 11 | None | branch |
| 167 | 162, 180 | yes | 162, 180 | None | branch |
| 170 | 73, 159, 163 | yes | 73, 159, 163 | None | branch, magick_check, item_gate |
| 172 | 95, 124, 271, 151, 236, 211, 250 | yes | 95, 124, 271, 151, 236, 211, 250 | None | branch, magick_check, item_gate, wp, endurance |
| 175 | 191, 116, 226 | yes | 191, 116, 226 | None | branch, magick_check, item_gate, wp |
| 176 | 153, 60 | yes | 153, 60 | None | branch, item_gate |
| 178 | 160, 93 | yes | 160, 93 | None | branch, item_gate |
| 179 | 285, 240 | yes | 285, 240 | None | branch, wp |
| 185 | 80, 253 | yes | 80, 253 | None | branch, wp |
| 187 | 230, 261 | yes | 230, 261 | None | branch, item_gate |
| 190 | 38, 21 | yes | 38, 21 | None | branch |
| 191 | 323, 314, 288 | yes | 323, 314, 288 | None | branch, wp |
| 195 | 157, 82 | yes | 157, 82 | None | branch |
| 196 | 50, 40 | yes | 50, 40 | None | branch |
| 198 | 80, 225 | yes | 80 | 225 | branch |
| 199 | 31, 48, 244 | yes | 31, 48, 244 | None | branch, magick_check |
| 200 | 64, 223, 76, 195 | yes | 64, 223, 76, 195 | None | branch, magick_check, item_gate |
| 204 | 329, 279, 304 | yes | 329, 279, 304 | None | branch, item_gate, wp, endurance |
| 205 | 163, 176 | yes | 163, 176 | None | branch, combat, endurance, loot |
| 208 | 81, 99 | yes | 81, 99 | None | branch |
| 209 | 131, 157 | yes | 131, 157 | None | branch, loot |
| 211 | 250, 172 | yes | 250, 172 | None | branch, magick_check, item_gate, wp |
| 212 | 309, 137 | yes | 309, 137 | None | branch |
| 213 | 267, 272, 284 | yes | 267, 272, 284 | None | branch |
| 214 | 92, 176, 45 | yes | 176, 45 | 92 | branch, magick_check, item_gate |
| 215 | 2, 156 | yes | 2, 156 | None | branch, magick_check, item_gate, wp, endurance, meal, loot |
| 222 | 239, 246, 260 | yes | 239, 246, 260 | None | branch |
| 223 | 34, 195 | yes | 34, 195 | None | branch |
| 226 | 295, 320 | yes | 295, 320 | None | branch, magick_check, wp, loot |
| 228 | 328, 6 | yes | 328, 6 | None | branch |
| 229 | 5, 30 | yes | 5, 30 | None | branch, item_gate, wp, endurance |
| 238 | 303, 104 | yes | 303, 104 | None | branch |
| 239 | 267, 272, 284 | yes | 267, 272, 284 | None | branch, wp |
| 241 | 300, 66, 20 | yes | 300, 66 | 20 | branch |
| 242 | 341, 316 | yes | 341 | 316 | branch, wp, endurance, loot |
| 243 | 125, 338, 333 | yes | 125, 338, 333 | None | branch, combat, endurance, loot |
| 244 | 167, 13 | yes | 167, 13 | None | branch |
| 248 | 204, 229, 254 | yes | 204, 229, 254 | None | branch, item_gate, wp, endurance |
| 249 | 282, 257 | yes | 282, 257 | None | branch |
| 250 | 326, 305 | yes | 326, 305 | None | branch, gear_loss |
| 251 | 50, 40 | yes | 50, 40 | None | branch |
| 253 | 80, 324 | yes | 80 | 324 | branch |
| 256 | 281, 107 | yes | 281, 107 | None | branch, loot |
| 264 | 190, 134 | yes | 190, 134 | None | branch, gear_loss |
| 266 | 330, 231 | yes | 330, 231 | None | branch |
| 267 | 332, 340, 347 | yes | 332, 340, 347 | None | branch |
| 268 | 8, 113 | yes | 8, 113 | None | branch, endurance |
| 270 | 201, 144 | yes | 201, 144 | None | branch, wp, endurance |
| 272 | 322, 315 | yes | 322 | 315 | branch, combat, endurance |
| 280 | 53, 16, 100 | yes | 53, 16, 100 | None | branch, magick_check, item_gate |
| 281 | 331, 32 | yes | 331, 32 | None | branch, combat, wp, endurance |
| 284 | 207, 310 | yes | 310 | 207 | branch, combat, endurance |
| 286 | 235, 214, 205 | yes | 235, 214, 205 | None | branch, random, magick_check, item_gate |
| 289 | 150, 175 | yes | 150, 175 | None | branch, magick_check, wp |
| 290 | 267, 272, 284 | yes | 267, 272, 284 | None | branch |
| 292 | 346, 199 | yes | 346, 199 | None | branch, item_gate |
| 293 | 318, 343 | yes | 343 | 318 | branch, endurance |
| 294 | 319, 344 | yes | 319, 344 | None | branch, endurance |
| 297 | 23, 333 | yes | 23, 333 | None | branch, loot |
| 309 | 137, 171 | yes | 137, 171 | None | branch, combat, endurance, loot |
| 310 | 267, 272 | yes | 267, 272 | None | branch |
| 314 | 320, 226, 150 | yes | 320, 226, 150 | None | branch, item_gate, wp, endurance |
| 321 | 137, 37 | yes | 137, 37 | None | branch, combat, endurance |
| 323 | 299, 226 | yes | 226 | 299 | branch, wp, endurance |
| 326 | 87, 220 | yes | 87 | 220 | branch |
| 327 | 78, 283 | yes | 78, 283 | None | branch |
| 331 | 307, 182 | yes | 307, 182 | None | branch |
| 332 | 96, 9 | yes | 96 | 9 | branch, item_gate, wp |
| 334 | 222, 234 | yes | 222, 234 | None | branch, gear_loss |
| 336 | 40, 50 | yes | 40, 50 | None | branch |
| 338 | 92, 137, 212 | yes | 137, 212 | 92 | branch, magick_check, item_gate |
| 339 | 217, 105 | yes | 217, 105 | None | branch, loot |
| 340 | 298, 287 | yes | 298, 287 | None | branch |
| 343 | 17, 242 | yes | 242 | 17 | branch, endurance |
| 349 | 173, 245 | yes | 245 | 173 | branch |

## Other Reachable Branch Points

- None

## Route-Family Maintenance Notes

- Keep the named route-family table in sync with section audit changes and assistant automation data.
- Rebuild route-smoke scripts from the named families before treating them as source-link proof.
- Endpoint rows marked `needs_classification` remain mandatory human-review stops.
- Route-only choices can stay on the book page; mechanical branches need support data or explicit manual notes.
