# GS Book 1 Section Audit

Book: Grey Star the Wizard

Method: numerical section-by-section audit from 1 through 350.

This file is the source-of-truth pass for section classification. It records what each section is, what the player can do next, and whether app automation is possible.

Status labels:

- `confirmed`: rule/section behavior is clear enough to build from.
- `needs ruling`: the section is understood, but the project needs a human decision.
- `manual`: the section is best left manual for now.
- `pending`: not audited yet.

## Audit Table

| Section | Section Type | Links | Automation Candidate | Current App Support | Status |
|---:|---|---|---|---|---|
| 1 | Magick-gated route choice | 202, 168 | Prompt Elementalism use if known and WP >= 1: use -> 202, decline/lack -> 168 | Reader links work; assistant prompt automation missing | confirmed |
| 2 | Meal/resource section, then forced route | 24 | Consume exactly 2 Meals or apply -6 Endurance | Meal/missed-meal controls exist, but no section-specific two-meal automation | confirmed |
| 3 | Meal/resource section, companion food loss, route choice | 85, 275 | Resolve personal Meal requirement, then remove up to 2 remaining Meals for companions | Meal/missed-meal controls exist, but no section-specific companion Meal automation | confirmed |
| 4 | Forced Willpower drain, then forced route | 350 | Set Willpower to 0 | WP controls exist, but no section-specific automation | confirmed |
| 5 | Staff result with Endurance loss, then forced route | 42 | Apply -2 WP and -3 END after legal source Staff choice; source route should require WP >= 2 | WP/END controls exist, but no section-specific automation | confirmed |
| 6 | Forced Endurance loss, then forced route | 325 | Apply -4 Endurance | END controls exist, but no section-specific automation | confirmed |
| 7 | Narrative forced route | 270 | None | Reader link works | confirmed |
| 8 | Plain route choice | 14, 19 | None | Reader links work | confirmed |
| 9 | Death ending | none | Mark terminal/death state | Reader displays deadend text; assistant death-state automation missing | confirmed |
| 10 | Item-gated route choice | 51, 90 | Check Kazim Stone: has -> 51, lacks -> 90 | Inventory controls exist, but no section-specific item gate prompt | confirmed |
| 11 | Forced Willpower loss, then route choice | 300, 66, 20 | Apply -1 Willpower, allowing negative WP, then choose response | WP controls exist, but no section-specific automation | confirmed |
| 12 | Forced Willpower loss, then forced route | 325 | Apply -3 Willpower, allowing negative WP | WP controls exist, but no section-specific automation | confirmed |
| 13 | Narrative forced route | 75 | None | Reader link works | confirmed |
| 14 | Death ending | none | Mark terminal/death state | Reader displays deadend text; assistant death-state automation missing | confirmed |
| 15 | Recovery/restoration section, then forced route | 218 | Add floor(current / 2) to END/WP; cap END at starting END; WP uncapped | END/WP controls exist, but no section-specific restoration automation | confirmed |
| 16 | Currency gain, then route choice | 200, 100 | Add 20 Nobles | Nobles controls exist, but no section-specific automation | confirmed |
| 17 | Death ending | none | Mark terminal/death state | Reader displays deadend text; assistant death-state automation missing | confirmed |
| 18 | Item-gated route choice plus plain route choices | 264, 190, 134 | Check Medallion of the Redeemer and Vial of Pink Liquid for 264; otherwise choose route | Inventory controls exist, but no section-specific item gate prompt | confirmed |
| 19 | Item/WP-gated route choice | 35, 46, 59 | Check Torch + Tinderbox route; check optional Staff glow route if WP is available; 46 handles WP cost | Inventory/WP controls exist, but no section-specific gate prompt | confirmed |
| 20 | Death ending | none | Mark terminal/death state | Reader displays deadend text; assistant death-state automation missing | confirmed |
| 21 | Narrative forced route | 39 | None | Reader link works | confirmed |
| 22 | Light-source route choice with optional WP spend | 122, 334 | Darkness -> 122; Torch/Tinderbox -> 334; Staff glow -> apply -1 WP then 334 | Inventory/WP controls exist, but no section-specific light-source prompt | confirmed |
| 23 | Magick-gated route choice plus plain route choices | 92, 137, 321 | Prophecy route if known/usable; stair choices otherwise | Magick controls exist, but no section-specific Magick prompt | confirmed |
| 24 | Plain route choice | 10, 33 | None | Reader links work | confirmed |
| 25 | Plain route choice toward possible item acquisition | 77, 129 | None in this section | Reader links work | confirmed |
| 26 | Plain route choice | 97, 166, 241 | None | Reader links work | confirmed |
| 27 | Narrative forced route | 195 | None | Reader link works | confirmed |
| 28 | Plain route choice | 308, 336 | None | Reader links work | confirmed |
| 29 | Plain route choice | 54, 104 | None | Reader links work | confirmed |
| 30 | Forced Willpower loss, then forced route | 128 | Apply -2 Willpower, allowing negative WP | WP controls exist, but no section-specific automation | confirmed |
| 31 | Optional Magick result with Willpower cost, then forced route | 75 | Apply -1 Willpower after legal Elementalism use | WP controls exist, but no section-specific automation | confirmed |
| 32 | Plain route choice | 107, 57 | None | Reader links work | confirmed |
| 33 | Plain route choice | 10, 69 | None | Reader links work | confirmed |
| 34 | Nobles-gated route choice | 76, 133 | Hand-over route only legal if Nobles > 0; section 133 handles money loss | Nobles controls exist, but no section-specific gate prompt | confirmed |
| 35 | Narrative forced route | 59 | None | Reader link works | confirmed |
| 36 | Plain route choice | 201, 144 | None | Reader links work | confirmed |
| 37 | Loot section, then forced route | 137 | Prompt to add Gaoler's Keys, +3 Nobles, optional Dagger | Item/Nobles controls exist, but no section-specific loot prompt | confirmed |
| 38 | Recovery, Alchemy/item handling, then forced route | 117 | Restore +2 WP and +4 END; handle Laumspur storage/use by Alchemy status | END/WP/item controls exist, but no section-specific recovery/item prompt | confirmed |
| 39 | Plain route choice | 55, 208 | None | Reader links work | confirmed |
| 40 | Magick-gated route choice plus plain route choices | 64, 223, 76, 195 | Prophecy route if known/usable; ordinary route choices otherwise | Magick controls exist, but no section-specific Magick prompt | confirmed |
| 41 | Narrative forced route | 349 | None | Reader link works | confirmed |
| 42 | Weapon-gated crisis route choice | 216, 262, 119 | Staff temporarily out of reach; Jewelled Dagger/other Weapon gates; Shan route always available | Inventory controls exist, but no section-specific weapon gate prompt | confirmed |
| 43 | Loot prompt plus Magick/plain route choices | 143, 68, 118 | Transfer selected items from Shan's Backpack; Prophecy route if known/usable | Item/Magick controls exist, but no section-specific loot/gate prompt | confirmed |
| 44 | Plain route choice | 317, 335 | None | Reader links work | confirmed |
| 45 | Plain route choice | 312, 80 | None | Reader links work | confirmed |
| 46 | Optional Staff-glow result with Willpower cost, then forced route | 35 | Apply -1 Willpower after legal optional Staff use | WP controls exist, but no section-specific automation | confirmed |
| 47 | Forced Endurance loss, then forced route | 146 | Apply -8 Endurance | END controls exist, but no section-specific automation | confirmed |
| 48 | Optional Sorcery result with Willpower cost, then forced route | 75 | Apply -3 Willpower after legal optional Sorcery use | WP controls exist, but no section-specific automation | confirmed |
| 49 | Random-number test with item/WP modifiers | 274, 210 | Roll random number; +1 Silver Charm; +2 if current WP > 10 | Random helper/manual; no section-specific random test automation | confirmed |
| 50 | Plain route choice | 40, 155 | None | Reader links work | confirmed |
| 51 | Item loss, then forced route | 102 | Delete Kazim Stone from Backpack Items | Item controls exist, but no section-specific automation | confirmed |
| 52 | Non-magic Willpower loss, then route choice | 152, 227 | Apply -1 Willpower, allowing negative WP | WP controls exist, but no section-specific automation | confirmed |
| 53 | Optional Prophecy result with Willpower cost, then forced route | 16 | Apply -1 Willpower after legal optional Prophecy use | WP controls exist, but no section-specific automation | confirmed |
| 54 | Magick-gated route choice plus plain route choices | 278, 184, 228, 238 | Prophecy route if known/usable; ordinary direction choices otherwise | Magick controls exist, but no section-specific Magick prompt | confirmed |
| 55 | Magick/Staff-gated route choice plus plain attack choice | 70, 81, 99 | Enchantment route if known and WP >= 2; Staff long-range route if WP >= 2; surprise attack always available | Magick/WP controls exist, but no section-specific prompt | confirmed |
| 56 | Optional Enchantment result with Willpower cost, then route choice | 251, 84 | Apply -2 Willpower after legal optional Enchantment use | WP controls exist, but no section-specific automation | confirmed |
| 57 | Forced Willpower loss, then route choice | 307, 182 | Apply -1 Willpower, allowing negative WP | WP controls exist, but no section-specific automation | confirmed |
| 58 | Recovery, Alchemy/item handling, then route choice | 101, 126 | Restore +3 WP and +6 END; handle Laumspur storage/use by Alchemy status | END/WP/item controls exist, but no section-specific recovery/item prompt | confirmed |
| 59 | Meal requirement and recovery, then forced route | 65 | Eat 1 Meal or lose 3 END; then restore +1 WP and +2 END | Meal/END/WP controls exist, but no section-specific automation | confirmed |
| 60 | Plain route choice | 45, 80 | None | Reader links work | confirmed |
| 61 | Plain route choice | 186, 111, 86 | None | Reader links work | confirmed |
| 62 | Plain route choice | 7, 36 | None | Reader links work | confirmed |
| 63 | Death ending | none | Mark terminal/death state | Reader displays deadend text; assistant death-state automation missing | confirmed |
| 64 | Optional Prophecy result with Willpower cost, then forced route | 195 | Apply -1 Willpower after legal optional Prophecy use | WP controls exist, but no section-specific automation | confirmed |
| 65 | Status/item-gated route choice | 72, 83 | Check worn/applied Yabari Ointment | Item/status controls are manual; no section-specific status gate | confirmed |
| 66 | Forced Endurance and Willpower loss, then forced route | 311 | Apply -3 Endurance and -1 Willpower, allowing negative WP | END/WP controls exist, but no section-specific automation | confirmed |
| 67 | Death ending | none | Mark terminal/death state | Reader displays deadend text; assistant death-state automation missing | confirmed |
| 68 | Forced Endurance loss, then route choice | 293, 118 | Apply -1 Endurance | END controls exist, but no section-specific automation | confirmed |
| 69 | Death ending | none | Mark terminal/death state | Reader displays deadend text; assistant death-state automation missing | confirmed |
| 70 | Optional Enchantment result with Willpower cost, then route choice | 88, 156 | Apply -2 Willpower after legal optional Enchantment use | WP controls exist, but no section-specific automation | confirmed |
| 71 | Loot/recovered money section, then forced route | 195 | Restore money handed to thief, add +10 Nobles, optional Dagger | Item/Nobles controls exist, but no stolen-money automation | confirmed |
| 72 | Narrative forced route | 22 | None | Reader link works | confirmed |
| 73 | Item consumption plus Magick/plain route choices | 92, 80, 45 | Delete Ezeran Acid/contaminated vial; Prophecy route if known/usable | Item/Magick controls exist, but no section-specific automation | confirmed |
| 74 | Item-gated route choice | 194, 219 | Check Coil of Rope | Item controls exist, but no section-specific item gate prompt | confirmed |
| 75 | Narrative forced route | 3 | None | Reader link works | confirmed |
| 76 | Forced Willpower loss, then forced route | 195 | Apply -1 Willpower, allowing negative WP | WP controls exist, but no section-specific automation | confirmed |
| 77 | Item gain, then route choice | 67, 147 | Add Kazim Stone as Backpack Item | Item controls exist, but no section-specific automation | confirmed |
| 78 | Meal requirement and recovery, then forced route | 29 | Eat 1 Meal or lose 3 END; then restore +1 WP and +2 END | Meal/END/WP controls exist, but no section-specific automation | confirmed |
| 79 | Forced Endurance loss, then forced route | 157 | Apply -1 Endurance | END controls exist, but no section-specific automation | confirmed |
| 80 | Plain route choice | 25, 41 | None | Reader links work | confirmed |
| 81 | Optional long-range Staff result with Willpower cost, then route choice | 99, 145 | Apply -2 Willpower after legal optional Staff use | WP controls exist, but no section-specific automation | confirmed |
| 82 | Nobles-gated route choice | 105, 339 | Buy-drink route only legal if Nobles > 0; later section handles cost | Nobles controls exist, but no section-specific gate prompt | confirmed |
| 83 | Optional Staff attack choice plus plain chase choice | 91, 98 | Staff attack route requires current WP >= 1; section 91 handles WP cost | WP controls exist, but no section-specific prompt | confirmed |
| 84 | Forced Willpower loss, then route choice | 196, 224 | Apply -3 Willpower, allowing negative WP | WP controls exist, but no section-specific automation | confirmed |
| 85 | Recovery section, then forced route | 18 | Restore +1 WP and +1 END | END/WP controls exist, but no section-specific automation | confirmed |
| 86 | Narrative forced route | 266 | None | Reader link works | confirmed |
| 87 | Evocation result, item gain, optional loot, then route choice | 125, 137, 212 | Add Amulet Special Item, apply -2 WP, optional Dagger | Item/WP controls exist, but no section-specific automation | confirmed |
| 88 | Optional long-range Staff result plus forced WP spend, then forced route | 189 | Apply total -3 WP; source attack requires WP >= 2; second mandatory WP can go negative | WP controls exist, but no section-specific automation | confirmed |
| 89 | Narrative forced route | 241 | None | Reader link works | confirmed |
| 90 | Sorcery/Staff-gated route choice | 139, 123 | Sorcery shield route requires Sorcery and WP >= 2; attack route requires WP >= 1 | Magick/WP controls exist, but no section-specific prompt | confirmed |
| 91 | Staff attack result plus light-source choice | 122, 141 | Apply -1 WP for attack; optional Staff light applies another -1 WP; Torch/Tinderbox light has no WP cost | WP/item controls exist, but no section-specific light prompt | confirmed |
| 92 | Prophecy information branch | return to caller | Apply -1 WP and return to noted section | WP controls exist, but no return-section automation | confirmed |
| 93 | Narrative forced route | 258 | None | Reader link works | confirmed |
| 94 | Forced Staff attack result | 215 | Apply -1 WP, allowing negative WP | WP controls exist, but no section-specific automation | confirmed |
| 95 | Sorcery commitment choice | 109, 172 | Route Sorcery attempt to 109; decline/lack reserves returns to 172 | Magick/WP controls exist, but no section-specific prompt | confirmed |
| 96 | Staff reaction result, then forced route | 146 | Apply -2 WP and -2 END | WP/END controls exist, but no section-specific automation | confirmed |
| 97 | Plain route choice | 241, 89 | None | Reader links work | confirmed |
| 98 | Light-source route choice | 108, 115, 122 | Torch/Tinderbox route free; Staff glow requires WP >= 1 and target 115 applies cost | Item/WP controls exist, but no section-specific light prompt | confirmed |
| 99 | Combat with post-combat route choice | 88, 94 | Fight Shadakine Crossbowmen CS 25 END 32 with +4 CS; route 88 requires WP >= 2 after victory | Combat controls exist, but no post-combat gate automation | confirmed |
| 100 | Plain route choice | 40, 121 | None | Reader links work | confirmed |
| 101 | Staff attack result and limited survival combat | 130 | Apply -2 WP; run five-round survival combat vs sequential Najin; Shan's borrowed weapon returns after combat | WP/combat/item controls exist, but no round-limit or loan/return automation | confirmed |
| 102 | Forced Willpower loss, then forced route | 149 | Apply -2 WP, allowing negative WP | WP controls exist, but no section-specific automation | confirmed |
| 103 | Death ending | none | Mark terminal/death state | Reader displays deadend text; assistant death-state automation missing | confirmed |
| 104 | Staff-action route choice | 248, 179 | Route 179 requires WP >= 1; target sections handle costs | WP controls exist, but no section-specific route gate prompt | confirmed |
| 105 | Prophecy-gated route choice plus ordinary conversation choices | 313, 79, 131, 209 | Prophecy route requires Prophecy and WP >= 1; target 313 applies cost | Magick/WP controls exist, but no section-specific prompt | confirmed |
| 106 | Narrative forced route | 117 | None | Reader link works | confirmed |
| 107 | Forced Staff attack result, then route choice | 307, 182 | Apply -2 WP, allowing negative WP | WP controls exist, but no section-specific automation | confirmed |
| 108 | Torchlight forced route | 135 | No WP cost or item deletion confirmed | Reader link works; no light-source status automation | confirmed |
| 109 | Sorcery result with resource loss and route choice | 243, 333 | Apply total -4 WP and -1 END; section 172 footnote can allow negative WP | WP/END controls exist, but no section-specific automation | confirmed |
| 110 | Hidden puzzle-solution forced route | 190 | None | Reader link works | confirmed |
| 111 | Optional Staff attack result, then forced route | 266 | Apply -2 WP after legal source attack | WP controls exist, but no section-specific automation | confirmed |
| 112 | Enchantment-gated route choice plus ordinary choices | 84, 56, 28 | Enchantment route requires Enchantment and WP >= 2; target 56 applies cost | Magick/WP controls exist, but no section-specific prompt | confirmed |
| 113 | Plain route choice | 138, 188 | None | Reader links work | confirmed |
| 114 | Sorcery result plus Prophecy branch and route choice | 92, 80, 45 | Apply -2 WP for Sorcery; Prophecy branch requires Prophecy and WP >= 1 | WP/Magick controls exist, but no Prophecy return automation | confirmed |
| 115 | Staff-light result, then forced route | 135 | Apply -1 WP and mark Staff light active if tracked | WP controls exist, but no light-source status automation | confirmed |
| 116 | Sorcery shield result with follow-up route choice | 150, 226 | Apply -2 WP before choice; route 150 spends another -2 WP before navigation | WP controls exist, but no branch-cost automation | confirmed |
| 117 | Forced Staff attack result followed by combat | 164 | Apply -1 WP, allowing negative WP; fight 2 Shadakine Warriors CS 15 END 25 | WP/combat controls exist, but no section-specific automation | confirmed |
| 118 | Forced Endurance loss, then route choice | 268, 293 | Apply -1 END | END controls exist, but no section-specific automation | confirmed |
| 119 | Forced Endurance loss, then forced route | 128 | Apply -2 END | END controls exist, but no section-specific automation | confirmed |
| 120 | Forced Staff attack result and limited survival combat | 189 | Apply -1 WP, allowing negative WP; survive three rounds vs Shadakine Rearguard CS 25 END 30 with +3 CS | WP/combat controls exist, but no round-limit automation | confirmed |
| 121 | Staff-gated route choice | 265, 300 | Attack route requires WP >= 1; target 265 applies cost | WP controls exist, but no section-specific prompt | confirmed |
| 122 | Death ending | none | Mark terminal/death state | Reader displays deadend text; assistant death-state automation missing | confirmed |
| 123 | Optional Staff attack result, then forced route | 149 | Apply -1 WP after legal source attack | WP controls exist, but no section-specific automation | confirmed |
| 124 | Enchantment result with route choice | 243, 23, 333 | Apply -2 WP, allowing negative WP by section 172 footnote | WP controls exist, but no section-specific automation | confirmed |
| 125 | Optional Special Item gain plus route choice | 137, 212, 333 | Optionally add Gaoler's Keys as a Special Item | Item controls exist, but no section-specific prompt | confirmed |
| 126 | Plain route choice | 161, 106 | None | Reader links work | confirmed |
| 127 | Plain route choice | 50, 40 | None | Reader links work | confirmed |
| 128 | Magick/item-gated route choice | 181, 206, 12 | Elementalism route requires WP >= 1; Enchantment route requires Calacena Mushrooms; targets handle costs/items | Magick/WP/item controls exist, but no route gate automation | confirmed |
| 129 | Plain route choice | 67, 147 | None | Reader links work | confirmed |
| 130 | Narrative forced route | 106 | None | Reader link works | confirmed |
| 131 | Narrative forced route | 300 | None | Reader link works | confirmed |
| 132 | Optional long-range Staff result, then forced route | 203 | Apply -2 WP after legal source Staff attack | WP controls exist, but no section-specific automation | confirmed |
| 133 | Money handover and combat with evade option | 27, 71 | Store current Nobles as stolen, set Nobles to 0; fight Cut-throat CS 10 END 12; evade after 2 rounds if alive | Nobles/combat controls exist, but no stolen-money or timed-evade automation | confirmed |
| 134 | Narrative forced route | 58 | None | Reader link works | confirmed |
| 135 | Narrative forced route into combat section | 197 | None in this section | Reader link works | confirmed |
| 136 | Prophecy-gated route choice | 345, 61 | Prophecy route requires Prophecy and WP >= 1; target 345 applies cost | Magick/WP controls exist, but no section-specific prompt | confirmed |
| 137 | Prophecy branch plus plain route choices | 92, 142, 163 | Prophecy branch requires Prophecy and WP >= 1, with return marker to 137 | Magick/WP controls exist, but no Prophecy return automation | confirmed |
| 138 | Death ending | none | Mark terminal/death state | Reader displays deadend text; assistant death-state automation missing | confirmed |
| 139 | Optional Sorcery result, then forced route | 149 | Apply -2 WP after legal source Sorcery choice; mark Sorcery shield active for section 149 | WP controls exist, but no section-specific automation | confirmed |
| 140 | Plain route choice | 112, 280 | None | Reader links work | confirmed |
| 141 | Narrative forced route into combat section | 197 | None in this section | Reader link works | confirmed |
| 142 | Item/Magick-gated locked-door route choice | 286, 159, 170, 163 | Gaoler's Keys route requires keys; Sorcery route requires Sorcery; Alchemy route requires Alchemy | Item/Magick controls exist, but no section-specific gate prompt | confirmed |
| 143 | Optional Prophecy result with resource loss, then route choice | 68, 118 | Apply -1 WP and -1 END after legal source Prophecy choice | WP/END controls exist, but no section-specific automation | confirmed |
| 144 | Narrative forced route | 172 | None | Reader link works | confirmed |
| 145 | Staff-gated route choice plus ordinary choices | 132, 99, 169 | Long-range Staff route requires WP >= 2; target 132 applies cost | WP controls exist, but no section-specific prompt | confirmed |
| 146 | Staff-gated route choice | 158, 232 | Staff bolt route requires WP >= 1; target 158 applies cost | WP controls exist, but no section-specific prompt | confirmed |
| 147 | Plain route choice | 221, 63 | None | Reader links work | confirmed |
| 148 | Plain route choice | 49, 233 | None in this section | Reader links work | confirmed |
| 149 | Special limited combat with per-round drain | 165 | Fight Kleasa CS 25 END 30; per round lose 1 WP and 2 END, or 1 END if Sorcery shield active; WP drain may go negative | Combat controls exist, but no per-round drain or limited-combat automation | confirmed |
| 150 | Forced resource loss with status-gated route | 348, 237 | Apply -4 WP allowing negative WP and -2 END; route by post-loss WP or Magic Talisman | WP/END/item controls exist, but no section-specific conditional route automation | confirmed |
| 151 | Alchemy ingredient-gated route choice | 297, 172 | Check Sulphur, Saltpetre, Ezeran Crystals, and empty vial; target 297 handles brewing | Inventory controls exist, but no recipe gate automation | confirmed |
| 152 | Plain route choice | 252, 277, 302 | None | Reader links work | confirmed |
| 153 | Sorcery-gated route choice | 185, 198 | Sorcery route requires Sorcery and WP >= 1; target 185 applies cost | Magick/WP controls exist, but no section-specific prompt | confirmed |
| 154 | Combat with one-round evade option | 4, 103 | Fight Cave Mantiz CS 15 END 18; may evade after 1 round | Combat controls exist, but timed evade requires manual handling | confirmed |
| 155 | Death ending | none | Mark terminal/death state | Reader displays deadend text; assistant death-state automation missing | confirmed |
| 156 | Plain route choice | 215, 120 | None in this section; targets handle combat/costs | Reader links work | confirmed |
| 157 | Alchemy-gated forced route | 183, 26 | Route to apothecary if Alchemy known; otherwise 26 | Magick controls exist, but no section-specific prompt | confirmed |
| 158 | Optional Staff attack result, then forced route | 232 | Apply -1 WP after legal source Staff choice | WP controls exist, but no section-specific automation | confirmed |
| 159 | Sorcery commitment and alternate route choice | 114, 170, 163 | Sorcery route requires Sorcery and WP >= 2; Alchemy route requires Alchemy | Magick/WP controls exist, but no section-specific prompt | confirmed |
| 160 | Item consumption, then forced route | 301 | Consume one Laumspur item/vial | Item controls exist, but no section-specific automation | confirmed |
| 161 | Loot prompt plus Alchemy-gated forced route | 193, 15 | Optional Jnana gifts; Laumspur later restores 3 END each; route by Alchemy status | Item/Magick controls exist, but no section-specific loot prompt | confirmed |
| 162 | Optional long-range Staff result, then forced route | 255 | Apply -2 WP after legal source Staff choice | WP controls exist, but no section-specific automation | confirmed |
| 163 | Narrative forced route | 333 | None | Reader link works | confirmed |
| 164 | Loot section, then forced route | 39 | Gain 10 Nobles; optionally add up to 2 Meals and one Sword | Item/Nobles controls exist, but no section-specific loot prompt | confirmed |
| 165 | Forced resource loss with status-gated route | 177, 192 | Apply -5 WP allowing negative WP and -5 END; route by post-loss WP if alive | WP/END controls exist, but no section-specific conditional route automation | confirmed |
| 166 | Plain route choice | 241, 11 | None | Reader links work | confirmed |
| 167 | Staff-gated route choice | 162, 180 | Long-range Staff route requires WP >= 2; target 162 applies cost | WP controls exist, but no section-specific prompt | confirmed |
| 168 | Meal requirement plus fixed Endurance loss, then forced route | 140 | Consume 2 Meals if available; lose 3 END per missing Meal; also lose 1 END fatigue | Meal/END controls exist, but no section-specific two-meal automation | confirmed |
| 169 | Narrative forced route | 203 | None | Reader link works | confirmed |
| 170 | Item/Sorcery-gated route choice | 73, 159, 163 | Ezeran Acid route requires acid; Sorcery fallback requires Sorcery | Item/Magick controls exist, but no section-specific gate prompt | confirmed |
| 171 | Loot section, then forced route | 137 | Gain 5 Nobles; optionally add Sword | Item/Nobles controls exist, but no section-specific loot prompt | confirmed |
| 172 | Forced Magick-selection hub | 95, 124, 271, 151, 236, 211, 250 | Present known Powers; section footnote allows target costs to drive WP negative | Magick/WP controls exist, but no section-specific forced-power menu | confirmed |
| 173 | Death ending | none | Mark terminal/death state | Reader displays deadend text; assistant death-state automation missing | confirmed |
| 174 | Narrative forced route | 148 | None | Reader link works | confirmed |
| 175 | Sorcery/WP resistance route choice | 191, 116, 226 | Destroy route requires Sorcery and WP >= 2; shield route requires Sorcery and WP >= 2; WP duel always available | Magick/WP controls exist, but no section-specific prompt | confirmed |
| 176 | Item-gated route choice | 153, 60 | Gaoler's Keys route optional; target 153 handles follow-up Sorcery gate | Item controls exist, but no section-specific gate prompt | confirmed |
| 177 | Death ending | none | Mark terminal/death state | Reader displays deadend text; assistant death-state automation missing | confirmed |
| 178 | Item-gated route choice | 160, 93 | Laumspur route requires one Laumspur; target 160 consumes it | Item controls exist, but no section-specific prompt | confirmed |
| 179 | Staff attack result with follow-up Staff/WP route choice | 285, 240 | Apply -1 WP on entry; route 285 requires WP >= 2 after that and target 285 applies cost | WP controls exist, but no section-specific prompt | confirmed |
| 180 | Narrative forced route | 255 | None | Reader link works | confirmed |
| 181 | Optional Elementalism result, then forced route | 325 | Apply -1 WP after legal source Elementalism choice | WP controls exist, but no section-specific automation | confirmed |
| 182 | Narrative forced route | 249 | None | Reader link works | confirmed |
| 183 | Shop/purchase prompt, then forced route | 26 | Purchase available alchemy goods with Nobles; Laumspur later restores 3 END each; Tarama Seeds are Special Items | Item/Nobles controls exist, but no section-specific shop prompt | confirmed |
| 184 | Narrative forced route | 325 | None | Reader link works | confirmed |
| 185 | Optional Sorcery result with route choice | 80, 253 | Apply -1 WP after legal source Sorcery choice | WP controls exist, but no section-specific automation | confirmed |
| 186 | Narrative forced route | 86 | None | Reader link works | confirmed |
| 187 | Origin/status-gated route choice | 230, 261 | Route by whether arrested at Inn of the Laughing Moon | Status tracking is manual; no section-specific gate prompt | confirmed |
| 188 | Narrative forced route | 8 | None | Reader link works | confirmed |
| 189 | Combat with Shan modifier | 215 | Fight Shadakine Officer CS 25 END 26 to death; add +3 CS | Combat controls exist, but no section-specific modifier automation | confirmed |
| 190 | Plain route choice | 38, 21 | None | Reader links work | confirmed |
| 191 | Sorcery/WP spending route choice | 323, 314, 288 | Spend 2, 3, or 4 WP before routing; route 323 additionally requires enough remaining WP for section 323's immediate and mandatory costs, route 314 additionally requires 1 WP remaining for section 314, and route 288 additionally requires 2 WP remaining for section 288 | WP controls exist, but no section-specific prompt | confirmed |
| 192 | Narrative forced route | 276 | None | Reader link works | confirmed |
| 193 | Alchemy loot prompt, then forced route | 15 | Optionally take alchemy items; Tarama Seeds are Special Items; Yabari Ointment can create worn status later | Item controls exist, but no section-specific loot prompt | confirmed |
| 194 | Coil of Rope result, then forced route | 269 | Source route requires Coil of Rope; no Rope deletion here | Reader link works | confirmed |
| 195 | Plain route choice | 157, 82 | None | Reader links work | confirmed |
| 196 | Plain route choice | 50, 40 | None | Reader links work | confirmed |
| 197 | Combat, no evade | 213 | Fight Soldier Mantiz CS 15 END 10 to death | Combat controls exist | confirmed |
| 198 | Plain route choice | 80, 225 | None | Reader links work | confirmed |
| 199 | Magick/WP-gated route choice | 31, 48, 244 | Elementalism route requires Elementalism and WP >= 1; Sorcery route requires Sorcery and WP >= 3; target sections apply costs | Magick/WP controls exist, but no section-specific prompt | confirmed |
| 200 | Prophecy-gated route choice | 64, 223, 76, 195 | Prophecy route requires Prophecy and WP >= 1; target 64 applies cost | Magick/WP controls exist, but no section-specific prompt | confirmed |
| 201 | Recovery, then forced route | 172 | Restore +1 END capped at starting END and +1 WP uncapped | END/WP controls exist, but no section-specific automation | confirmed |
| 202 | Optional Elementalism result, then forced route | 140 | Apply -1 WP after legal source Elementalism choice | WP controls exist, but no section-specific automation | confirmed |
| 203 | Combat with companion modifier | 156 | Fight 2 Shadakine Crossbowmen CS 15 END 18 to death; add +4 CS | Combat controls exist, but no section-specific modifier automation | confirmed |
| 204 | Forced Staff/WP cost with follow-up attack choice | 329, 279, 304 | Apply -2 WP; footnote permits negative WP or END substitution for missing WP; optional route 329 requires WP >= 1 after the initial cost | WP/END controls exist, but no footnote-choice automation | confirmed |
| 205 | Combat with modifier and evade | 163, 176 | Fight Shadakine Warrior CS 11 END 15; add +5 CS; evade any time to 163 | Combat controls exist, but no section-specific modifier automation | confirmed |
| 206 | Item consumption, then forced route | 325 | Consume Calacena Mushrooms after legal source choice | Item controls exist, but no section-specific automation | confirmed |
| 207 | Death ending | none | Mark terminal/death state | Reader displays deadend text; assistant death-state automation missing | confirmed |
| 208 | Staff/WP-gated route choice | 81, 99 | Long-range Staff route requires WP >= 2; target 81 applies cost | WP controls exist, but no section-specific prompt | confirmed |
| 209 | Loot prompt with route choice | 131, 157 | Optionally add Vial of Pink Liquid and Medallion of the Redeemer, then choose drink or leave | Item controls exist, but no section-specific loot prompt | confirmed |
| 210 | Forced END loss, then forced route | 74 | Apply -2 END | END controls exist, but no section-specific automation | confirmed |
| 211 | Prophecy result with Evocation-gated route choice | 250, 172 | Apply -1 WP using section 172 negative-WP exception; route 250 requires Evocation and no prior Evocation attempt | Magick/WP controls exist, but no section-specific prompt | confirmed |
| 212 | Plain route choice | 309, 137 | None | Reader links work | confirmed |
| 213 | Plain route choice | 267, 272, 284 | None | Reader links work | confirmed |
| 214 | Prophecy-gated route choice | 92, 176, 45 | Prophecy route requires Prophecy and WP >= 1; note return section 214 | Magick/WP controls exist, but no section-specific prompt | confirmed |
| 215 | Forced WP cost plus loot, then forced route | 2 | Apply -1 WP; footnote permits negative WP or END substitution for missing WP; optional herbwarden loot | WP/item controls exist, but no section-specific loot prompt | confirmed |
| 216 | Death ending | none | Mark terminal/death state | Reader displays deadend text; assistant death-state automation missing | confirmed |
| 217 | Forced Nobles loss, then forced route | 105 | Pay 5 Nobles; source route should require Nobles >= 5 | Nobles controls exist, but no section-specific automation | confirmed |
| 218 | Narrative forced route | 39 | None | Reader link works | confirmed |
| 219 | Companion status change, then forced route | 294 | Mark Shan dead/absent; no itemized backpack transfer here | Status tracking is manual | confirmed |
| 220 | Death ending | none | Mark terminal/death state | Reader displays deadend text; assistant death-state automation missing | confirmed |
| 221 | Recover gear and optional item placement, then forced route | 292 | Restore access to Staff/Backpack; optionally store Kazim Stone in Backpack if held and space allows | Item/status controls exist, but no section-specific recovery prompt | confirmed |
| 222 | Staff/WP-gated route choice | 239, 246, 260 | Long-range Staff route requires WP >= 2; target 239 applies cost | WP controls exist, but no section-specific prompt | confirmed |
| 223 | Plain route choice | 34, 195 | None | Reader links work | confirmed |
| 224 | Combat, no evade | 127 | Fight Shadakine Warrior CS 13 END 20 to death | Combat controls exist | confirmed |
| 225 | Death ending | none | Mark terminal/death state | Reader displays deadend text; assistant death-state automation missing | confirmed |
| 226 | Willpower/CS calculation route | 295, 320 | Calculate 50 - (current WP + current CS); 15+ -> 295, 14 or less -> 320 | Manual calculation only; no section-specific automation | confirmed |
| 227 | Narrative forced route | 29 | None | Reader link works | confirmed |
| 228 | Plain route choice | 328, 6 | None | Reader links work | confirmed |
| 229 | Staff attack result with follow-up route choice | 5, 30 | Apply -2 WP with footnote options; route 5 requires WP >= 2 after that; route 30 has its own insufficiency footnote | WP/END controls exist, but no footnote-choice automation | confirmed |
| 230 | Narrative forced route | 291 | None | Reader link works | confirmed |
| 231 | Combat with defensive penalty | 256 | Fight Quoku CS 12 END 30 to death; subtract 2 CS for this combat | Combat controls exist, but no section-specific modifier automation | confirmed |
| 232 | Narrative forced route | 154 | None | Reader link works | confirmed |
| 233 | Narrative forced route | 337 | None | Reader link works | confirmed |
| 234 | Narrative forced route | 197 | None | Reader link works | confirmed |
| 235 | Optional Psychomancy result, then forced route | 214 | Apply -1 WP after legal source Psychomancy choice | WP controls exist, but no section-specific automation | confirmed |
| 236 | Psychomancy result, then forced return | 172 | Apply -1 WP using section 172 negative-WP exception | WP controls exist, but no section-specific automation | confirmed |
| 237 | Failure ending | none | Mark terminal/failed state | Reader displays deadend text; assistant ending automation missing | confirmed |
| 238 | Plain route choice | 303, 104 | None | Reader links work | confirmed |
| 239 | Staff result with route choice | 267, 272, 284 | Apply -2 WP after legal source Staff choice; source route requires WP >= 2 | WP controls exist, but no section-specific automation | confirmed |
| 240 | Narrative forced route | 204 | None | Reader link works | confirmed |
| 241 | Plain route choice | 300, 66, 20 | None | Reader links work | confirmed |
| 242 | END/WP calculation route | 341, 316 | Add current END + current WP; 20+ -> 341, 19 or less -> 316 | Manual calculation only; no section-specific automation | confirmed |
| 243 | Combat with modifier, optional loot, route choice | 125, 338, 333 | Fight Gaoler CS 8 END 14 to death; add +4 CS; may keep Dagger after victory | Combat/item controls exist, but no section-specific modifier/loot automation | confirmed |
| 244 | Plain route choice | 167, 13 | None | Reader links work | confirmed |
| 245 | Gear recovery, then forced route | 292 | Restore Wizard's Staff, Backpack, and Backpack Items | Item/status controls exist, but no section-specific recovery prompt | confirmed |
| 246 | Combat, no evade | 290 | Fight Soldier Mantiz CS 14 END 10 to death | Combat controls exist | confirmed |
| 247 | Narrative forced route | 62 | None | Reader link works | confirmed |
| 248 | Staff result with follow-up route choice | 204, 229, 254 | Apply -1 WP with footnote options; route 254 requires WP >= 2 after that | WP/END controls exist, but no footnote-choice automation | confirmed |
| 249 | Plain route choice | 282, 257 | None | Reader links work | confirmed |
| 250 | Evocation attempt route choice | 326, 305 | Mark Evocation attempted; no WP cost stated here | Status tracking is manual; reader links work | confirmed |
| 251 | Enchantment result route choice | 50, 40 | No new cost; source Enchantment cost already paid | Reader links work | confirmed |
| 252 | Meal loot, then forced route | 327 | Add up to 5 Meals, respecting carrying limits | Meal/item controls exist, but no section-specific loot prompt | confirmed |
| 253 | Plain route choice | 80, 324 | None | Reader links work | confirmed |
| 254 | Staff result, then forced route | 279 | Apply -2 WP after legal source Staff choice; source route requires WP >= 2 | WP controls exist, but no section-specific automation | confirmed |
| 255 | Combat, no evade | 75 | Fight 2 Shadakine Warriors CS 15 END 25 to death | Combat controls exist | confirmed |
| 256 | Plain route choice | 281, 107 | None | Reader links work | confirmed |
| 257 | Forced WP cost, then forced route | 174 | Apply -1 WP with footnote options | WP/END controls exist, but no footnote-choice automation | confirmed |
| 258 | Narrative forced route | 62 | None | Reader link works | confirmed |
| 259 | Mental combat with fixed derived CS | 296 | Starting mental CS = current WP + current END; damage reduces END; mental CS stays fixed for the fight | Combat controls exist, but no section-specific mental combat automation | confirmed |
| 260 | Combat, no evade | 213 | Fight 2 Soldier Mantiz CS 18 END 20 to death | Combat controls exist | confirmed |
| 261 | Narrative forced route | 291 | None | Reader link works | confirmed |
| 262 | Death ending | none | Mark terminal/death state | Reader displays deadend text; assistant death-state automation missing | confirmed |
| 263 | Narrative forced route | 146 | None | Reader link works | confirmed |
| 264 | Item consumption plus hidden puzzle route | 110, 190, 134 | Requires Medallion + Vial from source; delete Vial of Pink Liquid; hidden solved route ->110 | Item controls exist, but no puzzle automation | confirmed |
| 265 | Staff result plus combat | 40 | Apply -1 WP after legal source Staff choice; fight Shadakine Warrior CS 14 END 18 to death | WP/combat controls exist, but no section-specific automation | confirmed |
| 266 | Plain route choice | 330, 231 | None | Reader links work | confirmed |
| 267 | Plain route choice | 332, 340, 347 | None | Reader links work | confirmed |
| 268 | Forced END loss, then route choice | 8, 113 | Apply -1 END | END controls exist, but no section-specific automation | confirmed |
| 269 | Item loss, then forced route | 294 | Delete Coil of Rope | Item controls exist, but no section-specific automation | confirmed |
| 270 | Recovery, then route choice | 201, 144 | Restore +1 WP uncapped and +3 END capped at starting END | END/WP controls exist, but no section-specific automation | confirmed |
| 271 | Elementalism result forced route | 273 | Source section 172 route requires Elementalism; cost is applied in section 273 | Reader link works | confirmed |
| 272 | Forced END loss plus timed combat | 322, 315 | Apply -2 END; fight 2 Soldier Mantiz CS 20 END 15; win within 3 rounds ->322, fourth round ->315 | END/combat controls exist, but no timed-combat automation | confirmed |
| 273 | Forced WP cost, then forced route | 259 | Apply -1 WP with section 172 forced-power footnote options | WP/END controls exist, but no footnote-choice automation | confirmed |
| 274 | Narrative forced route | 306 | None | Reader link works | confirmed |
| 275 | Narrative forced route | 18 | None | Reader link works | confirmed |
| 276 | Companion loss narrative forced route | 52 | Mark Tanith lost/dead/unavailable | Reader link works; no companion-state automation | confirmed |
| 277 | Narrative forced route | 252 | None | Reader link works | confirmed |
| 278 | Prophecy result forced route | 184 | Source section 54 route requires Prophecy and WP >= 1; apply -1 WP | WP controls exist, but no section-specific automation | confirmed |
| 279 | Forced WP cost, then forced route | 128 | Apply -1 WP with explicit insufficient-WP footnote options | WP/END controls exist, but no footnote-choice automation | confirmed |
| 280 | Prophecy-gated route choice | 53, 16, 100 | No immediate state; Prophecy route points to section 53 cost; sell-boat route points to section 16 Nobles gain | Reader links work | confirmed |
| 281 | One-round combat with CS modifier and WP threshold route | 331, 32 | Fight 1 round vs Large Quoku CS 15 END 30 at -1 CS; after round, WP >=10 ->331, WP <10 ->32 | Combat/WP controls exist, but no one-round combat automation | confirmed |
| 282 | Narrative forced route | 148 | None | Reader link works | confirmed |
| 283 | Forced END loss, then forced route | 227 | Apply -3 END | END controls exist, but no section-specific automation | confirmed |
| 284 | Item/status check plus combat | 207, 310 | If carrying lit Torch ->207; otherwise fight 4 Soldier Mantiz CS 20 END 25 to death | Item/combat controls exist, but no lit-Torch gate automation | confirmed |
| 285 | Staff result forced route | 128 | Source section 179 route requires WP >= 2 after initial cost; apply -2 WP | WP controls exist, but no section-specific automation | confirmed |
| 286 | Psychomancy gate or random route | 235, 214, 205 | If Psychomancy available ->235; otherwise random even ->214, odd ->205 | Random/manual controls exist; no automated random map | confirmed |
| 287 | Forced END loss, then forced route | 263 | Apply -2 END | END controls exist, but no section-specific automation | confirmed |
| 288 | Extra Sorcery WP cost, then forced route | 320 | Source section 191 route requires 2 WP remaining after 4-point spend; apply extra -2 WP | WP controls exist, but no section-specific automation | confirmed |
| 289 | WP threshold route | 150, 175 | Current WP <15 ->150; current WP >=15 ->175 | Manual threshold check only | confirmed |
| 290 | Plain route choice | 267, 272, 284 | None | Reader links work | confirmed |
| 291 | Gear confiscation narrative forced route | 178 | Mark Wizard's Staff, Backpack, and Backpack Items unavailable; retain non-Backpack items | Item/status controls exist, but no confiscation automation | confirmed |
| 292 | Special Item check route | 346, 199 | Amulet of the Shianti priest ->346; no Amulet ->199 | Item controls exist, but no section-specific gate automation | confirmed |
| 293 | Forced END loss, then route choice | 318, 343 | Apply -1 END | END controls exist, but no section-specific automation | confirmed |
| 294 | Companion loss plus END threshold route | 319, 344 | Mark Shan lost/dead/unavailable; current END <10 ->319, END >=10 ->344 | Threshold/status controls manual | confirmed |
| 295 | Forced END loss, then forced route | 187 | Apply -2 END | END controls exist, but no section-specific automation | confirmed |
| 296 | Narrative forced route | 41 | None | Reader link works | confirmed |
| 297 | Alchemy item conversion, then route choice | 23, 333 | Convert recipe items into Ezeran Acid; remove Sulphur, Saltpetre, Ezeran Crystals, and one empty Vial; add Ezeran Acid and two empty Vials | Item controls exist, but no recipe conversion automation | confirmed |
| 298 | Staff/WP plus END loss forced route | 263 | Source section 340 route requires Staff and WP >=2; apply -2 WP and -2 END | WP/END controls exist, but no section-specific automation | confirmed |
| 299 | Death ending | none | Mark terminal/death state | Reader displays deadend text; assistant death-state automation missing | confirmed |
| 300 | Gear confiscation forced route | 289 | Mark Wizard's Staff, Backpack, and Backpack Items unavailable; retain note of Backpack contents | Item/status controls exist, but no confiscation automation | confirmed |
| 301 | WP gain, then forced route | 247 | Restore +10 WP uncapped | WP controls exist, but no section-specific automation | confirmed |
| 302 | Narrative forced route | 252 | None | Reader link works | confirmed |
| 303 | Forced END loss, then forced route | 325 | Apply -2 END | END controls exist, but no section-specific automation | confirmed |
| 304 | Forced WP cost, then forced route | 128 | Apply -1 WP with explicit insufficient-WP footnote options | WP/END controls exist, but no footnote-choice automation | confirmed |
| 305 | Evocation result WP cost, then forced route | 172 | Apply -2 WP with section 172 forced-power footnote options; Evocation cannot be chosen again | WP/END/status controls exist, but no footnote-choice automation | confirmed |
| 306 | Death ending | none | Mark terminal/death state | Reader displays deadend text; assistant death-state automation missing | confirmed |
| 307 | Narrative forced route | 249 | None | Reader link works | confirmed |
| 308 | Combat with modifier, no evade | 127 | Fight Shadakine Warriors CS 20 END 19 as one enemy; add +4 CS for whole combat | Combat controls exist, but no section-specific modifier automation | confirmed |
| 309 | Combat with timed modifier and evade | 137, 171 | Fight Shadakine Guard CS 12 END 16; add +4 CS for first 2 rounds; may evade any time ->137; victory ->171 | Combat controls exist, but no timed modifier automation | confirmed |
| 310 | Plain route choice | 267, 272 | None | Reader links work | confirmed |
| 311 | Gear confiscation plus END loss forced route | 289 | Mark Wizard's Staff, Backpack, and Backpack Items unavailable; keep contents noted; apply -1 END | Item/status/END controls exist, but no confiscation automation | confirmed |
| 312 | Death ending | none | Mark terminal/death state | Reader displays deadend text; assistant death-state automation missing | confirmed |
| 313 | Prophecy result forced route | 209 | Source section 105 route requires Prophecy and WP >=1; apply -1 WP | WP controls exist, but no section-specific automation | confirmed |
| 314 | Kazim Stone WP/END loss and gated choice | 320, 226, 150 | Apply -1 WP and half-current END loss rounded down; then spend 2 WP ->320, spend 2 WP ->226, or insufficient WP ->150 | WP/END controls exist, but no half-loss or gated-choice automation | confirmed |
| 315 | Death ending | none | Mark terminal/death state | Reader displays deadend text; assistant death-state automation missing | confirmed |
| 316 | Death ending | none | Mark terminal/death state | Reader displays deadend text; assistant death-state automation missing | confirmed |
| 317 | Death ending | none | Mark terminal/death state | Reader displays deadend text; assistant death-state automation missing | confirmed |
| 318 | Death ending | none | Mark terminal/death state | Reader displays deadend text; assistant death-state automation missing | confirmed |
| 319 | Forced END loss, then forced route | 43 | Apply -1 END | END controls exist, but no section-specific automation | confirmed |
| 320 | Kazim Stone forced resource loss | 187 | Apply -4 WP, allowing negative WP under forced-loss ruling, and -4 END | WP/END controls exist, but no section-specific automation | confirmed |
| 321 | Combat with evade | 137, 37 | Fight Gaoler CS 8 END 10; may evade any time ->137; victory ->37 | Combat controls exist; any-time evade still manual | confirmed |
| 322 | Narrative forced route | 267 | None | Reader link works | confirmed |
| 323 | Kazim Stone WP/END loss and gated choice | 299, 226 | Apply -1 WP and half-current END loss rounded down; spend 2 WP ->299 or spend 1 WP ->226 | WP/END controls exist, but no half-loss or gated-choice automation | confirmed |
| 324 | Death ending | none | Mark terminal/death state | Reader displays deadend text; assistant death-state automation missing | confirmed |
| 325 | Narrative forced route | 136 | None | Reader link works | confirmed |
| 326 | Plain route choice | 87, 220 | None | Reader links work | confirmed |
| 327 | Plain route choice | 78, 283 | None | Reader links work | confirmed |
| 328 | Forced END loss, then forced route | 104 | Apply -2 END | END controls exist, but no section-specific automation | confirmed |
| 329 | Staff/WP plus END loss forced route | 42 | Source section 204 route requires WP >=1 after initial cost; apply -1 WP and -4 END | WP/END controls exist, but no section-specific automation | confirmed |
| 330 | Narrative forced route | 256 | None | Reader link works | confirmed |
| 331 | Plain route choice | 307, 182 | None in this section; fight target is section 307, evade target is section 182 | Reader links work | confirmed |
| 332 | Staff/WP threshold route | 96, 9 | Staff available and WP >=2 ->96; otherwise ->9; section 96 applies costs | WP/item controls exist, but no route-gate automation | confirmed |
| 333 | Narrative forced route | 259 | None | Reader link works | confirmed |
| 334 | Plain route choice | 222, 234 | None | Reader links work | confirmed |
| 335 | Companion loss narrative forced route | 294 | Mark Shan lost/dead/unavailable | Status tracking manual | confirmed |
| 336 | Plain route choice | 40, 50 | None | Reader links work | confirmed |
| 337 | Combat, no evade | 44 | Fight Wounded Quoku CS 14 END 18; no evade stated; victory ->44 | Combat controls exist; evade must be disabled | confirmed |
| 338 | Prophecy-gated return-section route choice | 92, 137, 212 | Prophecy route requires Prophecy and WP >=1, routes to 92 and returns here; ordinary choices ->137 or ->212 | Magick/WP controls exist, but no return-section automation | confirmed |
| 339 | Nobles loss, then route choice | 217, 105 | Source section 82 buy-drink route requires Nobles >0; apply -1 Noble, then choose conversation route | Nobles controls exist, but no section-specific automation | confirmed |
| 340 | Staff/WP-gated route choice | 298, 287 | Staff route requires Staff available and WP >=2; target 298 applies costs; jump route ->287 | WP/item controls exist, but no route-gate automation | confirmed |
| 341 | Forced END loss, then forced route | 8 | Apply -1 END | END controls exist, but no section-specific automation | confirmed |
| 342 | Unreachable forced END loss, then forced route | 74 | No normal in-book choice leads here; apply -3 END if reached | END controls exist; unreachable-section marker needed | confirmed |
| 343 | Forced END loss, then route choice | 17, 242 | Apply -1 END, then choose river route | END controls exist, but no section-specific automation | confirmed |
| 344 | Narrative forced route | 43 | None | Reader link works | confirmed |
| 345 | Prophecy result forced route | 61 | Source section 136 route requires Prophecy and WP >=1; apply -1 WP | WP controls exist, but no section-specific automation | confirmed |
| 346 | Narrative forced route | 199 | None | Reader link works | confirmed |
| 347 | Narrative forced route | 47 | None | Reader link works | confirmed |
| 348 | Narrative forced route | 187 | None | Reader link works | confirmed |
| 349 | Gear-recovery encounter route choice | 173, 245 | Tanith has Staff and Backpack, but section 245 handles restoration; no restoration here | Item controls exist, but restoration is route-specific | confirmed |
| 350 | Successful book ending | none | Mark book 1 completed successfully; external hook points to book 2 | Reader displays final text; success-state automation missing | confirmed |

