# GS Book 1 Pass 1 Rules Baseline

Book: Grey Star the Wizard

Status: Pass 1 complete. Book 1 app implementation has a dry-run playtest harness with a green run on 2026-05-20; see `testing/logs/GSBOOK1_PLAYTEST_REPORT.md`.

## Sources Read

- `books/gs/01gstw/title.htm`
- `books/gs/01gstw/gamerulz.htm`
- `books/gs/01gstw/powers.htm`
- `books/gs/01gstw/equipmnt.htm`
- `books/gs/01gstw/cmbtrulz.htm`
- `books/gs/01gstw/crsumary.htm`
- `books/gs/01gstw/crtable.htm`
- `books/gs/01gstw/random.htm`
- `books/gs/01gstw/sage.htm`
- `books/gs/01gstw/footnotz.htm`
- `books/gs/01gstw/errata.htm`
- `books/gs/01gstw/sect1.htm`

## Character Setup Baseline

Book 1 character creation requires:

- Combat Skill: random digit plus 10.
- Willpower: random digit plus 20.
- Endurance: random digit plus 20.
- The random digit can be 0 through 9; 0 counts as 0 for this setup.
- The player chooses five of the seven Lesser Magicks:
  - Sorcery
  - Enchantment
  - Elementalism
  - Alchemy
  - Prophecy
  - Psychomancy
  - Evocation
- Starting equipment:
  - Wizard's Staff as the starting weapon.
  - Backpack with four Meals.
  - Map of the Shadakine Empire as a Special Item.
  - No Nobles.
- If Alchemy is selected, the character starts with a Herb Pouch containing:
  - two Empty Vials
  - Vial of Saltpetre
  - Vial of Sulphur
- The player chooses one Shianti gift:
  - Jewelled Dagger, Special Item, combat bonus when used.
  - Magic Talisman, Special Item, one-time Willpower bonus.
  - Vial of Laumspur, Backpack Item, restores Endurance after combat.

## Inventory Rules Confirmed

- The Wizard's Staff counts as one weapon.
- Maximum weapons carried: two.
- Maximum Backpack Items: eight, including Meals.
- Each Meal takes one Backpack slot.
- Special Items do not take Backpack slots.
- Potions, vials, and ingredients can go in the Herb Pouch if the character has Alchemy; other Backpack Items must remain in the Backpack.
- Herb Pouch capacity: eight items.
- If instructed to eat and no Meal is available, the penalty is 3 Endurance.
- Items can be exchanged or discarded when not in combat.

## Willpower And Staff Rules Confirmed

- Willpower fuels Magical Powers and the Wizard's Staff.
- Willpower can rise above the starting value.
- Endurance cannot rise above the starting value unless a specific later rule says otherwise.
- If Willpower is zero or below, the character cannot cast spells or use the magical power of the Staff until Willpower is positive again.
- The Staff can still be used as a normal weapon when magical use is unavailable, but with the Staff-unavailable combat penalty.
- Footnotes allow a choice for some forced magic-use cases: subtract the listed Willpower even into negative values, or use the later 2 Endurance per missing 1 Willpower fallback. Project ruling: book rules trump house rules, so use the negative-Willpower path unless a section explicitly requires the Endurance fallback.
- Section-specific footnotes can override the normal optional-magic gate. Section 172 is the first clear case: its forced power menu can require choosing a Magical Power even when the final cost exceeds current Willpower, so the selected power cost may reduce Willpower below 0.

## Combat Rules Confirmed

- Combat ratio is Grey Star's current Combat Skill minus the enemy Combat Skill.
- If using the Wizard's Staff magically, the player must spend at least 1 Willpower.
- A random digit is cross-referenced against the Combat Results Table.
- Grey Star loses the table's player loss.
- Enemy loss from the table is multiplied by Willpower spent when using the Staff magically.
- Combat ends when either side reaches zero or below Endurance.
- Evade is only legal when the section text offers it.
- If evading after a combat round, enemy damage from that round is ignored and only Grey Star's damage applies.
- If entering combat without the Staff, apply a -6 Combat Skill penalty.
- If entering combat with no weapon, apply a -8 Combat Skill penalty.

## Errata And Footnote Rules To Carry Forward

- Equipment errata confirms the Herb Pouch capacity is eight.
- Jewelled Dagger project ruling: its +1 Combat Skill applies only when the Jewelled Dagger is selected as the active combat weapon.
- The Magic Talisman bonus is applied once and does not protect against Willpower later falling to zero or below.
- Some section errata changes item types and route links; section-specific rows must check local errata before implementation.
- Section 256 has an errata route correction away from an inappropriate instant-death destination.
- Section 332 includes a Willpower availability condition for a Staff-use option.

## Current App Comparison

Already supported:

- Random digit is 0 through 9.
- CLI new game can choose five Lesser Magicks for Book 1.
- Web/API new game can create a Book 1 character, choose the Shianti gift, and choose the required five Lesser Magicks.
- Base starting equipment exists in default inventory.
- Alchemy grants the starting Herb Pouch and starting alchemical items.
- Generic END, WP, CS, Nobles adjustment exists.
- Generic add/drop item controls exist.
- Generic meal/missed-meal handling exists, with Book 1 section-entry Meal automation where audited.
- Herb Pouch and Backpack consumables have use/eat controls for configured Laumspur/Rendalim effects.
- Generic combat resolution exists, including Staff Willpower spend, enemy-loss multiplier, evade handling, section combat presets, round limits, timed modifiers, fixed mental Combat Skill, per-round section effects, and Book 1 combat summary.
- Combat weapon handling distinguishes Staff magic, Staff as a normal weapon, other weapons, Jewelled Dagger, and unarmed combat. No weapon applies -8 CS; Staff unavailable with another weapon applies -6 CS.
- Gear confiscation/restoration is automated for the audited Book 1 gear-loss sections.
- Section 350 triggers a Book 1 completion screen, summary, BookHistory entry, and controlled transition into Book 2.

Needs build or UX work:

- A no-save resume from `current-position.json` restores a section but not a valid rolled/selected character.
- Forced and non-magic Willpower losses may reduce Willpower below 0 under book rules. Optional magic or Staff use still cannot be chosen without sufficient Willpower unless a section-specific footnote explicitly permits or forces the spend.
- Book-page route links remain the primary route-choice UI by design. The assistant Choices panel is reserved for mechanical choices such as loot, status toggles, rolls, WP costs, and combat presets.

## Section 1 Confirmed Audit Row

| Section | Trigger Timing | Rule Type | Preconditions | State Change | Prompt Needed | Legal Choices | Current App Support | Status |
|---:|---|---|---|---|---|---|---|---|
| 1 | after text | Magick-gated route choice | Elementalism known, and player chooses whether to use it | none confirmed | yes | Use Elementalism -> 202; lack/decline Elementalism -> 168 | book reader links work; no assistant prompt/automation | confirmed |

## Pass 2 Start Point

Pass 2 should begin with section 202 and section 168 as the first two route branches from section 1.
