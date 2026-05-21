# GS Book 3 Rules And Items Audit

Book: Beyond the Nightmare Gate

## Rules Baseline

- Local rules and footnotes confirm that Book 3 may re-pick Willpower while preserving earlier Combat Skill and Endurance by consistency ruling.
- Willpower can rise above the starting value; Endurance restoration remains capped by maximum Endurance.
- Forced magical or mental Willpower losses may drive WP below zero. Optional spell or Staff use still requires enough WP by the book rules.
- The Wizard's Staff is a weapon; if the Staff is unavailable, normal weapon combat carries the Staff-unavailable penalty and no-weapon combat uses the explicit no-weapon penalty.

## Item And State Support

| Topic | Book 3 Handling | App Support | Status |
|---|---|---|---|
| Gyronome | received with the Ethetron | simple automation at section 116 | implemented |
| Ethetron item choices | Short Sword, rope, healing potion, Backpack, Spear | loot buttons at section 116 | implemented |
| Crystal Tower keys | individual keys and bundled remaining keys | loot buttons and route notes | implemented |
| Senara buds/potions | restore WP when used | loot buttons and item-use effects | implemented |
| Ezeran Acid | optional acid creation for the tower door | WP-cost and loot buttons at section 319 | implemented |
| Weapon confiscation | Elessin take weapons but not Backpack | weapon-only store/restore actions | implemented |
| Ethetron Backpack stash | Backpack left behind and recovered later | backpack stash/restore actions | implemented |
| Final Moonstone fight | combat defeat routes to success | section 243 defeatRoute support | implemented |

## Manual / Watch Items

- The WP+END and CS+WP threshold choices remain manual route decisions with current stats visible in the assistant.
- Section 240 lets Tanith carry the remaining keys; the app records a flag but cannot know whether Tanith is currently separated unless the player follows the book state.
- Sections 144 and 190 are documented as unreachable source oversights.
