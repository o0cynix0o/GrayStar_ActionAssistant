# GS Book 3 Route Audit

Generated: 2026-05-21T08:43:37

Book: Beyond the Nightmare Gate

Status: machine route-graph baseline plus named route-family pass. Sections 144 and 190 are source irregularities called out by the local footnotes.

## Summary

| Metric | Value |
|---|---|
| Expected sections | 350 |
| Existing section files | 350 |
| Missing section files | None |
| Source edges | 701 |
| Bad source links | None |
| Reachable from section 1 | 348/350 |
| Unreachable from section 1 | 144, 190 |
| No incoming links | 190 |
| Endpoint sections | 29 |
| Branch points | 199 |
| Success-capable branch points | 199 |
| Detected success section | 350 |

## Shortest Success Path

- Length: 58 sections
- Path: 1, 211, 167, 302, 70, 264, 217, 246, 172, 91, 17, 250, 282, 116, 135, 140, 19, 13, 26, 45, 238, 241, 259, 245, 182, 278, 314, 14, 187, 94, 309, 20, 249, 148, 300, 216, 293, 324, 228, 201, 183, 169, 330, 338, 247, 215, 194, 51, 33, 75, 78, 304, 325, 341, 47, 275, 243, 350

## Mandatory Success Chokepoints

These sections dominate the detected success endpoint in the source-link graph. They are route-graph chokepoints, not proof that every legal state can pass through them.

- Count: 24
- Sections: 1, 33, 47, 75, 116, 135, 140, 167, 201, 215, 216, 228, 247, 250, 275, 278, 293, 300, 304, 324, 325, 330, 341, 350

## Opening Branches

| Branch | Reachable Sections | Can Reach Success | Reachable Endpoints | Early Merge Examples |
|---|---:|---|---|---|
| 1 -> 211 | 340 | yes | 7, 28, 40, 53, 63, 71, 80, 83, 104, 109, 126, 129, 164, 165, 168, 189, ... (+12 more) | 2, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 16, 17, 18, 19 |
| 1 -> 122 | 346 | yes | 7, 28, 40, 53, 63, 71, 80, 81, 83, 104, 109, 126, 129, 164, 165, 168, ... (+13 more) | 2, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 16, 17, 18, 19 |

## No-Incoming Review Notes

| Section | Route Audit Note |
|---:|---|
| 190 | Footnote says no choice leads here and calls it an oversight. Section 144 is only reached from this unreachable section, so both should stay documented as source irregularities. |

## Player-Facing Route Families

These names collapse the success-capable branch points into routes a player or tester can reason about. A family is not always a single exclusive path; many branches merge back into the main graph, so these are route themes with important entry sections, state changes, and test hooks.

