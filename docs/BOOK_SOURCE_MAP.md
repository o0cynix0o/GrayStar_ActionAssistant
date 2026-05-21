# Grey Star Book Source Map

This doc is the quick map for the local Grey Star book corpus used by audits and route work.

## Source Priority

Preferred source order:

1. local corpus under `books/gs/`
2. local rules and support pages in the same book folder
3. Project Aon plus errata as fallback or cross-check

The local corpus is the audit baseline. Do not copy large book passages into audit reports.

## Local Corpus Layout

Main local corpus root:

- `books/gs/`

Typical book folder contents:

- `title.htm`
- `sect1.htm` through the book's last section file
- `gamerulz.htm`
- `powers.htm`
- `equipmnt.htm`
- `action.htm`
- `cmbtrulz.htm`
- `crsumary.htm`
- `crtable.htm`
- `random.htm`
- `footnotz.htm`
- `errata.htm`
- `sage.htm`
- map, illustration, and art assets

Most useful files during audits:

- `sect*.htm`
  section text and route tracing
- `footnotz.htm`
  footnotes and exceptions
- `errata.htm`
  Project Aon errata notes and known corrections
- `gamerulz.htm`
  book-specific rules context
- `powers.htm`
  Lesser Magicks, staff behavior, and power descriptions
- `equipmnt.htm`
  starting equipment and inventory context
- `cmbtrulz.htm`
  Grey Star combat and Willpower rules
- `crsumary.htm`
  short combat sequence checklist
- `crtable.htm`
  combat result table reference
- `random.htm`
  random-number table guidance
- `action.htm`
  Action Chart and tracked fields
- `sage.htm`
  player-facing resource guidance and high-level caution notes

## Grey Star Book Folder Map

- `01gstw`
  `Grey Star the Wizard`
- `02tfc`
  `The Forbidden City`
- `03btng`
  `Beyond the Nightmare Gate`
- `04wotw`
  `War of the Wizards`

## Recommended Audit Start Pattern

For a new Grey Star book audit:

1. open `books/gs/<code>/title.htm` and confirm the title
2. inspect supporting pages: `gamerulz.htm`, `powers.htm`, `equipmnt.htm`, `action.htm`, `cmbtrulz.htm`, `crsumary.htm`, `crtable.htm`, `random.htm`, `footnotz.htm`, `errata.htm`, `sage.htm`
3. trace sections from `sect1.htm`
4. run a mechanical sweep across `sect*.htm`
5. write report files under `testing/logs/`
6. write generated sweep artifacts under `testing/tmp/`

## Current Book 1 Baseline

Book 1 folder:

- `books/gs/01gstw`

Expected section range:

- `sect1.htm` through `sect350.htm`

## Repo Hygiene

- `books/` is local reference material
- audit docs should reference source files and sections instead of copying text
- workflow docs belong in `docs/`
- local reports belong in `testing/logs/`
- generated sweep artifacts belong in `testing/tmp/`
