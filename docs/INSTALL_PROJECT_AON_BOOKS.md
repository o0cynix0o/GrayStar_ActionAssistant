# Install The Project Aon Book Files

Grey Star Action Assistant does not include the Grey Star book HTML files in the repository or release ZIP.

Project Aon provides the Internet Editions for personal use from its own distribution point. Their license allows you to receive/download the books for personal use, but it does not allow this project to redistribute the book files. Download the books directly from Project Aon, then place them in the local folder layout below.

Read the license here:

- https://www.projectaon.org/en/Main/License

## Use The Standard HTML Editions

Download the **standard** edition for each Grey Star book. This is the full-featured, multi-page HTML edition that matches the assistant's reader paths.

| Book | Project Aon page | Standard ZIP |
| --- | --- | --- |
| 1. Grey Star the Wizard | https://www.projectaon.org/en/Main/GreyStarTheWizard | https://www.projectaon.org/en/xhtml/gs/01gstw/01gstw.zip |
| 2. The Forbidden City | https://www.projectaon.org/en/Main/TheForbiddenCity | https://www.projectaon.org/en/xhtml/gs/02tfc/02tfc.zip |
| 3. Beyond the Nightmare Gate | https://www.projectaon.org/en/Main/BeyondTheNightmareGate | https://www.projectaon.org/en/xhtml/gs/03btng/03btng.zip |
| 4. War of the Wizards | https://www.projectaon.org/en/Main/WarOfTheWizards | https://www.projectaon.org/en/xhtml/gs/04wotw/04wotw.zip |

Project Aon also has an all-books download page:

- https://www.projectaon.org/en/Main/AllOfTheBooks

For this assistant, the four individual standard ZIPs are the simplest path.

## Expected Folder Layout

After extraction, your project should look like this:

```text
Grey Star/
  books/
    README.md
    gs/
      01gstw/
        title.htm
        sect1.htm
        ...
      02tfc/
        title.htm
        sect1.htm
        ...
      03btng/
        title.htm
        sect1.htm
        ...
      04wotw/
        title.htm
        sect1.htm
        ...
```

The assistant expects these exact folder names:

- `01gstw`
- `02tfc`
- `03btng`
- `04wotw`

## Manual Install

1. Download all four standard ZIPs from Project Aon.
2. Open your Grey Star Action Assistant folder.
3. Create this folder if it does not exist:

   ```text
   books\gs
   ```

4. Extract each ZIP into `books\gs`.
5. Confirm these files exist:

   ```text
   books\gs\01gstw\title.htm
   books\gs\02tfc\title.htm
   books\gs\03btng\title.htm
   books\gs\04wotw\title.htm
   ```

If you see an extra nested folder after extraction, move the book folder so the path matches the examples above.

## PowerShell Example

From the project folder:

```powershell
New-Item -ItemType Directory -Force .\books\gs

Expand-Archive "$env:USERPROFILE\Downloads\01gstw.zip" -DestinationPath .\books\gs -Force
Expand-Archive "$env:USERPROFILE\Downloads\02tfc.zip"  -DestinationPath .\books\gs -Force
Expand-Archive "$env:USERPROFILE\Downloads\03btng.zip" -DestinationPath .\books\gs -Force
Expand-Archive "$env:USERPROFILE\Downloads\04wotw.zip" -DestinationPath .\books\gs -Force

Test-Path .\books\gs\01gstw\title.htm
Test-Path .\books\gs\02tfc\title.htm
Test-Path .\books\gs\03btng\title.htm
Test-Path .\books\gs\04wotw\title.htm
```

Each `Test-Path` command should return `True`.

## After Installing

Start the assistant:

```powershell
.\Launch-GreyStar.ps1
```

Then open:

```text
http://127.0.0.1:8897/assistant.html
```

The book pane should load the Project Aon HTML files from your local `books\gs` folder.
