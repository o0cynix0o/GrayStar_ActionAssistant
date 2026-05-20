# GS Book 2 Rules And Items Audit

Book: The Forbidden City

## Implemented Item/State Support

- Meals from sections 2 and 12 are added as Backpack Items, respecting capacity.
- Section 149 stores unavailable Staff/Backpack gear; section 200 restores it.
- Section 297 permanently discards Backpack contents and marks the Backpack unavailable.
- Section 133 gift loot has separate buttons for Meals, Short Sword, Sheath, Backpack, Laumspur potions, and Rope.
- Black Rod, Mind Gem, Chaksu Pipes, Silver Knife, Gold Tooth, Karmo Potion, and Azawood Leaves are represented as loot or entry effects.
- Book 2-specific Laumspur potions are recorded as `Potion of Laumspur (+4 END)` so the Use button restores the amount stated in section 133.

## Manual / Watch Items

- Karmo Potion timing remains manual because section 45 explicitly gives the player discretion about when to apply the random END penalty.
- The Kazim duel and several END/WP threshold decisions remain route checks because the book page already presents the destinations and the assistant shows current values.
- Azawood bundles are represented as individual Azawood Leaf items; bundle-count wording should be handled manually if the player imports a bundled item from notes.

## Current Data Files

- `data/book2-simple-automations.json`
- `data/book2-section-flows.json`
