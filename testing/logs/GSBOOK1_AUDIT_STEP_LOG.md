# GS Book 1 Audit Step Log

Book: Grey Star the Wizard

## Current Audit State

Current step: Pass 1 complete. Next step is Pass 2 route branch audit from section 1.

Update: section-by-section audit mode approved. The numerical section audit now lives in `GSBOOK1_SECTION_AUDIT.md`.

The Grey Star audit standard has been added under `docs/`, and the first mechanical source sweep has generated the starter report set under `testing/logs/`.

## Completed Setup

- Added `docs/BOOK_AUDIT_WORKFLOW.md`.
- Added `docs/BOOK_SOURCE_MAP.md`.
- Confirmed local Book 1 folder: `books/gs/01gstw`.
- Confirmed section coverage: `sect1.htm` through `sect350.htm` are present.
- Generated `testing/tmp/gsbook1_source_inventory.json`.
- Generated `testing/tmp/gsbook1_source_sweep.json`.
- Created starter audit reports:
  - `GSBOOK1_AUTOMATION_LEDGER.md`
  - `GSBOOK1_ENDINGS_AND_ROUTE_FAMILIES.md`
  - `GSBOOK1_RULES_AND_ITEMS_AUDIT.md`
  - `GSBOOK1_COMBAT_AND_RANDOM_AUDIT.md`
  - `GSBOOK1_ACHIEVEMENT_CANDIDATES.md`
- Completed Pass 1 rules baseline:
  - `GSBOOK1_PASS1_RULES_BASELINE.md`
- Started section-by-section audit:
  - `GSBOOK1_SECTION_AUDIT.md`

## Step 1 Checklist

- [x] Read and confirm `title.htm`.
- [x] Read support pages:
  - `gamerulz.htm`
  - `powers.htm`
  - `equipmnt.htm`
  - `action.htm`
  - `cmbtrulz.htm`
  - `crsumary.htm`
  - `crtable.htm`
  - `random.htm`
  - `sage.htm`
  - `footnotz.htm`
  - `errata.htm`
- [x] Begin human route read at `sect1.htm`.
- For each section, update the automation ledger with confirmed state changes, prompts, combat exceptions, and item/Magick requirements.

## First Human-Read Anchor

Section 1 is the opening section. Its same-book choices point to sections 202 and 168.

Confirmed section 1 rule: Magick-gated route choice for Elementalism. No state change is confirmed at section 1.

Pass 2 originally pointed at route branches 202 and 168. The audit method has changed to numerical order, so the current working section is section 2, then section 3.

Section 2 ruling received: literal section logic. If the player cannot consume 2 Meals, apply the full 6 Endurance loss.

Section 3 ruling received: after Grey Star's own Meal requirement, remove up to 2 remaining Meals for Tanith and Shan.

Section 4 confirmed: set Willpower to 0, then route to section 350.

Section 5 ruling updated: book rules trump house rules. Mandatory/forced Willpower losses can reduce Willpower below 0 where the book or footnote permits. Later source audit found section 5 is only reached from section 229's optional Staff route, so section 229 should require WP >= 2 before route 5 is legal.

Sections 6-10 confirmed:

- Section 6: lose 4 Endurance, then route to section 325.
- Section 7: narrative forced route to section 270.
- Section 8: plain route choice to sections 14 or 19.
- Section 9: terminal death ending.
- Section 10: Kazim Stone gate to sections 51 or 90.

Sections 11-14 confirmed:

- Section 11: lose 1 Willpower, allowing negative WP, then choose surrender, attack, or run.
- Section 12: lose 3 Willpower, allowing negative WP, then route to section 325.
- Section 13: narrative forced route to section 75.
- Section 14: terminal death ending.

Section 15 ruling received: round down odd half-current-total recovery. Add `floor(current / 2)` to current Endurance and Willpower; Endurance remains capped at starting Endurance, and Willpower may exceed its starting value.

Sections 16-20 confirmed:

- Section 16: gain 20 Nobles, then choose street or harbour front.
- Section 17: terminal death ending.
- Section 18: Medallion of the Redeemer + Vial of Pink Liquid gate, plus ordinary route choices.
- Section 19: Torch/Tinderbox route, optional Staff-glow route if current Willpower is at least 1, or dark route.
- Section 20: terminal death ending.

Sections 21-25 confirmed:

