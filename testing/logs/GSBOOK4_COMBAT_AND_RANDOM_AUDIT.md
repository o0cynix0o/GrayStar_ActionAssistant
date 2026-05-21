# GS Book 4 Combat And Random Audit

Generated: 2026-05-21T09:04:35

Book: War of the Wizards

## Combat Presets

| Section | Label | Enemy | CS | END | Notes |
|---|---|---|---|---|---|
| 28 | Toad Demon: win within 3 rounds | Toad Demon | 17 | 16 | evadeRoute=41; roundLimit=3; roundExceededRoute=87; winWithinRounds=3 |
| 33 | Shadakine | Shadakine | 19 | 16 | victoryRoute=17 |
| 51 | Ape Demon: win speed matters | Ape Demon | 20 | 15 | modifier=-1; winWithinRounds=3 |
| 72 | Three Demons of the Plain | Three Demons of the Plain | 20 | 30 | victoryRoute=251 |
| 78 | Man Demon | Man Demon | 20 | 21 | victoryRoute=144 |
| 82 | Reptile Demon of the Plains | Reptile Demon of the Plains | 21 | 22 | victoryRoute=163 |
| 87 | Four Demons of the Plains | Four Demons of the Plains | 21 | 34 | modifier=-2; victoryRoute=251 |
| 111 | Winged Demon fly-by | Winged Demon | 20 | 20 | victoryRoute=306; roundLimit=1; roundExceededRoute=306; ignore END loss when enemy loss is higher |
| 123 | Three Ape Demons | Three Ape Demons | 24 | 25 | victoryRoute=168; evadeRoute=155 |
| 126 | Reptile Demon | Reptile Demon | 21 | 22 | victoryRoute=13 |
| 128 | Rat Demon on the saddle | Rat Demon | 19 | 20 | modifier=-2; victoryRoute=136 |
| 129 | Wytch-king Shasarak: weakened duel | Wytch-king Shasarak | 10 | 20 | victoryRoute=180 |
| 131 | Wytch-king Shasarak | Wytch-king Shasarak | 30 | 30 | victoryRoute=180 |
| 152 | Flying Snake fly-by | Flying Snake | 20 | 23 | victoryRoute=306; roundLimit=1; roundExceededRoute=306; ignore END loss when enemy loss is higher |
| 161 | Winged Demon: one round | Winged Demon | 20 | 31 | victoryRoute=178; roundLimit=1; roundExceededRoute=184 |
| 161 | Winged Demon: invulnerable | Winged Demon | 20 | 31 | victoryRoute=178; roundLimit=1; roundExceededRoute=184; ignorePlayerLossRounds=999 |
| 166 | Demon | Demon | 16 | 19 | victoryRoute=183 |
| 184 | Wounded Winged Demon: one round | Wounded Winged Demon | 15 | 12 | victoryRoute=178; roundLimit=1; roundExceededRoute=214 |
| 184 | Wounded Winged Demon: invulnerable | Wounded Winged Demon | 15 | 12 | victoryRoute=178; roundLimit=1; roundExceededRoute=214; ignorePlayerLossRounds=999 |
| 202 | Flying Snake fly-by | Flying Snake | 19 | 18 | victoryRoute=226; roundLimit=1; roundExceededRoute=226; ignore END loss when enemy loss is higher |
| 216 | Shadakine Officer | Shadakine Officer | 20 | 24 | victoryRoute=301; evadeRoute=290 |
| 221 | Ape Demon | Ape Demon | 18 | 17 | victoryRoute=150 |
| 226 | Insect Demon fly-by | Insect Demon | 18 | 17 | victoryRoute=265; roundLimit=1; roundExceededRoute=265; ignore END loss when enemy loss is higher |
| 233 | Demon Spiderfly | Demon Spiderfly | 25 | 24 | victoryRoute=197 |
| 233 | Demon Spiderfly: invulnerable | Demon Spiderfly | 25 | 24 | victoryRoute=197; ignorePlayerLossRounds=999 |
| 235 | Flying Snake: mounted penalty | Flying Snake | 21 | 24 | modifier=-2; victoryRoute=313; roundLimit=1; roundExceededRoute=313; ignore END loss when enemy loss is higher |
| 236 | Three Demons | Three Demons | 18 | 24 | victoryRoute=245 |
| 244 | Flying Snake fly-by | Flying Snake | 20 | 20 | victoryRoute=287; roundLimit=1; roundExceededRoute=287; ignore END loss when enemy loss is higher |
| 256 | Shadakine Warriors | Shadakine Warriors | 22 | 40 | modifier=3; victoryRoute=353 |
| 264 | Four Demons of the Plains | Four Demons of the Plains | 21 | 34 | victoryRoute=281 |
| 265 | Winged Ape: win in 1-2 rounds | Winged Ape | 22 | 16 | roundLimit=3; roundExceededRoute=206; winWithinRounds=2 |
| 269 | Shadakine Horseman charge | Shadakine Horseman | 19 | 20 | victoryRoute=17; roundLimit=1; roundExceededRoute=33 |
| 270 | Demon Master: win within 3 rounds | Demon Master | 30 | 40 | roundLimit=4; roundExceededRoute=276; winWithinRounds=3 |
| 288 | Two Demons of the Plains | Two Demons of the Plains | 18 | 20 | victoryRoute=163 |
| 296 | Ipage Demon | Ipage Demon | 20 | 20 | victoryRoute=39 |
| 302 | Three Reptile Demons: win speed matters | Three Reptile Demons | 24 | 25 | winWithinRounds=3 |
| 317 | Winged Demon fly-by | Winged Demon | 20 | 19 | victoryRoute=287; roundLimit=1; roundExceededRoute=287; ignore END loss when enemy loss is higher |
| 342 | Skeleton Warrior | Skeleton Warrior | 20 | 25 | victoryRoute=12 |
| 345 | Wytch-king Shasarak: final duel | Wytch-king Shasarak | 30 | 25 | victoryRoute=180 |

