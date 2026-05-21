# GS Book 3 Playtest Report

Generated: 2026-05-21T14:17:30

Scope: dry-run source, automation, flow, Book 3 edge mechanics, completion, achievements, and repeat-book checks. The script uses in-memory saves and does not touch the live campaign pointer.

Passed: 23
Warnings: 0
Failures: 0

## Passed

- All 350 Book 3 section files exist.
- Every Book 3 source link points to an existing section.
- Reachability matches the known Book 3 source irregularities: 144 and 190.
- Book 3 automation data loads.
- Book 3 flow data loads.
- Book 1 and 2 flow data still load.
- All 14 detected combat sections have combat presets.
- All 14 detected roll sections have roll helpers.
- Simple automation sweep covered 107 Book 3 sections.
- Roll helper sweep covered 140 outcomes.
- Loot sweep covered 23 buttons.
- Status sweep covered 1 toggles.
- Willpower-cost sweep covered 4 buttons.
- Combat sweep started 17 presets.
- Dynamic END roll modifiers route section 4 correctly.
- Book 3 Backpack stash and recovery preserve Backpack Items.
- Book 3 weapon-only confiscation preserves Backpack Items and restores weapons.
- Jewelled Dagger section preset forces unarmed combat with the reduced -6 CS penalty.
- Final Jahksa combat defeat routes to section 350 and activates completion.
- Senara Potion use restores 5 WP.
- Success-route smoke completes Book 3.
- Achievement sync/backfill unlocked expected Book 3 route set.
- Repeat Book 3 resets to section 1 and preserves achievements.

## Warnings

- None

## Failures

- None
