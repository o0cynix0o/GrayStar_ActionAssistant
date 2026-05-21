# Installing Project Aon Books

Grey Star Action Assistant does not include the Grey Star book HTML files. Download the standard multi-page HTML editions from Project Aon for personal use, then extract them into the app's `books\gs` folder.

Project Aon license:

- https://www.projectaon.org/en/Main/License

## Download These Four ZIPs

Use the **standard** edition for each book. On the Project Aon book page, choose the first **Download ZIP** link in the `standard` row. Do not use the `simple`, `simpler`, EPUB, MOBI, or other eBook downloads for the assistant.

| Book | Project Aon page | Standard ZIP |
| --- | --- | --- |
| 1. Grey Star the Wizard | https://www.projectaon.org/en/Main/GreyStarTheWizard | https://www.projectaon.org/en/xhtml/gs/01gstw/01gstw.zip |
| 2. The Forbidden City | https://www.projectaon.org/en/Main/TheForbiddenCity | https://www.projectaon.org/en/xhtml/gs/02tfc/02tfc.zip |
| 3. Beyond the Nightmare Gate | https://www.projectaon.org/en/Main/BeyondTheNightmareGate | https://www.projectaon.org/en/xhtml/gs/03btng/03btng.zip |
| 4. War of the Wizards | https://www.projectaon.org/en/Main/WarOfTheWizards | https://www.projectaon.org/en/xhtml/gs/04wotw/04wotw.zip |

## Put Them Here

After extraction, these files should exist:

```text
books\gs\01gstw\title.htm
books\gs\02tfc\title.htm
books\gs\03btng\title.htm
books\gs\04wotw\title.htm
```

## PowerShell Example

From the project folder:

```powershell
New-Item -ItemType Directory -Force .\books\gs

Expand-Archive "$env:USERPROFILE\Downloads\01gstw.zip" -DestinationPath .\books\gs -Force
Expand-Archive "$env:USERPROFILE\Downloads\02tfc.zip"  -DestinationPath .\books\gs -Force
Expand-Archive "$env:USERPROFILE\Downloads\03btng.zip" -DestinationPath .\books\gs -Force
Expand-Archive "$env:USERPROFILE\Downloads\04wotw.zip" -DestinationPath .\books\gs -Force
```

Each ZIP should create its own book folder: `01gstw`, `02tfc`, `03btng`, or `04wotw`.

Check the result:

```powershell
Test-Path .\books\gs\01gstw\title.htm
Test-Path .\books\gs\02tfc\title.htm
Test-Path .\books\gs\03btng\title.htm
Test-Path .\books\gs\04wotw\title.htm
```

Each command should return `True`.