## Confirmed Details

### Section 1

- Type: Magick-gated route choice.
- Check: Elementalism.
- State change: none confirmed.
- Choices:
  - use Elementalism -> 202
  - do not have/use Elementalism -> 168
- Build note: future section prompt should detect whether Elementalism is known and present the legal route choices. Route 202 also requires current Willpower of at least 1 because section 202 applies a 1 WP cost.

### Section 2

- Type: meal/resource section with a forced onward route.
- State change: consume exactly 2 Meals, or lose 6 Endurance.
- Out link: 24.
- Build note: future section automation should prompt for the meal requirement.
- Ruling: literal section logic. If the player cannot consume 2 Meals, apply the full 6 Endurance loss.

### Section 3

- Type: meal/resource section followed by route choice.
- Personal Meal requirement: eat 1 Meal or lose 3 Endurance.
- Companion Meal requirement: the section requires 2 Meals to be given to Tanith and Shan, with local errata confirming the wording "if you have any left."
- Choices:
  - sleep while Tanith and Shan keep watch -> 85
  - take first watch -> 275
- Build note: future section automation should resolve the personal Meal requirement first, then handle the companion Meal loss.
- Ruling: after resolving Grey Star's own Meal, remove up to 2 remaining Meals for Tanith and Shan. If 0 remain, remove 0; if 1 remains, remove 1; if 2 or more remain, remove 2.

