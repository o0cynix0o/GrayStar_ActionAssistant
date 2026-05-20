# Gray Star Full Book Audit Workflow

This is the Gray Star version of the Lone Wolf full book audit standard.

Use this when the task is to:

- read a Gray Star book from the local corpus
- map routes and endings
- find missing item, Magick, combat, and random-number rules
- create structured automation ledgers
- propose route, exploration, story, and item achievements
- leave repeatable local reports for later implementation work

## Standard Request Phrases

- `Run the Full Book Audit for Gray Star Book X`
- `Run the Full Book Audit + Build for Gray Star Book X`

The first means analysis and reports only.

The second means:

- analysis
- reports
- proposal
- implementation of approved findings
- player-facing guide draft or update, when scope changes enough to matter
- validation

## Source Material

Use the local book corpus first:

- `books/gs/`

For Gray Star book audits, the preferred source order is:

1. local corpus under `books/gs/<book-code>/`
2. local supporting pages in the same folder:
   - `gamerulz.htm`
   - `powers.htm`
   - `footnotz.htm`
   - `equipmnt.htm`
   - `action.htm`
   - `cmbtrulz.htm`
   - `crsumary.htm`
   - `crtable.htm`
   - `random.htm`
   - `errata.htm`
   - `sage.htm`
3. Project Aon text and errata only as fallback, cross-check, or gap filler

The local corpus is the primary offline audit baseline because it gives section files, rules pages, footnotes, images, and errata locally.

Do not copy large passages of book text into committed docs. Reference files and sections instead.

See also:

- `docs/BOOK_SOURCE_MAP.md`

## Expected Local Report Outputs

For each book, the audit should usually produce:

- `GSBOOKX_AUTOMATION_LEDGER.md`
- `GSBOOKX_ENDINGS_AND_ROUTE_FAMILIES.md`
- `GSBOOKX_RULES_AND_ITEMS_AUDIT.md`
- `GSBOOKX_COMBAT_AND_RANDOM_AUDIT.md`
- `GSBOOKX_ACHIEVEMENT_CANDIDATES.md`

These are local working reports and normally stay in `testing/logs/`.

`GSBOOKX_AUTOMATION_LEDGER.md` is the build handoff. It should be structured enough that implementation can work from it without rereading the whole book.

Generated sweep artifacts belong in `testing/tmp/`.

## Audit Steps

### 1. Read The Book Text

Start in the local corpus:

- confirm the book with `title.htm`
- read `gamerulz.htm`, `equipmnt.htm`, `action.htm`, `cmbtrulz.htm`, `crtable.htm`, `footnotz.htm`, and `errata.htm`
- read `powers.htm`, `sage.htm`, and `crsumary.htm` when present
- trace the adventure from `sect1.htm`

Review the book with an eye toward:

- branch points
- Magick checks
- item pickups
- forced item loss or inventory constraints
- Willpower and Endurance changes
- special combat rules
- random-number rolls
- permanent penalties or bonuses
- unique endings

### 2. Map Endings And Route Families

Identify:

- the success ending
- hard failure endings
- major winning route families
- important companion, item, or Magick dependencies

The goal is to understand the meaningful route families first, then fill in the smaller branches.

### 3. Run A Mechanical Text Sweep

Run a machine-assisted sweep over every `sect*.htm` for automation language.

Useful Gray Star search terms include:

- `lose`
- `gain`
- `restore`
- `deduct`
- `add`
- `erase`
- `discard`
- `Meal`
- `Willpower`
- `ENDURANCE`
- `COMBAT SKILL`
- `Random Number Table`
- `if you possess`
- `if you have`
- `if you lack`
- `if you know`
- `Wizard's Staff`
- `turn to`

Treat the sweep as a candidate generator, not as truth. The human audit must confirm context, timing, and whether the text describes an actual state change.

### 4. Build The Section Automation Ledger

Create one row per candidate automation section.

Recommended columns:

- section
- trigger timing
- rule type
- preconditions
- state change
- prompt needed
- legal prompt values or choices
- web-safe payload needed
- current app support
- acceptance test needed
- status

Use consistent trigger timing labels:

