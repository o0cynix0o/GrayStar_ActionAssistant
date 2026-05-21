# GS Book 4 Route Audit

Generated: 2026-05-21T09:06:08

Book: War of the Wizards

Status: machine route-graph baseline plus named route-family pass. All 360 section files are reachable from section 1 in the local source graph.

## Summary

| Metric | Value |
|---|---|
| Expected sections | 360 |
| Existing section files | 360 |
| Missing section files | None |
| Source edges | 552 |
| Bad source links | None |
| Reachable from section 1 | 360/360 |
| Unreachable from section 1 | None |
| No incoming links | None |
| Endpoint sections | 24 |
| Branch points | 151 |
| Success-capable branch points | 151 |
| Detected success section | 360 |

## Shortest Success Path

- Length: 45 sections
- Path: 1, 348, 326, 50, 239, 172, 257, 81, 169, 9, 217, 99, 201, 260, 298, 10, 29, 76, 90, 98, 118, 193, 175, 252, 321, 282, 354, 343, 312, 300, 254, 358, 242, 324, 347, 275, 351, 328, 191, 39, 92, 131, 180, 316, 360

## Mandatory Success Chokepoints

These sections dominate the detected success endpoint in the source-link graph. They are route-graph chokepoints, not proof that every legal state can pass through them.

- Count: 21
- Sections: 1, 10, 29, 39, 50, 239, 242, 254, 260, 282, 298, 300, 312, 321, 326, 328, 347, 351, 354, 358, 360

## Opening Branches

| Branch | Reachable Sections | Can Reach Success | Reachable Endpoints | Early Merge Examples |
|---|---:|---|---|---|
| 1 -> 348 | 357 | yes | 2, 27, 44, 54, 80, 94, 96, 130, 153, 160, 176, 192, 263, 299, 308, 315, ... (+8 more) | 2, 3, 4, 5, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18 |
| 1 -> 6 | 357 | yes | 2, 27, 44, 54, 80, 94, 96, 130, 153, 160, 176, 192, 263, 299, 308, 315, ... (+8 more) | 2, 3, 4, 5, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18 |
| 1 -> 340 | 357 | yes | 2, 27, 44, 54, 80, 94, 96, 130, 153, 160, 176, 192, 263, 299, 308, 315, ... (+8 more) | 2, 3, 4, 5, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18 |

## Player-Facing Route Families

These names collapse the success-capable branch points into routes a player or tester can reason about. A family is not always a single exclusive path; many branches merge back into the main graph, so these are route themes with important entry sections, state changes, and test hooks.