### Section 4

- Type: forced Willpower drain with a forced onward route.
- State change: set Willpower to 0.
- Out link: 350.
- Build note: future section automation should offer/apply "use all remaining Willpower" as a section action.

### Section 5

- Type: Staff result and Endurance loss with a forced onward route.
- State change: lose 2 Willpower and 3 Endurance.
- Out link: 42.
- Build note: section 5 has no insufficient-Willpower footnote. Its only source is section 229's optional long-range Staff choice, so section 229 should require current Willpower of at least 2 before this route is legal.
- Ruling note: mandatory/forced Willpower losses can reduce Willpower below 0 where the book or a footnote permits it; this section is source-gated instead.

### Section 6

- Type: forced Endurance loss with a forced onward route.
- State change: lose 4 Endurance.
- Out link: 325.
- Build note: future section automation should offer/apply the heat-exhaustion Endurance loss.

### Section 7

- Type: narrative forced route.
- State change: none confirmed.
- Out link: 270.
- Build note: no automation needed beyond normal navigation.

### Section 8

- Type: plain route choice.
- State change: none confirmed.
- Choices:
  - sleep in the cave -> 14
  - enter the tunnel -> 19
- Build note: no section-specific automation needed beyond normal choice display.

### Section 9

- Type: death ending.
- State change: mark adventure ended/dead.
- Out link: none.
- Build note: future section automation should mark this as a terminal death section.

### Section 10

- Type: item-gated route choice.
- Check: Kazim Stone.
- State change: none confirmed.
- Choices:
  - have Kazim Stone -> 51
  - do not have Kazim Stone -> 90
- Build note: future section prompt should detect inventory/Special Item ownership and present the legal route choices.

### Section 11

- Type: forced Willpower loss followed by route choice.
- State change: lose 1 Willpower, allowing Willpower to fall below 0.
- Choices:
  - surrender -> 300
  - attack -> 66
  - run -> 20
- Build note: future section automation should apply the forced Staff-cost rule, then present the three route choices.

### Section 12

- Type: forced Willpower loss with a forced onward route.
- State change: lose 3 Willpower, allowing Willpower to fall below 0.
- Out link: 325.
- Build note: this section has an explicit footnote offering negative Willpower or Endurance fallback. Use the negative-Willpower book-rule path unless a later section explicitly requires the Endurance fallback.

### Section 13

- Type: narrative forced route.
- State change: none confirmed.
- Out link: 75.
- Build note: no automation needed beyond normal navigation.

### Section 14

- Type: death ending.
- State change: mark adventure ended/dead.
- Out link: none.
- Build note: future section automation should mark this as a terminal death section.

### Section 15

- Type: recovery/restoration section with a forced onward route.
- State change: increase current Endurance and Willpower by half of their current totals, rounding down for odd current totals; Endurance still cannot exceed starting Endurance, while Willpower may exceed its starting value.
- Out link: 218.
- Build note: future section automation needs a restoration action after the rounding rule is decided.
- Ruling: round down. Example: current Willpower 15 restores 7, becoming 22.

### Section 16

- Type: currency gain followed by route choice.
- State change: gain 20 Nobles.
- Choices:
  - enter narrow street -> 200
  - explore harbour front -> 100
- Build note: future section automation should offer/apply the Nobles gain.

### Section 17

