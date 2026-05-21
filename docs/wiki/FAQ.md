# FAQ

## Is This A Replacement For The Books?

No. The assistant is a play aid. You still read and play from the book text.

## Where Do I Get The Book Files?

Download the Grey Star books directly from Project Aon for your own personal use. The assistant does not include or redistribute the book HTML files.

Project Aon license:

- https://www.projectaon.org/en/Main/License

Use the **standard** multi-page HTML ZIPs:

| Book | Standard ZIP |
| --- | --- |
| 1. Grey Star the Wizard | https://www.projectaon.org/en/xhtml/gs/01gstw/01gstw.zip |
| 2. The Forbidden City | https://www.projectaon.org/en/xhtml/gs/02tfc/02tfc.zip |
| 3. Beyond the Nightmare Gate | https://www.projectaon.org/en/xhtml/gs/03btng/03btng.zip |
| 4. War of the Wizards | https://www.projectaon.org/en/xhtml/gs/04wotw/04wotw.zip |

Extract them into:

```text
books\gs
```

You should end up with:

```text
books\gs\01gstw\title.htm
books\gs\02tfc\title.htm
books\gs\03btng\title.htm
books\gs\04wotw\title.htm
```

PowerShell example from the project folder:

```powershell
New-Item -ItemType Directory -Force .\books\gs

Expand-Archive "$env:USERPROFILE\Downloads\01gstw.zip" -DestinationPath .\books\gs -Force
Expand-Archive "$env:USERPROFILE\Downloads\02tfc.zip"  -DestinationPath .\books\gs -Force
Expand-Archive "$env:USERPROFILE\Downloads\03btng.zip" -DestinationPath .\books\gs -Force
Expand-Archive "$env:USERPROFILE\Downloads\04wotw.zip" -DestinationPath .\books\gs -Force
```

The longer walkthrough is here:

- [Installing Project Aon Books](Installing-Project-Aon-Books)

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

## What Is Done For The Books?

Books 1, 2, 3, and 4 have assistant rules, achievements, strategy guides, and green dry-run playtest reports.
