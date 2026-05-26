# FAQ

This page is for the things that are easy to miss while playing: what the buttons do, when the assistant is helping, and where the book still expects you to make the call.

## Is This A Replacement For The Books?

No. The assistant is a local play aid. You still read the Project Aon book text, click the book links, and make the choices yourself.

Think of the assistant as the Action Chart, dice table, combat tracker, save clerk, and achievement notebook sitting beside the book.

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

The longer walkthrough is here:

- [Installing Project Aon Books](Installing-Project-Aon-Books)

## Why Do I Need `localhost`?

The assistant talks to a local Python server. If you open `assistant.html` directly as a file, the book pane may open but the assistant can be disconnected.

Use:

```text
http://localhost:8797/assistant.html
```

If the assistant says disconnected, or only the book side loads, this is the first thing to check.

## How Do I Start The App?

From the project folder, run:

```powershell
.\Launch-GreyStar.ps1
```

Or:

```powershell
python .\launch_greystar.py
```

Then open:

```text
http://localhost:8797/assistant.html
```

## When Does The App Save?

The app autosaves during normal play after meaningful state changes: section movement, inventory changes, stat changes, combat state, notes, achievements, and UI preferences.

There is no normal reason to turn that off. The assistant exists to protect the bookkeeping.

## What Is `Apply Effects`?

Use **Apply Effects** when the current section has an audited effect that changes your character or game state.

Examples:

- gain or lose Endurance or Willpower
- add or remove items
- mark gear as lost, stored, or returned
- mark special section flags
- finish a book

The assistant does not automatically apply every section effect the moment you land on a page because some effects depend on your choice, timing, or inventory. Read the section, then press the button when that effect is the one you are taking.

## What Is The Bottom Notification Bar?

The bottom bar is a receipt drawer for the last important thing the assistant did.

Collapsed, it gives you the quick version:

```text
Automation - Applied -3 END
```

Click it and it opens the longer receipt:

```text
Where: Book 2, section 129
Why: This section has an audited Endurance loss.
Endurance: 25/28 -> 22/28
How: You pressed Apply Effects. The assistant used the section audit, updated the sheet, and saved the game.
```

The receipt drawer is used for section automation, Manual Mode advice, item use, Karmo controls, loot choices, combat rounds, death recovery, book completion, achievements, rolls, and normal assistant notices.

It is there so the app does not feel like a mystery box. You can see what changed, why the assistant changed it, and how it was applied.

## What Is `Section Roll`?

Grey Star uses random numbers from **0 to 9**, like the Random Number Table in the books.

The roll button gives you that number. If the current section audit has a special roll rule, the assistant applies the section's modifier or result table and shows the result.

If the section has no special roll rule, it is just a clean 0-9 roll.

## What Is A Route Check?

Some sections ask you to do quick book math before choosing where to turn. For example:

```text
Add together your COMBAT SKILL and current WILLPOWER points.
```

When the audit knows that rule, the **Choices** card shows the calculation, the current result, and the route that matches your sheet.

If the section has a stat loss first, the route check may wait until you press **Apply Effects** or record that cost by hand. That way the route is based on the same numbers the book expects you to use.

## Why Did The Choices Card Not Show My Book Choices?

Most normal route choices already appear as links in the book pane. Use those links normally.

The **Choices** card is mainly for assistant-side choices: loot, audited section options, route checks, special rolls, costs, combat starts, and effects that need a structured button.

If the book page already says where to turn and the link works, the assistant does not need to duplicate it.

## What Do The Triangle And Dot On A Card Do?

The white triangle collapses or expands a card.

- Down triangle: the card is open.
- Right triangle: the card is collapsed.

Collapsed cards stay visible as a one-line title, so they are easy to reopen.

The white dot opens the card menu. That menu handles layout work such as moving, resizing, or closing the card.

## What Is The Difference Between Collapse And Close?

**Collapse** keeps the card on the page, but shrinks it down.

**Close Card** removes the card from the current layout. To bring it back, open **Settings**, find **Closed Cards**, and click **Re-add**.

Use collapse for "I want this out of the way." Use close for "I do not want this card in this layout right now."