| Route Family | Entry / Trigger Sections | What It Represents | Route Stakes / Notes | Achievement / App Hooks |
|---|---|---|---|---|
| Opening: Neverness To Crystal Tower | 1, 122, 211, 167, 302 | The first push across the cloud plain and toward the Crystal Tower. | Both opening choices can still reach the Moonstone. Use this family to make sure the Book 3 start remains playable from either branch. | Opening route links, early Willpower costs, Crystal Tower approach choices. |
| Crystal Tower Key Route | 56, 10, 150, 197, 240, 242, 252, 287 | The five animal keys and the riddle that points to the Serpent Key. | Wrong keys are dangerous but useful replay territory. The Serpent Key opens the tower, while the other keys create story, combat, and item branches. | `gs3_keybearer`, `gs3_serpent_solution`; key loot buttons, poison damage, animal-key combat and route checks. |
| Ethetron And Singing City Route | 116, 135, 140, 19, 45, 238, 241, 259 | The flying-machine route into the realm of the Elessin. | This family covers the Gyronome, Ethetron item choices, landing rolls, and the first real arrival in the Singing City. | `gs3_ethetron_pilot`, `gs3_singing_city`; roll helpers, loot picker, Gyronome item. |
| Elessin Judgment And Gear Trouble | 191, 107, 182, 344, 278 | Weapon confiscation, weapon return, Backpack stashing, and Backpack recovery. | Book 3 separates weapon-only confiscation from Backpack stashing, so route tests need to verify the two states do not overwrite each other. | `gs3_weapons_taken`, `gs3_weapons_returned`, `gs3_ethetron_stash`, `gs3_ethetron_recovery`; weapon and Backpack state automation. |
| Screaming God / Guardian Route | 4, 22, 44, 55, 115, 182 | The route around the statue of the Screaming God and the Guardian's warning. | This is a major story branch and a good replay target. It also creates END-based roll checks while carrying the statue. | `gs3_guardians_song`; END roll helpers, Guardian route notes. |
| Chaos-Bird Route | 64, 78, 108, 133, 188, 290, 304 | The Ethetron attack by Chaos-birds. | This family tests flying combat, Elementalism cost, a WP-based crash roll, and the optional Tanith weapon aid. | `gs3_chaos_bird_survivor`; combat presets, roll helpers, status flag. |
| Paradox And Tanith Rescue | 12, 67, 207, 213, 253, 276, 288, 314 | The strange bargain route and the effort to free Tanith from enchantment. | This is the emotional center of the book. It is also a steady Willpower drain, so it needs careful automation and achievement backfill. | `gs3_paradox_bargain`, `gs3_tanith_rescued`; chained WP costs and route achievements. |
| Vale And Healing Route | 216, 177, 293, 324, 338 | The gentler recovery stretch in the valley. | This family is the best place to verify healing, Senara buds, Senara potions, and rest bonuses. | `gs3_senara_brewer`; healing automations and consumable item use. |
| Jahksa / Shadow Brother Route | 291, 123, 131, 249, 148, 300, 243, 350 | Grey Star's dark double and the final Moonstone fight. | The final combat is unusual: losing the fight can lead to the successful ending. This family needs a dedicated combat test. | `gs3_shadow_brother`, `gs3_final_truth`, `gs3_moonstone_claimed`; defeat-route combat and completion screen. |
| Failure / Death Endpoint Families | 7, 28, 40, 53, 63, 71, 80, 81, 83, 104, 109, 126, 129, 164, 165, 168, 189, 203, 233, 269, 270, 271, 272, 286, 292, 308, 328, 349 | Terminal failure leaves detected in the Book 3 graph. | These are the endpoints the death screen and rewind/repeat flow should handle. | Death/failure automation and route endpoint coverage. |
| Source Irregularities | 144, 190 | Sections called out by the local footnotes as unreachable by normal choices. | Section 190 has no incoming source link, and section 144 is only reached through 190. Keep them documented, but do not treat them as legal route coverage. | Route-audit notes only. |

## Route Testing Notes

- Both opening branches can reach section 350, but the path merges often. Use route-family coverage plus mechanic coverage rather than trying to name every possible full path.
- Sections 144 and 190 are source irregularities from the local footnotes and should not be counted as missed legal player routes.
- The final combat at section 243 needs special testing because combat defeat routes to the successful ending at section 350.

## Endpoint Inventory

