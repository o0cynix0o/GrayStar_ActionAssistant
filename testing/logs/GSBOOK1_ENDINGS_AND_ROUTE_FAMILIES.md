# GS Book 1 Endings And Route Families

Book: Grey Star the Wizard

Status: superseded by the dedicated route graph report for branch coverage. See `GSBOOK1_ROUTE_AUDIT.md`.

The route families are still not fully human-classified, but the route graph baseline now exists.

Current route-audit baseline:

- Expected sections: 350
- Existing section files: 350
- Reachable from section 1: 348/350
- Unreachable/no-incoming sections: 110, 342
- Detected success section: 350
- Endpoint sections: 29
- Branch points: 166

## Link Integrity Baseline

- Expected sections: 350
- Found sections: 350
- Missing sections: None
- Terminal or no-section-out-link candidates: 9, 14, 17, 20, 63, 67, 69, 92, 103, 122, 138, 155, 173, 177, 207, 216, 220, 225, 237, 262, 299, 306, 312, 315, 316, 317, 318, 324, 350
- No incoming section link candidates: 110, 342

## Confirmed/Probable Endpoints

| Section | Preliminary Classification | Evidence | Status |
|---:|---|---|---|
| 350 | probable book transition / success endpoint | no same-book section link; points forward to Book 2 title page | needs final human confirmation |
| 9 | terminal/failure candidate | no same-book out links in parser output | needs classification |
| 14 | terminal/failure candidate | no same-book out links in parser output | needs classification |
| 17 | terminal/failure candidate | no same-book out links in parser output | needs classification |
| 20 | terminal/failure candidate | no same-book out links in parser output | needs classification |
| 63 | terminal/failure candidate | no same-book out links in parser output | needs classification |
| 67 | terminal/failure candidate | no same-book out links in parser output | needs classification |
| 69 | terminal/failure candidate | no same-book out links in parser output | needs classification |
| 92 | terminal/failure candidate | no same-book out links in parser output | needs classification |
| 103 | terminal/failure candidate | no same-book out links in parser output | needs classification |
| 122 | terminal/failure candidate | no same-book out links in parser output | needs classification |
| 138 | terminal/failure candidate | no same-book out links in parser output | needs classification |
| 155 | terminal/failure candidate | no same-book out links in parser output | needs classification |
| 173 | terminal/failure candidate | no same-book out links in parser output | needs classification |
| 177 | terminal/failure candidate | no same-book out links in parser output | needs classification |
| 207 | terminal/failure candidate | no same-book out links in parser output | needs classification |
| 216 | terminal/failure candidate | no same-book out links in parser output | needs classification |
| 220 | terminal/failure candidate | no same-book out links in parser output | needs classification |
| 225 | terminal/failure candidate | no same-book out links in parser output | needs classification |
| 237 | terminal/failure candidate | no same-book out links in parser output | needs classification |
| 262 | terminal/failure candidate | no same-book out links in parser output | needs classification |
| 299 | terminal/failure candidate | no same-book out links in parser output | needs classification |
| 306 | terminal/failure candidate | no same-book out links in parser output | needs classification |
| 312 | terminal/failure candidate | no same-book out links in parser output | needs classification |
| 315 | terminal/failure candidate | no same-book out links in parser output | needs classification |
| 316 | terminal/failure candidate | no same-book out links in parser output | needs classification |
| 317 | terminal/failure candidate | no same-book out links in parser output | needs classification |
| 318 | terminal/failure candidate | no same-book out links in parser output | needs classification |
| 324 | terminal/failure candidate | no same-book out links in parser output | needs classification |

## Opening Route Start

| Section | Out Links | Notes |
|---:|---|---|
| 1 | 202, 168 | opening branch; no state automation confirmed yet |

## Route Families To Classify

- Opening mainland approach branches from section 1.
- Lost Tribe / Kundi route appears to culminate at section 350 and transition into Book 2.
- Death and failure route families need classification from the terminal candidates above.
- Human review needed for endpoint sections marked `needs_classification` in `GSBOOK1_ROUTE_AUDIT.md`.
- Human review needed for the source-unreachable sections 110 and 342, especially because section 342 appeared in the earlier dry-run route smoke but is not linked by the local source graph.
