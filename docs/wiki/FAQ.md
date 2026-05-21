# FAQ

## Is This A Replacement For The Books?

No. The assistant is a play aid. You still read and play from the book text.

## Why Do I Need `localhost`?

The assistant talks to a local Python server. If you open `assistant.html` directly as a file, the book pane may open but the assistant can be disconnected.

Use:

```text
http://localhost:8797/assistant.html
```

## When Does The App Save?

The app autosaves during normal play after meaningful state changes. This includes inventory changes, stat changes, section movement, combat state, notes, and achievement updates.

## Why Is There No Autosave Off Switch?

Because this app is a bookkeeping assistant. Turning autosave off would make it easier to lose the state the assistant exists to protect.

## How Do I Use A Potion?

Open the Inventory tab and use the item action for the potion or herb. Supported potions apply their known effect automatically. If the book gives you a timing choice, make the timing choice manually.

## Why Did A Choice Not Appear In The Choices Card?

Normal route choices are often already presented as links on the book page. The assistant's choice and flow controls are mainly for places where the app needs a structured button, such as loot, rolls, Willpower costs, or special section effects.

## What Happens When I Die?

The app shows death recovery options:

- **Rewind**: go back before the failed section.
- **Repeat**: restore the section-entry state and try again.

## Can Willpower Go Negative?

The app follows the book rules. If a book-legal effect can push Willpower below zero, the assistant allows it rather than applying a house-rule floor.

## Are Saves Pushed To GitHub?

No. The `saves` folder is ignored by git. Your character state stays local.

## What Is Done For Book 3 And Book 4?

Books 1, 2, and 3 have assistant rules, achievements, strategy guides, and green dry-run playtest reports.

Book 4 is available in the local reader, but still needs the full book workflow before it has the same level of assistant help.