- Type: death ending.
- State change: mark adventure ended/dead.
- Out link: none.
- Build note: future section automation should mark this as a terminal death section.

### Section 18

- Type: item-gated route choice plus plain route choices.
- Check: Medallion of the Redeemer and Vial of Pink Liquid.
- State change: none confirmed.
- Choices:
  - have both checked items -> 264
  - take Shan's advice -> 190
  - seek Jnana's counsel -> 134
- Build note: future section prompt should detect whether both required items are present before presenting the 264 route as legal.

### Section 19

- Type: item/WP-gated route choice.
- State change: none in this section; section 46 applies the Staff-glow Willpower cost.
- Choices:
  - have Torch and Tinderbox, and choose to light the Torch -> 35
  - spend 1 Willpower to create Staff glow -> 46
  - lack/decline those options -> 59
- Build note: this is optional magic use, so the Staff-glow choice should only be legal when current Willpower is at least 1. Optional magic cannot be chosen without sufficient Willpower.

### Section 20

- Type: death ending.
- State change: mark adventure ended/dead.
- Out link: none.
- Build note: future section automation should mark this as a terminal death section.

### Section 21

- Type: narrative forced route.
- State change: none confirmed for Grey Star. Shan's short sword is narrative companion gear, not an Action Chart change.
- Out link: 39.
- Build note: no automation needed beyond normal navigation.

### Section 22

- Type: light-source route choice with optional Willpower spend.
- State change options:
  - continue in darkness -> no state change
  - use Torch and Tinderbox -> no resource loss confirmed
  - use Wizard's Staff glow -> lose 1 Willpower
- Choices:
  - continue in darkness -> 122
  - light the way -> 334
- Build note: the `light the way` choice needs a sub-choice/source: Torch/Tinderbox if carried, or Staff glow if current Willpower is at least 1. Optional magic cannot be chosen without sufficient Willpower.

### Section 23

- Type: Magick-gated route choice plus plain route choices.
- Check: Prophecy known and usable.
- State change: none confirmed in this section.
- Choices:
  - use Prophecy -> 92, with return to 23 later
  - take left stairway -> 137
  - take right stairway -> 321
- Build note: future section prompt should support a temporary-information Magick branch that returns to the originating section.

### Section 24

- Type: plain route choice.
- State change: none confirmed.
- Choices:
  - investigate -> 10
  - pretend to sleep -> 33
- Build note: no section-specific automation needed beyond normal choice display.

### Section 25

- Type: plain route choice toward possible item acquisition.
- State change: none in this section; section 77 handles the Kazim Stone pickup if chosen.
- Choices:
  - take Kazim Stone -> 77
  - leave immediately -> 129
- Build note: no state change should be applied until the pickup section confirms it.

### Section 26

- Type: plain route choice.
- State change: none confirmed.
- Choices:
  - act as if nothing has happened -> 97
  - confront the follower -> 166
  - leave the market square and run -> 241
- Build note: no section-specific automation needed beyond normal choice display.

### Section 27

- Type: narrative forced route.
- State change: none confirmed.
- Out link: 195.
- Build note: no automation needed beyond normal navigation.

### Section 28

- Type: plain route choice.
- State change: none confirmed.
- Choices:
  - aid the people -> 308
  - escape under cover of chaos -> 336
- Build note: no section-specific automation needed beyond normal choice display.

### Section 29

- Type: plain route choice.
- State change: none confirmed.
- Choices:
  - move away from the river -> 54
  - keep to the river -> 104
- Build note: no section-specific automation needed beyond normal choice display.

### Section 30

- Type: forced Willpower loss with a forced onward route.
- State change: lose 2 Willpower, allowing Willpower to fall below 0.
- Out link: 128.
- Build note: this section has the standard forced-magic insufficient-WP footnote. Use the negative-Willpower book-rule path unless a later section explicitly requires the Endurance fallback.

### Section 31

- Type: optional Magick result with Willpower cost and a forced onward route.
- State change: lose 1 Willpower.
- Out link: 75.
- Build note: this section is reached from an optional Elementalism choice, so the source choice should only be legal when Elementalism is known and current Willpower is at least 1.

### Section 32

- Type: plain route choice.
- State change: none confirmed.
- Choices:
  - long-range attack on the Quoku -> 107
  - defend Shan -> 57
- Build note: no state change is applied until the chosen target section defines it.

### Section 33

- Type: plain route choice.
- State change: none confirmed.
- Choices:
  - investigate -> 10
  - leave Tanith alone -> 69
- Build note: no section-specific automation needed beyond normal choice display.

### Section 34

- Type: Nobles-gated route choice.
- Check: Nobles greater than 0 for the hand-over route.
- State change: none in this section; section 133 handles handing over the money pouch.
- Choices:
  - no money, or refuse to hand it over -> 76
  - hand over money -> 133
- Build note: future section prompt should only allow the money hand-over route when Grey Star has at least 1 Noble.

### Section 35

- Type: narrative forced route.
- State change: none confirmed. Light is extinguished narratively; no consumable resource loss is stated.
- Out link: 59.
- Build note: no automation needed beyond normal navigation.

### Section 36

- Type: plain route choice.
- State change: none confirmed.
- Choices:
  - sleep to build strength -> 201
  - do not sleep -> 144
- Build note: no section-specific automation needed beyond normal choice display.

### Section 37

- Type: loot section with a forced onward route.
- State change options: add Gaoler's Keys as a Special Item carried in hand; add 3 Nobles; optionally add Dagger as a Weapon.
- Out link: 137.
- Build note: future section automation should show a loot prompt with required/likely pickups and optional weapon pickup. Dagger must respect normal weapon limits.

### Section 38

- Type: recovery and item handling section with a forced onward route.
- State change: restore 2 Willpower and 4 Endurance. Endurance remains capped at starting Endurance; Willpower may exceed starting Willpower.
- Item/Magick handling:
  - if Alchemy is known, Laumspur may be stored in the Herb Pouch
  - if Alchemy is not known, Laumspur must be swallowed while fresh for +4 Endurance and cannot be stored
- Out link: 117.
- Build note: future section automation needs an Alchemy-aware Laumspur prompt. Any Endurance gain from swallowing Laumspur remains capped at starting Endurance.

### Section 39

- Type: plain route choice.
- State change: none confirmed.
- Choices:
  - aid the Knights of the White Mountain -> 55
  - skirt around the battle and cross the road -> 208
- Build note: no section-specific automation needed beyond normal choice display.

### Section 40

- Type: Magick-gated route choice plus plain route choices.
- Check: Prophecy known and usable.
- State change: none in this section.
- Choices:
  - use Prophecy -> 64
  - left alleyway -> 223
  - right alleyway -> 76
  - continue along narrow street -> 195
- Build note: future section prompt should display the optional Prophecy branch only when the power is known and currently usable.

### Section 41

- Type: narrative forced route.
- State change: none confirmed.
- Out link: 349.
- Build note: no automation needed beyond normal navigation.

### Section 42

- Type: weapon-gated crisis route choice.
- Local condition: Wizard's Staff is out of reach for this immediate choice. No permanent deletion from the Action Chart is confirmed.
- State change: none confirmed in this section.
- Choices:
  - have Jewelled Dagger and use it -> 216
  - have any other Weapon except Staff and use it -> 262
  - tell Shan to use his sword -> 119
- Build note: future section prompt should exclude Staff from the valid weapon list for this decision only.

### Section 43

- Type: loot prompt plus Magick/plain route choices.
- Loot available from Shan's Backpack:
  - 3 Meals
  - Small Vial of Laumspur, restores 2 Endurance
  - 2 Torches
  - Coil of Rope
  - Tinderbox
- Storage rule: Shan's Backpack cannot be kept. Chosen items must transfer to Grey Star's Backpack, except the Small Vial of Laumspur may go in the Herb Pouch if Alchemy is known.
- Choices:
  - use Prophecy -> 143
  - explore basin/lake area -> 68
  - search for cliff-scaling route -> 118
- Build note: future section automation needs a capacity-aware loot transfer prompt and an optional Prophecy route.

### Section 44

- Type: plain route choice.
- State change: none confirmed.
- Choices:
  - move Quoku corpse -> 317
  - continue journey around ravine -> 335
- Build note: no section-specific automation needed beyond normal choice display.

### Section 45

- Type: plain route choice.
- State change: none confirmed.
- Choices:
  - open the door -> 312
  - head back to the other stairway -> 80
- Build note: no section-specific automation needed beyond normal choice display.

### Section 46

- Type: optional Staff-glow result with Willpower cost and a forced onward route.
- State change: lose 1 Willpower.
- Out link: 35.
- Build note: this section is reached by choosing optional Staff magic, so the source route should only be legal when current Willpower is at least 1.

### Section 47

- Type: forced Endurance loss with a forced onward route.
- State change: lose 8 Endurance.
- Out link: 146.
- Build note: future section automation should offer/apply the Endurance loss.

### Section 48

- Type: optional Sorcery result with Willpower cost and a forced onward route.
- State change: lose 3 Willpower.
- Out link: 75.
- Build note: this section is reached from an optional Sorcery choice in section 199, so that source choice should require Sorcery and current Willpower of at least 3.

### Section 49

- Type: random-number test with item and Willpower modifiers.
- State change: none confirmed.
- Test:
  - roll a random number
  - add 1 if Silver Charm of Jnana the Wise is carried
  - add 2 if current Willpower is greater than 10
- Outcomes:
  - total 0-6 -> 274
  - total 7-12 -> 210
- Build note: future section automation should calculate the modifiers from state and show the resulting legal route.

### Section 50

- Type: plain route choice.
- State change: none confirmed.
- Choices:
  - dive into the narrow street -> 40
  - stand and fight -> 155
- Build note: no section-specific automation needed beyond normal choice display.

### Section 51

- Type: item loss section with a forced onward route.
- State change: delete Kazim Stone from Backpack Items.
- Out link: 102.
- Build note: future section automation should remove the Kazim Stone when this section is applied.

### Section 52

- Type: non-magic Willpower loss followed by route choice.
- State change: lose 1 Willpower due to traumatic sleep, allowing Willpower to fall below 0.
- Choices:
  - investigate shack -> 152
  - continue journey -> 227
- Build note: book rules allow non-magic Willpower losses to reduce Willpower below 0.
- Ruling: book rules trump house rules; apply the full Willpower loss even if it creates a negative Willpower score.

### Section 53

- Type: optional Prophecy result with Willpower cost and a forced onward route.
- State change: lose 1 Willpower.
- Out link: 16.
- Build note: this section is reached from an optional Prophecy choice, so the source choice should only be legal when Prophecy is known and current Willpower is at least 1.

### Section 54

- Type: Magick-gated route choice plus plain route choices.
- Check: Prophecy known and usable.
- State change: none in this section.
- Choices:
  - use Prophecy -> 278
  - turn left -> 184
  - turn right -> 228
  - continue straight ahead -> 238
- Build note: future section prompt should display the optional Prophecy branch only when the power is known and currently usable.

### Section 55

- Type: Magick/Staff-gated route choice plus plain attack choice.
- State change: none in this section; sections 70 and 81 handle the Willpower costs for the optional Enchantment and long-range Staff routes.
- Choices:
  - use Enchantment -> 70
  - attack with Wizard's Staff at long range -> 81
  - make a surprise attack -> 99
- Build note: section 70 costs 2 Willpower and requires Enchantment; section 81 costs 2 Willpower for long-range Staff use. These optional routes should require current Willpower of at least 2 before choosing them.

### Section 56

- Type: optional Enchantment result with Willpower cost followed by route choice.
- State change: lose 2 Willpower.
- Choices:
  - continue the Enchantment spell -> 251
  - break trance and aid the crowd -> 84
- Build note: this section is reached from an optional Enchantment choice, so the source choice should only be legal when Enchantment is known and current Willpower is at least 2.

### Section 57

- Type: forced Willpower loss followed by route choice.
- State change: lose 1 Willpower, allowing Willpower to fall below 0.
- Choices:
  - attack the Quoku again -> 307
  - escape -> 182
- Build note: this section has the standard forced-magic insufficient-WP footnote. Use the negative-Willpower book-rule path unless a later section explicitly requires the Endurance fallback.

### Section 58

- Type: recovery and item handling section followed by route choice.
- State change: restore 3 Willpower and 6 Endurance. Endurance remains capped at starting Endurance; Willpower may exceed starting Willpower.
- Item/Magick handling:
  - if Alchemy is known, Laumspur may be stored in the Herb Pouch
  - if Alchemy is not known, Laumspur may be swallowed while fresh for +4 Endurance and cannot be stored
- Choices:
  - attack the Najin -> 101
  - wait for them to draw closer -> 126
- Build note: future section automation needs an Alchemy-aware Laumspur prompt. Any Endurance gain from swallowing Laumspur remains capped at starting Endurance. The attack-the-Najin route leads to a section 101 Staff blast costing 2 Willpower, so that source choice should require current Willpower of at least 2.

### Section 59

- Type: Meal requirement and recovery section with a forced onward route.
- State change: eat 1 Meal or lose 3 Endurance; then restore 1 Willpower and 2 Endurance.
- Out link: 65.
- Build note: resolve the Meal requirement before applying the rest recovery. Endurance gains remain capped at starting Endurance; Willpower may exceed starting Willpower.

### Section 60

- Type: plain route choice.
- State change: none confirmed.
- Choices:
  - right-hand stairway -> 45
  - left stairway -> 80
- Build note: no section-specific automation needed beyond normal choice display.

### Section 61

- Type: plain route choice.
- State change: none confirmed.
- Choices:
  - slip past the Quoku -> 186
  - attack nearest Quoku -> 111
  - run for it -> 86
- Build note: the attack route leads to section 111, which spends 2 Willpower on a Staff attack, so that source choice should require current Willpower of at least 2.

### Section 62

- Type: plain route choice.
- State change: none confirmed.
- Choices:
  - attempt conversation with the girl -> 7
  - do not converse -> 36
- Build note: no section-specific automation needed beyond normal choice display.

### Section 63

- Type: death ending.
- State change: mark adventure ended/dead.
- Out link: none.
- Build note: future section automation should mark this as a terminal death section.

### Section 64

- Type: optional Prophecy result with Willpower cost and a forced onward route.
- State change: lose 1 Willpower.
- Out link: 195.
- Build note: this section is reached from optional Prophecy choices, so source choices should only be legal when Prophecy is known and current Willpower is at least 1.

### Section 65

- Type: status/item-gated route choice.
- Check: Yabari Ointment is currently worn/applied.
- State change: none confirmed in this section.
- Choices:
  - wearing Yabari Ointment -> 72
  - not wearing Yabari Ointment -> 83
- Build note: future automation should track applied ointment as a status, not merely as an inventory item.

### Section 66

- Type: forced Endurance and Willpower loss with a forced onward route.
- State change: lose 3 Endurance and 1 Willpower, allowing Willpower to fall below 0.
- Out link: 311.
- Build note: future section automation should apply both resource losses before navigation.

### Section 67

- Type: death ending.
- State change: mark adventure ended/dead.
- Out link: none.
- Build note: future section automation should mark this as a terminal death section.

### Section 68

- Type: forced Endurance loss followed by route choice.
- State change: lose 1 Endurance.
- Choices:
  - continue exploring Lake Shenwu -> 293
  - climb the basin slope and survey the wall -> 118
- Build note: future section automation should apply the Endurance loss before presenting route choices.

### Section 69

- Type: death ending.
- State change: mark adventure ended/dead.
- Out link: none.
- Build note: future section automation should mark this as a terminal death section.

### Section 70

- Type: optional Enchantment result with Willpower cost followed by route choice.
- State change: lose 2 Willpower.
- Choices:
  - fire at remaining bridge enemies from hiding -> 88
  - charge into the fight -> 156
- Build note: this section is reached from an optional Enchantment choice in section 55, so the source choice should only be legal when Enchantment is known and current Willpower is at least 2.

### Section 71

- Type: loot/recovered money section with a forced onward route.
- State change: recover money handed to the thief and gain 10 Nobles; optionally add the thief's Dagger as a Weapon.
- Out link: 195.
- Build note: future section automation may need a temporary `stolenNobles` value from section 133 to restore the handed-over money accurately. Dagger must respect normal weapon limits.

### Section 72

- Type: narrative forced route.
- State change: none confirmed.
- Out link: 22.
- Build note: no automation needed beyond normal navigation.

### Section 73

- Type: item consumption plus Magick/plain route choices.
- State change: delete Ezeran Acid and discard the contaminated vial.
- Choices:
  - use Prophecy -> 92, with return to 73 later
  - take left-hand stairway -> 80
  - take right-hand stairway -> 45
- Build note: future section automation should remove the acid/vial item and preserve a return-section marker for the Prophecy branch.

### Section 74

- Type: item-gated route choice.
- Check: Coil of Rope.
- State change: none confirmed in this section.
- Choices:
  - have Coil of Rope -> 194
  - lack Coil of Rope -> 219
- Build note: future section prompt should detect the Rope item and present the legal route.

### Section 75

- Type: narrative forced route.
- State change: none confirmed.
- Out link: 3.
- Build note: no automation needed beyond normal navigation.

### Section 76

- Type: forced Willpower loss with a forced onward route.
- State change: lose 1 Willpower, allowing Willpower to fall below 0.
- Out link: 195.
- Build note: future section automation should apply the forced Staff-cost rule before navigation.

### Section 77

- Type: item gain followed by route choice.
- State change: add Kazim Stone as a Backpack Item.
- Choices:
  - attack the young girl -> 67
  - question her -> 147
- Build note: section 51 later confirms the Kazim Stone is treated as a Backpack Item when stolen.

### Section 78

- Type: Meal requirement and recovery section with a forced onward route.
- State change: eat 1 Meal or lose 3 Endurance; then restore 1 Willpower and 2 Endurance.
- Out link: 29.
- Build note: resolve the Meal requirement before applying the rest recovery. Endurance gains remain capped at starting Endurance; Willpower may exceed starting Willpower.

### Section 79

- Type: forced Endurance loss with a forced onward route.
- State change: lose 1 Endurance.
- Out link: 157.
- Build note: future section automation should apply the Endurance loss before navigation.

### Section 80

- Type: plain route choice.
- State change: none confirmed.
- Choices:
  - open the glowing door -> 25
  - take the other exit -> 41
- Build note: no section-specific automation needed beyond normal choice display.

### Section 81

- Type: optional long-range Staff result with Willpower cost followed by route choice.
- State change: lose 2 Willpower.
- Choices:
  - follow Shan to protect him -> 99
  - leave Shan to his fate -> 145
- Build note: this section is reached from optional long-range Staff choices, so the source choice should require current Willpower of at least 2.

### Section 82

- Type: Nobles-gated route choice.
- Check: Nobles greater than 0 for the buy-drink route.
- State change: none in this section; later sections handle drink cost/outcome.
- Choices:
  - no money or save money -> 105
  - buy a drink -> 339
- Build note: future section prompt should only allow buying a drink when Grey Star has at least 1 Noble.

### Section 83

- Type: optional Staff attack choice plus plain chase choice.
- State change: none in this section; section 91 handles the Staff attack cost.
- Choices:
  - attack with Wizard's Staff -> 91
  - chase the creature -> 98
- Build note: Staff attack route should require current Willpower of at least 1 before choosing it.

### Section 84