- on entry before text
- on entry after text
- after combat
- after random roll
- after prompt choice
- after inventory choice
- after book transition
- manual only

### 5. Audit Missing Rules And Items

Scan for high-value automation candidates:

- Magick-gated branches
- Willpower spending and restoration
- item bonuses or special item behavior
- section entry damage or healing
- forced gains and losses
- combat exceptions
- permanent stat changes
- book-specific restrictions

Mark each candidate as:

- already supported
- partly supported
- missing
- better left manual for now

### 6. Audit Combat Exceptions

Create a combat exception table for every combat found in the book.

Recommended columns:

- section
- enemy name
- enemy Combat Skill
- enemy Endurance
- Willpower/staff rules
- weapon restrictions
- evade rules
- auto-win or auto-loss conditions
- post-combat state changes
- current app support
- acceptance test needed

### 7. Audit Random Number And Prompt Flows

Create a table for every roll or structured choice that should be supported by automation or the web UI.

Recommended columns:

- section
- prompt label
- visible option text
- legal values
- random number modifier
- zero-counts-as-ten behavior
- result mapping
- state changes
- web context text needed
- current app support
- acceptance test needed

### 8. Compare Against The App

Check the current script and web UI so the audit distinguishes:

- what the book contains
- what the app already supports
- what still needs implementation

For this project, start with:

- `garystar.py`
- `app_server.py`
- `assistant.html`
- `data/crt.json`

### 9. Draft Achievement Candidates

Propose a first batch of:

- route achievements
- exploration achievements
- story achievements
- item or discovery achievements
- survival and resource achievements

Good achievement candidates are memorable, triggerable from reliable state, and do not depend on copied book text.

For each proposed achievement, record:

- stable ID
- display name
- book number
- category
- player-facing description
- unlock trigger
- trigger source: section history, book summary, combat history, inventory, status flag, or completed-book state
- whether it can be backfilled from existing saves
- dry-run acceptance check

Prefer durable triggers over fragile one-off UI events. Good triggers include:

- completed book number
- specific section or section-combination visits
- combat history entries and combat summary counts
- final book summary stats
- inventory items present in current state or book-completion summary
- recorded death/recovery counts

Avoid achievement triggers that require copied story text, exact prose matching, or a manual button press just to rebuild history.

The achievement workflow for each book is:

1. Draft the candidate list during the audit.
2. Show the list to the user for approval before implementation.
3. Implement approved definitions and trigger checks.
4. Sync achievements automatically from save history whenever state is loaded or served.
5. Preserve unlocked achievements permanently within the save/profile state.
6. Add or update the Achievements tab so the player can inspect unlocked, locked, and recent achievements.
7. Add backfill tests using dry-run saves so finished books can populate achievements without replaying.

Do not add a manual "rebuild achievements" button unless the user specifically asks for one. Automatic sync/backfill is the standard.

### 10. Write The Reports

Summarize:

- endings and route families
- the automation ledger
- missing rules and items
- combat and random-number exceptions
- top implementation candidates
- achievement candidates

The reports should let a later chat continue without rereading the conversation.

### 11. Propose Top Build Candidates

Before implementation, summarize:

- the best missing rules to automate first
- the best achievement batch to add
- which achievements should backfill from existing save data
- which achievements require a future replay
- assumptions and ambiguities
- acceptance checks for each proposed automation

### 12. Implement Approved Findings

If the user approves build-out:

- add rule and item support
- add achievement definitions and trigger checks
- add automatic achievement sync/backfill during load and state serving
- expose achievement payloads to the web app
- add or update the Achievements tab
- keep route-only choices on the book page unless the assistant needs a mechanical prompt
- keep unlocked achievements when death recovery, rewind, repeat-book, or next-book transitions occur
- add or update the book-complete repeat option when replay cleanup is useful
- update player-facing docs when behavior changes
- validate in both CLI and web paths when possible

The repeat-book option should:

- keep the same character
- keep the same inventory unless the book rules or user ask otherwise
- keep completed-book records and unlocked achievements
- reset current section to section 1 of the completed book
- reset Endurance to current maximum
- reset Willpower to the stored book-start Willpower value
- reset current combat, death state, section checkpoints, and current-book stats for the new pass
- preserve the ability to continue to the next book from the completed-book screen before repeating

