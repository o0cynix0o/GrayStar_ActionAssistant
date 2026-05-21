# GS Book 4 Rules And Items Audit

Generated: 2026-05-21T09:04:35

Book: War of the Wizards

## Implemented Rule Support

- Book 4 start and completion are supported by existing campaign continuation plus section 360 completion automation.
- Potion of Invulnerability can be consumed by section automation or item use; it removes the potion, returns an Empty Vial, and sets an invulnerability flag.
- Potion of Laumspur (+6 END), Potion of Alether (+2 CS), and Tarama Seed use effects are recognized by the item-use system.
- Phinomel Pods can be gathered at sections 11, 16, and 40 and spent at section 355 for a Leafwater Combat Skill boost.
- Shadakine uniform state is recorded by the uniform route automations.
- The Wizard's Staff is removed and marked unavailable at the final shatter sections.

## Item Button Coverage

- Loot/action buttons: 40.
- Major item clusters: Phinomel Pods, Masbate supplies, Theurgy ingredients, Invulnerability Potion, Laumspur, Alether, Tarama Seeds, Calacena, Mustow, Temeris, Ezeran Acid, Leafwater Staff boost.

## Remaining Manual Judgment

- Tarama Seeds waive one eligible spell or long-range Staff cost. The app records a ready flag when used, but the player still chooses which exact cost it cancels.
- Section 295's random result is the WP cost; the app displays the adjusted result and route, but the player applies the resulting cost.
- Final sections 316 and 356 are story-completion expenditure rather than a numbered stat adjustment.