- Type: forced Willpower loss followed by route choice.
- State change: lose 3 Willpower, allowing Willpower to fall below 0.
- Choices:
  - jump to the ground -> 196
  - finish off the remaining warrior -> 224
- Build note: the section forces the Staff attack after arrival; apply book-rule negative Willpower behavior if needed.

### Section 85

- Type: recovery section with a forced onward route.
- State change: restore 1 Willpower and 1 Endurance.
- Out link: 18.
- Build note: Endurance gain remains capped at starting Endurance; Willpower may exceed starting Willpower.

### Section 86

- Type: narrative forced route.
- State change: none confirmed.
- Out link: 266.
- Build note: no automation needed beyond normal navigation.

### Section 87

- Type: Evocation result, item gain, optional loot, and route choice.
- State change: add Amulet as a Special Item; lose 2 Willpower for Evocation; optionally add Dagger as a Weapon.
- Choices:
  - take Gaoler's Keys/free prisoners -> 125
  - take left stairway without delay -> 137
  - take right stairway -> 212
- Build note: this is on the Evocation/dead-priest route. Dagger must respect normal weapon limits.

### Section 88

- Type: optional long-range Staff result plus mandatory follow-up Willpower spend with a forced onward route.
- State change: lose 2 Willpower for the long-range attack, then lose 1 more Willpower for the follow-up attack. The second spend can take Willpower below 0 under book rules.
- Out link: 189.
- Build note: source choices that lead here as optional long-range Staff fire should require current Willpower of at least 2.

### Section 89

- Type: narrative forced route.
- State change: none confirmed.
- Out link: 241.
- Build note: no automation needed beyond normal navigation.

### Section 90

- Type: Sorcery/Staff-gated route choice.
- State change: none in this section; sections 139 and 123 handle Willpower costs.
- Choices:
  - use Sorcery shield -> 139
  - attack Mother Magri's apparition -> 123
- Build note: Sorcery route should require Sorcery and current Willpower of at least 2. Attack route should require current Willpower of at least 1 for the Staff attack in section 123.

### Section 91

- Type: Staff attack result, then light-source route choice.
- State change: lose 1 Willpower for killing the Cave Mantiz. If choosing to light the Staff here, lose 1 additional Willpower and treat the Staff light as active until extinguished. Torch/Tinderbox light has no Willpower cost.
- Choices:
  - proceed in darkness -> 122
  - light your way -> 141
- Build note: the source route from section 83 should require current Willpower of at least 1 for the Staff attack. The Staff-light subchoice in this section should require current Willpower of at least 1 after the attack cost. Torch/Tinderbox and Staff light share the same destination, so the prompt should capture which light source was used before navigating.

### Section 92

- Type: temporary Prophecy information branch.
- State change: lose 1 Willpower for Prophecy.
- Out link: return to the previously noted adventure number.
- Build note: source choices that lead here should require Prophecy and current Willpower of at least 1. This section needs return-section context rather than a fixed destination.

### Section 93

- Type: narrative forced route.
- State change: none confirmed.
- Out link: 258.
- Build note: no automation needed beyond normal navigation.

### Section 94

- Type: forced Staff attack result with a forced onward route.
- State change: lose 1 Willpower, allowing Willpower to fall below 0 under the section footnote/book-rule negative-Willpower path.
- Out link: 215.
- Build note: the footnote offers the alternate Endurance fallback from a later book, but the current project ruling uses the book-permitted negative-Willpower path unless a section explicitly requires otherwise.

### Section 95

- Type: Sorcery commitment choice returning to the section 172 power menu if declined.
- State change: none in this section; section 109 handles the actual cost.
- Choices:
  - force the door with Sorcery -> 109
  - decline/lack sufficient Willpower -> 172
- Build note: section 109 reveals the final cost as 4 Willpower and 1 Endurance. This power menu is governed by the section 172 footnote, which can force a Magical Power choice even when the final Willpower cost exceeds current Willpower. Preserve the book's "unknown cost once begun" warning, and allow the section 109 cost to reduce Willpower below 0 if needed.

### Section 96

- Type: Staff reaction result with forced resource loss and route.
- State change: lose 2 Willpower and 2 Endurance.
- Out link: 146.
- Build note: source section 332 already gates this route to players with at least 2 Willpower for Staff use, so the section 96 Willpower cost should not require negative-Willpower handling in normal play.

### Section 97

- Type: plain route choice.
- State change: none confirmed.
- Choices:
  - run from the market square -> 241
  - lose yourself in the crowd -> 89
- Build note: no section-specific automation needed beyond normal choice display.

### Section 98

- Type: light-source route choice.
- State change: none in this section; section 115 applies the Staff-light Willpower cost.
- Choices:
  - light Torch with Torch and Tinderbox -> 108
  - create Staff glow -> 115
  - no light source or decline -> 122
- Build note: Torch route requires Torch and Tinderbox. Staff-glow route should require current Willpower of at least 1 before choosing it; section 115 applies the -1 Willpower cost.

### Section 99

- Type: combat with post-combat Staff/charge route choice.
- Combat: Shadakine Crossbowmen, Combat Skill 25, Endurance 32. Fight as one enemy, to the death; add +2 Combat Skill for surprise and +2 more for Shan, for +4 total during this combat.
- State change: none outside combat.
- Choices after victory:
  - attack the Shadakine on the bridge at long range -> 88
  - charge the Shadakine -> 94
- Build note: long-range Staff route to section 88 should require current Willpower of at least 2 before choosing it. Charge route has no source Willpower gate; section 94 applies its forced Staff cost and can go negative by footnote/book rule.

### Section 100

- Type: plain route choice.
- State change: none confirmed.
- Choices:
  - run away -> 40
  - obey the Shadakine -> 121
- Build note: no section-specific automation needed beyond normal choice display.

### Section 101

- Type: Staff attack result followed by limited survival combat.
- State change: lose 2 Willpower for the opening Staff blast. If Grey Star has another weapon-capable item besides the Wizard's Staff, Shan uses it during the fight for +2 Combat Skill; project ruling is that the borrowed weapon is returned to inventory after the combat.
- Combat: nine Najin attack one at a time. The combat ends after five combat rounds if Grey Star is still alive, even if Najin remain.
  - Najin 1: Combat Skill 10, Endurance 10
  - Najin 2: Combat Skill 9, Endurance 10
  - Najin 3: Combat Skill 10, Endurance 10
  - Najin 4: Combat Skill 7, Endurance 9
  - Najin 5: Combat Skill 8, Endurance 10
  - Najin 6: Combat Skill 10, Endurance 12
  - Najin 7: Combat Skill 9, Endurance 9
  - Najin 8: Combat Skill 11, Endurance 9
  - Najin 9: Combat Skill 10, Endurance 9
- Out link: survive five rounds -> 130.
- Build note: source section 58 should require current Willpower of at least 2 before choosing the attack route. Combat automation needs a round-limit survival mode across sequential enemies, plus temporary weapon loan/return handling.

### Section 102

- Type: forced Willpower loss with a forced onward route.
- State change: lose 2 Willpower, allowing Willpower to fall below 0.
- Out link: 149.
- Build note: this is a forced mental injury, not an optional spell or Staff use.

### Section 103

- Type: terminal death ending.
- State change: adventure ends in death.
- Out link: none.
- Build note: mark as terminal once ending automation exists.

### Section 104

- Type: Staff-action route choice while trapped by Yaku vines.
- State change: none in this section; target sections handle costs.
- Choices:
  - slash the tendril around your ankle -> 248
  - unleash a bolt at the centre of the Yaku plant -> 179
- Build note: section 179 applies a 1 Willpower Staff-bolt cost and should require current Willpower of at least 1 before choosing from this section. Section 248 has its own footnote allowing the listed Willpower cost to go negative under the project book-rule path.

### Section 105

- Type: Prophecy-gated route choice plus ordinary conversation choices.
- State change: none in this section; section 313 handles the Prophecy cost.
- Choices:
  - use Prophecy -> 313
  - speak to tattooed sailor -> 79
  - talk to merchant -> 131
  - speak to hooded character -> 209
- Build note: Prophecy route should require Prophecy and current Willpower of at least 1 before choosing it.

### Section 106

- Type: narrative forced route.
- State change: none confirmed.
- Out link: 117.
- Build note: no automation needed beyond normal navigation.

### Section 107

- Type: forced Staff attack result followed by route choice.
- State change: lose 2 Willpower, allowing Willpower to fall below 0 under the section footnote/book-rule path.
- Choices:
  - finish off the Quoku -> 307
  - make another run for it -> 182
- Build note: section 107 has its own insufficient-Willpower footnote, so apply the negative-Willpower path if needed.

### Section 108

- Type: torchlight narrative forced route.
- State change: no inventory deletion confirmed. If light-source state is tracked, Torch is now active.
- Out link: 135.
- Build note: reached from the Torch/Tinderbox route in section 98; no Willpower cost.

### Section 109

- Type: Sorcery result with resource loss and route choice.
- State change: lose 4 Willpower total and 1 Endurance. The Willpower loss may reduce Willpower below 0 under the section 172 forced-power footnote/book-rule path.
- Choices:
  - confront the gaoler -> 243
  - go in the opposite direction -> 333
- Build note: the text narrates intermediate exertions, but the final stated cost is 4 Willpower total, not 2+3+4.

### Section 110

- Type: hidden puzzle-solution information section with forced route.
- State change: none confirmed.
- Out link: 190.
- Build note: footnote identifies this as the correct solution to the riddle in section 264; this resolves the apparent no-incoming-link status as a puzzle/answer destination.

### Section 111

- Type: optional Staff attack result with forced onward route.
- State change: lose 2 Willpower.
- Out link: 266.
- Build note: source section 61 should require current Willpower of at least 2 before choosing the attack route.

### Section 112

- Type: Enchantment-gated route choice plus ordinary choices.
- State change: none in this section; target sections handle costs.
- Choices:
  - destroy the Shadakine warriors as the crowd demands -> 84
  - use Enchantment to escape -> 56
  - escape without magic -> 28
- Build note: Enchantment route should require Enchantment and current Willpower of at least 2 before choosing it. Section 84 handles the forced Staff cost for the crowd-demand route.

### Section 113

- Type: plain route choice.
- State change: none confirmed.
- Choices:
  - reach for the crevice -> 138
  - accept defeat at the Wall of Azakawa -> 188
- Build note: no section-specific automation needed beyond normal choice display.

### Section 114

- Type: Sorcery result followed by Prophecy branch and route choices.
- State change: lose 2 Willpower for Sorcery.
- Choices:
  - use Prophecy -> 92, then return to section 114
  - take left-hand stairway -> 80
  - take right-hand stairway -> 45
- Build note: source section 159 should require Sorcery and current Willpower of at least 2 before choosing the Sorcery route. Prophecy branch should require Prophecy and current Willpower of at least 1; section 92 applies the Prophecy cost.

### Section 115

- Type: Staff-light result with forced onward route.
- State change: lose 1 Willpower and mark Staff light active until extinguished.
- Out link: 135.
- Build note: source section 98 gates this optional Staff-light route at current Willpower of at least 1.

### Section 116

- Type: Sorcery shield result with follow-up route choice.
- State change: lose 2 Willpower before the choice.
- Choices:
  - spend another 2 Willpower to withstand the assault -> 150
  - exert will from behind the Sorcery shield -> 226
- Build note: source section 175 should require Sorcery and current Willpower of at least 2 for the shield route. The section 150 branch spends another 2 Willpower in section 116 before navigation and should require current Willpower of at least 2 after the initial shield cost.

### Section 117

- Type: forced Staff attack result followed by combat.
- State change: lose 1 Willpower, allowing Willpower to fall below 0 under the forced-cost project rule.
- Combat: 2 Shadakine Warriors, Combat Skill 15, Endurance 25. No evade; fight to the death.
- Out link: victory -> 164.
- Build note: no Combat Skill modifier is stated despite the narrative comment about improved battle skill.

### Section 118

- Type: forced Endurance loss followed by route choice.
- State change: lose 1 Endurance.
- Choices:
  - investigate the crack in the cliff -> 268
  - return to Shenwu Falls/Lake Shenwu -> 293
- Build note: apply the Endurance loss before presenting the route choice.

### Section 119

- Type: forced Endurance loss with forced onward route.
- State change: lose 2 Endurance.
- Out link: 128.
- Build note: this is not a combat despite the physical struggle language.

### Section 120

- Type: forced Staff attack result followed by limited survival combat.
- State change: lose 1 Willpower, allowing Willpower to fall below 0 under the section footnote/book-rule path.
- Combat: Shadakine Rearguard, Combat Skill 25, Endurance 30. Shan adds +3 Combat Skill. No evade offered; fight as one enemy.
- Out link: alive after three combat rounds -> 189.
- Build note: automate this as a three-round survival combat despite the "to the death" wording; if the enemy is defeated earlier, the only onward route is still section 189.

### Section 121

- Type: route choice with optional Staff-combat source gate.
- State change: none in this section; section 265 handles the attack cost and combat.
- Choices:
  - resist arrest by attacking the Shadakine -> 265
  - submit without revealing powers/purpose -> 300
- Build note: attack route leads to a section 265 Staff blast costing 1 Willpower, so that source choice should require current Willpower of at least 1.

### Section 122

- Type: terminal death ending.
- State change: adventure ends in death.
- Out link: none.
- Build note: mark as terminal once ending automation exists.

### Section 123

- Type: optional Staff attack result with forced onward route.
- State change: lose 1 Willpower.
- Out link: 149.
- Build note: source section 90 should require current Willpower of at least 1 before choosing the Staff attack route.

### Section 124

- Type: Enchantment result with route choice.
- State change: lose 2 Willpower, allowing Willpower to fall below 0 under the section 172 forced-power footnote/book-rule path.
- Choices:
  - pounce on the gaoler -> 243
  - run to the right -> 23
  - turn left along the corridor -> 333
- Build note: this is reached from the section 172 forced power menu, so the cost may go negative if needed.

### Section 125

- Type: optional Special Item gain followed by route choice.
- State change: optionally add Gaoler's Keys as a Special Item.
- Choices:
  - go back to take the left stairway -> 137
  - go back to take the right stairway -> 212
  - enter narrow passageway -> 333
- Build note: item gain should be optional because the text says "If you decide to keep" the keys.

### Section 126

- Type: plain route choice.
- State change: none confirmed.
- Choices:
  - follow the Najin -> 161
  - leave the Chansi Hills -> 106
- Build note: no section-specific automation needed beyond normal choice display.

### Section 127

- Type: plain route choice.
- State change: none confirmed.
- Choices:
  - run towards the main entrance -> 50
  - run down the narrow street -> 40
- Build note: no section-specific automation needed beyond normal choice display.

### Section 128

- Type: Magick/item-gated route choice.
- State change: none in this section; targets handle costs and item consumption.
- Choices:
  - use Elementalism -> 181
  - use Enchantment with Calacena Mushrooms -> 206
  - fight your way out -> 12
- Build note: Elementalism route should require Elementalism and current Willpower of at least 1; section 181 applies the Willpower cost. Enchantment route requires Enchantment and Calacena Mushrooms; section 206 consumes the mushrooms and shows no Willpower cost. Section 12 applies the fight-out cost with its own negative-Willpower footnote.

### Section 129

- Type: plain route choice.
- State change: none confirmed.
- Choices:
  - attack the young girl -> 67
  - question her -> 147
- Build note: no section-specific automation needed beyond normal choice display.

### Section 130

- Type: narrative forced route.
- State change: none confirmed.
- Out link: 106.
- Build note: this is the post-survival route from section 101.

### Section 131

- Type: narrative forced route.
- State change: none confirmed.
- Out link: 300.
- Build note: no section-specific automation needed beyond normal navigation.

### Section 132

- Type: optional long-range Staff attack result with forced onward route.
- State change: lose 2 Willpower.
- Out link: 203.
- Build note: source section 145 should require current Willpower of at least 2 before allowing the long-range Staff attack route.

### Section 133

- Type: money handover followed by combat with an evade option.
- State change: hand over the money pouch. Store current Nobles as `stolenNobles` or equivalent, then set Nobles to 0.
- Combat: Cut-throat, Combat Skill 10, Endurance 12. The cut-throat is trying to kill Grey Star.
- Choices:
  - evade after 2 combat rounds if still alive -> 27
  - fight to the death and win -> 71
- Build note: section 34 should only allow this route when Nobles are greater than 0. Section 71 should restore the stored stolen Nobles and then add the 10 Nobles reward.

### Section 134

- Type: narrative forced route.
- State change: none confirmed.
- Out link: 58.
- Build note: no section-specific automation needed beyond normal navigation.

### Section 135

- Type: narrative forced route into a combat section.
- State change: none confirmed.
- Out link: 197.
- Build note: no state change occurs here; section 197 handles the Mantiz combat.

### Section 136

- Type: Prophecy-gated route choice.
- State change: none in this section; section 345 applies the Prophecy Willpower cost.
- Choices:
  - use Prophecy -> 345
  - lack/decline Prophecy -> 61
- Build note: Prophecy route should require Prophecy known and current Willpower of at least 1 before choosing it.

### Section 137

- Type: Prophecy branch plus plain route choices.
- State change: none in this section; section 92 applies the Prophecy Willpower cost and returns to this section.
- Choices:
  - use Prophecy -> 92, with return to 137 later
  - take the left exit -> 142
  - turn right -> 163
- Build note: Prophecy route should require Prophecy known and current Willpower of at least 1, and should preserve return-section context.

### Section 138

- Type: terminal death ending.
- State change: adventure ends in death.
- Out link: none.
- Build note: mark as terminal once ending automation exists.

### Section 139

- Type: optional Sorcery result with forced onward route.
- State change: lose 2 Willpower and mark the Sorcery shield active for section 149.
- Out link: 149.
- Build note: source section 90 should require Sorcery known and current Willpower of at least 2 before choosing the Sorcery shield route.

### Section 140

- Type: plain route choice.
- State change: none confirmed.
- Choices:
  - enter the port before nightfall -> 112
  - wait for darkness -> 280
- Build note: no section-specific automation needed beyond normal choice display.

### Section 141

- Type: narrative forced route into a combat section.
- State change: none confirmed.
- Out link: 197.
- Build note: no state change occurs here; section 197 handles the Mantiz combat.

### Section 142

- Type: item/Magick-gated locked-door route choice.
- State change: none in this section; target sections handle any costs or tests.
- Choices:
  - use Gaoler's Keys -> 286
  - use Sorcery -> 159
  - use Alchemy -> 170
  - take right-hand archway -> 163
- Build note: gate 286 on Gaoler's Keys, 159 on Sorcery known, and 170 on Alchemy known. The Sorcery path's commitment/cost is handled by section 159/114.

### Section 143

- Type: optional Prophecy result with resource loss followed by route choice.
- State change: lose 1 Willpower and 1 Endurance.
- Choices:
  - explore the basin and Lake Shenwu -> 68
  - find a way to scale the cliffs -> 118
- Build note: source section 43 should require Prophecy known and current Willpower of at least 1 before choosing this route.

### Section 144

- Type: narrative forced route.
- State change: none confirmed.
- Out link: 172.
- Build note: no section-specific automation needed beyond normal navigation.

### Section 145