### 13. Run The Playtesting Ladder

After implementation, run validation in six levels. The goal is complete route, branch, and mechanic coverage, plus a few full-path smoke tests. Do not try to enumerate infinite full playthroughs when loops or repeated state changes make that impractical.

#### 1. Basic Validation

Confirm the book and app data are structurally sound:

- every `sect*.htm` file exists for the expected section range
- every source section link points to an existing section
- rules/supporting pages needed by the audit exist or are documented as missing
- JSON data files load without syntax errors
- Python files compile
- the web API starts and returns state
- the live save pointer is protected before any dry-run work

#### 2. Audit Coverage

Confirm every section has been accounted for:

- every section is classified by type: story, route choice, loot, combat, stat change, meal, random roll, Magick check, gear loss/restore, death/failure, book completion, or special case
- every mechanical effect is recorded in the section audit or automation ledger
- every ambiguity is either resolved with a user ruling or marked as manual/undecided
- every combat and random-number section appears in the combat/random audit

#### 3. Automation Coverage

For every recorded mechanic, confirm it has one of three outcomes:

- app automation exists
- a manual UI control exists
- the reason it remains manual is documented

This includes:

- END, WP, CS, Nobles changes
- Meal rules
- item gain/loss/use
- Herb Pouch and Backpack handling
- status flags
- Magick gates and costs
- random roll helpers
- combat presets
- death/recovery
- book completion and transition
- achievement definitions and automatic sync/backfill
- repeat-book restart behavior

#### 4. Branch Coverage

Test every outgoing route at least once:

- crawl all book-page links from every section
- confirm all target sections exist
- confirm every reachable branch from section 1 is represented in route data or source-link checks
- exercise each branch family at least once in dry-run state
- document unreachable or errata-corrected branches

Route choices can remain on the book page links when the assistant panel would only duplicate navigation. Mechanical branches still need assistant support or documentation.

#### 5. Mechanic Outcome Coverage

Test every non-trivial mechanic outcome:

- every random roll result band
- every loot picker option
- every status toggle
- every WP-cost mode, including book-approved negative WP or END substitution when applicable
- every death/failure ending style
- every gear loss and gear restore path
- every combat preset start
- combat victory, defeat, evade, survival, timeout, round-limit, timed-modifier, fixed-CS, and per-round-effect cases where applicable
- every book completion and carry-forward transition
- every achievement trigger category
- expected unlocked/missing achievement counts for at least one representative save
- repeat-book reset while preserving achievements

These tests should run against copied or in-memory saves. They must not change the live campaign save unless the user explicitly asks.

#### 6. Full-Path Smoke Tests

Run a small set of realistic full-route dry runs:

- one successful route to the book completion section
- one route that exercises death/recovery
- one route that exercises gear loss/restoration
- one route that earns a story or discovery achievement
- one low-Willpower route
- one low-Endurance route
- one important item/Magick-gated route
- one repeat-book cleanup run from a completed-book state
- book-specific edge-case routes found during the audit

The success target is not "every infinite playthrough." The success target is 100% route/branch/mechanic coverage plus representative complete paths.

## What Usually Stays Manual

Leave rules manual when they are too ambiguous, too isolated, or easy for the player to perform once without bookkeeping pain.

Document them anyway so they are not lost.

## What Usually Gets Automated First

Highest-value automation candidates are usually:

- Willpower and Endurance changes
- item gains and forced losses
- Magick-gated prompts
- special combat setup rules
- reliable story achievement triggers
- achievement auto-backfill from durable save data
- completion and repeat-book replay support

## Naming Conventions

Reports:

- `GSBOOK1_*`
- `GSBOOK2_*`
- `GSBOOK3_*`
- `GSBOOK4_*`

Temporary sweep artifacts:

- `gsbook1_source_sweep.json`
- `gsbook1_source_inventory.json`

## Success Condition

The audit is successful when another chat can pick up the book with:

- route picture
- missing rule list
- item list
- combat and random-flow list
- achievement plan
- implemented/backfillable achievement status
- local report files
- validation notes
- a completed six-level playtesting ladder, or clear notes on which levels still need data/user rulings

without needing the original conversation.