- Section 21: narrative forced route to section 39.
- Section 22: darkness route, or light-source route via Torch/Tinderbox or Staff glow; Staff glow costs 1 WP and is optional magic.
- Section 23: optional Prophecy branch to section 92, with return note, or stairway choices.
- Section 24: plain route choice to sections 10 or 33.
- Section 25: route choice toward Kazim Stone pickup or immediate exit; no pickup is applied until section 77.

Sections 26-30 confirmed:

- Section 26: plain route choice to sections 97, 166, or 241.
- Section 27: narrative forced route to section 195.
- Section 28: plain route choice to sections 308 or 336.
- Section 29: plain route choice to sections 54 or 104.
- Section 30: lose 2 Willpower, allowing negative WP, then route to section 128.

Sections 31-35 confirmed:

- Section 31: optional Elementalism result; lose 1 WP, then route to section 75.
- Section 32: plain route choice to sections 107 or 57.
- Section 33: plain route choice to sections 10 or 69.
- Section 34: Nobles-gated route choice; section 133 handles money loss.
- Section 35: narrative forced route to section 59.

Sections 36-40 confirmed:

- Section 36: plain route choice to sections 201 or 144.
- Section 37: loot prompt for Gaoler's Keys, 3 Nobles, and optional Dagger.
- Section 38: restore 2 WP and 4 END, then resolve Laumspur by Alchemy status.
- Section 39: plain route choice to sections 55 or 208.
- Section 40: optional Prophecy branch, plus three ordinary street/alley choices.

Sections 41-45 confirmed:

- Section 41: narrative forced route to section 349.
- Section 42: Staff locally out of reach; Jewelled Dagger/other Weapon/Shan routes.
- Section 43: loot transfer from Shan's Backpack plus optional Prophecy branch.
- Section 44: plain route choice to sections 317 or 335.
- Section 45: plain route choice to sections 312 or 80.

Sections 46-50 confirmed:

- Section 46: optional Staff-glow result; lose 1 WP, then route to section 35.
- Section 47: lose 8 END, then route to section 146.
- Section 48: optional Sorcery result; lose 3 WP, then route to section 75.
- Section 49: random-number test with Silver Charm and WP>10 modifiers.
- Section 50: plain route choice to sections 40 or 155.

Section 51 confirmed: delete Kazim Stone from Backpack Items, then route to section 102.

Section 52 ruling received: book rules allow Willpower to go negative. Apply the full -1 WP traumatic/sleep loss even if current Willpower is 0 or lower.

Sections 53-55 confirmed:

- Section 53: optional Prophecy result; lose 1 WP, then route to section 16.
- Section 54: optional Prophecy branch, plus left/right/straight route choices.
- Section 55: Enchantment route and long-range Staff route both need 2 WP before choosing; surprise attack route is always available.

Sections 56-60 confirmed:

- Section 56: optional Enchantment result; lose 2 WP, then choose continue spell or aid crowd.
- Section 57: lose 1 WP, allowing negative WP, then choose attack again or escape.
- Section 58: restore 3 WP and 6 END, then resolve Laumspur by Alchemy status; attack-the-Najin route should require WP >= 2 for section 101.
- Section 59: Meal or -3 END, then restore 1 WP and 2 END.
- Section 60: plain route choice to sections 45 or 80.

Sections 61-70 confirmed:

- Section 61: plain route choice to sections 186, 111, or 86; attack route should require WP >= 2 for section 111.
- Section 62: plain route choice to sections 7 or 36.
- Section 63: terminal death ending.
- Section 64: optional Prophecy result; lose 1 WP, then route to section 195.
- Section 65: Yabari Ointment worn/applied status gate.
- Section 66: lose 3 END and 1 WP, allowing negative WP, then route to section 311.
- Section 67: terminal death ending.
- Section 68: lose 1 END, then choose section 293 or 118.
- Section 69: terminal death ending.
- Section 70: optional Enchantment result; lose 2 WP, then choose section 88 or 156.

Sections 71-80 confirmed:

- Section 71: recover handed-over money, add 10 Nobles, optional Dagger, then route to section 195.
- Section 72: narrative forced route to section 22.
- Section 73: delete Ezeran Acid/contaminated vial, optional Prophecy branch, or stair choices.
- Section 74: Coil of Rope gate to sections 194 or 219.
- Section 75: narrative forced route to section 3.
- Section 76: lose 1 WP, allowing negative WP, then route to section 195.
- Section 77: add Kazim Stone as Backpack Item, then choose attack/question.
- Section 78: Meal or -3 END, then restore 1 WP and 2 END.
- Section 79: lose 1 END, then route to section 157.
- Section 80: plain route choice to sections 25 or 41.

Sections 81-90 confirmed:

- Section 81: optional long-range Staff result; lose 2 WP, then choose protect Shan or leave him.
- Section 82: Nobles gate for buying a drink.
- Section 83: optional Staff attack route to section 91, or chase route to section 98.
- Section 84: lose 3 WP, allowing negative WP, then choose section 196 or 224.
- Section 85: restore 1 WP and 1 END, then route to section 18.
- Section 86: narrative forced route to section 266.
- Section 87: add Amulet Special Item, lose 2 WP for Evocation, optional Dagger, then choose route.
- Section 88: optional long-range Staff result with total -3 WP; second WP spend can go negative.
- Section 89: narrative forced route to section 241.
- Section 90: Sorcery shield route or Staff-attack route; target sections handle WP costs.

Sections 91-100 confirmed:

- Section 91: Staff attack result costs 1 WP; optional Staff light costs 1 more WP in this section, while Torch/Tinderbox light has no WP cost.
- Section 92: Prophecy information branch; lose 1 WP, then return to the noted section.
- Section 93: narrative forced route to section 258.
- Section 94: forced Staff attack costs 1 WP and may make WP negative under the footnote/book-rule path.
- Section 95: Sorcery commitment choice; section 109 applies the eventual 4 WP and 1 END cost, with section 172's forced-power footnote allowing negative WP if needed.
- Section 96: Staff reaction result; lose 2 WP and 2 END, then route to section 146.
- Section 97: plain route choice to sections 241 or 89.
- Section 98: light-source choice; Torch/Tinderbox -> 108, Staff glow -> 115, darkness -> 122.
- Section 99: combat with Shadakine Crossbowmen CS 25 END 32; +4 CS modifier; post-combat choice to sections 88 or 94.
- Section 100: plain route choice to sections 40 or 121.

Section 101 ruling received: Shan returns the borrowed weapon to inventory after the Najin fight.

Sections 101-110 confirmed:

- Section 101: section 58 source route requires WP >= 2; lose 2 WP; survive five combat rounds against sequential Najin; Shan's borrowed weapon gives +2 CS and is returned after combat.
- Section 102: lose 2 WP, allowing negative WP, then route to section 149.
- Section 103: terminal death ending.
- Section 104: Staff-action route choice; targets 248 and 179 handle costs, with 179 requiring WP >= 1 from this source.
- Section 105: Prophecy-gated route to 313, plus three ordinary conversation choices.
- Section 106: narrative forced route to section 117.
- Section 107: lose 2 WP, allowing negative WP by footnote, then choose finish Quoku or run.
- Section 108: torchlight forced route to section 135.
- Section 109: Sorcery result; lose 4 WP total and 1 END, allowing negative WP under section 172's forced-power footnote.
- Section 110: hidden riddle-solution destination from section 264, then forced route to section 190.

Sections 111-120 confirmed:

- Section 111: section 61 source route requires WP >= 2; lose 2 WP, then route to section 266.
- Section 112: Enchantment-gated escape route to 56, plus crowd-demand route to 84 and non-magic escape to 28.
- Section 113: plain route choice to sections 138 or 188.
- Section 114: lose 2 WP for Sorcery, optional Prophecy branch to 92, then stair choices.
- Section 115: lose 1 WP, mark Staff light active, then route to section 135.
- Section 116: lose 2 WP for Sorcery shield; route to 150 spends another 2 WP before navigation, or route to 226 for a will contest.
- Section 117: lose 1 WP, allowing negative WP under forced-cost rule, then fight 2 Shadakine Warriors CS 15 END 25.
- Section 118: lose 1 END, then choose section 268 or 293.
- Section 119: lose 2 END, then route to section 128.
- Section 120: lose 1 WP by footnote, then three-round survival combat vs Shadakine Rearguard CS 25 END 30 with +3 CS from Shan.

Sections 121-130 confirmed:

- Section 121: attack route to 265 should require WP >= 1; submit route goes to 300.
- Section 122: terminal death ending.
- Section 123: lose 1 WP for Staff attack, then route to section 149.
- Section 124: Enchantment result from section 172; lose 2 WP, allowing negative WP by forced-power footnote, then choose route.
- Section 125: optional Gaoler's Keys Special Item, then route choice.
- Section 126: plain route choice to sections 161 or 106.
- Section 127: plain route choice to sections 50 or 40.
- Section 128: Elementalism route requires WP >= 1 and target 181 applies cost; Enchantment + Calacena Mushrooms route target 206 consumes mushrooms with no WP cost shown.
- Section 129: plain route choice to sections 67 or 147.
- Section 130: narrative forced route to section 106.

Sections 131-140 confirmed:

- Section 131: narrative forced route to section 300.
- Section 132: section 145 source route requires WP >= 2; lose 2 WP, then route to section 203.
- Section 133: store current Nobles as stolen, set Nobles to 0, then fight Cut-throat CS 10 END 12; evade after 2 rounds to section 27 or win to section 71.
- Section 134: narrative forced route to section 58.
- Section 135: narrative forced route to section 197.
- Section 136: Prophecy route to 345 requires Prophecy and WP >= 1; decline/lack route goes to section 61.
- Section 137: optional Prophecy branch to 92 with return marker to 137, plus route choices to sections 142 and 163.
- Section 138: terminal death ending.
- Section 139: section 90 source route requires Sorcery and WP >= 2; lose 2 WP, mark Sorcery shield active for section 149, then route to section 149.
- Section 140: plain route choice to sections 112 or 280.

Sections 141-150 confirmed:

- Section 141: narrative forced route to section 197.
- Section 142: locked-door choice; Gaoler's Keys -> 286, Sorcery -> 159, Alchemy -> 170, right archway -> 163.
- Section 143: Prophecy result from section 43; lose 1 WP and 1 END, then choose section 68 or 118.
- Section 144: narrative forced route to section 172.
- Section 145: long-range Staff route to 132 requires WP >= 2; ordinary routes go to 99 or 169.
- Section 146: Staff bolt route to 158 requires WP >= 1; dash route goes to 232.
- Section 147: plain route choice to sections 221 or 63.
- Section 148: plain route choice to random jump section 49 or Quoku sequence section 233; not combat itself.
- Section 149: special Kleasa combat; per round lose 1 WP and 2 END, or 1 END with Sorcery shield active; route to 165 if alive after four rounds or enemy defeated.
- Section 150: lose 4 WP, allowing negative WP, and 2 END; post-loss WP or Magic Talisman controls route to 348 vs 237.

Sections 151-160 confirmed:

- Section 151: Alchemy recipe gate; Sulphur, Saltpetre, Ezeran Crystals, and empty vial -> 297, otherwise return to 172.
- Section 152: plain route choice to sections 252, 277, or 302.
- Section 153: Sorcery route to 185 requires Sorcery and WP >= 1; decline/lack route goes to 198.
- Section 154: combat vs Cave Mantiz CS 15 END 18; evade after one round to 4 or win to 103.
- Section 155: terminal death ending.
- Section 156: plain route choice to sections 215 or 120.
- Section 157: Alchemy gate; Alchemy -> 183, no Alchemy -> 26.
- Section 158: section 146 source route requires WP >= 1; lose 1 WP, then route to 232.
- Section 159: Sorcery commitment route to 114 requires Sorcery and WP >= 2; Alchemy route to 170 requires Alchemy; archway route goes to 163.
- Section 160: consume one Laumspur, then route to section 301.

Sections 161-170 confirmed:

- Section 161: Jnana loot prompt, then Alchemy gate to section 193 or section 15.
- Section 162: section 167 source route requires WP >= 2; lose 2 WP, then route to section 255.
- Section 163: narrative forced route to section 333.
- Section 164: gain 10 Nobles, optional 2 Meals and Sword, then route to section 39.
- Section 165: lose 5 WP, allowing negative WP, and 5 END; if alive route by post-loss WP to section 177 or 192.
- Section 166: plain route choice to sections 241 or 11.
- Section 167: long-range Staff route to 162 requires WP >= 2; stand-ground route goes to 180.
- Section 168: consume up to 2 Meals, lose 3 END per missing Meal, also lose 1 END fatigue, then route to 140.
- Section 169: narrative forced route to section 203.
- Section 170: Ezeran Acid route to 73, Sorcery fallback to 159, or right exit to 163.