- Type: route choice with optional long-range Staff gate.
- State change: none in this section; section 132 applies the Staff attack cost.
- Choices:
  - fire another long-range attack -> 132
  - help Shan -> 99
  - charge the warriors on the bridge -> 169
- Build note: long-range Staff route should require current Willpower of at least 2 before choosing it.

### Section 146

- Type: route choice with optional Staff attack gate.
- State change: none in this section; section 158 applies the Staff attack cost.
- Choices:
  - fire a bolt from the Wizard's Staff -> 158
  - dash into the undergrowth -> 232
- Build note: Staff bolt route should require current Willpower of at least 1 before choosing it.

### Section 147

- Type: plain route choice.
- State change: none confirmed.
- Choices:
  - agree to Tanith's request -> 221
  - ignore her -> 63
- Build note: no section-specific automation needed beyond normal choice display.

### Section 148

- Type: plain route choice.
- State change: none confirmed.
- Choices:
  - jump across the ravine -> 49
  - stand and fight the Quoku -> 233
- Build note: this section is not combat itself; the combat-sweep flag is a false positive caused by the wording of the route choice.

### Section 149

- Type: special limited combat with per-round resource drain.
- State change per combat round: lose 1 Willpower, allowing Willpower to fall below 0. Also lose 2 Endurance per round, reduced to 1 Endurance per round if the Sorcery shield from section 139 is active.
- Combat: Kleasa, Combat Skill 25, Endurance 30. No evade; fight until the success condition or death.
- Success route: if still alive after 4 combat rounds, or if the Kleasa is defeated before that, go to 165.
- Build note: combat automation needs per-round WP/END drain, a Sorcery-shield modifier, and a four-round survival limit. Clear the local Sorcery shield state after this combat.

### Section 150

- Type: forced resource loss with status-gated route.
- State change: lose 4 Willpower, allowing Willpower to fall below 0, and lose 2 Endurance.
- Conditional route:
  - if post-loss Willpower is above 0, or Magic Talisman of the Shianti is carried -> 348
  - if post-loss Willpower is 0 or below and no Magic Talisman is carried -> 237
- Build note: route must be evaluated after applying the resource loss.

### Section 151

- Type: Alchemy ingredient-gated route choice.
- State change: none in this section; section 297 handles brewing and item changes.
- Check: Sulphur, Saltpetre, Ezeran Crystals, and an empty vial. Item location should follow the general alchemy storage rule: ingredients, vials, and potions may be carried in the Herb Pouch or Backpack if storage is tracked.
- Choices:
  - all ingredients and empty vial -> 297
  - missing any required ingredient or vial -> 172
- Build note: route 297 is part of the section 172 forced-power loop; target section handles the actual recipe result.

### Section 152

- Type: plain route choice.
- State change: none confirmed.
- Choices:
  - enter the shack -> 252
  - burst in through the door -> 277
  - send Shan to investigate -> 302
- Build note: no section-specific automation needed beyond normal choice display.

### Section 153

- Type: Sorcery-gated route choice.
- State change: none in this section; section 185 applies the Sorcery cost.
- Choices:
  - use Sorcery to bar the door -> 185
  - lack/decline Sorcery -> 198
- Build note: Sorcery route should require Sorcery known and current Willpower of at least 1 before choosing it.

### Section 154

- Type: combat with a one-round evade option.
- State change: combat only.
- Combat: Cave Mantiz, Combat Skill 15, Endurance 18.
- Choices:
  - evade after 1 combat round -> 4
  - win the combat -> 103
- Build note: timed evade is section-specific; section 103 is a terminal death destination despite being the victory route.

### Section 155

- Type: terminal death ending.
- State change: adventure ends in death.
- Out link: none.
- Build note: mark as terminal once ending automation exists.

### Section 156

- Type: plain route choice.
- State change: none confirmed.
- Choices:
  - attack the Shadakine officer -> 215
  - attack the main Shadakine force -> 120
- Build note: target sections handle their own combat and resource costs. Section 215 has a source-specific footnote for arriving from 156 that should be handled when section 215 is audited.

### Section 157

- Type: Alchemy-gated forced route choice.
- State change: none confirmed.
- Choices:
  - Alchemy known -> 183
  - no Alchemy -> 26
- Build note: this is an automatic Magick gate, not a free choice.

### Section 158

- Type: optional Staff attack result with forced onward route.
- State change: lose 1 Willpower.
- Out link: 232.
- Build note: source section 146 should require current Willpower of at least 1 before choosing this Staff route.

### Section 159

- Type: Sorcery commitment and alternate route choice.
- State change: none in this section; section 114 applies the Sorcery cost.
- Choices:
  - commit to Sorcery -> 114
  - use Alchemy instead -> 170
  - take open archway -> 163
- Build note: the Sorcery route should require Sorcery known and current Willpower of at least 2 before choosing it; the Alchemy route should require Alchemy known.

### Section 160

- Type: item consumption with forced onward route.
- State change: consume one Laumspur item or vial.
- Out link: 301.
- Build note: source section 178 should require at least one Laumspur before offering this route. No Meal requirement is stated despite the narrative food.

### Section 161

- Type: loot prompt followed by Alchemy-gated forced route.
- Loot available from Jnana:
  - Silver Charm as a Special Item
  - up to 5 Meals
  - Broadsword as a Weapon
  - 2 Potions of Laumspur, each later restoring 3 Endurance when swallowed; Backpack Items or Herb Pouch Items if Alchemy is known
  - Coil of Rope as a Backpack Item
- State change: add selected loot, respecting Backpack, Herb Pouch, Weapon, and Special Item handling.
- Conditional route:
  - Alchemy known -> 193
  - no Alchemy -> 15
- Build note: Shan and Tanith receiving food/backpacks/weapons is companion narrative, not Grey Star inventory.

### Section 162

- Type: optional long-range Staff attack result with forced onward route.
- State change: lose 2 Willpower.
- Out link: 255.
- Build note: source section 167 should require current Willpower of at least 2 before choosing this route.

### Section 163

- Type: narrative forced route.
- State change: none confirmed.
- Out link: 333.
- Build note: no section-specific automation needed beyond normal navigation.

### Section 164

- Type: loot section with forced onward route.
- State change: gain 10 Nobles; optionally add up to 2 Meals and one Sword as a Weapon.
- Out link: 39.
- Build note: Shan taking a sword is companion narrative, not a Grey Star inventory change. Meals and Sword should respect capacity/weapon limits.

### Section 165

- Type: forced resource loss with status-gated route.
- State change: lose 5 Willpower, allowing Willpower to fall below 0, and lose 5 Endurance.
- Conditional route, if still alive:
  - post-loss Willpower 0 or below -> 177
  - post-loss Willpower above 0 -> 192
- Build note: route must be evaluated after applying the resource loss. If Endurance falls to 0 or below, normal death handling applies.

### Section 166

- Type: plain route choice.
- State change: none confirmed.
- Choices:
  - try to escape -> 241
  - confront the Shadakine -> 11
- Build note: no section-specific automation needed beyond normal choice display.

### Section 167

- Type: route choice with optional long-range Staff gate.
- State change: none in this section; section 162 applies the Staff attack cost.
- Choices:
  - long-range attack at the chariot -> 162
  - let the chariot draw closer -> 180
- Build note: long-range Staff route should require current Willpower of at least 2 before choosing it.

### Section 168

- Type: two-Meal requirement plus fixed Endurance loss with forced onward route.
- State change: consume 2 Meals if available; for each missing Meal, lose 3 Endurance under the normal Meal rule. Also lose 1 Endurance for fatigue.
- Out link: 140.
- Build note: unlike section 2, this section has no local all-or-nothing failure text; use the baseline per-missing-Meal rule.

### Section 169

- Type: narrative forced route.
- State change: none confirmed.
- Out link: 203.
- Build note: no section-specific automation needed beyond normal navigation.

### Section 170

- Type: item/Sorcery-gated route choice.
- State change: none in this section; section 73 handles Ezeran Acid consumption and section 159/114 handles Sorcery costs.
- Choices:
  - prepared vial of Ezeran Acid -> 73
  - no acid and try Sorcery -> 159
  - take the right-hand exit -> 163
- Build note: Ezeran Acid route should require a prepared vial of Ezeran Acid. Sorcery fallback should require Sorcery known; section 159 handles the final Sorcery commitment gate.

### Section 171

- Type: loot section with forced onward route.
- State change: gain 5 Nobles; optionally add the guard's Sword as a Weapon.
- Out link: 137.
- Build note: Sword pickup should respect normal Weapon limits.

### Section 172

- Type: forced Magick-selection hub.
- State change: none in this section; target sections apply their own costs and effects.
- Choices:
  - Sorcery escape -> 95
  - Enchantment -> 124
  - Elementalism -> 271
  - Alchemy -> 151
  - Psychomancy -> 236
  - Prophecy -> 211
  - Evocation -> 250
- Build note: only known Powers should be selectable. This section's footnote explicitly allows the forced selected Power's cost to reduce Willpower below 0; preserve that exception for target sections reached from this menu. The sweep's out link to section 175 is a cross-book footnote reference, not a local route.

### Section 173

- Type: terminal death ending.
- State change: adventure ends in death.
- Out link: none.
- Build note: mark as terminal once ending automation exists.

### Section 174

- Type: narrative forced route.
- State change: none confirmed.
- Out link: 148.
- Build note: no section-specific automation needed beyond normal navigation.

### Section 175

- Type: Sorcery/WP resistance route choice.
- State change: none in this section; target sections handle costs and tests.
- Choices:
  - use Sorcery to destroy the Kazim Stone -> 191
  - use Sorcery to shield the mind -> 116
  - resist with Willpower -> 226
- Build note: Sorcery routes require Sorcery known. Route 191 should require current Willpower of at least 2 because section 191's minimum spend is 2 WP. Route 116 should require current Willpower of at least 2 because section 116 immediately applies that cost. The non-Sorcery Willpower duel route is always available.

### Section 176

- Type: item-gated route choice.
- State change: none confirmed.
- Choices:
  - use Gaoler's Keys to lock the door -> 153
  - continue immediately -> 60
- Build note: route 153 requires Gaoler's Keys here; section 153 then handles any Sorcery option.

### Section 177

- Type: terminal death ending.
- State change: adventure ends in death.
- Out link: none.
- Build note: mark as terminal once ending automation exists.

### Section 178

- Type: item-gated route choice.
- State change: none in this section; section 160 consumes the Laumspur if chosen.
- Choices:
  - give Laumspur to the old man -> 160
  - lack/keep Laumspur -> 93
- Build note: source route to 160 requires at least one Laumspur.

### Section 179

- Type: Staff attack result with follow-up route choice.
- State change: lose 1 Willpower for the initial Staff attack.
- Choices:
  - fire another bolt at the Yaku to free Shan -> 285
  - rush to Shan's side -> 240
- Build note: source section 104 should require current Willpower of at least 1 before choosing route 179. After the initial cost, route 285 should require current Willpower of at least 2 because section 285 applies a further 2 WP cost.

### Section 180

- Type: narrative forced route.
- State change: none confirmed.
- Out link: 255.
- Build note: no section-specific automation needed beyond normal navigation.

### Section 181

- Type: optional Elementalism result with forced onward route.
- State change: lose 1 Willpower.
- Out link: 325.
- Build note: source section 128 should require Elementalism known and current Willpower of at least 1 before choosing this route.

### Section 182

- Type: narrative forced route.
- State change: none confirmed.
- Out link: 249.
- Build note: no section-specific automation needed beyond normal navigation.

### Section 183

- Type: shop/purchase prompt with forced onward route.
- Available purchases:
  - Jar of Ezeran Crystals, cost 5 Nobles
  - Pestle and Mortar, Backpack Item, cost 5 Nobles
  - Bottle of Naphtha, cost 2 Nobles
  - 2 Vials of Laumspur, cost 2 Nobles each; each later restores 3 Endurance when swallowed
  - Vial of Graveweed Essence, cost 1 Noble
  - Vial of Alether, cost 2 Nobles
  - Bundle of dried Azawood Leaves, cost 5 Nobles
  - 3 Tarama Seeds, cost 3 Nobles each; Tarama Seeds may be recorded as Special Items and take no Herb Pouch or Backpack space.
- State change: subtract Nobles for chosen purchases and add chosen items, respecting stock and storage. Since this route requires Alchemy, potions, vials, and ingredients may use Herb Pouch space when appropriate.
- Out link: 26.
- Build note: future automation wants a stock-limited shop prompt with Nobles affordability and storage placement.

### Section 184

- Type: narrative forced route.
- State change: none confirmed.
- Out link: 325.
- Build note: no section-specific automation needed beyond normal navigation.

### Section 185

- Type: optional Sorcery result followed by route choice.
- State change: lose 1 Willpower.
- Choices:
  - take the left stairway -> 80
  - take the right stairway -> 253
- Build note: source section 153 should require Sorcery known and current Willpower of at least 1 before choosing this route.

### Section 186

- Type: narrative forced route.
- State change: none confirmed.
- Out link: 86.
- Build note: no section-specific automation needed beyond normal navigation.

### Section 187

- Type: origin/status-gated route choice.
- State change: none confirmed.
- Conditional route:
  - arrested at the Inn of the Laughing Moon -> 230
  - otherwise -> 261
- Build note: future route automation needs an origin/status flag for arrests at the inn, likely set by the arrest route that leads into the dungeons.

### Section 188

- Type: narrative forced route.
- State change: none confirmed.
- Out link: 8.
- Build note: no section-specific automation needed beyond normal navigation.

### Section 189

- Type: combat with Shan Combat Skill modifier.
- State change: combat only.
- Combat: Shadakine Officer, Combat Skill 25, Endurance 26. No evade; fight to the death. Add +3 Combat Skill because Shan is with Grey Star.
- Victory route: 215.
- Build note: combat payload needs a +3 Combat Skill modifier.

### Section 190

- Type: plain route choice.
- State change: none confirmed.
- Choices:
  - follow the Suhni River north then west -> 38
  - follow the Great Suhn Road south then west -> 21
- Build note: no section-specific automation needed beyond normal choice display.

### Section 191

- Type: Sorcery/WP spending route choice.
- Preconditions: reached from section 175 by choosing the Sorcery destroy-Stone route; Sorcery known and current Willpower of at least 2 are required before entering.
- State change: subtract the selected Willpower amount before routing.
- Choices:
  - spend 2 Willpower -> 323, then section 323 applies an extra 1 Willpower cost and has at least one mandatory follow-up Willpower cost
  - spend 3 Willpower -> 314, then section 314 applies an extra 1 Willpower cost
  - spend 4 Willpower -> 288, then section 288 applies an extra 2 Willpower cost
- Build note: this is optional Sorcery, so do not allow a branch that would drive Willpower negative. Present only choices the current Willpower can pay for. Route 323 should require at least 4 current Willpower before the section 191 spend, or at least 2 Willpower remaining after the 2-point spend, so section 323's immediate -1 WP and mandatory extinguish option can be paid. Route 314 should require at least 4 current Willpower before the section 191 spend, or at least 1 Willpower remaining after the 3-point spend. Route 288 should require at least 6 current Willpower before the section 191 spend, or at least 2 Willpower remaining after the 4-point spend.

### Section 192

- Type: narrative forced route.
- State change: none confirmed.
- Out link: 276.
- Build note: no section-specific automation needed beyond normal navigation.

### Section 193

- Type: Alchemy loot prompt with forced onward route.
- Preconditions: source section 161 requires Alchemy for this route.
- Available loot:
  - Pestle and Mortar, Backpack Item.
  - Packet of Ezeran Crystals, Herb Pouch item.
  - Jar of Yabari Ointment, Herb Pouch item; may be applied at any time by deleting the item and marking worn ointment status.
  - 4 Tarama Seeds, Special Items that take no Backpack or Herb Pouch space.
- State change: add any selected items, respecting storage. No Nobles cost.
- Out link: 15.
- Build note: Tarama Seeds can pay for one spell or one outside-close-combat Staff use, but not spell maintenance, mental attacks, or close combat Staff spending.

### Section 194

- Type: Coil of Rope result with forced onward route.
- Preconditions: source section 74 requires Coil of Rope.
- State change: none confirmed; do not delete the Coil of Rope here.
- Out link: 269.
- Build note: no section-specific automation needed beyond preserving the source item gate.

### Section 195

- Type: plain route choice.
- State change: none confirmed.
- Choices:
  - seek information in the market square -> 157
  - enter the Inn of the Laughing Moon -> 82
- Build note: entering the inn is not itself the later arrest-origin flag; that should be set by the actual arrest route.

### Section 196

- Type: plain route choice.
- State change: none confirmed.
- Choices:
  - leave the harbour by the main entrance -> 50
  - leave by the narrow street -> 40
- Build note: no section-specific automation needed beyond normal choice display.

### Section 197

- Type: combat, no evade.
- State change: combat only.
- Combat: Soldier Mantiz, Combat Skill 15, Endurance 10. No evade; fight to the death.
- Victory route: 213.
- Build note: generic combat works, with evade disabled.

### Section 198

- Type: plain route choice.
- State change: none confirmed.
- Choices:
  - left stairway -> 80
  - right stairway -> 225
- Build note: no section-specific automation needed beyond normal choice display.

### Section 199

- Type: Magick/WP-gated route choice.
- State change: none in this section; target sections apply the Willpower costs.
- Choices:
  - Elementalism to destroy the bridge -> 31
  - Sorcery to create a barrier -> 48
  - conserve energy -> 244
- Build note: route 31 requires Elementalism and current Willpower of at least 1. Route 48 requires Sorcery and current Willpower of at least 3. Route 244 is always available.

### Section 200

- Type: Prophecy-gated route choice.
- State change: none in this section; section 64 applies the Prophecy cost.
- Choices:
  - use Prophecy -> 64
  - left alleyway -> 223
  - right alleyway -> 76
  - continue along the narrow street -> 195
- Build note: route 64 requires Prophecy and current Willpower of at least 1.

### Section 201

- Type: recovery with forced onward route.
- State change: restore 1 Endurance and 1 Willpower.
- Out link: 172.
- Build note: Endurance recovery is capped at starting Endurance; Willpower recovery is uncapped.

### Section 202

- Type: optional Elementalism result with forced onward route.
- State change: lose 1 Willpower.
- Out link: 140.
- Build note: source section 1 should require Elementalism known and current Willpower of at least 1 before choosing this route.

### Section 203

- Type: combat with companion Combat Skill modifier.
- State change: combat only.
- Combat: 2 Shadakine Crossbowmen, Combat Skill 15, Endurance 18. No evade; fight to the death. Add +4 Combat Skill because Tanith and Shan aid Grey Star.
- Victory route: 156.
- Build note: combat payload needs a +4 Combat Skill modifier.

### Section 204

- Type: forced Staff/WP cost with follow-up attack choice.
- State change: lose 2 Willpower for cutting Shan free.
- Footnote: if there is insufficient Willpower, the player may either allow the Willpower total to go negative or cover missing Willpower with Endurance at 2 END per 1 missing WP.
- Choices:
  - fire at the heart of the nearest Yaku plant -> 329
  - attack the Yaku vine holding the right leg -> 279
  - attack the Yaku vine on the left leg -> 304
- Build note: section automation should apply the initial cost before presenting choices and preserve the footnote exception for insufficient WP. The optional Staff route to section 329 should require current Willpower of at least 1 after the initial section 204 cost because section 329 applies another Staff cost and has no insufficiency footnote.

