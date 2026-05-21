# GS Book 1 Playtest Report

Generated: 2026-05-21T11:25:06

Scope: dry-run route, automation, combat, gear restore, and completion checks. The script uses in-memory saves and does not touch the live campaign pointer.

Passed checks: 26
Warnings: 0
Failures: 0

## Passed

- All 350 Book 1 section HTML files exist.
- All Book 1 source links point to existing sections.
- Simple automation sweep covered 155 sections.
- Flow sweep: 20 roll outcomes, 39 loot buttons, 7 status toggles, 16 WP costs, 26 combat presets.
- Section 149 records per-round special effects with shield=False.
- Section 149 shield=False applies the correct extra END loss.
- Section 149 records per-round special effects with shield=True.
- Section 149 shield=True applies the correct extra END loss.
- Section 259 mental Combat Skill stays fixed after round damage.
- Section 281 one-round WP threshold routes to 331 from WP 20.
- Section 281 one-round WP threshold routes to 32 from WP 5.
- Wizard's Staff can be used as a normal weapon at 0 WP without the -6 penalty.
- No weapon applies the explicit -8 CS penalty.
- No Staff plus another weapon applies the Staff-unavailable -6 CS penalty.
- Jewelled Dagger gives +1 CS only when selected as the combat weapon.
- Section 291 stores unavailable gear.
- Section 221 restores gear from section 291.
- Section 300 stores unavailable gear.
- Section 221 restores gear from section 300.
- Section 311 stores unavailable gear.
- Section 245 restores gear from section 311.
- Section 350 activates the Book 1 completion payload.
- Book 1 continue flow advances to Book 2 and carries completion state.
- Book repeat restarts the completed book with END/WP reset and the same character.
- Book 1 achievement sync backfills route and story unlocks from history.
- Successful-route smoke reached section 350 across 141 route stops.