| Route Family | Entry / Trigger Sections | What It Represents | Route Stakes / Notes | Achievement / App Hooks |
|---|---|---|---|---|
| Opening: Shianti Counsel | 1, 348, 6, 340, 326, 50 | The last quiet moment before Grey Star returns to Magnamund. | All three opening questions merge quickly. They are good smoke checks for the Moonstone handoff and the Book 4 start state. | `gs4_moonstone_bearer`; Book 4 start rules, Moonstone inventory, Higher Magick setup. |
| Lissan Plain Survival | 239, 172, 60, 267, 36, 234, 43, 241 | The water, heat, and first Masbate trail across the Lissan Plain. | This family catches early END attrition, Prophecy/Visionary scouting, and the Phinomel plant branch. | `gs4_phinomel_harvest`; END losses, Phinomel roll helpers, Phinomel loot buttons. |
| Masbate Rescue And Hidden Tribe | 58, 67, 85, 97, 116, 126, 38, 150, 298 | The tortured Masbate survivor, demon trap, and return of Samu's people. | The route can go through scouting magic, ambushes, and several demon fights before revealing that the Masbate survived. | `gs4_masbate_found`; demon combat presets, scouting WP costs, Masbate route checks. |
| Invulnerability And Portal Prep | 10, 15, 19, 24, 29, 34, 49, 76, 84 | The planning phase before the ride to Tilos. | This family covers Theurgy/Thaumaturgy/Necromancy choices, Potion of Invulnerability crafting, and the Masbate supply cache. | `gs4_invulnerability_brewed`, `gs4_invulnerability_used`; potion loot/use automation and protection flags. |
| Demon Portal Of Tilos | 70, 76, 90, 98, 104, 112, 134, 139, 158, 167, 209, 268 | The ride to the portal and the confrontation with Agarash through the fire. | This family contains several expensive Moonstone and Staff costs, including the Book 4 footnote cases that allow negative WP or END substitution. | `gs4_portal_closed`; WP-cost buttons, invulnerability combat variants, portal close route. |
| Demon Chase And Shadakine Uniform | 13, 17, 37, 45, 220, 250, 285, 292, 302 | The route where Grey Star turns the pursuing demon horde toward the Shadakine. | The Shadakine uniform matters because it helps steer the horde into the enemy army instead of into Grey Star. | `gs4_uniform_taken`; uniform flag, horseman combat, chase-route survival checks. |
| Bridge At Lanzi | 75, 175, 252, 256, 270, 353 | The Masbate bridge action and the demon/Shadakine collision. | This is the big set-piece in the middle of the book: bridge destruction, mass combat, and the Demon Master. | `gs4_lanzi_bridge`; high WP bridge cost, Demon Master timed combat, route outcomes. |
| Freedom Guild And Fernmost | 282, 321, 312, 300, 331, 336, 355, 359 | Rejoining Sado, retreating to Fernmost, and gathering the late-game herb cache. | This family handles the best recovery stretch in the book and the Leafwater opportunity for a stronger Staff. | `gs4_freedom_guild`, `gs4_fernmost_rest`, `gs4_alchemy_cache`, `gs4_leafwater_staff`; healing, potion loot, CS boost. |
| Night Battle And Road To Shadaki | 347, 275, 351, 328, 191, 342, 12 | The late war against the Shadakine and the final approach to Shasarak. | This family includes night-fighting choices, the Morn Pass danger, and the teleport decision into Shadaki. | `gs4_shadaki_arrival`; night-battle WP costs, teleport choices, Skeleton Warrior combat. |
| Shasarak And Agarash | 39, 92, 129, 131, 145, 180, 310, 316, 350, 356, 360 | The final duel, the broken Staff, and the choice that seals Agarash's portal. | This family is the final endgame spine. It needs direct tests for Shasarak combat, Staff removal, Book 4 completion, and repeat-final-book behavior. | `gs4_shasarak_duel`, `gs4_staff_shattered`, `gs4_agarash_defied`, `gs4_wizard_regent`; final combats and completion screen. |
| Failure / Death Endpoint Families | 2, 27, 44, 54, 80, 94, 96, 130, 153, 160, 176, 192, 263, 299, 308, 315, 319, 322, 335, 339, 346, 349, 357 | Terminal failure leaves detected in the Book 4 graph. | These are the endpoints the death screen and rewind/repeat flow should handle. | Death/failure automation and endpoint coverage. |

## Route Testing Notes

- All Book 4 section files are reachable from section 1 in the source graph, so route testing should focus on state gates and mechanic coverage rather than missing links.
- The Book 4 final stretch has multiple ways to reach Shasarak and multiple ways to resolve Agarash. Treat sections 316, 356, and 360 as separate endgame checks.
- Several portal sections use the Book 4 footnote rule for insufficient Willpower. Test both straight negative-WP spending and END-for-missing-WP handling.

## Endpoint Inventory

