# GS Book 2 Route Audit

Generated: 2026-05-20T15:21:43

Book: The Forbidden City

Status: machine route-graph baseline. Human route-family names and story classifications still need review.

## Summary

| Metric | Value |
|---|---|
| Expected sections | 310 |
| Existing section files | 310 |
| Missing section files | None |
| Source edges | 487 |
| Bad source links | None |
| Reachable from section 1 | 310/310 |
| Unreachable from section 1 | None |
| No incoming links | None |
| Endpoint sections | 27 |
| Branch points | 145 |
| Success-capable branch points | 145 |
| Detected success section | 310 |

## Shortest Success Path

- Length: 63 sections
- Path: 1, 126, 257, 78, 235, 105, 61, 149, 200, 275, 144, 266, 276, 250, 53, 287, 203, 159, 40, 211, 50, 22, 60, 214, 195, 111, 295, 72, 299, 66, 291, 145, 120, 129, 52, 186, 294, 124, 254, 92, 84, 166, 307, 26, 284, 76, 108, 38, 168, 240, 54, 103, 170, 148, 267, 23, 273, 85, 157, 272, 229, 172, 310

## Mandatory Success Chokepoints

These sections dominate the detected success endpoint in the source-link graph. They are route-graph chokepoints, not proof that every legal state can pass through them.

- Count: 25
- Sections: 1, 26, 52, 54, 60, 66, 85, 103, 111, 124, 126, 144, 148, 168, 195, 214, 229, 240, 250, 257, 267, 272, 276, 291, 310

## Opening Branches

| Branch | Reachable Sections | Can Reach Success | Reachable Endpoints | Early Merge Examples |
|---|---:|---|---|---|
| 1 -> 126 | 309 | yes | 3, 33, 56, 70, 90, 98, 102, 110, 127, 128, 152, 167, 179, 193, 202, 213, ... (+11 more) | None |

## Endpoint Inventory

