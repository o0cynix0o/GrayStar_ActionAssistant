# Combat Guide

The Combat tab is built to handle normal Grey Star combat plus book-specific exceptions found during the section audit.

## Basic Combat Flow

1. Enter or select the enemy from the current section.
2. Confirm Combat Skill and Endurance values.
3. Roll or enter the random number for each combat round.
4. Apply the round result.
5. Continue until the enemy is defeated, Grey Star dies, or the section's special rule stops combat.

## Random Number

Grey Star uses a random number from `0` to `9`, matching the random number table style.

Use **Roll 0-9** in the Section card when the book calls for a random number outside combat.

## Weapons

The app follows the Grey Star weapon rulings agreed during Book 1 work:

- The Wizard's Staff can be used as a normal weapon even at 0 Willpower.
- If Weapons is empty, combat uses the explicit no-weapon penalty of `-8 CS`.
- If the Staff is unavailable but another weapon exists, use the Staff-unavailable `-6 CS` behavior only where Grey Star rules call for it.
- The Jewelled Dagger bonus applies only when the Jewelled Dagger is selected as the combat weapon.

## Special Combat Effects

Some sections add effects outside the standard Combat Results Table.

Examples already modeled include:

- per-round Willpower loss
- per-round Endurance loss
- shielded and unshielded combat variants
- fixed mental Combat Skill for psychic or mental combat
- one-round or limited-round combat
- first-round damage exceptions

When the audit found a section-specific rule, the app stores it with the section's combat preset so the Combat tab can apply it.

## Death And Recovery

If combat kills Grey Star, the app offers recovery choices:

- **Rewind**: go back to the previous section state.
- **Repeat**: restore the entry state for the failed section and try again.

Repeat is useful when the route is right but the fight went badly.

