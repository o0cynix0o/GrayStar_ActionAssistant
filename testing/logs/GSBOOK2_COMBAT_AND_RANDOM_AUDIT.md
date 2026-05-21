# GS Book 2 Combat And Random Audit

Book: The Forbidden City

## Combat Presets

| Section | Label | Enemy | CS | END | Notes |
|---:|---|---|---:|---:|---|
| 4 | Swamp Giant | Swamp Giant | 16 | 30 | victoryRoute=65 |
| 10 | Swamp Giant | Swamp Giant | 16 | 30 | victoryRoute=65 |
| 11 | Shadakine Warriors | Shadakine Warriors | 18 | 24 | victoryRoute=82 |
| 20 | Magdi Hound: win within 4 rounds | Magdi Hound | 20 | 30 | modifier=-2; roundLimit=4; roundExceededRoute=149; winWithinRounds=4 |
| 39 | Wildman | Wildman | 14 | 20 | victoryRoute=259 |
| 39 | Wildman with Prophecy warning (+2 CS) | Wildman | 14 | 20 | modifier=2; victoryRoute=259 |
| 61 | Magdi: win within 5 rounds | Magdi | 20 | 30 | modifier=-2; roundLimit=5; roundExceededRoute=149; winWithinRounds=5 |
| 82 | Magdi Hound | Magdi Hound | 20 | 30 | modifier=-2; victoryRoute=247 |
| 83 | Dead City Wretch (+2 CS) | Dead City Wretch | 15 | 25 | modifier=2; victoryRoute=197 |
| 99 | Shadakine Warrior: ignore round 1 END loss | Shadakine Warrior | 17 | 20 | ignorePlayerLossRounds=1; victoryRoute=40 |
| 116 | Dead City Wretch (-2 CS) | Dead City Wretch | 15 | 25 | modifier=-2; victoryRoute=197 |
| 123 | Magdi Hounds | Magdi Hounds | 25 | 35 | modifier=-2; victoryRoute=177 |
| 134 | Mad Courtiers: survive 3 rounds | Mad Courtiers | 18 | 23 | roundLimit=3; survivalRoute=153 |
| 163 | Shadakine Warrior | Shadakine Warrior | 18 | 25 | victoryRoute=88 |
| 176 | 3 Dead City Wretches | 3 Dead City Wretches | 18 | 25 | victoryRoute=308 |
| 251 | Mad Guard | Mad Guard | 20 | 25 | victoryRoute=134 |
| 254 | Gatekeeper | Gatekeeper | 10 | 28 | victoryRoute=158 |
| 273 | Scree Wyrm: win within 3 rounds | Scree Wyrm | 18 | 22 | roundLimit=3; roundExceededRoute=182; winWithinRounds=3 |
| 301 | Wildman | Wildman | 14 | 20 | victoryRoute=259 |

## Random / Roll Helpers

| Section | Summary | Outcomes |
|---:|---|---|
| 5 | Swim the lake under fire | 0-7 -> 236; 8-12 -> 74 |
| 32 | Foraging result | 0-3 -> 106; 4-6 -> 217; 7-9 -> 173 |
| 45 | Karmo potion side-effect roll; Karmo controls can apply END loss equal to the raw roll when the player chooses | 0-9 -> 71 |
| 89 | Crossing the mud flats | 0-4 -> 110; 5-11 -> 100 |
| 146 | Enchantment against the Shadakine line | 0-5 -> 42; 6-12 -> 289 |
| 153 | Only roll here if current END is 9 or lower | 0-5 -> 27; 6-9 -> 33 |
| 160 | Extend the Shield of Sorcery to Urik | 0-6 -> 118; 7-9 -> 44 |
| 188 | Control the Ooslo after Staff attack | 0-5 -> 15; 6-9 -> 140 |
| 268 | Conserve Willpower behind the Shield | 0-6 -> 44; 7-9 -> 118 |

## Manual Or Special Notes

- Section 45 Karmo Potion: the app records the potion, doubles END/WP from the item Use button, applies the side-effect roll when the player chooses, and finishes the potion by halving END/WP after combat. The timing of the random side-effect penalty remains player-controlled because the section footnote allows either order.
- Section 49/141 Kazim duel: the book asks for a calculation using current END + WP against 40; the route links remain on the page and current stats are visible in the assistant.
- Section 153/164/219/286 conditional branches are stat-check route choices; navigation remains on the book page.