| Section | Classification | Reachable | Tags | Shortest Path |
|---:|---|---|---|---|
| 2 | death_or_failure | yes | leaf | 1, 348, 326, 50, 239, 172, 257, 81, 169, 9, 217, 99, 201, 260, 298, 10, 29, 76, 90, 98, 118, 193, 175, 252, ... (+22 more) |
| 27 | death_or_failure | yes | leaf | 1, 348, 326, 50, 239, 60, 267, 36, 234, 43, 58, 116, 126, 13, 27 |
| 44 | death_or_failure | yes | leaf | 1, 348, 326, 50, 239, 172, 257, 81, 169, 9, 217, 99, 201, 260, 298, 10, 29, 70, 224, 237, 271, 44 |
| 54 | death_or_failure | yes | leaf | 1, 348, 326, 50, 239, 60, 267, 36, 234, 43, 58, 116, 126, 13, 54 |
| 80 | death_or_failure | yes | leaf | 1, 348, 326, 50, 239, 172, 257, 81, 169, 9, 217, 99, 201, 260, 298, 10, 29, 70, 224, 237, 249, 274, 134, 139, ... (+17 more) |
| 94 | death_or_failure | yes | leaf | 1, 348, 326, 50, 239, 172, 257, 81, 169, 9, 217, 99, 201, 260, 298, 10, 29, 76, 90, 98, 118, 193, 142, 279, ... (+3 more) |
| 96 | death_or_failure | yes | leaf | 1, 348, 326, 50, 239, 172, 257, 81, 169, 9, 217, 99, 201, 260, 298, 10, 29, 70, 224, 237, 249, 274, 134, 139, ... (+14 more) |
| 130 | death_or_failure | yes | leaf | 1, 348, 326, 50, 239, 60, 267, 36, 297, 225, 148, 130 |
| 153 | death_or_failure | yes | leaf, magick_check | 1, 348, 326, 50, 239, 172, 257, 81, 169, 9, 217, 99, 201, 260, 298, 10, 29, 70, 224, 237, 249, 274, 134, 153 |
| 160 | death_or_failure | yes | leaf | 1, 348, 326, 50, 239, 60, 267, 36, 234, 43, 67, 89, 141, 160 |
| 176 | death_or_failure | yes | leaf | 1, 348, 326, 50, 239, 172, 257, 81, 169, 9, 217, 99, 201, 260, 298, 10, 29, 70, 224, 237, 249, 274, 134, 139, ... (+2 more) |
| 192 | death_or_failure | yes | leaf, magick_check | 1, 348, 326, 50, 239, 172, 257, 81, 169, 9, 217, 99, 201, 260, 298, 10, 29, 70, 224, 237, 249, 274, 134, 139, ... (+3 more) |
| 263 | death_or_failure | yes | leaf | 1, 348, 326, 50, 239, 172, 257, 81, 169, 9, 217, 99, 201, 260, 298, 10, 29, 76, 90, 98, 118, 193, 175, 252, ... (+7 more) |
| 299 | death_or_failure | yes | leaf | 1, 348, 326, 50, 239, 60, 267, 36, 234, 43, 67, 89, 299 |
| 308 | death_or_failure | yes | leaf | 1, 348, 326, 50, 239, 172, 257, 81, 169, 9, 217, 99, 201, 260, 298, 10, 29, 70, 224, 237, 249, 274, 134, 139, ... (+17 more) |
| 315 | death_or_failure | yes | leaf | 1, 348, 326, 50, 239, 172, 257, 81, 169, 9, 217, 99, 201, 260, 298, 10, 29, 70, 224, 237, 249, 274, 134, 139, ... (+10 more) |
| 319 | death_or_failure | yes | leaf | 1, 348, 326, 50, 239, 172, 257, 81, 169, 9, 217, 99, 201, 260, 298, 10, 29, 70, 224, 237, 249, 274, 134, 139, ... (+11 more) |
| 322 | death_or_failure | yes | leaf | 1, 348, 326, 50, 239, 172, 257, 81, 169, 9, 217, 99, 201, 260, 298, 10, 29, 76, 90, 98, 118, 193, 175, 252, ... (+21 more) |
| 335 | death_or_failure | yes | leaf | 1, 348, 326, 50, 239, 172, 257, 81, 169, 9, 217, 99, 201, 260, 298, 10, 29, 76, 90, 98, 118, 193, 175, 252, ... (+10 more) |
| 339 | death_or_failure | yes | leaf | 1, 348, 326, 50, 239, 172, 257, 81, 169, 9, 217, 99, 201, 260, 298, 10, 29, 76, 90, 98, 118, 193, 175, 252, ... (+7 more) |
| 346 | death_or_failure | yes | leaf | 1, 348, 326, 50, 239, 172, 257, 81, 169, 9, 217, 99, 201, 260, 298, 10, 29, 76, 90, 98, 118, 193, 175, 252, ... (+14 more) |
| 349 | death_or_failure | yes | leaf | 1, 348, 326, 50, 239, 172, 257, 81, 169, 9, 217, 99, 201, 260, 298, 10, 29, 76, 90, 98, 118, 193, 175, 252, ... (+13 more) |
| 357 | death_or_failure | yes | leaf | 1, 348, 326, 50, 239, 172, 257, 81, 169, 9, 217, 99, 201, 260, 298, 10, 29, 76, 90, 98, 118, 193, 175, 252, ... (+10 more) |
| 360 | success | yes | leaf | 1, 348, 326, 50, 239, 172, 257, 81, 169, 9, 217, 99, 201, 260, 298, 10, 29, 76, 90, 98, 118, 193, 175, 252, ... (+21 more) |