| Section | Classification | Reachable | Tags | Shortest Path |
|---:|---|---|---|---|
| 3 | needs_classification | yes | leaf | 1, 126, 257, 78, 235, 105, 61, 149, 200, 275, 144, 266, 276, 250, 53, 287, 3 |
| 33 | needs_classification | yes | leaf | 1, 126, 257, 78, 235, 105, 61, 149, 200, 275, 144, 266, 276, 250, 53, 287, 203, 159, 40, 211, 50, 22, 60, 214, ... (+25 more) |
| 56 | death_or_failure | yes | leaf | 1, 126, 257, 188, 15, 125, 230, 51, 56 |
| 70 | death_or_failure | yes | leaf | 1, 126, 257, 78, 235, 105, 61, 149, 200, 275, 144, 266, 276, 250, 53, 287, 203, 159, 40, 211, 50, 22, 60, 214, ... (+13 more) |
| 90 | death_or_failure | yes | leaf | 1, 126, 257, 188, 15, 125, 181, 183, 95, 210, 90 |
| 98 | death_or_failure | yes | leaf | 1, 126, 257, 78, 115, 283, 98 |
| 102 | death_or_failure | yes | leaf | 1, 126, 257, 188, 15, 125, 181, 183, 68, 102 |
| 110 | death_or_failure | yes | leaf | 1, 126, 257, 78, 235, 25, 252, 249, 194, 12, 89, 110 |
| 127 | death_or_failure | yes | leaf | 1, 126, 257, 78, 235, 105, 61, 149, 200, 275, 144, 266, 276, 250, 53, 287, 203, 159, 40, 211, 50, 22, 60, 214, ... (+25 more) |
| 128 | death_or_failure | yes | leaf | 1, 126, 257, 188, 15, 125, 274, 180, 155, 128 |
| 152 | needs_classification | yes | leaf | 1, 126, 257, 188, 15, 125, 181, 183, 68, 223, 152 |
| 167 | death_or_failure | yes | leaf | 1, 126, 257, 78, 235, 105, 61, 149, 200, 275, 144, 266, 276, 250, 53, 287, 21, 167 |
| 179 | death_or_failure | yes | leaf | 1, 126, 257, 78, 235, 105, 61, 149, 200, 275, 144, 179 |
| 193 | death_or_failure | yes | leaf | 1, 126, 257, 78, 235, 105, 61, 149, 200, 275, 144, 266, 276, 250, 53, 287, 203, 159, 40, 211, 50, 22, 60, 214, ... (+39 more) |
| 202 | death_or_failure | yes | leaf | 1, 126, 257, 78, 235, 105, 61, 149, 200, 275, 144, 266, 276, 250, 53, 287, 203, 159, 40, 211, 50, 22, 60, 214, ... (+5 more) |
| 213 | death_or_failure | yes | leaf | 1, 126, 257, 78, 235, 105, 61, 149, 200, 275, 144, 266, 276, 250, 53, 287, 203, 159, 40, 211, 50, 22, 60, 214, ... (+31 more) |
| 220 | death_or_failure | yes | leaf | 1, 126, 257, 78, 235, 105, 61, 149, 200, 275, 144, 266, 276, 250, 53, 287, 203, 159, 40, 211, 50, 22, 60, 214, ... (+23 more) |
| 236 | death_or_failure | yes | leaf | 1, 126, 257, 188, 15, 125, 274, 180, 155, 5, 236 |
| 239 | death_or_failure | yes | leaf | 1, 126, 257, 78, 235, 105, 61, 149, 200, 275, 144, 266, 276, 250, 53, 287, 21, 239 |
| 242 | death_or_failure | yes | leaf | 1, 126, 257, 78, 235, 105, 61, 149, 200, 275, 144, 266, 276, 250, 53, 287, 203, 159, 40, 211, 50, 22, 60, 214, ... (+29 more) |
| 244 | death_or_failure | yes | leaf | 1, 126, 257, 78, 235, 105, 61, 149, 200, 275, 144, 266, 276, 250, 53, 287, 21, 244 |
| 260 | death_or_failure | yes | leaf | 1, 126, 257, 78, 235, 105, 61, 149, 200, 275, 144, 266, 276, 250, 53, 287, 203, 159, 40, 211, 50, 22, 60, 214, ... (+22 more) |
| 261 | needs_classification | yes | leaf | 1, 126, 257, 188, 15, 125, 181, 183, 95, 210, 261 |
| 263 | death_or_failure | yes | leaf | 1, 126, 257, 188, 15, 125, 181, 183, 68, 258, 263 |
| 277 | death_or_failure | yes | leaf | 1, 126, 257, 78, 235, 105, 61, 149, 200, 275, 144, 266, 276, 250, 53, 287, 203, 159, 40, 211, 50, 22, 60, 214, ... (+14 more) |
| 280 | death_or_failure | yes | leaf, magick_check | 1, 126, 257, 78, 235, 105, 61, 149, 200, 275, 144, 266, 276, 250, 101, 222, 207, 6, 55, 141, 280 |
| 310 | success | yes | leaf | 1, 126, 257, 78, 235, 105, 61, 149, 200, 275, 144, 266, 276, 250, 53, 287, 203, 159, 40, 211, 50, 22, 60, 214, ... (+39 more) |

## Success-Capable Branch Points

These are branch sections reachable from section 1 that can still reach the detected success ending.

