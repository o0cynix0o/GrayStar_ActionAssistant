# GS Book 1 Combat And Random Audit

Book: Grey Star the Wizard

Status: combat candidates are confirmed from source text. Book 1 combat/random presets are implemented in `data/book1-section-flows.json` and covered by the dry-run playtest harness as of 2026-05-20.

Current QA result:

- Section flow sweep covered 20 roll outcomes and 26 combat presets.
- Section 149 per-round Kleasa drain is tested with and without Sorcery shield.
- Section 259 fixed mental Combat Skill is tested after round damage.
- Section 281 one-round Willpower threshold routing is tested for both branches.
- Successful-route smoke reached section 350 across 141 route stops.
- See `testing/logs/GSBOOK1_PLAYTEST_REPORT.md` for the latest generated report.

Pass 1 combat baseline:

- Combat ratio is Grey Star Combat Skill minus enemy Combat Skill.
- Magical Staff use requires at least 1 Willpower and multiplies enemy Endurance loss by Willpower spent.
- Staff-unavailable combat applies -6 Combat Skill.
- No-weapon combat applies -8 Combat Skill.
- Evade is only legal when offered by section text; enemy damage from an evade round is ignored.
- Current app supports generic Staff combat, evade, Book 1 section combat presets, timed modifiers, round-limit routes, fixed mental Combat Skill, per-round special section effects, active weapon selection, Jewelled Dagger +1 when selected, Staff-as-normal-weapon at 0 WP, no-weapon -8 CS, and Staff-unavailable -6 CS with another weapon.

Weapon rulings now covered by dry-run checks:

- Wizard's Staff can be used as a normal weapon at 0 WP without the -6 penalty.
- No weapon applies the explicit -8 CS penalty.
- No Staff plus another weapon applies the Staff-unavailable -6 CS penalty.
- Jewelled Dagger gives +1 CS only when selected as the combat weapon.

Note: the table below preserves the original audit notes. Rows that say "needs" refer to the build state when the audit was written; current implementation status is tracked by `data/book1-section-flows.json` and the playtest report.

## Combat Candidates