Sections 171-180 confirmed:

- Section 171: gain 5 Nobles, optional Sword, then route to section 137.
- Section 172: forced Magick-selection hub; known Powers only, and target costs may use the section 172 negative-WP footnote exception.
- Section 173: terminal death ending.
- Section 174: narrative forced route to section 148.
- Section 175: Sorcery/WP resistance choice; Sorcery routes require Sorcery and WP >= 2, WP duel route always available.
- Section 176: Gaoler's Keys route to 153, or continue to 60.
- Section 177: terminal death ending.
- Section 178: Laumspur route to 160 requires Laumspur; keep/lack route goes to 93.
- Section 179: lose 1 WP for Staff attack; second bolt route to 285 requires WP >= 2 after that, or rush to Shan via 240.
- Section 180: narrative forced route to section 255.

Sections 181-190 confirmed:

- Section 181: section 128 source route requires Elementalism and WP >= 1; lose 1 WP, then route to 325.
- Section 182: narrative forced route to section 249.
- Section 183: apothecary shop prompt with stock-limited alchemy goods and Tarama Seed special-item handling, then route to 26.
- Section 184: narrative forced route to section 325.
- Section 185: section 153 source route requires Sorcery and WP >= 1; lose 1 WP, then choose 80 or 253.
- Section 186: narrative forced route to section 86.
- Section 187: route by arrest origin/status, Inn of the Laughing Moon -> 230, otherwise -> 261.
- Section 188: narrative forced route to section 8.
- Section 189: combat vs Shadakine Officer CS 25 END 26, no evade/to death, Shan +3 CS, victory -> 215.
- Section 190: plain route choice to sections 38 or 21.

Sections 191-200 confirmed:

- Section 191: Sorcery/WP spend menu; spend 2/3/4 WP before routing to 323/314/288, and only branches affordable with current WP are legal.
- Section 192: narrative forced route to section 276.
- Section 193: Alchemy loot prompt for Pestle and Mortar, Ezeran Crystals, Yabari Ointment, and 4 Tarama Seeds, then route to 15.
- Section 194: Coil of Rope source route result; no Rope deletion here, then route to 269.
- Section 195: plain route choice to section 157 or 82.
- Section 196: plain route choice to section 50 or 40.
- Section 197: combat vs Soldier Mantiz CS 15 END 10, no evade/to death, victory -> 213.
- Section 198: plain route choice to section 80 or 225.
- Section 199: Elementalism route requires Elementalism and WP >= 1; Sorcery route requires Sorcery and WP >= 3; conserve route goes to 244.
- Section 200: Prophecy route requires Prophecy and WP >= 1; ordinary routes go to 223, 76, or 195.

Sections 201-210 confirmed:

- Section 201: restore 1 END capped at starting END and 1 WP uncapped, then route to 172.
- Section 202: section 1 source route requires Elementalism and WP >= 1; lose 1 WP, then route to 140.
- Section 203: combat vs 2 Shadakine Crossbowmen CS 15 END 18, no evade/to death, Tanith and Shan +4 CS, victory -> 156.
- Section 204: lose 2 WP for Staff use; footnote permits negative WP or END substitution for missing WP, then choose 329, 279, or 304.
- Section 205: combat vs Shadakine Warrior CS 11 END 15, +5 CS, evade any time to 163, victory -> 176.
- Section 206: consume Calacena Mushrooms after the legal section 128 source choice, then route to 325.
- Section 207: terminal death ending.
- Section 208: long-range Staff route to 81 requires WP >= 2; charge route goes to 99.
- Section 209: optional Redeemer loot, Vial of Pink Liquid and Medallion of the Redeemer, then choose 131 or 157.
- Section 210: lose 2 END, then route to 74.

Sections 211-220 confirmed:

- Section 211: Prophecy result from section 172 loses 1 WP with the section 172 negative-WP exception; Evocation route to 250 requires Evocation and no prior Evocation attempt.
- Section 212: plain route choice to section 309 or 137.
- Section 213: plain route choice to section 267, 272, or 284.
- Section 214: Prophecy route to 92 requires Prophecy and WP >= 1 with return marker 214; ordinary routes go to 176 or 45.
- Section 215: lose 1 WP with explicit insufficient-WP footnote options, offer herbwarden loot, then route to 2.
- Section 216: terminal death ending.
- Section 217: lose 5 Nobles, then route to 105; source route should require at least 5 Nobles.
- Section 218: narrative forced route to section 39.
- Section 219: Shan dies/is absent; no itemized backpack transfer here, then route to 294.
- Section 220: terminal death ending.

