# Command Reference

The web app is the main interface. The older command-line assistant still exists, but the browser UI is the normal play surface.

## Top Book Controls

- **Book 1 / Book 2 / Book 3 / Book 4**: open a specific book.
- **Current**: return to the current saved section.
- **Title**: open the current book title page.

## Status Cards

The top row shows:

- current book
- current section
- Endurance
- Willpower
- Combat Skill

These cards are informational. Use the Vitals controls to change values.

## Section Card

- **Roll 0-9**: generates a random number like the book's random number table.
- Section text below the buttons shows which book and section are active.

Use this card for section-level play aids, especially random-number checks and current-section confirmation.

## Vitals Card

Use this for fast stat adjustments:

- Endurance `-1`
- Endurance `+1`
- Willpower `-1`
- Willpower `+1`
- direct set fields

Use this when the book gives a result that is not represented by a dedicated button.

## Inventory Controls

Use **Add Item** to add:

- Weapons
- Backpack Items
- Special Items
- Herb Pouch Items

Use **Drop Item** to remove carried items.

Use **Eat Meal** and **Missed Meal** for normal food bookkeeping.

## Tabs

- **Sheet**: character overview and new character controls.
- **Inventory**: full carried item management.
- **Magicks**: selected Magical Powers and Willpower spend buttons.
- **Sections**: section history and navigation support.
- **Combat**: active fight controls and combat log.
- **Saves**: save/load controls.
- **Notes**: player notes.
- **Achievements**: unlocked, locked, recent, and book-specific progress.

## Death Screen

When Grey Star dies or reaches a terminal failure, the app presents recovery options:

- **Rewind**: restore the state from before the current section visit.
- **Repeat**: try the failed section again from its entry snapshot.

Use Rewind when you want to undo the route choice. Use Repeat when you want to try the fight or roll again.

## Command-Line Assistant

The browser app is still the easiest way to play, but `greystar.py` now has a much stronger terminal surface for keyboard-first testing and play.

Useful CLI commands:

- `sheet`: show the Action Chart.
- `choices`: show current section links, roll helper, combat presets, and loot options.
- `loot`: open the current section loot picker.
- `loot <number>` or `loot all`: apply audited loot.
- `drop`: remove an item by numbered slot.
- `drop backpack 2`: drop a specific slot.
- `use <item>` or `use herb 1`: use a configured consumable.
- `combat`: show combat status.
- `combat start <name> <cs> <end>`: start tracked combat.
- `combat round [wp] [roll]`: resolve a round.
- `death`: show the active death/recovery screen.
- `repeat`: retry the failed section from its ready checkpoint.
- `rewind`: return to the previous section checkpoint.
