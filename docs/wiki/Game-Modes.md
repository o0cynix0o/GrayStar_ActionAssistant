# Game Modes

Grey Star has three play modes. They all use the same character, save files, achievements, and book position, so you can switch styles without starting over.

Open the Assistant menu with the small white dot in the upper-right of the assistant panel, then choose **Auto**, **Manual**, or **CLI**. The current mode is always shown in the top bar.

## Auto Mode

Auto Mode is the recommended default.

- section effects can be applied with the **Apply Effects** button
- section-aware rolls and loot helpers are available
- combat presets can start tracked fights
- meals, potions, inventory, saves, death recovery, and achievements all stay active

## Manual Mode

Manual Mode keeps the sheet and bookkeeping, but turns off the section automation helpers.

Use this when you want the book to feel closer to the paper-table experience. You can still adjust END and WP, add or drop inventory, use potions, save, load, and track achievements. The app will not apply audited section math, roll routing, section loot, section Willpower costs, combat presets, or auto-resolve combat for you.

## CLI Mode

CLI Mode replaces the normal assistant body with the terminal assistant. It runs through the same local save data as the web GUI, so you can play a section in the terminal and then switch back to Auto or Manual mode.

When you enter CLI Mode, the app saves first. When you leave CLI Mode, the web assistant reloads the latest save from disk.

## What Counts As A Rule

The app treats the book text as the authority. If a section says to lose Willpower, spend Endurance, lose equipment, store equipment, roll a random number, or apply a combat exception, that is the standard the assistant tries to model.

## Manual Choices

Some choices stay manual because the book gives the player discretion.

Examples:

- choosing whether to use a power
- picking a route from visible book links
- deciding timing where the section explicitly lets the player choose
- applying unusual one-off logic that is clearer to do by hand