| Section | Classification | Reachable | Tags | Shortest Path |
|---:|---|---|---|---|
| 7 | death_or_failure | yes | leaf | 1, 211, 167, 302, 56, 240, 200, 7 |
| 28 | death_or_failure | yes | leaf | 1, 211, 167, 302, 70, 264, 217, 246, 172, 91, 17, 250, 282, 116, 135, 140, 19, 77, 85, 220, 284, 305, 332, 344, ... (+7 more) |
| 40 | death_or_failure | yes | leaf | 1, 211, 167, 302, 56, 240, 200, 40 |
| 53 | death_or_failure | yes | leaf | 1, 211, 167, 302, 56, 240, 200, 53 |
| 63 | death_or_failure | yes | leaf | 1, 211, 167, 302, 70, 264, 217, 246, 172, 63 |
| 71 | death_or_failure | yes | leaf | 1, 211, 167, 302, 70, 264, 217, 246, 172, 91, 17, 250, 282, 116, 135, 140, 19, 13, 26, 45, 238, 241, 71 |
| 80 | death_or_failure | yes | leaf | 1, 211, 167, 302, 70, 264, 217, 246, 172, 91, 17, 250, 282, 116, 135, 140, 19, 13, 26, 45, 238, 241, 322, 99, ... (+1 more) |
| 81 | death_or_failure | yes | leaf | 1, 122, 81 |
| 83 | death_or_failure | yes | leaf | 1, 211, 167, 302, 70, 264, 217, 246, 172, 91, 17, 250, 282, 116, 135, 140, 19, 13, 26, 45, 238, 241, 259, 245, ... (+28 more) |
| 104 | death_or_failure | yes | leaf | 1, 211, 167, 302, 70, 264, 217, 246, 172, 91, 17, 250, 282, 116, 135, 140, 19, 13, 26, 45, 238, 241, 259, 245, ... (+5 more) |
| 109 | death_or_failure | yes | leaf | 1, 211, 167, 302, 70, 264, 217, 246, 172, 91, 17, 250, 282, 116, 135, 140, 109 |
| 126 | death_or_failure | yes | leaf | 1, 211, 167, 302, 70, 264, 217, 246, 126 |
| 129 | death_or_failure | yes | leaf | 1, 211, 167, 302, 70, 264, 217, 246, 172, 91, 17, 250, 282, 116, 135, 140, 19, 13, 26, 45, 238, 241, 259, 245, ... (+24 more) |
| 164 | death_or_failure | yes | leaf | 1, 211, 167, 302, 70, 264, 217, 246, 172, 91, 17, 250, 282, 116, 135, 164 |
| 165 | death_or_failure | yes | leaf | 1, 211, 167, 302, 70, 264, 217, 246, 172, 91, 17, 250, 282, 116, 135, 140, 19, 13, 26, 45, 238, 241, 259, 245, ... (+10 more) |
| 168 | death_or_failure | yes | leaf | 1, 211, 167, 302, 70, 264, 217, 246, 172, 91, 17, 250, 282, 116, 135, 168 |
| 189 | death_or_failure | yes | leaf | 1, 211, 167, 302, 70, 264, 217, 246, 172, 91, 17, 250, 282, 116, 135, 189 |
| 203 | death_or_failure | yes | leaf | 1, 211, 167, 302, 70, 264, 217, 246, 172, 91, 17, 250, 282, 116, 135, 203 |
| 233 | death_or_failure | yes | leaf | 1, 211, 167, 302, 70, 264, 217, 246, 172, 91, 17, 250, 282, 116, 135, 140, 19, 13, 26, 45, 238, 241, 259, 245, ... (+22 more) |
| 269 | death_or_failure | yes | leaf | 1, 211, 167, 257, 269 |
| 270 | death_or_failure | yes | leaf | 1, 211, 167, 302, 70, 264, 217, 246, 172, 91, 17, 250, 282, 116, 135, 140, 19, 13, 26, 45, 238, 241, 322, 99, ... (+3 more) |
| 271 | death_or_failure | yes | leaf | 1, 211, 167, 302, 70, 264, 217, 246, 172, 91, 17, 250, 282, 116, 135, 140, 19, 77, 85, 220, 271 |
| 272 | death_or_failure | yes | leaf | 1, 211, 167, 302, 56, 277, 272 |
| 286 | death_or_failure | yes | leaf | 1, 211, 167, 302, 70, 264, 217, 246, 172, 91, 17, 250, 282, 116, 135, 140, 19, 13, 26, 45, 238, 241, 259, 245, ... (+34 more) |
| 292 | death_or_failure | yes | leaf | 1, 211, 167, 302, 70, 264, 292 |
| 308 | death_or_failure | yes | leaf | 1, 211, 167, 302, 56, 240, 200, 29, 318, 311, 89, 42, 110, 2, 221, 298, 295, 258, 308 |
| 328 | death_or_failure | yes | leaf | 1, 211, 167, 302, 56, 240, 200, 29, 318, 311, 89, 42, 110, 2, 221, 298, 295, 328 |
| 349 | death_or_failure | yes | leaf | 1, 211, 167, 302, 56, 240, 200, 29, 349 |
| 350 | success | yes | leaf | 1, 211, 167, 302, 70, 264, 217, 246, 172, 91, 17, 250, 282, 116, 135, 140, 19, 13, 26, 45, 238, 241, 259, 245, ... (+34 more) |