Sections 221-230 confirmed:

- Section 221: recover Staff and Backpack; optionally place Kazim Stone in Backpack if held and space allows, then route to 292.
- Section 222: long-range Staff route to 239 requires WP >= 2; other routes go to 246 or 260.
- Section 223: plain route choice to section 34 or 195.
- Section 224: combat vs Shadakine Warrior CS 13 END 20, no evade/to death, victory -> 127.
- Section 225: terminal death ending.
- Section 226: calculation route, 50 - (current WP + current CS); 15+ -> 295, 14 or less -> 320.
- Section 227: narrative forced route to section 29.
- Section 228: plain route choice to section 328 or 6.
- Section 229: lose 2 WP with explicit insufficient-WP footnote options; route 5 requires WP >= 2 after that, route 30 has its own footnote.
- Section 230: narrative forced route to section 291.

Sections 231-240 confirmed:

- Section 231: combat vs Quoku CS 12 END 30, no evade, -2 CS defensive penalty, victory -> 256.
- Section 232: narrative forced route to section 154.
- Section 233: narrative forced route to section 337.
- Section 234: narrative forced route to section 197.
- Section 235: section 286 source route requires Psychomancy and WP >= 1; lose 1 WP, then route to 214.
- Section 236: Psychomancy result from section 172 loses 1 WP with the section 172 negative-WP exception, then returns to 172.
- Section 237: terminal failure ending.
- Section 238: plain route choice to section 303 or 104.
- Section 239: section 222 source route requires WP >= 2; lose 2 WP, then choose 267, 272, or 284.
- Section 240: narrative forced route to section 204.

Sections 241-250 confirmed:

- Section 241: plain route choice to section 300, 66, or 20.
- Section 242: calculation route, current END + current WP; 20+ -> 341, 19 or less -> 316.
- Section 243: combat vs Gaoler CS 8 END 14, no evade/to death, +4 CS, optional Dagger after victory, then choose 125, 338, or 333.
- Section 244: plain route choice to section 167 or 13.
- Section 245: restore Wizard's Staff, Backpack, and Backpack Items, then route to 292.
- Section 246: combat vs Soldier Mantiz CS 14 END 10, no evade/to death, victory -> 290.
- Section 247: narrative forced route to section 62.
- Section 248: lose 1 WP with explicit insufficient-WP footnote options; route 254 requires WP >= 2 after that, routes 204 and 229 have their own footnotes.
- Section 249: plain route choice to section 282 or 257.
- Section 250: Evocation attempt choice; mark Evocation attempted, then accept bargain -> 326 or refuse -> 305.

Sections 251-258 confirmed:

- Section 251: Enchantment result route choice to section 50 or 40; source cost already paid.
- Section 252: add up to 5 Meals, respecting capacity, then route to 327.
- Section 253: plain route choice to section 80 or 324.
- Section 254: section 248 source route requires WP >= 2; lose 2 WP, then route to 279.
- Section 255: combat vs 2 Shadakine Warriors CS 15 END 25, no evade/to death, victory -> 75.
- Section 256: plain route choice to section 281 or 107.
- Section 257: lose 1 WP with explicit insufficient-WP footnote options, then route to 174.
- Section 258: narrative forced route to section 62.

Section 259 ruling received:
- Darkling Room damage reduces END.
- Mental Combat Skill is fixed from starting current WP + current END for the whole combat.

Sections 259-270 confirmed:

- Section 259: mental combat vs Darkling Room CS 28 END 30; player mental CS fixed from current WP + END at combat start; damage reduces END; victory -> 296.
- Section 260: combat vs 2 Soldier Mantiz CS 18 END 20, no evade/to death, victory -> 213.
- Section 261: narrative forced route to section 291.
- Section 262: terminal death ending.
- Section 263: narrative forced route to section 146.
- Section 264: delete Vial of Pink Liquid; hidden solved puzzle route -> 110; fallback routes -> 190 or 134.
- Section 265: lose 1 WP, then combat vs Shadakine Warrior CS 14 END 18, no evade/to death, victory -> 40.
- Section 266: plain route choice to section 330 or 231.
- Section 267: plain route choice to section 332, 340, or 347.
- Section 268: lose 1 END, then choose section 8 or 113.
- Section 269: delete Coil of Rope, then route to section 294.
- Section 270: restore +1 WP uncapped and +3 END capped at starting END, then choose section 201 or 144.