| Section | Parsed Combat | Out Links | Current App Support | Status |
|---:|---|---|---|---|
| 99 | Shadakine Crossbowmen fight as one enemy, to the death. Add +2 Combat Skill for surprise and +2 more for Shan, for +4 total. Enemy CS 25 END 32 | 88, 94 | generic combat available; needs post-combat WP-gated route prompt for section 88 | confirmed |
| 101 | Nine Najin attack one at a time; survive five combat rounds to continue. If Grey Star has another weapon-capable item besides the Wizard's Staff, Shan uses it for +2 Combat Skill; project ruling returns the borrowed weapon to inventory after combat. Najin 1 CS 10 END 10<br>Najin 2 CS 9 END 10<br>Najin 3 CS 10 END 10<br>Najin 4 CS 7 END 9<br>Najin 5 CS 8 END 10<br>Najin 6 CS 10 END 12<br>Najin 7 CS 9 END 9<br>Najin 8 CS 11 END 9<br>Najin 9 CS 10 END 9 | 130 | generic combat available; needs section automation for five-round survival and temporary weapon loan/return | confirmed |
| 117 | 2 Shadakine Warriors CS 15 END 25. No evade; fight to the death. Section also applies -1 WP before combat, allowing negative WP under forced-cost rule. | 164 | generic combat available; needs section WP action | confirmed |
| 120 | Shadakine Rearguard CS 25 END 30. Shan adds +3 Combat Skill. Survival combat ends after 3 rounds alive; section applies -1 WP by footnote before combat. | 189 | generic combat available; needs round-limit automation | confirmed |
| 133 | Cut-throat CS 10 END 12. Store current Nobles as stolen, set Nobles to 0, then fight; may evade after 2 rounds if still alive, or fight to death and win. | 27, 71 | generic combat available; needs stolen-money and timed-evade automation | confirmed |
| 149 | Kleasa CS 25 END 30. No evade; special limited combat. Each round drains 1 WP, allowing negative WP, and 2 END; if Sorcery shield from section 139 is active, each round drains 1 END instead. Route to 165 if alive after 4 rounds or if the Kleasa is defeated earlier. | 165 | generic combat available; needs per-round drain, shield modifier, and round-limit automation | confirmed |
| 154 | Cave Mantiz CS 15 END 18. May evade after one combat round to 4; victory routes to 103. | 4, 103 | generic combat available; timed evade remains manual | confirmed |
| 189 | Shadakine Officer CS 25 END 26. No evade; fight to the death. Shan adds +3 Combat Skill for this combat. | 215 | generic combat available; needs section +3 CS modifier automation | confirmed |
| 197 | Soldier Mantiz CS 15 END 10. No evade; fight to the death. | 213 | generic combat available; evade must be disabled | confirmed |
| 203 | 2 Shadakine Crossbowmen CS 15 END 18. No evade; fight to the death. Tanith and Shan add +4 Combat Skill for this fight. | 156 | generic combat available; needs section +4 CS modifier automation | confirmed |
| 205 | Shadakine Warrior CS 11 END 15. Add +5 Combat Skill for surprise and Shan's help. May evade at any time to 163; victory routes to 176. | 163, 176 | generic combat available; needs section +5 CS modifier automation | confirmed |
| 224 | Shadakine Warrior CS 13 END 20. No evade; fight to the death. | 127 | generic combat available; evade must be disabled | confirmed |
| 231 | Quoku CS 12 END 30. No evade; fight until victory or death. Subtract 2 Combat Skill for defensive tactics during this combat. | 256 | generic combat available; needs section -2 CS modifier automation | confirmed |
| 243 | Gaoler CS 8 END 14. No evade; fight to the death. Shan and surprise add +4 Combat Skill. After victory, optional Dagger as Weapon, then route choice. | 125, 338, 333 | generic combat available; needs section +4 CS modifier and post-victory loot automation | confirmed |
| 246 | Soldier Mantiz CS 14 END 10. No evade; fight to the death. | 290 | generic combat available; evade must be disabled | confirmed |
| 255 | 2 Shadakine Warriors CS 15 END 25. No evade; fight to the death. | 75 | generic combat available; evade must be disabled | confirmed |
| 259 | Darkling Room CS 28 END 30. Grey Star's mental Combat Skill is fixed at current Willpower + current Endurance at combat start. Damage reduces Grey Star's Endurance. | 296 | generic combat available; needs fixed derived-CS mental combat automation | confirmed |
| 260 | 2 Soldier Mantiz CS 18 END 20. No evade; fight both together to the death. | 213 | generic combat available; evade must be disabled | confirmed |
| 265 | Shadakine Warrior CS 14 END 18. Section applies -1 WP before combat; no evade; fight to the death. | 40 | generic combat available; needs section WP action | confirmed |
| 272 | 2 Soldier Mantiz CS 20 END 15. Section applies -2 END before combat. No evade; timed combat: win in three rounds or less ->322, if combat enters a fourth round ->315. | 322, 315 | generic combat available; needs section END action and three-round limit automation | confirmed |
| 281 | Large Quoku CS 15 END 30. Deduct 1 Combat Skill for this combat. Fight one round only, then route by current Willpower: WP 10+ ->331, WP <10 ->32. | 331, 32 | generic combat available; needs temporary -1 CS modifier, one-round limit, and post-round WP threshold | confirmed |
| 284 | 4 Soldier Mantiz CS 20 END 25 if not carrying a lit Torch. No evade; fight to the death; victory ->310. Lit Torch route goes to 207 before combat. | 207, 310 | generic combat available; needs lit-Torch gate | confirmed |
| 308 | Shadakine Warriors CS 20 END 19. Fight as one enemy. Add +4 Combat Skill for the whole combat due to surprise. No evade; victory ->127. | 127 | generic combat available; needs temporary +4 CS modifier | confirmed |
| 309 | Shadakine Guard CS 12 END 16. Add +4 Combat Skill for the first two rounds only. May evade at any time ->137; victory ->171. | 137, 171 | generic combat available; needs timed +4 CS modifier | confirmed |
| 321 | Gaoler CS 8 END 10. May evade at any time to 137; victory routes to 37. | 137, 37 | generic combat available; needs any-time evade route surfaced | confirmed |
| 337 | Wounded Quoku CS 14 END 18. No evade stated; victory routes to 44. | 44 | generic combat available; evade must be disabled | confirmed |

## Random Number Candidates

| Section | Out Links | Current App Support | Status |
|---:|---|---|---|
| 49 | Roll 0-9; add +1 if carrying the Silver Charm of Jnana the Wise; add +2 if current WP > 10. Modified total 0-6 ->274; modified total 7-12 ->210. | automated roll helper with modifiers and route result | confirmed |
| 286 | Psychomancy ->235; without Psychomancy: random 0/2/4/6/8 ->214, random 1/3/5/7/9 ->205 | automated even/odd roll helper; Psychomancy route remains a book-page choice | confirmed |

## Notes For Human Pass

- Confirm every combat enemy name directly from source before building tests.
- Confirm whether any combat has forced Willpower spend, staff restrictions, evade handling, or post-combat state changes.
- Confirm random sections 49 and 286 result mappings before any automation.