## Why Did New Character Disappear?

After you create and save a character, the New Character card hides from the main sheet layout. That gives more room to the cards you use while playing.

You can still start over from the app controls or by loading/importing a different save.

## What Is Manual Mode For?

Manual Mode keeps the sheet, inventory, notes, saves, and achievements, but changes audited helpers into advice-only buttons.

Use it when you want to do the book math yourself, or when you are testing something and do not want the assistant to apply section helpers.

In Manual Mode, buttons like **Apply Effects**, **Section Roll**, section loot **Apply**, section combat **Start**, and combat **Auto Resolve** do not change your sheet. Click them to open the bottom receipt drawer instead.

The **Why** line reads like guide advice. The **How to do it** lines are direct control instructions, such as:

```text
Vitals card > END: click -1 once, or type the new value in Set and click Set.
Choices card > Status Flags: click Set to turn the flag on, or Clear to turn it off.
Assistant menu > Mode: click Auto to turn automation on, Manual for advice-only play, or CLI for the terminal view.
```

Auto Mode is the normal way to play with the assistant.

## How Do I Use A Potion, Herb, Or Meal?

Open the **Inventory** tab. Supported consumables show a **Use** button beside the item.

Meals show an **Eat** button. The quick Add Item card also has **Eat Meal** and **Missed Meal** buttons.

Common supported consumables include:

- Karmo Potion
- Senara Potion
- Senara Bud
- Healing Potion
- Rendalim
- Potion of Invulnerability
- Potion of Alether
- Tarama Seed
- Laumspur items

Some items are not consumed, but toggle a state. For example, Yabari Ointment shows a button that turns its protection flag on or off.

If an item does not show **Use**, the assistant does not have a safe audited effect for it yet. Apply the effect manually with the stat buttons, then keep playing.

## How Does The Karmo Potion Work?

Use the **Karmo Potion** from the Herb Pouch when the book allows it.

The assistant will:

- remove the potion
- return an Empty Vial
- double current Endurance and Willpower
- mark the Karmo effect as active

While Karmo is active, the Section card can show Karmo controls. Use those controls to apply the side-effect roll and to finish the potion after the relevant combat.

When you finish Karmo, the assistant halves current Endurance and Willpower, rounded down.

## What Happens When Gear Is Taken Away?

Some sections take Grey Star's Staff, Backpack, or other equipment and tell you to remember what you had.

The assistant stores that gear in the **Stored Gear** card. The items are treated as unavailable while the book has taken them away, but the record is kept so the assistant can restore them when the book returns them.

If you manually add or remove gear during one of these stretches, double-check the Stored Gear card before moving on.

## How Do I Use Combat?

If a section has an audited combat preset, use the **Start** button from the Section Assistant or Combat tab.

For a manual fight, open **Combat** and fill in:

- enemy name
- enemy Combat Skill
- enemy Endurance
- active weapon
- Staff Magic on or off
- optional combat modifier
- optional victory or evade section

Then resolve rounds with the combat form.

## What Is `Staff WP` Or `Staff WP / Round`?

That number controls how much Willpower Grey Star spends when using the Wizard's Staff in tracked combat.

Leave Staff Magic off when you are not using the Staff magically. If Staff Magic is on, the tracker spends the selected Willpower during each round and uses that value for the Staff combat math.

The field exists because some fights use ordinary weapon combat and some fights involve Staff-powered magic. The assistant needs to know which one you are doing.

## What Are Victory Section And Evade Section?

Those are optional routing helpers for tracked combat.

Use **Victory Section** when the book says where to turn after winning the fight.

Use **Evade Section** when the book says where to turn if you evade.

They do not change combat math. They just let the assistant offer the correct next section after the fight ends.

## What If I Have No Weapon?

If your Weapons list is empty, the assistant treats combat as no-weapon combat and applies the no-weapon penalty.

If the Wizard's Staff is unavailable but another weapon exists, the assistant does not pretend the Staff is there. Staff-unavailable penalties are only applied where the Grey Star rules or audited section support calls for them.

## How Does The Jewelled Dagger Bonus Work?