## Random / Roll Helpers

| Section | Summary | Modifiers | Outcomes |
|---|---|---|---|
| 3 | Turn the well mechanism | - | [0, 1, 2, 3, 4] -> 79; [5, 6, 7, 8, 9] -> 63 |
| 4 | Gather Phinomel Pods | Current WP from wp, Current END from end | -999 to 29 -> 40; 30 to 49 -> 16; 50 to 999 -> 11 |
| 62 | Reach the Forest of Fernmost | Current END from end | -999 to 11 -> 96; 12 to 999 -> 71 |
| 148 | Teleport without seeing the destination | Silver Charm of Jnana +1, Magic Talisman +1, Sorcery +1, Prophecy +1, Psychomancy +1, Visionary +1, Telergy +1 | -999 to 5 -> 130; 6 to 999 -> 55 |
| 149 | Long-range shot at the winged reptile | Silver Charm of Jnana +1, Magic Talisman +1 | -999 to 5 -> 171; 6 to 999 -> 182 |
| 238 | Swim the River Dosar in armour | Current END from end | -999 to 12 -> 80; 13 to 999 -> 86 |
| 255 | Sorcery blast against the stone doors | Magic Talisman +2 | -999 to 3 -> 208; 4 to 999 -> 283 |
| 259 | Dodge the charging chariot | Current END from end | -999 to 11 -> 263; 12 to 999 -> 199 |
| 295 | Thaumaturgy door assault: total is WP spent; reroll if the result is 0 | Subtract 1 -1 | -999 to 0 -> None; 1 to 999 -> 156 |
| 318 | Long-range shot at the Shadakine horseman | Current WP from wp, Current END from end | -999 to 24 -> 173; 25 to 999 -> 220 |

## Special Notes

- Book 4 adds conditional fly-by support: when the section says to ignore Grey Star END loss if the enemy loses more ENDURANCE, the combat log records the ignored loss.
- Invulnerability variants are present for the major combats that explicitly ignore Grey Star END loss after potion/Thaumaturgy protection.
- Round-limited combats use win-within and timeout routing so the correct follow-up section is chosen.