### Section 205

- Type: combat with Combat Skill modifier and evade.
- State change: combat only.
- Combat: Shadakine Warrior, Combat Skill 11, Endurance 15. Add +5 Combat Skill for surprise and Shan's help.
- Routes:
  - evade at any time by fleeing down the right-hand exit -> 163
  - win the fight -> 176
- Build note: combat payload needs a +5 Combat Skill modifier and an always-available evade route to 163.

### Section 206

- Type: item consumption with forced onward route.
- Preconditions: source section 128 requires Enchantment and Calacena Mushrooms for this route.
- State change: consume/delete the Calacena Mushrooms.
- Out link: 325.
- Build note: no Willpower cost is stated here.

### Section 207

- Type: terminal death ending.
- State change: adventure ends in death.
- Out link: none.
- Build note: mark as terminal once ending automation exists.

### Section 208

- Type: Staff/WP-gated route choice.
- State change: none in this section; section 81 applies the Staff cost.
- Choices:
  - attack at long range with Wizard's Staff -> 81
  - charge the crossbowmen -> 99
- Build note: route 81 requires current Willpower of at least 2 because section 81 applies that cost.

### Section 209

- Type: loot prompt followed by route choice.
- Optional loot:
  - Vial of Pink Liquid, Backpack Item.
  - Medallion of the Redeemer, Special Item worn around the neck.
- Choices:
  - accept the drink -> 131
  - leave the inn -> 157
- Build note: future automation should offer the Redeemer items before the drink/leave route choice.

### Section 210

- Type: forced Endurance loss with forced onward route.
- State change: lose 2 Endurance.
- Out link: 74.
- Build note: future section automation should offer/apply the fall damage before navigation.

### Section 211

- Type: Prophecy result with Evocation-gated route choice.
- State change: lose 1 Willpower.
- Choices:
  - raise the dead priest -> 250
  - ignore the vision or if Evocation was already attempted -> 172
- Build note: this is a target of section 172, so the section 172 negative-WP exception applies to the 1 WP Prophecy cost. Route 250 requires Evocation known and should be blocked once the Evocation attempt has already been made.

### Section 212

- Type: plain route choice.
- State change: none confirmed.
- Choices:
  - attack the sleeping Shadakine guard -> 309
  - leave quietly and take the other stairway -> 137
- Build note: no section-specific automation needed beyond normal choice display.

### Section 213

- Type: plain route choice.
- State change: none confirmed.
- Choices:
  - passage sloping upwards -> 267
  - passage sloping downwards -> 272
  - return the way Grey Star came -> 284
- Build note: no section-specific automation needed beyond normal choice display.

### Section 214

- Type: Prophecy-gated route choice.
- State change: none in this section; section 92 applies the Prophecy cost.
- Choices:
  - use Prophecy -> 92, with return section 214 noted
  - left stairway -> 176
  - right stairway -> 45
- Build note: route 92 requires Prophecy and current Willpower of at least 1.

### Section 215

- Type: forced Willpower cost and loot prompt with forced onward route.
- State change: lose 1 Willpower for the continuing battle.
- Footnote: if there is insufficient Willpower, the player may either allow the Willpower total to go negative or cover missing Willpower with Endurance at 2 END per 1 missing WP.
- Optional loot:
  - Potion of Rendalim's Elixir, restores 6 Endurance when used.
  - Enough food for 5 Meals.
  - Pestle and Mortar, Backpack Item.
  - 3 Tarama Seeds, Special Items that take no Backpack or Herb Pouch space.
  - Sealed pouch of Calacena Mushrooms.
- Out link: 2.
- Build note: carry loot in the Herb Pouch unless otherwise indicated, or in the Backpack if there is no Herb Pouch. The author-overlook footnote about arriving from section 156 is narrative only.

### Section 216

- Type: terminal death ending.
- State change: adventure ends in death.
- Out link: none.
- Build note: mark as terminal once ending automation exists.

### Section 217

- Type: forced Nobles loss with forced onward route.
- State change: lose 5 Nobles.
- Out link: 105.
- Build note: the source route should require at least 5 Nobles, because no alternative is offered once the bribe starts.

### Section 218

- Type: narrative forced route.
- State change: none confirmed.
- Out link: 39.
- Build note: no section-specific automation needed beyond normal navigation.

### Section 219

- Type: companion status change with forced onward route.
- State change: Shan is dead/absent. Grey Star takes up Shan's backpack narratively, but this section does not list item transfers.
- Out link: 294.
- Build note: future automation may need a Shan-dead/absent status flag for later text or loot handling.

### Section 220

- Type: terminal death ending.
- State change: adventure ends in death.
- Out link: none.
- Build note: mark as terminal once ending automation exists.

### Section 221

- Type: gear recovery and optional item placement with forced onward route.
- State change: restore access to Grey Star's Staff and Backpack if they were being tracked as confiscated/hidden.
- Optional item handling: if Grey Star has the Kazim Stone and there is room in the Backpack, it may be recorded there as a Backpack Item.
- Out link: 292.
- Build note: future automation may need a confiscated/recovered gear status; otherwise this is mainly a Kazim Stone capacity prompt.

### Section 222

- Type: Staff/WP-gated route choice.
- State change: none in this section; section 239 applies the Staff cost.
- Choices:
  - long-range Staff attack -> 239
  - charge the soldier Mantiz -> 246
  - head back -> 260
- Build note: route 239 requires current Willpower of at least 2 because section 239 applies that cost and has no insufficient-WP footnote.

### Section 223

- Type: plain route choice.
- State change: none confirmed.
- Choices:
  - seek information in the alley -> 34
  - return to the narrow street -> 195
- Build note: no section-specific automation needed beyond normal choice display.

### Section 224

- Type: combat, no evade.
- State change: combat only.
- Combat: Shadakine Warrior, Combat Skill 13, Endurance 20. No evade; fight to the death.
- Victory route: 127.
- Build note: generic combat works, with evade disabled.

### Section 225

- Type: terminal death ending.
- State change: adventure ends in death.
- Out link: none.
- Build note: mark as terminal once ending automation exists.

### Section 226

- Type: Willpower/Combat Skill calculation route.
- Formula: final score = 50 - (current Willpower + current Combat Skill).
- Routes:
  - final score 15 or more -> 295
  - final score 14 or less -> 320
- Build note: current Willpower may be negative, so use the actual current value in the calculation.

### Section 227

- Type: narrative forced route.
- State change: none confirmed.
- Out link: 29.
- Build note: no section-specific automation needed beyond normal navigation.

### Section 228

- Type: plain route choice.
- State change: none confirmed.
- Choices:
  - head west to pick up the Azan River -> 328
  - retrace steps -> 6
- Build note: no section-specific automation needed beyond normal choice display.

### Section 229

- Type: Staff attack result with follow-up route choice.
- State change: lose 2 Willpower for the first Yaku attack.
- Footnote: if there is insufficient Willpower for the first attack, the player may either allow the Willpower total to go negative or cover missing Willpower with Endurance at 2 END per 1 missing WP.
- Choices:
  - launch another long-range attack on a Yaku threatening Shan -> 5
  - attack the tendrils slithering towards Grey Star -> 30
- Build note: after section 229's initial cost, route 5 should require current Willpower of at least 2 because section 5 has no insufficiency footnote. Route 30 has its own explicit insufficiency footnote.

### Section 230

- Type: narrative forced route.
- State change: none confirmed.
- Out link: 291.
- Build note: no section-specific automation needed beyond normal navigation.

### Section 231

- Type: combat with defensive Combat Skill penalty.
- State change: combat only.
- Combat: Quoku, Combat Skill 12, Endurance 30. No evade; fight until victory or death. Subtract 2 Combat Skill for this combat because Grey Star must avoid the creature's poisonous skin.
- Victory route: 256.
- Build note: combat payload needs a -2 Combat Skill modifier and evade disabled.

### Section 232

- Type: narrative forced route.
- State change: none confirmed.
- Out link: 154.
- Build note: no section-specific automation needed beyond normal navigation.

### Section 233

- Type: narrative forced route.
- State change: none confirmed in this section.
- Out link: 337.
- Build note: Shan is grabbed here narratively, but section 337 resolves the immediate combat response.

### Section 234

- Type: narrative forced route.
- State change: none confirmed.
- Out link: 197.
- Build note: no section-specific automation needed beyond normal navigation.

### Section 235

- Type: optional Psychomancy result with forced onward route.
- State change: lose 1 Willpower.
- Out link: 214.
- Build note: source section 286 requires Psychomancy. Because there is no insufficient-WP footnote here, the Psychomancy route should require current Willpower of at least 1 before entering section 235.

### Section 236

- Type: Psychomancy result with forced return to the section 172 power hub.
- State change: lose 1 Willpower.
- Out link: 172.
- Build note: this is a target of section 172, so the section 172 negative-WP exception applies to the 1 WP Psychomancy cost.

### Section 237

- Type: terminal failure ending.
- State change: adventure ends in failure.
- Out link: none.
- Build note: mark as terminal once ending automation exists.

### Section 238

- Type: plain route choice.
- State change: none confirmed.
- Choices:
  - leave the river bank again and head east/south -> 303
  - take chances with Yaku plants along the river -> 104
- Build note: no section-specific automation needed beyond normal choice display.

### Section 239

- Type: Staff result followed by route choice.
- State change: lose 2 Willpower.
- Choices:
  - upward-sloping passage -> 267
  - downward-sloping passage -> 272
  - return the way Grey Star came -> 284
- Build note: source section 222 should require current Willpower of at least 2 before choosing this route because section 239 has no insufficiency footnote.

### Section 240

- Type: narrative forced route.
- State change: none confirmed.
- Out link: 204.
- Build note: no section-specific automation needed beyond normal navigation.

### Section 241

- Type: plain route choice.
- State change: none confirmed.
- Choices:
  - obey the Shadakine officer -> 300
  - attack them -> 66
  - turn and make a break for it -> 20
- Build note: no section-specific automation needed beyond normal choice display.

### Section 242

- Type: Endurance/Willpower calculation route.
- Formula: current Endurance + current Willpower.
- Routes:
  - total 20 or more -> 341
  - total 19 or less -> 316
- Build note: use the actual current Willpower value, including negative values if present.

### Section 243

- Type: combat with Combat Skill modifier, optional loot, and post-combat route choice.
- State change: combat first; after victory, optional Dagger as a Weapon.
- Combat: Gaoler, Combat Skill 8, Endurance 14. No evade; fight to the death. Add +4 Combat Skill for Shan's help and surprise.
- Choices after victory:
  - take Gaoler's Keys and free prisoners -> 125
  - head in the direction the gaoler came from -> 338
  - head in the opposite direction -> 333
- Build note: combat payload needs +4 Combat Skill and evade disabled. Section 125 handles the Gaoler's Keys follow-up.

### Section 244

- Type: plain route choice.
- State change: none confirmed.
- Choices:
  - stand and fight -> 167
  - dash for the forest -> 13
- Build note: no section-specific automation needed beyond normal choice display.

### Section 245

- Type: gear recovery with forced onward route.
- State change: restore Wizard's Staff, Backpack, and Backpack Items to the Action Chart.
- Out link: 292.
- Build note: future automation may need a confiscated/recovered gear status.

### Section 246

- Type: combat, no evade.
- State change: combat only.
- Combat: Soldier Mantiz, Combat Skill 14, Endurance 10. No evade; fight to the death.
- Victory route: 290.
- Build note: generic combat works, with evade disabled.

### Section 247

- Type: narrative forced route.
- State change: none confirmed.
- Out link: 62.
- Build note: no section-specific automation needed beyond normal navigation.

### Section 248

- Type: Staff result with follow-up route choice.
- State change: lose 1 Willpower for cutting the tendril from Grey Star's ankle.
- Footnote: if there is insufficient Willpower for the first cost, the player may either allow the Willpower total to go negative or cover missing Willpower with Endurance at 2 END per 1 missing WP.
- Choices:
  - free Shan by attacking the tendril -> 204
  - strike at the heart of the Yaku attacking Grey Star -> 229
  - long-range Staff bolt at the Yaku attacking Shan -> 254
- Build note: route 204 and route 229 have their own insufficient-WP footnotes. Route 254 should require current Willpower of at least 2 after section 248's cost because section 254 has no insufficiency footnote.

### Section 249

- Type: plain route choice.
- State change: none confirmed.
- Choices:
  - shout a warning to Shan -> 282
  - hurry to Shan's side -> 257
- Build note: no section-specific automation needed beyond normal choice display.

### Section 250

- Type: Evocation attempt route choice.
- State change: mark Evocation attempted.
- Choices:
  - accept the dead priest's bargain -> 326
  - refuse -> 305
- Build note: this section has no Willpower cost stated. It should set an Evocation-attempted flag because section 211 blocks a repeat attempt.

### Section 251

- Type: Enchantment result followed by route choice.
- State change: none in this section; the Enchantment cost was already paid by the source section.
- Choices:
  - leave by the main entrance to the harbour -> 50
  - turn into the dark, narrow street -> 40
- Build note: no section-specific automation needed beyond normal choice display.

### Section 252

- Type: loot with forced onward route.
- State change: add up to 5 Meals, respecting carrying limits.
- Out link: 327.
- Build note: future automation should offer a Meal loot prompt.

### Section 253

- Type: plain route choice.
- State change: none confirmed.
- Choices:
  - run back down and head for the other stairway -> 80
  - attack the Shadakine guard -> 324
- Build note: no section-specific automation needed beyond normal choice display.

### Section 254

- Type: Staff result with forced onward route.
- State change: lose 2 Willpower.
- Out link: 279.
- Build note: source section 248 should require current Willpower of at least 2 before choosing this route because section 254 has no insufficiency footnote.

### Section 255

- Type: combat, no evade.
- State change: combat only.
- Combat: 2 Shadakine Warriors, Combat Skill 15, Endurance 25. No evade; fight to the death.
- Victory route: 75.
- Build note: generic combat works, with evade disabled.

### Section 256

- Type: plain route choice.
- State change: none confirmed.
- Choices:
  - stand and fight the Quoku -> 281
  - keep running -> 107
- Build note: no section-specific automation needed beyond normal choice display.

### Section 257

- Type: forced Willpower cost with forced onward route.
- State change: lose 1 Willpower.
- Footnote: if there is insufficient Willpower, the player may either allow the Willpower total to go negative or cover missing Willpower with Endurance at 2 END per 1 missing WP.
- Out link: 174.
- Build note: future automation should preserve the footnote options.

### Section 258

- Type: narrative forced route.
- State change: none confirmed.
- Out link: 62.
- Build note: no section-specific automation needed beyond normal navigation.

### Section 259

- Type: mental combat with fixed derived Combat Skill.
- Combat: Darkling Room, Combat Skill 28, Endurance 30.
- Starting mental Combat Skill: current Willpower + current Endurance.
- Ruling: Darkling Room damage reduces Grey Star's Endurance. Grey Star's mental Combat Skill stays fixed from the starting calculation for the whole combat.
- Victory route: 296.
- Build note: future automation needs a fixed computed Combat Skill and Endurance damage handling for this mental combat.

### Section 260

- Type: combat, no evade.
- Combat: 2 Soldier Mantiz, Combat Skill 18, Endurance 20.
- Rule: Grey Star is trapped between them and must fight them both together.
- Victory route: 213.
- Build note: no evade option; route only after victory.

### Section 261

- Type: narrative forced route.
- State change: none confirmed.
- Out link: 291.
- Build note: no section-specific automation needed beyond normal navigation.

### Section 262

- Type: death ending.
- State change: mark adventure ended/dead.
- Out link: none.
- Build note: future ending automation should mark this as a terminal death section.

### Section 263

- Type: narrative forced route.
- State change: none confirmed.
- Out link: 146.
- Build note: no section-specific automation needed beyond normal navigation.

### Section 264

- Type: item consumption plus hidden puzzle route.
- Prerequisite: source route from section 18 requires the Medallion of the Redeemer and Vial of Pink Liquid.
- State change: delete the Vial of Pink Liquid after drinking the potion; keep the Medallion.
- Routes:
  - solved rune puzzle -> 110
  - take Shan's advice -> 190
  - seek Jnana's counsel -> 134
- Build note: future automation should remove the vial and support the hidden puzzle answer route plus fallback choices.

### Section 265

- Type: Staff result plus combat.
- Prerequisite: source section 121 attack route requires current Willpower of at least 1.
- State change: lose 1 Willpower.
- Combat: Shadakine Warrior, Combat Skill 14, Endurance 18.
- Victory route: 40.
- Build note: no evade option; route only after victory.

### Section 266

- Type: plain route choice.
- State change: none confirmed.
- Choices:
  - evade the diving Quoku -> 330
  - stand and fight -> 231
- Build note: normal choice prompt only; section 231 contains the combat.

### Section 267

- Type: plain route choice.
- State change: none confirmed.
- Choices:
  - east corridor -> 332
  - western exit -> 340
  - southern exit -> 347
- Build note: normal choice prompt only.

### Section 268

- Type: forced Endurance loss, then route choice.
- State change: lose 1 Endurance.
- Choices:
  - crawl into the cave -> 8
  - continue scaling the cliff -> 113
- Build note: future automation should apply -1 Endurance before presenting the choices.

### Section 269

- Type: item loss, then forced route.
- Prerequisite: Coil of Rope carried from the source route.
- State change: delete Coil of Rope.
- Out link: 294.
- Build note: future automation should remove the Rope before routing onward.

### Section 270

- Type: recovery, then route choice.
- State change: restore 1 Willpower and 3 Endurance.
- Ruling: Willpower recovery is uncapped; Endurance recovery caps at starting Endurance.
- Choices:
  - sleep now -> 201
  - do not sleep -> 144
- Build note: text says Grey Star does not have the Wizard's Staff here, but this section does not itself apply a new inventory change.

### Section 271

- Type: Elementalism result forced route.
- Prerequisite: source section 172 route requires Elementalism.
- State change: none in this section; the Willpower cost is applied in section 273.
- Out link: 273.
- Build note: no section-specific automation needed here beyond normal navigation.

### Section 272

- Type: forced Endurance loss plus timed combat.
- State change: lose 2 Endurance before combat.
- Combat: 2 Soldier Mantiz, Combat Skill 20, Endurance 15.
- Timed result:
  - win in three rounds or less -> 322
  - if combat enters a fourth round -> 315 immediately
- Build note: future automation needs a three-round combat limit and failure route.

### Section 273

- Type: forced Willpower cost with forced onward route.
- Prerequisite: source section 172 Elementalism choice; section 172 footnote permits insufficient-WP handling because a Magical Power choice is forced there.
- State change: lose 1 Willpower; if insufficient WP, allow negative WP or pay 2 END per missing WP.
- Out link: 259.
- Build note: future automation should preserve the section 172 footnote options.

### Section 274

- Type: narrative forced route.
- State change: none confirmed.
- Out link: 306.
- Build note: no section-specific automation needed beyond normal navigation.

### Section 275

- Type: narrative forced route.
- State change: none confirmed.
- Out link: 18.
- Build note: no section-specific automation needed beyond normal navigation.

### Section 276

- Type: companion loss narrative forced route.
- State change: mark Tanith lost/dead/unavailable.
- Out link: 52.
- Build note: future companion-state automation should record Tanith's sacrifice.