The Jewelled Dagger bonus applies when the Jewelled Dagger is actually chosen as the combat weapon.

Just owning it is not enough.

## How Do I Use A Magical Shield In A Fight?

Only use a shield if the book route actually gave you one.

For example, some fights have different damage if you entered with a Sorcery shield already raised. The assistant tracks that kind of thing through route flags or section audit data. If you did not take the route that raised the shield, the fight should not suddenly offer shield protection.

Book text wins here. If the book says the shield is up, use the shield route or flag. If it does not, fight normally.

## What Happens When I Die?

The death screen gives two recovery choices:

- **Repeat** restores the state from when you entered the current section, so you can try the same fight or roll again.
- **Rewind** restores the previous section state, so you can make a different route choice.

Repeat is best for bad combat luck. Rewind is best when the mistake happened before the death section.

## What Does Repeat Restore?

Repeat restores the section-entry snapshot: Endurance, Willpower, inventory, combat setup, and other state from when you entered that section.

That matters because a fight may spend Willpower, use a potion, eat inventory, or damage Grey Star before killing him. Repeat puts you back at the start of that attempt.

## Can Willpower Go Negative?

The assistant follows the book rules over house rules.

If an audited book effect can legally push Willpower below zero, the assistant allows it. It does not automatically floor Willpower at zero unless the book or audit says to.

## Does Endurance Cap At My Starting Endurance?

Normal healing should not push Endurance above the current maximum unless a special effect says otherwise.

Some special effects, like Karmo, temporarily change the situation. In those cases, use the assistant's audited controls and read the message it gives back.

## Why Do Some Meal Or Provision Sections Feel Odd?

The books sometimes ask for meals in ways that are not as simple as "eat one Meal."

Some sections care whether you can pay the full cost. Some allow partial loss of supplies. The audit stores the section's own handling, so use **Apply Effects** and read the result message.

If the section text gives you a choice, make the choice first, then apply the matching effect.

## What Does "Book Rules Trump House Rules" Mean?

It means the assistant tries to follow the printed section logic, even when a cleaner app rule would be easier.

Examples:

- Willpower is not forced to stay at zero if the book logic can push it lower.
- Odd meal costs follow the section audit.
- Shield, Staff, and weapon penalties depend on the book's route and wording.
- Some timing choices stay in the player's hands instead of being auto-fired.

If the app and the book disagree, trust the book and use Manual Mode or the quick stat controls to correct the sheet.

## How Do Achievements Unlock?

Achievements unlock when the assistant sees the required section, route, item, combat result, or book-completion flag.

When an achievement unlocks, the app shows a notification. You can review all unlocked and locked achievements in the **Achievements** tab.

Some achievements are meant as replay targets. You do not need to unlock everything in one campaign run.

## Can I Replay A Book With The Same Character?

Yes. The book-completion screen can repeat the current book with the same character.

That is useful for achievement hunting. The assistant resets Endurance and Willpower back to base for the replay while keeping the character identity and campaign record.

## Are Saves Pushed To GitHub?

No. Saves stay local.

The `saves` folder, current position, UI preferences, and runtime files are ignored by git and are not included in release ZIPs.

Use the **Saves** tab if you want to export a character or back up all saves.

## Why Did My Card Sizes Or Collapsed Cards Come Back After Restart?

That is intentional. Layout, card sizes, closed cards, and collapsed cards are saved as UI preferences.

If you want to start over, open **Settings** and use the layout reset buttons.

## What If Something Looks Wrong?

First, trust the book text.

Then check:

- Are you on `localhost`, not a direct file path?
- Are you in Auto Mode or Manual Mode?
- Is the current section correct?
- Did you press Apply Effects for the section effect you chose?
- Is the needed item actually in the right inventory slot?
- Is a card collapsed or closed?

If the assistant state is wrong, use the quick stat buttons, inventory controls, or Manual Mode to correct it and keep going.

## What Is Complete For The Four Books?

Books 1, 2, 3, and 4 have assistant rules, achievements, strategy guides, and dry-run playtest reports.

The app is still a play aid, not a replacement for player judgment. The strongest workflow is still: read the book, make your choice, then let the assistant handle the bookkeeping.