## Success-Capable Branch Points

These are branch sections reachable from section 1 that can still reach the detected success ending.

| Section | Targets | Can Reach Success | Success Targets | Non-success Targets | Tags |
|---:|---|---|---|---|---|
| 1 | 348, 6, 340 | yes | 348, 6, 340 | None | branch |
| 3 | 63, 79 | yes | 63, 79 | None | branch, random |
| 4 | 11, 16, 40 | yes | 11, 16, 40 | None | branch, random, wp, endurance, loot |
| 5 | 350, 316 | yes | 350, 316 | None | branch, item_gate, wp |
| 9 | 196, 203, 211, 217, 69, 187 | yes | 196, 203, 211, 217, 69, 187 | None | branch, magick_check, item_gate |
| 10 | 15, 19, 24, 29 | yes | 15, 19, 24, 29 | None | branch |
| 13 | 22, 27, 54 | yes | 22 | 27, 54 | branch |
| 14 | 81, 213 | yes | 81, 213 | None | branch |
| 15 | 34, 19, 24, 29 | yes | 34, 19, 24, 29 | None | branch, magick_check |
| 17 | 285, 292 | yes | 285, 292 | None | branch |
| 18 | 295, 255, 289, 181, 234 | yes | 295, 255, 289, 181, 234 | None | branch, magick_check, item_gate |
| 19 | 57, 24, 29 | yes | 57, 24, 29 | None | branch, magick_check, wp |
| 21 | 92, 190 | yes | 92, 190 | None | branch, wp, endurance |
| 23 | 35, 65, 93 | yes | 35, 65, 93 | None | branch, magick_check |
| 24 | 57, 19, 29 | yes | 57, 19, 29 | None | branch, magick_check, wp |
| 28 | 41, 72, 87 | yes | 41, 72, 87 | None | branch, combat, item_gate, endurance |
| 29 | 70, 76 | yes | 70, 76 | None | branch |
| 31 | 51, 47 | yes | 51, 47 | None | branch |
| 35 | 46, 105 | yes | 46, 105 | None | branch, wp |
| 36 | 297, 234 | yes | 297, 234 | None | branch |
| 39 | 21, 92 | yes | 21, 92 | None | branch, item_gate, wp |
| 42 | 202, 223 | yes | 202, 223 | None | branch |
| 43 | 58, 67, 85 | yes | 58, 67, 85 | None | branch, magick_check, item_gate |
| 46 | 105, 117 | yes | 105, 117 | None | branch, wp |
| 47 | 88, 103 | yes | 88, 103 | None | branch, wp |
| 50 | 162, 239 | yes | 162, 239 | None | branch, magick_check, item_gate |
| 51 | 109, 123 | yes | 109, 123 | None | branch, combat, endurance |
| 52 | 73, 78 | yes | 73, 78 | None | branch, magick_check, wp |
| 58 | 67, 97, 116 | yes | 67, 97, 116 | None | branch, magick_check, wp |
| 60 | 267, 273, 286 | yes | 267, 273, 286 | None | branch |
| 62 | 71, 96 | yes | 71 | 96 | branch, random, item_gate, endurance, loot |
| 67 | 97, 116, 89 | yes | 97, 116, 89 | None | branch, wp |
| 69 | 232, 243, 262 | yes | 232, 243, 262 | None | branch, wp |
| 70 | 224, 231 | yes | 224, 231 | None | branch |
| 76 | 84, 90 | yes | 84, 90 | None | branch, item_gate |
| 77 | 14, 36 | yes | 14, 36 | None | branch, endurance |
| 79 | 124, 185, 229 | yes | 124, 185, 229 | None | branch, magick_check, item_gate |
| 81 | 146, 169, 177, 213 | yes | 146, 169, 177, 213 | None | branch, magick_check, item_gate |
| 85 | 97, 116 | yes | 97, 116 | None | branch |
| 86 | 314, 7, 26, 175 | yes | 314, 7, 26, 175 | None | branch, magick_check, item_gate |
| 88 | 64, 228 | yes | 64, 228 | None | branch, item_gate, wp |
| 89 | 141, 299 | yes | 141 | 299 | branch |
| 90 | 98, 106, 114 | yes | 98, 106, 114 | None | branch |
| 92 | 131, 145 | yes | 131, 145 | None | branch, wp |
| 95 | 14, 36 | yes | 14, 36 | None | branch, endurance |
| 97 | 288, 82 | yes | 288, 82 | None | branch |
| 98 | 118, 128 | yes | 118, 128 | None | branch, item_gate |
| 104 | 112, 175 | yes | 112, 175 | None | branch, item_gate, wp, endurance |
| 106 | 149, 161 | yes | 149, 161 | None | branch |
| 110 | 14, 36 | yes | 14, 36 | None | branch |
| 112 | 158, 175 | yes | 158, 175 | None | branch, item_gate, wp, endurance |
| 113 | 174, 215 | yes | 174, 215 | None | branch, magick_check, wp |
| 114 | 98, 106 | yes | 98, 106 | None | branch, wp |
| 115 | 289, 181, 234 | yes | 289, 181, 234 | None | branch, magick_check, item_gate, wp |
| 116 | 89, 126 | yes | 89, 126 | None | branch |
| 118 | 193, 207 | yes | 193, 207 | None | branch |
| 119 | 30, 74, 293 | yes | 30, 74, 293 | None | branch |
| 121 | 233, 218, 204 | yes | 233, 218, 204 | None | branch |
| 123 | 155, 168 | yes | 155, 168 | None | branch, combat, endurance |
| 125 | 310, 129 | yes | 310, 129 | None | branch, wp, endurance |
| 132 | 143, 248 | yes | 143, 248 | None | branch, magick_check, wp |
| 134 | 139, 153 | yes | 139 | 153 | branch, magick_check |
| 135 | 3, 48 | yes | 3, 48 | None | branch |
| 139 | 158, 175 | yes | 158, 175 | None | branch, magick_check, item_gate, wp, endurance |
| 141 | 221, 160 | yes | 221 | 160 | branch |
| 142 | 249, 266, 279 | yes | 249, 266, 279 | None | branch, magick_check, item_gate, wp |
| 147 | 66, 59 | yes | 66, 59 | None | branch |
| 148 | 130, 55 | yes | 55 | 130 | branch, random, magick_check, item_gate, loot |
| 149 | 171, 182 | yes | 171, 182 | None | branch, random, item_gate, loot |
| 151 | 166, 253 | yes | 166, 253 | None | branch |
| 157 | 344, 357 | yes | 344 | 357 | branch, wp |
| 158 | 167, 176 | yes | 167 | 176 | branch, item_gate, wp |
| 159 | 83, 122, 115 | yes | 83, 122, 115 | None | branch, magick_check, item_gate, wp |
| 161 | 178, 184 | yes | 178, 184 | None | branch, combat, item_gate, endurance |
| 167 | 192, 209, 176 | yes | 209 | 192, 176 | branch, item_gate, wp |
| 169 | 213, 9 | yes | 213, 9 | None | branch, magick_check, wp |
| 170 | 165, 133, 108, 311 | yes | 165, 133, 108, 311 | None | branch, magick_check, item_gate, loot |
| 172 | 222, 257 | yes | 222, 257 | None | branch |
| 177 | 146, 213, 9 | yes | 146, 213, 9 | None | branch, magick_check, item_gate, wp |
| 180 | 350, 316 | yes | 350, 316 | None | branch, item_gate, wp |
| 183 | 189, 219 | yes | 189, 219 | None | branch, combat |
| 184 | 178, 214 | yes | 178, 214 | None | branch, combat, item_gate, endurance |
| 186 | 37, 45 | yes | 37, 45 | None | branch |
| 190 | 307, 323 | yes | 307, 323 | None | branch, wp |
| 191 | 296, 39 | yes | 296, 39 | None | branch, loot |
| 193 | 142, 175 | yes | 142, 175 | None | branch, item_gate, wp, endurance |
| 194 | 83, 122, 115 | yes | 83, 122, 115 | None | branch, magick_check, item_gate, wp |
| 195 | 280, 308 | yes | 280 | 308 | branch, wp |
| 196 | 278, 291, 102 | yes | 278, 291, 102 | None | branch, magick_check, wp |
| 200 | 113, 137, 151 | yes | 113, 137, 151 | None | branch |
| 203 | 91, 132, 164, 198 | yes | 91, 132, 164, 198 | None | branch, magick_check, wp |
| 204 | 104, 94, 233 | yes | 104, 233 | 94 | branch, item_gate, wp |
| 208 | 295, 289, 181, 234 | yes | 295, 289, 181, 234 | None | branch, magick_check, item_gate |
| 210 | 302, 315 | yes | 302 | 315 | branch |
| 212 | 317, 244 | yes | 317, 244 | None | branch, item_gate, wp |
| 215 | 179, 53 | yes | 179, 53 | None | branch |
| 216 | 290, 301 | yes | 290, 301 | None | branch, combat, endurance |
| 218 | 104, 94 | yes | 104 | 94 | branch, item_gate, loot |
| 220 | 285, 292 | yes | 285, 292 | None | branch, wp |
| 223 | 277, 212 | yes | 277, 212 | None | branch |
| 225 | 194, 159, 148, 18 | yes | 194, 159, 148, 18 | None | branch, magick_check, item_gate |
| 227 | 35, 65, 93 | yes | 35, 65, 93 | None | branch, magick_check, item_gate |
| 231 | 246, 258 | yes | 246, 258 | None | branch |
| 234 | 241, 43 | yes | 241, 43 | None | branch, magick_check, item_gate, endurance |
| 237 | 249, 266, 271 | yes | 249, 266, 271 | None | branch, magick_check, item_gate, wp |
| 238 | 80, 86 | yes | 86 | 80 | branch, random, endurance, loot |
| 239 | 172, 60 | yes | 172, 60 | None | branch |
| 240 | 101, 261 | yes | 101, 261 | None | branch |
| 241 | 4, 43 | yes | 4, 43 | None | branch |
| 242 | 324, 330, 335 | yes | 324, 330 | 335 | branch, item_gate, wp |
| 245 | 205, 154 | yes | 205, 154 | None | branch |
| 247 | 66, 59 | yes | 66, 59 | None | branch |
| 255 | 283, 208 | yes | 283, 208 | None | branch, random, item_gate, wp, loot |
| 257 | 81, 213 | yes | 81, 213 | None | branch |
| 259 | 199, 263 | yes | 199 | 263 | branch, random, endurance, loot |
| 261 | 111, 152 | yes | 111, 152 | None | branch, item_gate, wp |
| 265 | 206, 68 | yes | 206, 68 | None | branch, combat, endurance |
| 268 | 31, 47 | yes | 31, 47 | None | branch |
| 269 | 17, 33 | yes | 17, 33 | None | branch, combat, endurance |
| 270 | 188, 276 | yes | 188, 276 | None | branch, combat, endurance |
| 271 | 284, 44 | yes | 284 | 44 | branch, wp, loot |
| 274 | 294, 134 | yes | 294, 134 | None | branch, magick_check, item_gate |
| 277 | 304, 235 | yes | 304, 235 | None | branch, item_gate, wp |
| 279 | 8, 121 | yes | 8, 121 | None | branch, item_gate |
| 280 | 314, 7, 26, 175 | yes | 314, 7, 26, 175 | None | branch, magick_check, item_gate |
| 284 | 52, 61 | yes | 52, 61 | None | branch |
| 286 | 77, 95, 127 | yes | 77, 95, 127 | None | branch |
| 297 | 225, 234 | yes | 225, 234 | None | branch, loot |
| 300 | 339, 254 | yes | 254 | 339 | branch, wp, endurance |
| 302 | 56, 319 | yes | 56 | 319 | branch, combat, endurance |
| 310 | 5, 2 | yes | 5 | 2 | branch, wp, endurance, loot |
| 311 | 318, 269 | yes | 318, 269 | None | branch |
| 312 | 336, 331, 300 | yes | 336, 331, 300 | None | branch, magick_check, item_gate, endurance |
| 318 | 220, 173 | yes | 220, 173 | None | branch, random, wp, endurance, loot |
| 320 | 334, 125 | yes | 334, 125 | None | branch |
| 321 | 305, 282 | yes | 305, 282 | None | branch, wp |
| 325 | 303, 263, 259 | yes | 303, 259 | 263 | branch, item_gate, wp |
| 327 | 325, 343 | yes | 325, 343 | None | branch, wp |
| 328 | 191, 342, 12 | yes | 191, 342, 12 | None | branch, magick_check, item_gate, wp, endurance |
| 331 | 355, 359 | yes | 355, 359 | None | branch, combat, magick_check, item_gate, wp, endurance, gear_loss |
| 336 | 355, 359 | yes | 355, 359 | None | branch, combat, magick_check, item_gate, wp, endurance, gear_loss |
| 337 | 333, 327, 343 | yes | 333, 327, 343 | None | branch, wp |
| 338 | 120, 138, 341, 349 | yes | 120, 138, 341 | 349 | branch, magick_check, wp |
| 344 | 216, 242 | yes | 216, 242 | None | branch |
| 347 | 338, 332, 275 | yes | 338, 332, 275 | None | branch, magick_check, item_gate, wp |
| 350 | 322, 356 | yes | 356 | 322 | branch, wp, endurance |
| 351 | 328, 346 | yes | 328 | 346 | branch |
| 352 | 195, 238, 256 | yes | 195, 238, 256 | None | branch, wp |
| 353 | 314, 7, 26, 175 | yes | 314, 7, 26, 175 | None | branch, magick_check, item_gate |
| 354 | 337, 343 | yes | 337, 343 | None | branch |
| 358 | 157, 216, 242 | yes | 157, 216, 242 | None | branch, wp |

## Other Reachable Branch Points

- None

## Route-Family Maintenance Notes

- Keep the named route-family table in sync with section audit changes and assistant automation data.
- Rebuild route-smoke scripts from the named families before treating them as source-link proof.
- Endpoint rows marked `needs_classification` remain mandatory human-review stops.
- Route-only choices can stay on the book page; mechanical branches need support data or explicit manual notes.
