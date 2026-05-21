# Campaign and Saves

The assistant keeps local save files for your character and campaign state.

## Save Location

By default, local saves live in:

```text
./saves
```

The `saves` folder is ignored by git so your personal play state does not get pushed to GitHub.

## Autosave

Autosave is always part of the normal workflow. The app saves after important state changes so section progress, inventory, combat state, and achievements are not lost.

## Book Completion

When a book is completed, the app records the completion and offers next-step choices.

Current supported flow includes:

- continue to the next book
- repeat the completed book with the same character
- preserve completed-book records and achievements

For a full example of one character moving through all four books, see the [Full Campaign Story Run](Full-Campaign-Story-Run).

## Repeat Book

Repeat Book starts that book again at section 1.

It resets current Endurance and Willpower back to the character's base values for the replay, while keeping the same campaign identity and achievement profile.

## Death Recovery

When Grey Star dies or reaches a terminal failure, the app stores a section-entry snapshot.

Recovery options:

- **Rewind**: go back before the failed section.
- **Repeat**: try the same section again from its entry state.

Inventory, Endurance, Willpower, and combat changes from the failed attempt are restored according to that snapshot.