Sections 271-280 confirmed:

- Section 271: Elementalism result forced route to section 273; source section 172 requires Elementalism and cost is paid in section 273.
- Section 272: lose 2 END, then timed combat vs 2 Soldier Mantiz CS 20 END 15; win within 3 rounds -> 322, round 4 -> 315.
- Section 273: lose 1 WP with section 172 forced-power insufficiency options, then route to section 259.
- Section 274: narrative forced route to section 306.
- Section 275: narrative forced route to section 18.
- Section 276: Tanith is lost/dead/unavailable, then route to section 52.
- Section 277: narrative forced route to section 252.
- Section 278: Prophecy result; source section 54 requires Prophecy and WP >= 1; lose 1 WP, then route to section 184.
- Section 279: lose 1 WP with explicit insufficient-WP footnote options, then route to section 128.
- Section 280: Prophecy-gated route choice to section 53, sell boat -> 16, or do not sell -> 100.

Sections 281-290 confirmed:

- Section 281: one-round combat vs Large Quoku CS 15 END 30 with -1 CS; after the round WP 10+ -> 331, WP <10 -> 32.
- Section 282: narrative forced route to section 148.
- Section 283: lose 3 END, then route to section 227.
- Section 284: lit Torch -> 207; otherwise combat vs 4 Soldier Mantiz CS 20 END 25, no evade/to death, victory -> 310.
- Section 285: section 179 source route requires WP >= 2 after its initial cost; lose 2 WP, then route to section 128.
- Section 286: Psychomancy -> 235; without Psychomancy random even -> 214, odd -> 205.
- Section 287: lose 2 END, then route to section 263.
- Section 288: section 191 route requires 2 WP remaining after the 4-point spend; lose extra 2 WP, then route to section 320.
- Section 289: current WP <15 -> 150, current WP >=15 -> 175.
- Section 290: plain route choice to section 267, 272, or 284.

Sections 291-300 confirmed:

- Section 291: Staff, Backpack, and Backpack Items are confiscated/unavailable; non-Backpack items remain; route to section 178.
- Section 292: Amulet of the Shianti priest -> 346; no Amulet -> 199.
- Section 293: lose 1 END, then choose section 318 or 343.
- Section 294: Shan is lost/dead/unavailable; current END <10 -> 319, END >=10 -> 344.
- Section 295: lose 2 END, then route to section 187.
- Section 296: narrative forced route to section 41.
- Section 297: Alchemy conversion creates Ezeran Acid, removes recipe ingredients, preserves two empty Vials, then choose section 23 or 333.
- Section 298: section 340 source route requires Staff and WP >= 2; lose 2 WP and 2 END, then route to section 263.
- Section 299: terminal death ending.
- Section 300: Staff, Backpack, and Backpack Items are confiscated/unavailable; Backpack contents are noted for later recovery; route to section 289.

Sections 301-310 confirmed:

- Section 301: restore +10 WP uncapped, then route to section 247.
- Section 302: narrative forced route to section 252.
- Section 303: lose 2 END, then route to section 325.
- Section 304: lose 1 WP with explicit insufficient-WP footnote options, then route to section 128.
- Section 305: lose 2 WP with section 172 forced-power insufficiency options; Evocation cannot be chosen again; return to section 172.
- Section 306: terminal death ending.
- Section 307: narrative forced route to section 249.
- Section 308: combat vs Shadakine Warriors CS 20 END 19 as one enemy, +4 CS for whole combat, no evade, victory -> 127.
- Section 309: combat vs Shadakine Guard CS 12 END 16, +4 CS for first two rounds, evade any time -> 137, victory -> 171.
- Section 310: plain route choice to section 267 or 272.

Sections 311-320 confirmed:

