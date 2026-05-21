# Grey Star Action Assistant v1.1.0 Release Notes

This release adds the web play-mode switch and brings the terminal assistant directly into the browser.

## Added

- Auto, Manual, and CLI play modes in the web assistant menu.
- Persistent mode indicator in the assistant top bar.
- Manual Mode for players who want bookkeeping without section automation.
- Embedded CLI Mode using the same save data as the web assistant.
- `greystar.ps1` terminal entry point.
- Launcher support for starting both the HTTP app and WebSocket CLI bridge.
- Wiki documentation for the new play modes.

## Changed

- `launch_greystar.py` now starts the web app and CLI bridge together.
- `ws_server.py` prefers the PowerShell terminal entry point on Windows.
- README now documents the embedded CLI bridge.

## Verified

- Python compile check passed.
- Book 1 playtest: 26 passed, 0 warnings, 0 failures.
- Book 2 playtest: 19 passed, 0 warnings, 0 failures.
- Book 3 playtest: 23 passed, 0 warnings, 0 failures.
- Book 4 playtest: 24 passed, 0 warnings, 0 failures.
- Campaign story run: 11 passed, 0 warnings, 0 failures.
- Achievement 100% run: 7 passed, 0 warnings, 0 failures.