| Section | Targets | Can Reach Success | Success Targets | Non-success Targets | Tags |
|---:|---|---|---|---|---|
| 2 | 45, 71 | yes | 45, 71 | None | branch, magick_check, item_gate, meal |
| 5 | 236, 74 | yes | 74 | 236 | branch, random, item_gate, loot |
| 6 | 238, 55 | yes | 238, 55 | None | branch, magick_check, item_gate |
| 12 | 67, 89 | yes | 67, 89 | None | branch, magick_check, item_gate, meal |
| 16 | 57, 22, 35 | yes | 57, 22, 35 | None | branch, magick_check, item_gate |
| 17 | 299, 265 | yes | 299, 265 | None | branch, magick_check, item_gate |
| 18 | 62, 70 | yes | 62 | 70 | branch, endurance |
| 19 | 135, 248 | yes | 135, 248 | None | branch |
| 20 | 149, 97 | yes | 149, 97 | None | branch, combat, magick_check, endurance |
| 21 | 167, 109, 239, 244 | yes | 109 | 167, 239, 244 | branch, magick_check |
| 23 | 273, 243 | yes | 273, 243 | None | branch |
| 26 | 284, 87 | yes | 284, 87 | None | branch |
| 27 | 135, 248 | yes | 135, 248 | None | branch |
| 29 | 112, 136, 219 | yes | 112, 136, 219 | None | branch, wp |
| 32 | 106, 217, 173 | yes | 106, 217, 173 | None | branch, random |
| 37 | 46, 23, 64 | yes | 46, 23, 64 | None | branch, magick_check, item_gate, loot |
| 41 | 307, 150 | yes | 307, 150 | None | branch, wp |
| 43 | 201, 117, 240 | yes | 201, 117, 240 | None | branch, magick_check, item_gate, wp |
| 46 | 233, 245 | yes | 233, 245 | None | branch |
| 47 | 290, 139 | yes | 290, 139 | None | branch, magick_check, item_gate, wp |
| 49 | 280, 205 | yes | 205 | 280 | branch, magick_check, wp, endurance, loot |
| 50 | 22, 16 | yes | 22, 16 | None | branch |
| 51 | 226, 56 | yes | 226 | 56 | branch, magick_check, wp |
| 52 | 186, 18 | yes | 186, 18 | None | branch |
| 53 | 91, 287 | yes | 91, 287 | None | branch |
| 59 | 129, 137, 138 | yes | 129, 137, 138 | None | branch, magick_check, item_gate |
| 61 | 149, 271 | yes | 149, 271 | None | branch, combat, endurance |
| 64 | 23, 46 | yes | 23, 46 | None | branch, magick_check, wp |
| 65 | 165, 71 | yes | 165, 71 | None | branch, magick_check |
| 67 | 79, 89 | yes | 79, 89 | None | branch, magick_check, wp |
| 68 | 223, 258, 147, 102 | yes | 223, 258, 147 | 102 | branch, magick_check, item_gate, wp |
| 69 | 290, 139 | yes | 290, 139 | None | branch, magick_check, item_gate, wp |
| 71 | 121, 28 | yes | 121, 28 | None | branch, magick_check, item_gate, endurance |
| 72 | 299, 265 | yes | 299, 265 | None | branch, magick_check, item_gate |
| 73 | 231, 116 | yes | 231, 116 | None | branch, magick_check, item_gate |
| 76 | 108, 220, 281 | yes | 108, 281 | 220 | branch, magick_check, item_gate |
| 78 | 115, 235 | yes | 115, 235 | None | branch, endurance |
| 79 | 13, 4 | yes | 13, 4 | None | branch |
| 81 | 22, 16 | yes | 22, 16 | None | branch |
| 84 | 221, 166 | yes | 221, 166 | None | branch |
| 85 | 157, 304 | yes | 157, 304 | None | branch, item_gate |
| 88 | 123, 156 | yes | 123, 156 | None | branch |
| 89 | 110, 100 | yes | 100 | 110 | branch, random, item_gate, loot |
| 91 | 139, 290, 208 | yes | 139, 290, 208 | None | branch, magick_check, item_gate, wp, endurance |
| 92 | 175, 84 | yes | 175, 84 | None | branch |
| 94 | 306, 127 | yes | 306 | 127 | branch, loot |
| 95 | 210, 297 | yes | 210, 297 | None | branch, magick_check, item_gate |
| 101 | 222, 53 | yes | 222, 53 | None | branch |
| 103 | 170, 224, 279, 242 | yes | 170, 224, 279 | 242 | branch, magick_check, item_gate, wp, loot |
| 104 | 175, 73 | yes | 175, 73 | None | branch |
| 105 | 61, 185 | yes | 61, 185 | None | branch, wp |
| 108 | 38, 184, 248 | yes | 38, 184, 248 | None | branch |
| 111 | 132, 209, 227, 256, 269, 295 | yes | 132, 209, 227, 256, 269, 295 | None | branch, magick_check, item_gate |
| 112 | 286, 190, 253 | yes | 286, 190, 253 | None | branch, wp |
| 113 | 122, 143, 229 | yes | 122, 143, 229 | None | branch, magick_check, item_gate |
| 115 | 163, 283 | yes | 163, 283 | None | branch |
| 119 | 39, 116 | yes | 39, 116 | None | branch, wp, loot |
| 122 | 143, 229 | yes | 143, 229 | None | branch, magick_check, item_gate, wp |
| 124 | 212, 254 | yes | 212, 254 | None | branch |
| 125 | 181, 230, 274 | yes | 181, 230, 274 | None | branch, magick_check, item_gate |
| 126 | 216, 257 | yes | 216, 257 | None | branch, magick_check, item_gate |
| 130 | 221, 301 | yes | 221, 301 | None | branch |
| 131 | 282, 305 | yes | 282, 305 | None | branch, magick_check, item_gate |
| 135 | 270, 178 | yes | 270, 178 | None | branch, magick_check, item_gate |
| 136 | 286, 253 | yes | 286, 253 | None | branch, magick_check, wp |
| 140 | 25, 105 | yes | 25, 105 | None | branch, endurance |
| 141 | 280, 205 | yes | 205 | 280 | branch, wp, endurance, loot |
| 142 | 31, 49 | yes | 31, 49 | None | branch |
| 143 | 122, 229 | yes | 122, 229 | None | branch, magick_check, wp |
| 144 | 179, 196, 266 | yes | 196, 266 | 179 | branch, magick_check, item_gate |
| 145 | 120, 162 | yes | 120, 162 | None | branch, item_gate, loot |
| 146 | 42, 289 | yes | 42, 289 | None | branch, random, item_gate, loot |
| 148 | 267, 213 | yes | 267 | 213 | branch, item_gate, loot |
| 151 | 123, 156 | yes | 123, 156 | None | branch |
| 153 | 19, 27, 33 | yes | 19, 27 | 33 | branch, random, endurance |
| 155 | 5, 128 | yes | 5 | 128 | branch, magick_check, item_gate, wp |
| 160 | 118, 44 | yes | 118, 44 | None | branch, random, wp |
| 161 | 94, 300, 127 | yes | 94, 300 | 127 | branch |
| 162 | 59, 120 | yes | 59, 120 | None | branch, magick_check, wp |
| 163 | 30, 88 | yes | 30, 88 | None | branch, combat, wp, endurance |
| 164 | 191, 277 | yes | 191 | 277 | branch, endurance |
| 165 | 121, 28 | yes | 121, 28 | None | branch, magick_check, item_gate, wp, endurance |
| 166 | 307, 150 | yes | 307, 150 | None | branch, wp, endurance |
| 168 | 293, 201, 117, 240 | yes | 293, 201, 117, 240 | None | branch, magick_check, item_gate |
| 169 | 232, 202 | yes | 232 | 202 | branch, endurance |
| 170 | 148, 279 | yes | 148, 279 | None | branch, magick_check, wp |
| 171 | 66, 202 | yes | 66 | 202 | branch, endurance |
| 174 | 14, 142 | yes | 14, 142 | None | branch, magick_check, wp |
| 175 | 39, 119 | yes | 39, 119 | None | branch, magick_check, item_gate |
| 180 | 155, 199 | yes | 155, 199 | None | branch, magick_check, item_gate |
| 182 | 206, 255 | yes | 206, 255 | None | branch |
| 183 | 68, 95 | yes | 68, 95 | None | branch, wp |
| 184 | 161, 94, 302, 127 | yes | 161, 94, 302 | 127 | branch |
| 185 | 149, 156 | yes | 149, 156 | None | branch |
| 186 | 164, 294 | yes | 164, 294 | None | branch, item_gate |
| 187 | 201, 117, 240 | yes | 201, 117, 240 | None | branch, magick_check, item_gate, wp |
| 188 | 15, 140 | yes | 15, 140 | None | branch, random, wp |
| 194 | 2, 12 | yes | 2, 12 | None | branch |
| 196 | 179, 131 | yes | 131 | 179 | branch, wp |
| 199 | 68, 95 | yes | 68, 95 | None | branch, magick_check, wp |
| 203 | 159, 99 | yes | 159, 99 | None | branch, wp |
| 207 | 6, 146, 234 | yes | 6, 146, 234 | None | branch, magick_check, item_gate, wp, endurance |
| 210 | 90, 228, 261, 309 | yes | 228, 309 | 90, 261 | branch, wp |
| 214 | 32, 195 | yes | 32, 195 | None | branch, item_gate, endurance, meal |
| 215 | 170, 224, 242 | yes | 170, 224 | 242 | branch, magick_check, item_gate |
| 219 | 48, 189, 114 | yes | 48, 189, 114 | None | branch, wp |
| 223 | 74, 152 | yes | 74 | 152 | branch, wp |
| 224 | 96, 170 | yes | 96, 170 | None | branch, item_gate |
| 225 | 11, 20 | yes | 11, 20 | None | branch |
| 227 | 107, 63, 24 | yes | 107, 63, 24 | None | branch, item_gate, wp |
| 229 | 264, 172, 218 | yes | 264, 172, 218 | None | branch, magick_check |
| 230 | 7, 34, 51, 86 | yes | 7, 34, 51, 86 | None | branch, magick_check, wp |
| 231 | 241, 83, 84 | yes | 241, 83, 84 | None | branch, wp |
| 234 | 29, 6, 146 | yes | 29, 6, 146 | None | branch, magick_check, item_gate, wp |
| 235 | 25, 105 | yes | 25, 105 | None | branch |
| 237 | 170, 224, 242 | yes | 170, 224 | 242 | branch, magick_check, item_gate |
| 238 | 174, 292, 198 | yes | 174, 292, 198 | None | branch, magick_check, item_gate |
| 243 | 262, 85 | yes | 262, 85 | None | branch |
| 245 | 273, 243 | yes | 273, 243 | None | branch |
| 246 | 260, 84 | yes | 84 | 260 | branch |
| 248 | 161, 302, 127 | yes | 161, 302 | 127 | branch |
| 250 | 101, 53 | yes | 101, 53 | None | branch, item_gate |
| 252 | 225, 249 | yes | 225, 249 | None | branch |
| 254 | 92, 158 | yes | 92, 158 | None | branch, combat, endurance |
| 257 | 78, 188, 278 | yes | 78, 188, 278 | None | branch, magick_check, item_gate |
| 258 | 74, 263 | yes | 74 | 263 | branch, wp |
| 259 | 176, 77 | yes | 176, 77 | None | branch |
| 264 | 229, 193 | yes | 229 | 193 | branch |
| 265 | 80, 171 | yes | 80, 171 | None | branch, magick_check, item_gate |
| 267 | 23, 37, 46, 64 | yes | 23, 37, 46, 64 | None | branch, magick_check, item_gate |
| 268 | 44, 118 | yes | 44, 118 | None | branch, random, wp |
| 272 | 113, 122, 143, 229 | yes | 113, 122, 143, 229 | None | branch, magick_check, item_gate |
| 273 | 85, 182 | yes | 85, 182 | None | branch, combat, endurance |
| 274 | 74, 180 | yes | 74, 180 | None | branch, wp |
| 278 | 160, 192, 268 | yes | 160, 192, 268 | None | branch, wp |
| 279 | 288, 237, 215 | yes | 288, 237, 215 | None | branch, wp |
| 283 | 98, 151 | yes | 151 | 98 | branch, endurance |
| 284 | 76, 296 | yes | 76, 296 | None | branch |
| 286 | 48, 189 | yes | 48, 189 | None | branch, wp |
| 287 | 3, 203, 21, 303 | yes | 203, 21, 303 | 3 | branch, magick_check, item_gate, wp, endurance |
| 288 | 170, 224, 242 | yes | 170, 224 | 242 | branch, magick_check, item_gate |
| 290 | 47, 36, 58, 69 | yes | 47, 36, 58, 69 | None | branch |
| 291 | 145, 154 | yes | 145, 154 | None | branch, magick_check, item_gate, endurance |
| 292 | 174, 146, 234 | yes | 174, 146, 234 | None | branch, magick_check, item_gate, wp |
| 293 | 285, 187, 240, 43 | yes | 285, 187, 240, 43 | None | branch |

## Other Reachable Branch Points

- None

## Route-Family Starter Notes

- Treat each section 1 target as an opening route family until human review gives it a story name.
- Treat success-capable branch points as the first checklist for route-family classification.
- Treat endpoint rows marked `needs_classification` as mandatory human-review stops.
- Route-only choices can stay on the book page; mechanical branches need support data or explicit manual notes.