### Section 277

- Type: narrative forced route.
- State change: none confirmed.
- Out link: 252.
- Build note: no section-specific automation needed beyond normal navigation.

### Section 278

- Type: Prophecy result forced route.
- Prerequisite: source section 54 route requires Prophecy and current Willpower of at least 1.
- State change: lose 1 Willpower.
- Out link: 184.
- Build note: optional Magical Power use, so require enough Willpower before the source route is legal.

### Section 279

- Type: forced Willpower cost with forced onward route.
- State change: lose 1 Willpower.
- Footnote: if there is insufficient Willpower, the player may either allow the Willpower total to go negative or cover missing Willpower with Endurance at 2 END per 1 missing WP.
- Out link: 128.
- Build note: future automation should preserve the footnote options; the section 175 link in the footnote is a cross-book rules reference, not a local route.

### Section 280

- Type: Prophecy-gated route choice.
- State change: none in this section.
- Choices:
  - use Prophecy -> 53
  - agree to sell the boat -> 16
  - refuse to sell and enter Port of Suhn -> 100
- Build note: route 53 requires Prophecy and leads to its own -1 WP cost; route 16 handles the 20 Nobles gain.

### Section 281

- Type: one-round combat with Combat Skill modifier and Willpower threshold route.
- Combat: Large Quoku, Combat Skill 15, Endurance 30.
- Modifier: deduct 1 Combat Skill for this combat.
- Limit: fight one combat round only.
- Route check after the round:
  - current Willpower 10 or more -> 331
  - current Willpower less than 10 -> 32
- Build note: future automation needs a one-round combat mode, a temporary -1 CS modifier, and a post-round WP threshold check.

### Section 282

- Type: narrative forced route.
- State change: none confirmed.
- Out link: 148.
- Build note: no section-specific automation needed beyond normal navigation.

### Section 283

- Type: forced Endurance loss with forced onward route.
- State change: lose 3 Endurance.
- Out link: 227.
- Build note: future automation should apply -3 Endurance before routing onward.

### Section 284

- Type: lit-Torch check plus combat.
- Check: carrying a lit Torch.
- Routes:
  - lit Torch -> 207
  - no lit Torch: fight 4 Soldier Mantiz, Combat Skill 20, Endurance 25; victory -> 310
- Build note: future automation should gate the torch route and disable evade for the combat.

### Section 285

- Type: Staff result forced route.
- Prerequisite: source section 179 route requires current Willpower of at least 2 after section 179's initial cost.
- State change: lose 2 Willpower.
- Out link: 128.
- Build note: optional Staff use, so do not allow this branch unless the cost can be paid.

### Section 286

- Type: Psychomancy gate or random route.
- Check: Psychomancy.
- Routes:
  - has Psychomancy -> 235
  - no Psychomancy and random number 0, 2, 4, 6, or 8 -> 214
  - no Psychomancy and random number 1, 3, 5, 7, or 9 -> 205
- Build note: future automation should present the Psychomancy route when legal and otherwise use the even/odd random-number map.

### Section 287

- Type: forced Endurance loss with forced onward route.
- State change: lose 2 Endurance.
- Out link: 263.
- Build note: future automation should apply -2 Endurance before routing onward.

### Section 288

- Type: extra Sorcery Willpower cost with forced onward route.
- Prerequisite: source section 191 route spends 4 Willpower first and should leave at least 2 Willpower for this extra cost.
- State change: lose 2 Willpower.
- Out link: 320.
- Build note: because no insufficient-WP footnote is present, the section 191 branch to 288 should require enough Willpower for both the 4-point draw and this extra 2-point cost.

### Section 289

- Type: Willpower threshold route.
- State change: none confirmed.
- Check:
  - current Willpower less than 15 -> 150
  - current Willpower 15 or more -> 175
- Build note: future automation should present an automatic threshold route based on current Willpower.

### Section 290

- Type: plain route choice.
- State change: none confirmed.
- Choices:
  - upward-sloping passage -> 267
  - downward-sloping passage -> 272
  - back the way you came -> 284
- Build note: normal choice prompt only.

### Section 291

- Type: gear confiscation narrative forced route.
- State change: Wizard's Staff, Backpack, and Backpack Items are unavailable; retain non-Backpack items such as the Herb Pouch.
- Out link: 178.
- Build note: do not delete Backpack contents; mark them as confiscated/unavailable so section 245 can restore them later.

### Section 292

- Type: Special Item check route.
- Check: Amulet of the Shianti priest.
- Choices:
  - has Amulet -> 346
  - no Amulet -> 199
- Build note: future automation should gate the routes by Special Item possession.

### Section 293

- Type: forced Endurance loss, then route choice.
- State change: lose 1 Endurance.
- Choices:
  - swim towards the waterfall -> 318
  - investigate cliffs on the other side -> 343
- Build note: future automation should apply -1 Endurance before presenting choices.

### Section 294

- Type: companion loss plus Endurance threshold route.
- State change: mark Shan lost/dead/unavailable.
- Check:
  - current Endurance less than 10 -> 319
  - current Endurance 10 or more -> 344
- Build note: future automation should record Shan's loss and route by current Endurance.

### Section 295

- Type: forced Endurance loss with forced onward route.
- State change: lose 2 Endurance.
- Out link: 187.
- Build note: future automation should apply -2 Endurance before routing onward.

### Section 296

- Type: narrative forced route.
- State change: none confirmed.
- Out link: 41.
- Build note: no section-specific automation needed beyond normal navigation.

### Section 297

- Type: Alchemy item conversion, then route choice.
- Prerequisite: source section 151 requires Sulphur, Saltpetre, Ezeran Crystals, and an empty Vial.
- State change:
  - remove Sulphur.
  - remove Saltpetre.
  - remove Ezeran Crystals.
  - convert one empty Vial into Ezeran Acid.
  - add two empty Vials from the spent Sulphur and Saltpetre containers.
- Choices:
  - go right -> 23
  - go left -> 333
- Build note: if empty Vial count is tracked, this conversion should preserve the two emptied ingredient vials and one prepared Ezeran Acid vial.

### Section 298

- Type: Staff/Willpower plus Endurance loss forced route.
- Prerequisite: source section 340 Staff attack route requires the Wizard's Staff and current Willpower of at least 2.
- State change: lose 2 Willpower and 2 Endurance.
- Out link: 263.
- Build note: optional Staff use, so do not allow this branch unless the WP cost can be paid.

### Section 299

- Type: death ending.
- State change: mark adventure ended/dead.
- Out link: none.
- Build note: future ending automation should mark this as a terminal death section.

### Section 300

- Type: gear confiscation forced route.
- State change: Wizard's Staff, Backpack, and Backpack Items are unavailable; keep note of Backpack Items for later recovery.
- Out link: 289.
- Build note: do not delete Backpack contents; mark them as confiscated/unavailable so section 245 can restore them later.

### Section 301

- Type: Willpower gain with forced onward route.
- State change: restore 10 Willpower.
- Ruling: Willpower gains are uncapped.
- Out link: 247.
- Build note: future automation should apply +10 Willpower before routing onward.

### Section 302

- Type: narrative forced route.
- State change: none confirmed.
- Out link: 252.
- Build note: no section-specific automation needed beyond normal navigation.

### Section 303

- Type: forced Endurance loss with forced onward route.
- State change: lose 2 Endurance.
- Out link: 325.
- Build note: future automation should apply -2 Endurance before routing onward.

### Section 304

- Type: forced Willpower cost with forced onward route.
- State change: lose 1 Willpower.
- Footnote: if there is insufficient Willpower, the player may either allow the Willpower total to go negative or cover missing Willpower with Endurance at 2 END per 1 missing WP.
- Out link: 128.
- Build note: future automation should preserve the footnote options; the section 175 link in the footnote is a cross-book rules reference, not a local route.

### Section 305

- Type: Evocation result Willpower cost with forced return route.
- Prerequisite: source section 250 came from the forced-power menu in section 172, so section 172's insufficiency footnote applies.
- State change: lose 2 Willpower; if insufficient WP, allow negative WP or pay 2 END per missing WP. Evocation cannot be chosen again from section 172.
- Out link: 172.
- Build note: future automation should mark Evocation unavailable/used for the repeated section 172 choice.

### Section 306

- Type: death ending.
- State change: mark adventure ended/dead.
- Out link: none.
- Build note: future ending automation should mark this as a terminal death section.

### Section 307

- Type: narrative forced route.
- State change: none confirmed.
- Out link: 249.
- Build note: no section-specific automation needed beyond normal navigation.

### Section 308

- Type: combat with modifier, no evade.
- Combat: Shadakine Warriors, Combat Skill 20, Endurance 19.
- Modifier: add 4 Combat Skill for the whole combat due to surprise.
- Victory route: 127.
- Build note: future automation should apply a temporary +4 CS modifier and disable evade.

### Section 309

- Type: combat with timed modifier and evade.
- Combat: Shadakine Guard, Combat Skill 12, Endurance 16.
- Modifier: add 4 Combat Skill for the first two rounds only.
- Routes:
  - evade at any time -> 137
  - victory -> 171
- Build note: future automation should support timed combat modifiers.

### Section 310

- Type: plain route choice.
- State change: none confirmed.
- Choices:
  - upward-sloping passage -> 267
  - downward-sloping passage -> 272
- Build note: normal choice prompt only.

### Section 311

- Type: gear confiscation plus forced Endurance loss with forced onward route.
- State changes: mark Wizard's Staff, Backpack, and Backpack Items unavailable; keep note of Backpack Items for later recovery. Lose 1 Endurance from the crude treatment.
- Out link: 289.
- Build note: future automation should preserve Backpack contents rather than deleting them, then apply -1 Endurance before routing onward.

### Section 312

- Type: death ending.
- State change: mark adventure ended/dead.
- Out link: none.
- Build note: future ending automation should mark this as a terminal death section.

### Section 313

- Type: Prophecy result Willpower cost with forced onward route.
- Prerequisite: source section 105 requires Prophecy and, under the optional-power ruling, at least 1 Willpower before choosing this route.
- State change: lose 1 Willpower.
- Out link: 209.
- Build note: future automation should gate the section 105 Prophecy route by Power and WP before applying this cost.

### Section 314

- Type: Kazim Stone duel result with Willpower cost, half-current Endurance loss, and route choice.
- Prerequisite: source section 191 spend-3 branch should require at least 1 Willpower remaining after the 3-point spend, so the immediate section 314 cost can be paid.
- State changes: lose 1 Willpower, then lose half current Endurance, rounded down.
- Choices:
  - if current Willpower is at least 2, spend 2 Willpower to duplicate Mother Magri's attack -> 320
  - if current Willpower is at least 2, spend 2 Willpower to extinguish the circle of light -> 226
  - if current Willpower is less than 2 for either option -> 150
- Build note: future automation needs a half-current Endurance loss action and a WP-gated two-option prompt after the -1 WP cost.

### Section 315

- Type: death ending.
- State change: mark adventure ended/dead.
- Out link: none.
- Build note: future ending automation should mark this as a terminal death section.

### Section 316

- Type: death ending.
- State change: mark adventure ended/dead.
- Out link: none.
- Build note: future ending automation should mark this as a terminal death section.

### Section 317

- Type: death ending.
- State change: mark adventure ended/dead.
- Out link: none.
- Build note: future ending automation should mark this as a terminal death section.

### Section 318

- Type: death ending.
- State change: mark adventure ended/dead.
- Out link: none.
- Build note: future ending automation should mark this as a terminal death section.

### Section 319

- Type: forced Endurance loss with forced onward route.
- State change: lose 1 Endurance.
- Out link: 43.
- Build note: future automation should apply -1 Endurance before routing onward.

### Section 320

- Type: Kazim Stone duel resource loss with forced onward route.
- State changes: lose 4 Willpower, allowing negative Willpower under the forced-loss ruling, and lose 4 Endurance; these losses are in addition to any earlier Kazim Stone duel losses.
- Out link: 187.
- Build note: future automation should apply both resource losses on entry before routing onward.

### Section 321

- Type: combat with evade.
- Combat: Gaoler, Combat Skill 8, Endurance 10.
- Routes:
  - evade at any time -> 137
  - victory -> 37
- Build note: generic combat works, but future automation should surface the any-time evade route.

### Section 322

- Type: narrative forced route.
- State change: none confirmed.
- Out link: 267.
- Build note: no section-specific automation needed beyond normal navigation.

### Section 323

- Type: Kazim Stone duel result with Willpower cost, half-current Endurance loss, and follow-up WP choices.
- Prerequisite: source section 191 spend-2 branch should require at least 2 Willpower remaining after the 2-point spend, so section 323's immediate -1 WP and the safe forced extinguish option can both be paid. The route to section 299 additionally requires at least 2 Willpower after the immediate section 323 cost.
- State changes: lose 1 Willpower, then lose half current Endurance, rounded down.
- Choices:
  - if current Willpower is at least 2 after the immediate cost, spend 2 Willpower to turn the attack against Mother Magri -> 299
  - otherwise, spend 1 Willpower to extinguish the energy field -> 226
- Build note: future automation needs the half-current Endurance loss action and should only offer the section 299 branch when the 2 WP cost can be paid.

### Section 324

- Type: death ending.
- State change: mark adventure ended/dead.
- Out link: none.
- Build note: future ending automation should mark this as a terminal death section.

### Section 325

- Type: narrative forced route.
- State change: none confirmed.
- Out link: 136.
- Build note: no section-specific automation needed beyond normal navigation.

### Section 326

- Type: route choice.
- State change: none confirmed.
- Choices:
  - agree to speak the tome -> 87
  - deny the dead -> 220
- Build note: normal choice prompt only.

### Section 327

- Type: route choice.
- State change: none confirmed.
- Choices:
  - head back to the shack -> 78
  - keep moving towards the Azanam -> 283
- Build note: normal choice prompt only.

### Section 328

- Type: forced Endurance loss with forced onward route.
- State change: lose 2 Endurance.
- Out link: 104.
- Build note: future automation should apply -2 Endurance before routing onward.

### Section 329

- Type: optional Staff result with Willpower and Endurance loss.
- Prerequisite: source section 204 route should require at least 1 Willpower after section 204's initial Staff cost; section 329 has no insufficiency footnote.
- State changes: lose 1 Willpower and 4 Endurance.
- Out link: 42.
- Build note: future automation should gate the section 204 route by current WP before applying section 329's losses.

### Section 330

- Type: narrative forced route.
- State change: none confirmed.
- Out link: 256.
- Build note: no section-specific automation needed beyond normal navigation.

### Section 331

- Type: route choice.
- State change: none confirmed.
- Choices:
  - fight the Quoku -> 307
  - evade combat -> 182
- Build note: normal choice prompt only; the fight route does not start combat in this section.

### Section 332

- Type: Staff/WP threshold route.
- Check: Wizard's Staff available and current Willpower at least 2 for the Staff route.
- State change: none in this section; section 96 applies the 2 Willpower cost and 2 Endurance loss.
- Routes:
  - Staff/WP check passes -> 96
  - Staff/WP check fails -> 9
- Build note: future automation should gate the section 96 route by Staff availability and current WP before target section 96 applies costs.

### Section 333

- Type: narrative forced route.
- State change: none confirmed.
- Out link: 259.
- Build note: no section-specific automation needed beyond normal navigation.

### Section 334

- Type: route choice.
- State change: none confirmed.
- Choices:
  - left passage -> 222
  - right passage -> 234
- Build note: normal choice prompt only.

### Section 335

- Type: companion loss narrative forced route.
- State change: mark Shan lost/dead/unavailable.
- Out link: 294.
- Build note: future automation should preserve Shan's lost status before routing onward; section 294 also handles Shan loss on another branch.

### Section 336

- Type: route choice.
- State change: none confirmed.
- Choices:
  - narrow street -> 40
  - main entrance -> 50
- Build note: normal choice prompt only.

### Section 337

- Type: combat, no evade stated.
- Combat: Wounded Quoku, Combat Skill 14, Endurance 18.
- Victory route: 44.
- Build note: future automation should disable evade.

### Section 338

- Type: Prophecy-gated return-section route plus ordinary route choice.
- State change: none in this section; section 92 applies the 1 Willpower Prophecy cost and returns to section 338.
- Choices:
  - Prophecy, if known and current WP >= 1 -> 92, then return to 338
  - left stairway -> 137
  - right stairway -> 212
- Build note: future automation should store this section as the return target before routing to section 92.

### Section 339

- Type: forced Nobles loss with route choice.
- Prerequisite: source section 82 buy-drink route requires Nobles > 0.
- State change: lose 1 Noble for ale.
- Choices:
  - talk to innkeeper -> 217
  - do not talk -> 105
- Build note: future automation should apply -1 Noble before presenting the conversation choice.

### Section 340

- Type: Staff/WP-gated route choice plus ordinary route.
- State change: none in this section; section 298 applies the Staff attack cost and Endurance loss.
- Choices:
  - attack with Wizard's Staff, requiring Staff available and WP >= 2 -> 298
  - jump onto Cave Mantiz -> 287
- Build note: future automation should gate the Staff route by Staff availability and current WP; the target section 298 applies the costs.

### Section 341

- Type: forced Endurance loss with forced onward route.
- State change: lose 1 Endurance.
- Out link: 8.
- Build note: future automation should apply -1 Endurance before routing onward.

### Section 342

- Type: unreachable forced Endurance loss with forced onward route.
- Footnote: no choice leads to this section; Project Aon marks this as an authorial oversight.
- State change: lose 3 Endurance.
- Out link: 74.
- Build note: keep the section data available, but do not expect a normal in-book source route.

### Section 343

- Type: forced Endurance loss with route choice.
- State change: lose 1 Endurance.
- Choices:
  - wade across the River Azan -> 17
  - jump across stepping stones -> 242
- Build note: future automation should apply -1 Endurance before presenting the route choice.

### Section 344

- Type: narrative forced route.
- State change: none confirmed.
- Out link: 43.
- Build note: no section-specific automation needed beyond normal navigation.

### Section 345

- Type: Prophecy result Willpower cost with forced onward route.
- Prerequisite: source section 136 requires Prophecy and WP >= 1.
- State change: lose 1 Willpower.
- Out link: 61.
- Build note: future automation should gate the section 136 Prophecy route before applying this cost.

### Section 346

- Type: narrative forced route.
- State change: none confirmed.
- Out link: 199.
- Build note: no section-specific automation needed beyond normal navigation.

### Section 347

- Type: narrative forced route.
- State change: none confirmed.
- Out link: 47.
- Build note: no section-specific automation needed beyond normal navigation.

### Section 348

- Type: narrative forced route.
- State change: none confirmed.
- Out link: 187.
- Build note: no section-specific automation needed beyond normal navigation.

### Section 349

- Type: gear-recovery encounter route choice.
- State change: none in this section; Tanith is carrying the Wizard's Staff and Backpack, but section 245 handles restoration if that branch is chosen.
- Choices:
  - attack Tanith -> 173
  - persuade Tanith -> 245
- Build note: future automation should not restore gear here; restoration belongs to section 245.

### Section 350

- Type: successful book ending / next-book hook.
- State change: mark book 1 completed successfully.
- Out link: none local; external continuation points to Grey Star book 2, The Forbidden City.
- Build note: future ending automation should mark this as a terminal success section rather than a death ending.