## Success-Capable Branch Points

These are branch sections reachable from section 1 that can still reach the detected success ending.

| Section | Targets | Can Reach Success | Success Targets | Non-success Targets | Tags |
|---:|---|---|---|---|---|
| 1 | 211, 122 | yes | 211, 122 | None | branch, loot |
| 2 | 198, 221 | yes | 198, 221 | None | branch |
| 4 | 115, 59, 65 | yes | 115, 59 | 65 | branch, random, endurance, loot |
| 6 | 248, 93 | yes | 248 | 93 | branch, random, loot |
| 8 | 2, 149 | yes | 2, 149 | None | branch, magick_check, item_gate |
| 10 | 240, 227, 235, 252, 277, 97, 161, 193 | yes | 240, 227, 235, 252, 277, 97, 161, 193 | None | branch, magick_check, item_gate |
| 11 | 42, 349, 40, 7, 311 | yes | 42, 311 | 349, 40, 7 | branch |
| 15 | 36, 3 | yes | 36, 3 | None | branch, magick_check, wp |
| 16 | 57, 25, 49, 37, 69 | yes | 57, 25, 49 | 37, 69 | branch, magick_check, item_gate |
| 19 | 13, 77 | yes | 13, 77 | None | branch, random, item_gate, loot |
| 21 | 271, 284 | yes | 284 | 271 | branch, wp, endurance, loot |
| 22 | 59, 65 | yes | 59 | 65 | branch, random, endurance, loot |
| 23 | 132, 143, 206, 347, 70 | yes | 132, 143, 206, 347, 70 | None | branch, magick_check, item_gate |
| 24 | 27, 165, 148 | yes | 27, 148 | 165 | branch, magick_check, item_gate, wp |
| 26 | 45, 66 | yes | 45, 66 | None | branch |
| 27 | 41, 54, 73, 88 | yes | 41, 54, 73, 88 | None | branch |
| 29 | 349, 318, 234 | yes | 318, 234 | 349 | branch |
| 30 | 58, 155 | yes | 58, 155 | None | branch, item_gate |
| 31 | 150, 137 | yes | 150, 137 | None | branch, wp |
| 32 | 67, 104 | yes | 67 | 104 | branch, wp |
| 41 | 73, 54, 88, 165 | yes | 73, 54, 88 | 165 | branch, magick_check, wp |
| 42 | 110, 8, 149 | yes | 110, 8, 149 | None | branch, magick_check, item_gate |
| 43 | 36, 15, 3 | yes | 36, 15, 3 | None | branch, magick_check |
| 44 | 59, 65 | yes | 59 | 65 | branch, random, endurance, loot, gear_loss |
| 48 | 244, 212 | yes | 244, 212 | None | branch, item_gate |
| 49 | 340, 322 | yes | 340, 322 | None | branch, wp |
| 52 | 184, 232, 254 | yes | 184, 232, 254 | None | branch |
| 54 | 41, 73, 88, 165 | yes | 41, 73, 88 | 165 | branch, wp |
| 56 | 240, 227, 235, 252, 277, 10, 97, 161, 193 | yes | 240, 227, 235, 252, 277, 10, 97, 161, ... (+1 more) | None | branch, magick_check, item_gate |
| 57 | 99, 107 | yes | 99, 107 | None | branch, combat, item_gate, endurance |
| 58 | 225, 335 | yes | 225, 335 | None | branch |
| 60 | 74, 310 | yes | 74, 310 | None | branch, endurance |
| 61 | 240, 227, 235, 252, 277 | yes | 240, 227, 235, 252, 277 | None | branch, wp |
| 66 | 45, 72, 21 | yes | 45, 72, 21 | None | branch, wp |
| 70 | 264, 206, 56, 223, 339, 347 | yes | 264, 206, 56, 223, 339, 347 | None | branch, magick_check, item_gate |
| 72 | 45, 326 | yes | 45, 326 | None | branch |
| 73 | 41, 54, 88, 165 | yes | 41, 54, 88 | 165 | branch, magick_check, wp |
| 75 | 64, 108, 78 | yes | 64, 108, 78 | None | branch, magick_check, item_gate |
| 77 | 85, 214 | yes | 85, 214 | None | branch |
| 78 | 304, 83 | yes | 304 | 83 | branch, random, magick_check, wp, loot |
| 79 | 208, 121 | yes | 208, 121 | None | branch |
| 85 | 103, 220, 260 | yes | 103, 220, 260 | None | branch, magick_check, item_gate, wp |
| 86 | 345, 327 | yes | 345, 327 | None | branch, magick_check, item_gate |
| 88 | 96, 101 | yes | 96, 101 | None | branch |
| 89 | 42, 349, 118 | yes | 42, 118 | 349 | branch |
| 92 | 283, 44 | yes | 44 | 283 | branch, endurance |
| 95 | 267, 289, 333, 348, 90 | yes | 267, 289, 333, 348, 90 | None | branch |
| 96 | 138, 142, 148 | yes | 138, 142, 148 | None | branch, wp |
| 97 | 61, 124 | yes | 61, 124 | None | branch, combat, endurance |
| 99 | 71, 107, 80, 209 | yes | 107, 209 | 71, 80 | branch |
| 100 | 56, 23, 70, 347 | yes | 56, 23, 70, 347 | None | branch, magick_check, item_gate, loot |
| 101 | 142, 165 | yes | 142 | 165 | branch, magick_check, wp |
| 106 | 252, 227, 240, 277 | yes | 252, 227, 240, 277 | None | branch |
| 107 | 80, 71, 92 | yes | 92 | 80, 71 | branch |
| 112 | 264, 285, 181 | yes | 264, 285, 181 | None | branch, wp |
| 113 | 192, 47, 185 | yes | 192, 47, 185 | None | branch, magick_check, item_gate, wp, loot |
| 114 | 208, 121 | yes | 208, 121 | None | branch |
| 116 | 135, 147, 152 | yes | 135, 147, 152 | None | branch, magick_check, item_gate, endurance, loot |
| 118 | 261, 312, 319, 173, 125, 239 | yes | 261, 312, 319, 173, 125, 239 | None | branch, magick_check, item_gate |
| 119 | 269, 100 | yes | 100 | 269 | branch |
| 121 | 120, 102, 111, 139, 145 | yes | 120, 102, 111, 139 | 145 | branch, random, magick_check, item_gate |
| 122 | 81, 43 | yes | 43 | 81 | branch |
| 124 | 7, 29, 40, 53 | yes | 29 | 7, 40, 53 | branch |
| 127 | 199, 219, 207, 213 | yes | 199, 219, 207, 213 | None | branch, magick_check, item_gate |
| 128 | 47, 162, 146 | yes | 47, 162, 146 | None | branch, magick_check, item_gate |
| 130 | 34, 46, 60 | yes | 34, 46, 60 | None | branch |
| 131 | 82, 141, 35, 123 | yes | 82, 141, 35, 123 | None | branch, item_gate |
| 132 | 56, 206, 223, 347, 70 | yes | 56, 206, 223, 347, 70 | None | branch, magick_check, item_gate |
| 133 | 78, 188 | yes | 78, 188 | None | branch, magick_check, item_gate, loot |
| 134 | 345, 327 | yes | 345, 327 | None | branch, magick_check, item_gate |
| 135 | 140, 164, 168, 189, 203 | yes | 140 | 164, 168, 189, 203 | branch |
| 136 | 151, 166, 196 | yes | 151, 166, 196 | None | branch, item_gate |
| 140 | 130, 109, 19 | yes | 130, 19 | 109 | branch |
| 142 | 148, 165 | yes | 148 | 165 | branch |
| 143 | 240, 227, 235, 252, 277, 10, 97, 161, 193 | yes | 240, 227, 235, 252, 277, 10, 97, 161, ... (+1 more) | None | branch, magick_check, item_gate |
| 147 | 135, 152 | yes | 135, 152 | None | branch, magick_check, item_gate, wp |
| 150 | 252, 235, 240, 277 | yes | 252, 235, 240, 277 | None | branch, loot |
| 152 | 135, 147 | yes | 135, 147 | None | branch, magick_check, item_gate, wp |
| 153 | 242, 197 | yes | 242, 197 | None | branch |
| 154 | 169, 159 | yes | 169, 159 | None | branch, magick_check, item_gate, wp |
| 155 | 5, 79 | yes | 5, 79 | None | branch, magick_check, item_gate, endurance, loot |
| 160 | 154, 169 | yes | 154, 169 | None | branch, magick_check, item_gate |
| 161 | 240, 227, 235, 252, 277, 10, 97, 193 | yes | 240, 227, 235, 252, 277, 10, 97, 193 | None | branch, magick_check, item_gate, wp |
| 162 | 192, 113, 185 | yes | 192, 113, 185 | None | branch, magick_check, item_gate, wp |
| 166 | 71, 39, 55 | yes | 39, 55 | 71 | branch, magick_check, item_gate |
| 167 | 257, 302 | yes | 257, 302 | None | branch |
| 170 | 136, 151, 166, 196 | yes | 136, 151, 166, 196 | None | branch, item_gate |
| 171 | 84, 129 | yes | 84 | 129 | branch, wp, loot |
| 172 | 63, 91 | yes | 91 | 63 | branch, random, item_gate, loot |
| 173 | 125, 239 | yes | 125, 239 | None | branch, magick_check, wp |
| 174 | 156, 86, 104 | yes | 156, 86 | 104 | branch, random, magick_check, item_gate, wp, loot |
| 175 | 76, 114, 5 | yes | 76, 114, 5 | None | branch, magick_check, item_gate |
| 176 | 192, 113, 185 | yes | 192, 113, 185 | None | branch, magick_check, item_gate, wp |
| 181 | 264, 285 | yes | 264, 285 | None | branch |
| 183 | 169, 160 | yes | 169, 160 | None | branch, magick_check, item_gate |
| 184 | 225, 335 | yes | 225, 335 | None | branch, loot |
| 185 | 192, 113 | yes | 192, 113 | None | branch, wp |
| 186 | 252, 235, 240, 277 | yes | 252, 235, 240, 277 | None | branch |
| 187 | 94, 134 | yes | 94, 134 | None | branch |
| 191 | 259, 202, 9 | yes | 259, 202, 9 | None | branch, magick_check, item_gate, gear_loss |
| 192 | 113, 47 | yes | 113, 47 | None | branch, endurance |
| 193 | 229, 240, 235, 252, 277, 227 | yes | 229, 240, 235, 252, 277, 227 | None | branch, magick_check, wp |
| 195 | 5, 79 | yes | 5, 79 | None | branch, magick_check, item_gate |
| 196 | 151, 136, 170, 166 | yes | 151, 136, 170, 166 | None | branch, item_gate |
| 197 | 252, 235, 227, 240 | yes | 252, 235, 227, 240 | None | branch, loot |
| 198 | 266, 221 | yes | 266, 221 | None | branch, loot |
| 200 | 7, 29, 40, 53 | yes | 29 | 7, 40, 53 | branch |
| 201 | 183, 160 | yes | 183, 160 | None | branch |
| 202 | 16, 28 | yes | 16 | 28 | branch, wp |
| 204 | 349, 311 | yes | 311 | 349 | branch |
| 205 | 231, 78, 83 | yes | 231, 78 | 83 | branch, magick_check, item_gate |
| 206 | 223, 264, 339 | yes | 223, 264, 339 | None | branch |
| 207 | 237, 199, 219, 213 | yes | 237, 199, 219, 213 | None | branch, magick_check, item_gate, wp |
| 208 | 170, 136, 151, 166, 196 | yes | 170, 136, 151, 166, 196 | None | branch, item_gate |
| 209 | 283, 297 | yes | 297 | 283 | branch, endurance |
| 213 | 253, 265 | yes | 253, 265 | None | branch, wp |
| 214 | 45, 6 | yes | 45, 6 | None | branch |
| 215 | 194, 171 | yes | 194, 171 | None | branch |
| 216 | 177, 293 | yes | 177, 293 | None | branch, magick_check, item_gate, endurance |
| 217 | 292, 246 | yes | 246 | 292 | branch, random, item_gate, loot |
| 218 | 350, 286 | yes | 350 | 286 | branch |
| 219 | 163, 179 | yes | 163, 179 | None | branch, magick_check, wp |
| 220 | 271, 284 | yes | 284 | 271 | branch, wp, endurance, loot |
| 221 | 336, 298 | yes | 336, 298 | None | branch, loot |
| 222 | 71, 334, 316 | yes | 334, 316 | 71 | branch |
| 223 | 264, 339, 285 | yes | 264, 339, 285 | None | branch |
| 225 | 195, 180 | yes | 195, 180 | None | branch, endurance |
| 226 | 316, 71, 334 | yes | 316, 334 | 71 | branch, wp |
| 227 | 31, 87 | yes | 31, 87 | None | branch |
| 229 | 227, 235, 240, 252, 277 | yes | 227, 235, 240, 252, 277 | None | branch, magick_check |
| 230 | 71, 226, 39, 55 | yes | 226, 39, 55 | 71 | branch, magick_check, item_gate |
| 231 | 98, 251, 68, 281 | yes | 68, 281 | 98, 251 | branch |
| 234 | 256, 204 | yes | 256, 204 | None | branch |
| 235 | 178, 296 | yes | 178, 296 | None | branch, random |
| 239 | 89, 349 | yes | 89 | 349 | branch |
| 241 | 322, 71, 259 | yes | 322, 259 | 71 | branch |
| 242 | 252, 235, 227, 240 | yes | 252, 235, 227, 240 | None | branch, loot |
| 243 | 218, 286, 350 | yes | 218, 350 | 286 | branch, combat, endurance |
| 245 | 182, 322 | yes | 182, 322 | None | branch, magick_check |
| 246 | 126, 172 | yes | 172 | 126 | branch, random, item_gate, loot |
| 247 | 215, 233 | yes | 215 | 233 | branch, wp, loot |
| 248 | 271, 284 | yes | 284 | 271 | branch, wp, endurance, loot |
| 249 | 24, 27, 148, 165 | yes | 24, 27, 148 | 165 | branch, magick_check, item_gate |
| 250 | 210, 282, 299 | yes | 210, 282, 299 | None | branch, magick_check, item_gate |
| 252 | 227, 235, 240, 277 | yes | 227, 235, 240, 277 | None | branch, endurance |
| 253 | 276, 265 | yes | 276, 265 | None | branch, wp |
| 254 | 267, 289, 333, 348, 90 | yes | 267, 289, 333, 348, 90 | None | branch |
| 256 | 311, 40 | yes | 311 | 40 | branch |
| 257 | 323, 269, 302, 337 | yes | 323, 302, 337 | 269 | branch, magick_check, item_gate |
| 258 | 308, 321 | yes | 321 | 308 | branch |
| 260 | 45, 66 | yes | 45, 66 | None | branch |
| 261 | 125, 239 | yes | 125, 239 | None | branch, wp |
| 262 | 208, 121 | yes | 208, 121 | None | branch |
| 264 | 217, 292 | yes | 217 | 292 | branch, item_gate |
| 267 | 313, 342 | yes | 313, 342 | None | branch |
| 275 | 243, 218 | yes | 243, 218 | None | branch |
| 277 | 272, 153 | yes | 153 | 272 | branch |
| 278 | 303, 314 | yes | 303, 314 | None | branch |
| 280 | 48, 274, 301, 294 | yes | 48, 274, 301, 294 | None | branch, magick_check, item_gate |
| 285 | 329, 269 | yes | 329 | 269 | branch |
| 287 | 252, 227, 277, 240 | yes | 252, 227, 277, 240 | None | branch, loot |
| 289 | 313, 342 | yes | 313, 342 | None | branch |
| 290 | 304, 83 | yes | 304 | 83 | branch, random, wp, loot |
| 291 | 123, 131 | yes | 123, 131 | None | branch |
| 295 | 258, 328 | yes | 258 | 328 | branch |
| 296 | 287, 106 | yes | 287, 106 | None | branch, combat, item_gate, endurance |
| 297 | 4, 22 | yes | 4, 22 | None | branch |
| 298 | 268, 295 | yes | 268, 295 | None | branch, magick_check, item_gate |
| 299 | 317, 282, 210 | yes | 317, 282, 210 | None | branch, magick_check, wp |
| 302 | 56, 23, 70, 347 | yes | 56, 23, 70, 347 | None | branch, magick_check, item_gate, loot |
| 307 | 38, 52, 95, 157 | yes | 38, 52, 95, 157 | None | branch |
| 309 | 20, 62 | yes | 20, 62 | None | branch, item_gate |
| 310 | 13, 77 | yes | 13, 77 | None | branch, random, item_gate, loot |
| 311 | 7, 89, 11, 349 | yes | 89, 11 | 7, 349 | branch |
| 312 | 125, 89, 349 | yes | 125, 89 | 349 | branch |
| 314 | 14, 32 | yes | 14, 32 | None | branch, magick_check, item_gate |
| 315 | 274, 280, 301, 294 | yes | 274, 280, 301, 294 | None | branch, magick_check, item_gate |
| 316 | 245, 209 | yes | 245, 209 | None | branch |
| 318 | 118, 349, 311 | yes | 118, 311 | 349 | branch |
| 320 | 274, 280, 301, 294 | yes | 274, 280, 301, 294 | None | branch, magick_check, item_gate |
| 322 | 99, 107 | yes | 99, 107 | None | branch, combat, item_gate, endurance |
| 323 | 269, 119, 302, 337 | yes | 119, 302, 337 | 269 | branch, magick_check, item_gate |
| 324 | 228, 236 | yes | 228, 236 | None | branch, magick_check, item_gate, wp, endurance |
| 326 | 271, 284 | yes | 284 | 271 | branch, wp, endurance, loot |
| 329 | 269, 264 | yes | 264 | 269 | branch |
| 330 | 338, 306 | yes | 338, 306 | None | branch |
| 331 | 30, 307 | yes | 30, 307 | None | branch |
| 332 | 344, 315 | yes | 344, 315 | None | branch |
| 333 | 267, 289, 348, 90 | yes | 267, 289, 348, 90 | None | branch |
| 334 | 71, 80, 92 | yes | 92 | 71, 80 | branch, wp |
| 336 | 298, 224 | yes | 298, 224 | None | branch, magick_check, item_gate |
| 337 | 269, 323, 302 | yes | 323, 302 | 269 | branch, magick_check, wp |
| 339 | 112, 264, 285 | yes | 112, 264, 285 | None | branch, wp |
| 341 | 47, 128 | yes | 47, 128 | None | branch |
| 344 | 307, 331 | yes | 307, 331 | None | branch |
| 345 | 288, 327 | yes | 288, 327 | None | branch, magick_check, wp |
| 346 | 334, 316, 209 | yes | 334, 316, 209 | None | branch, magick_check |
| 347 | 206, 56, 264, 223, 70 | yes | 206, 56, 264, 223, 70 | None | branch, magick_check, item_gate, wp, loot |
| 348 | 267, 289, 333, 90 | yes | 267, 289, 333, 90 | None | branch, loot |

## Other Reachable Branch Points

- None

## Route-Family Maintenance Notes

- Keep the named route-family table in sync with section audit changes and assistant automation data.
- Rebuild route-smoke scripts from the named families before treating them as source-link proof.
- Endpoint rows marked `needs_classification` remain mandatory human-review stops.
- Route-only choices can stay on the book page; mechanical branches need support data or explicit manual notes.