- Section 191 consistency update: spend-3 route to section 314 requires enough WP to pay section 314's immediate extra 1 WP cost; require WP 4+ before the section 191 spend, or 1+ remaining after it.
- Section 311: Wizard's Staff, Backpack, and Backpack Items are confiscated/unavailable; Backpack contents are noted for later recovery; lose 1 END, then route to section 289.
- Section 312: terminal death ending.
- Section 313: Prophecy result; source section 105 requires Prophecy and WP >= 1; lose 1 WP, then route to section 209.
- Section 314: after legal section 191 spend-3 route, lose 1 WP and half current END rounded down; if WP >= 2, spend 2 WP to route to section 320 or spend 2 WP to route to section 226; otherwise route to section 150.
- Section 315: terminal death ending.
- Section 316: terminal death ending.
- Section 317: terminal death ending.
- Section 318: terminal death ending.
- Section 319: lose 1 END, then route to section 43.
- Section 320: lose 4 WP, allowing negative WP under forced-loss ruling, and lose 4 END in addition to earlier Kazim Stone losses, then route to section 187.

Sections 321-330 confirmed:

- Section 191 consistency update: spend-2 route to section 323 requires enough WP for section 323's immediate extra 1 WP cost and its safe mandatory 1 WP follow-up; require WP 4+ before the section 191 spend, or 2+ remaining after it.
- Section 204 consistency update: optional Staff route to section 329 requires WP >= 1 after section 204's initial cost because section 329 has another Staff cost and no insufficiency footnote.
- Section 321: combat vs Gaoler CS 8 END 10; evade any time -> 137; victory -> 37.
- Section 322: narrative forced route to section 267.
- Section 323: after legal section 191 spend-2 route, lose 1 WP and half current END rounded down; spend 2 WP -> 299 or spend 1 WP -> 226.
- Section 324: terminal death ending.
- Section 325: narrative forced route to section 136.
- Section 326: route choice to section 87 or 220.
- Section 327: route choice to section 78 or 283.
- Section 328: lose 2 END, then route to section 104.
- Section 329: after legal section 204 Staff route, lose 1 WP and 4 END, then route to section 42.
- Section 330: narrative forced route to section 256.

Sections 331-340 confirmed:

- Section 331: route choice to fight the Quoku -> 307 or evade combat -> 182; no combat occurs in this section.
- Section 332: Staff/WP threshold; Staff available and WP >= 2 -> 96, otherwise -> 9. Section 96 applies the costs.
- Section 333: narrative forced route to section 259.
- Section 334: route choice to section 222 or 234.
- Section 335: mark Shan lost/dead/unavailable, then route to section 294.
- Section 336: route choice to section 40 or 50.
- Section 337: combat vs Wounded Quoku CS 14 END 18, no evade stated, victory -> 44.
- Section 338: Prophecy route requires Prophecy and WP >= 1, goes to section 92 and returns to 338; ordinary choices -> 137 or 212.
- Section 339: after section 82 buy-drink gate, lose 1 Noble, then choose section 217 or 105.
- Section 340: Staff route requires Staff available and WP >= 2 -> 298; jump route -> 287. Target sections apply costs.

Sections 341-350 confirmed:

- Section 341: lose 1 END, then route to section 8.
- Section 342: unreachable by normal choices per Project Aon footnote; lose 3 END, then route to section 74.
- Section 343: lose 1 END, then choose section 17 or 242.
- Section 344: narrative forced route to section 43.
- Section 345: Prophecy result; source section 136 requires Prophecy and WP >= 1; lose 1 WP, then route to section 61.
- Section 346: narrative forced route to section 199.
- Section 347: narrative forced route to section 47.
- Section 348: narrative forced route to section 187.
- Section 349: Tanith carries the Staff and Backpack, but no gear restoration happens here; choose attack -> 173 or persuade -> 245.
- Section 350: successful book ending / next-book hook to Grey Star book 2.

Current working section: numeric section audit complete through section 350.

## First Follow-Up Targets

- Numeric section audit is complete through section 350.
- Combat candidates and random-number sections 49 and 286 are confirmed in `GSBOOK1_COMBAT_AND_RANDOM_AUDIT.md`.
- No-incoming notes: section 110 is the confirmed riddle solution target; section 342 is unreachable by normal choices per Project Aon footnote.
- Implementation pass started: simple deterministic section-entry effects are now in `data/book1-simple-automations.json`; next pass should add prompts/gates, random routing, and special combat flows.
