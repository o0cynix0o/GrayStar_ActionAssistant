# Grey Star Action Assistant v1.1.1 Release Notes

This release corrects the public package so Project Aon book files are no longer redistributed.

## Changed

- Removed Project Aon book HTML files from git tracking and release packages.
- Added `docs/INSTALL_PROJECT_AON_BOOKS.md` with Project Aon links and install examples.
- Added a local `install-books.html` guide page.
- Updated README, NOTICE, and public release docs to explain that users must download the books directly from Project Aon for personal use.
- Updated the app home and library pages so they no longer depend on bundled book image assets.
- Added a release packaging guard that fails if `books/gs` files are tracked.

## Notes

Your local `books/gs` folder can still exist and the app will still use it. It is now ignored by git and excluded from release ZIPs.
