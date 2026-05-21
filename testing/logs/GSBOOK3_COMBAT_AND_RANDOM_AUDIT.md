# GS Book 3 Combat And Random Audit

Book: Beyond the Nightmare Gate

## Combat Presets

| Section | Label | Enemy | CS | END | Notes |
|---:|---|---|---:|---:|---|
| 17 | Daemonak | Daemonak | 21 | 28 | victoryRoute=250 |
| 57 | Elessi Leader: unarmed/no Dagger | Elessi Leader | 12 | 25 | forceUnarmed=True; victoryRoute=107; evadeRoute=99 |
| 57 | Elessi Leader: Jewelled Dagger reduces penalty | Elessi Leader | 12 | 25 | modifier=2; forceUnarmed=True; victoryRoute=107; evadeRoute=99 |
| 64 | Chaos-bird | Chaos-bird | 20 | 24 | victoryRoute=133 |
| 87 | Giant Eagle: survive 3 rounds | Giant Eagle | 30 | 30 | roundLimit=3; survivalRoute=150; victoryRoute=150 |
| 97 | Tower Door: ignore Gray Star END loss | Tower Door | 30 | 45 | victoryRoute=124; evadeRoute=61; ignorePlayerLossRounds=999 |
| 108 | Chaos-bird | Chaos-bird | 20 | 25 | victoryRoute=133 |
| 123 | Jahksa: survive 3 rounds | Jahksa | 30 | 30 | roundLimit=3; survivalRoute=117; victoryRoute=117 |
| 137 | Wounded Eagle | Wounded Eagle | 30 | 25 | victoryRoute=186 |
| 178 | Wounded Wolf | Wounded Wolf | 20 | 20 | victoryRoute=106 |
| 188 | Chaos-birds | Chaos-birds | 26 | 30 | victoryRoute=205 |
| 188 | Chaos-birds with Tanith armed (+2 CS) | Chaos-birds | 26 | 30 | modifier=2; victoryRoute=205 |
| 194 | Creature of the Mists: survive 2 rounds | Creature of the Mists | 21 | 25 | roundLimit=2; survivalRoute=51; victoryRoute=51 |
| 243 | Final Jahksa: defeat leads to the Moonstone | Jahksa | 30 | 35 | victoryRoute=286; evadeRoute=218; defeatRoute=350 |
| 296 | Giant Wolf: win within 3 rounds | Giant Wolf | 20 | 26 | roundLimit=3; roundExceededRoute=287; winWithinRounds=3 |
| 322 | Elessi Leader: no Staff/no Dagger | Elessi Leader | 12 | 25 | forceUnarmed=True; victoryRoute=107; evadeRoute=99 |
| 322 | Elessi Leader: Jewelled Dagger reduces penalty | Elessi Leader | 12 | 25 | modifier=2; forceUnarmed=True; victoryRoute=107; evadeRoute=99 |

## Random / Roll Helpers

| Section | Summary | Modifiers | Outcomes |
|---:|---|---|---|
| 4 | Carry the statue down the palace steps | Current END from end | -999 to 19 -> 65; 20 to 999 -> 59 |
| 6 | Long-range Staff attack against the Elessin | Current CS from cs | -999 to 14 -> 93; 15 to 999 -> 248 |
| 19 | Land the Ethetron after crossing the Gate | Talisman of the Shianti +2 | 0 to 3 -> 13; 4 to 11 -> 77 |
| 22 | Carry the statue through the palace | Current END from end | -999 to 19 -> 65; 20 to 999 -> 59 |
| 44 | Carry the statue down the long steps | Current END from end | -999 to 19 -> 65; 20 to 999 -> 59 |
| 78 | Elementalism in the Chaos-bird attack | Current WP from wp | -999 to 8 -> 83; 9 to 999 -> 304 |
| 121 | Sneak behind the palace guard | - | 0 to 5 -> 139; 6 to 9 -> 145 |
| 172 | Haul Tanith up the Crystal Tower | Silver Charm of Jnana the Wise +1, Talisman of the Shianti +1 | 0 to 5 -> 63; 6 to 11 -> 91 |
| 174 | Resist the Realm of Paradox without Enchantment | Current WP from wp | -999 to 19 -> 104; 20 to 999 -> 86 |
| 217 | Climb the Crystal Tower | Silver Charm of Jnana the Wise +1, Talisman of the Shianti +1 | 0 to 5 -> 292; 6 to 11 -> 246 |
| 235 | Wolf Key ambush | - | 0 to 4 -> 178; 5 to 9 -> 296 |
| 246 | Bring Tanith up after the first climb | Silver Charm of Jnana the Wise +1, Talisman of the Shianti +1 | 0 to 4 -> 126; 5 to 11 -> 172 |
| 290 | Chaos-bird corpse collision | Current WP from wp | -999 to 8 -> 83; 9 to 999 -> 304 |
| 310 | Land the Ethetron after the white-light Gate | Talisman of the Shianti +2 | 0 to 3 -> 13; 4 to 11 -> 77 |

## Special Notes

- Section 243 is intentionally supported with a `defeatRoute` to section 350 because the book sends combat defeat to the Moonstone ending instead of a normal death.
- Sections 57 and 322 use `forceUnarmed` presets so the no-weapon and Jewelled Dagger penalties do not get confused with normal Staff combat.
- Rolls that add current END, WP, or CS use dynamic roll modifiers in the assistant.
