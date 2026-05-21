# Grey Star Action Assistant — GUI Refinements

Make the following changes to the web-based GUI. These apply across all tabs (Sheet, Combat, etc.), not just the Sheet tab, unless noted.

## 1. Contextual Tooltips on Hover

Add hover tooltips to **only the non-obvious sections** of the interface — places where a new user can't tell what the section does or how to use it. Example: the **Staff Willpower** section on the Combat tab should have a tooltip explaining how it works.

- Tooltip shows on hover over the section header (or the section as a whole).
- **Do not** add tooltips to every section — it would be overwhelming. Use them selectively, only where the function isn't self-evident.
- Tooltip content should explain *how to use the section*, not just what it is.

## 2. Per-Card Context Menu

Each card gets a **small white dot in its upper-right corner**. Clicking the dot opens a context menu containing:

- **Move controls** — up / down / left / right
- **Resize controls** — Small (compact) / Medium (normal) / Large (full)
- **Open / Close** the section
- Room to grow with other card-level options later

Do **not** add broad drag-and-drop behavior in this pass.

Drag-and-drop is deferred. Later, test it on **one card only** as a controlled prototype before expanding it to the rest of the interface.

### Exception — Top Status Card Row

The row of **status cards at the very top of the interface** (the same ones referenced in section 3) is **completely static**. These cards must:

- **Not** have the white dot or context menu.
- **Not** be draggable.
- **Not** be resizable by the user.
- **Not** be closeable.

They are fixed, unchangeable, and unmovable. Treat them as part of the app chrome, not as user-configurable cards.

## 3. Layout: Book Name Card + Status Cards

The book name card is too short — long book titles get cut off. Rework the row so the title has room to breathe:

- **Lengthen the book name card** so the full title displays.
- **Shrink the status cards** in the same row — they're currently wider than they need to be. Make them more square (less rectangular) so the saved horizontal space can go to the book name card.

(This row is the static row from section 2's exception — the layout change here is a one-time developer adjustment, not a user-facing control.)

## 4. App-Level Menu + Restoring Closed Sections

Closing sections (item 2) creates a problem: how does the user get a closed section back? Solve it with an **app-level context menu**:

- Put a **small white dot in the upper-right corner of the main Assistant window** (separate from the per-card dots).
- Clicking it opens a menu with **app-focused actions**:
  - **Re-add a removed section** (list the closed ones so they can be brought back)
  - **Save game**
  - **Auto-save on / off** toggle
  - **Shut down the app**
  - **Settings** — link to a settings page

The Settings page should have a clear way to navigate back to the main Assistant view.

## 5. Spelling Correction — "Gary" / "Gray" → "Grey" (Project-Wide)

The project name has been misspelled throughout the codebase. The **canonical correct spelling is "Grey Star"** (British "Grey", matching the Lone Wolf *Grey Star the Wizard* book series). Existing references use the incorrect "Gary" or "Gray" forms and must be corrected.

Find every occurrence of "Gary" or "Gray" that refers to **this project, app, character, or wizard** and replace with "Grey". This includes:

- **Code identifiers** — variable names, function names, class names, element IDs, CSS classes, data attributes
- **Comments and docstrings**
- **String literals and UI text** — anything displayed to the user
- **File names** — rename files containing "Gary"/"Gray" in their name
- **Folder names** — including the project's own root folder:
  - `C:\Scripts\Gray Star\` → `C:\Scripts\Grey Star\`
  - `C:\Scripts\Gray Star\wiki\` → `C:\Scripts\Grey Star\wiki\`
- **Documentation, README files, and config files**
- **Git remotes / repo names** if they contain the misspelling (flag these; don't push remote renames without confirming)

### Do NOT touch

- Unrelated uses of the word "gray" — e.g., a CSS color value `#808080` named `gray`, or a comment about the color gray, should stay as-is. Only replace occurrences that refer to the project / character.
- Third-party library code, `node_modules`, or any vendor folder.

### After renaming

- Verify the app still loads and the GUI still works — broken paths or imports from the folder rename are the most likely regression.
- Update any launcher scripts, shortcuts, or hardcoded paths that pointed at the old folder name.
- Update this file's own name and any internal references if needed.

## Scope notes

- Sections 1–4 are GUI-only.
- Section 5 is a project-wide rename and may touch non-GUI files.
- Behavior should be consistent across all tabs **except** the static top status card row, which is exempt from all user-facing controls in section 2.
- Drag-and-drop is intentionally out of scope for the first GUI refinement pass. Prototype it later on one card before wider rollout.
- Persistence: card positions, sizes, open/closed state, and auto-save preference should survive a reload (localStorage is fine).
