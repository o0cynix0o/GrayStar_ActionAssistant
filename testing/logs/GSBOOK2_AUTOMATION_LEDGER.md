# GS Book 2 Automation Ledger

Book: The Forbidden City

Status: implemented for high-confidence Book 2 mechanical effects in `data/book2-simple-automations.json` and `data/book2-section-flows.json`. Karmo Potion now has guided item-use controls; the player still chooses whether to apply the side-effect END loss before or after finishing the potion because the Project Aon footnote leaves that timing to player discretion.

## Simple Automation

| Section | Trigger Timing | Rule Type | State Change | Current App Support | Status |
|---:|---|---|---|---|---|
| 2 | on section entry | add_item | add 3 Meals from Urik's Lianor | simple automation | implemented |
| 3 | on section entry | ending | terminal death or failure | simple automation | implemented |
| 4 | on section entry | stat | lose 2 END | simple automation | implemented |
| 7 | on section entry | stat | lose 2 WP | simple automation | implemented |
| 12 | on section entry | add_item | add 3 Meals from Urik's Lianor | simple automation | implemented |
| 28 | on section entry | stat | lose 2 END to Blood Nymph bites | simple automation | implemented |
| 33 | on section entry | ending | terminal death or failure | simple automation | implemented |
| 34 | on section entry | stat | lose 3 WP | simple automation | implemented |
| 35 | on section entry | stat | lose 1 WP | simple automation | implemented |
| 36 | on section entry | stat | lose 3 WP | simple automation | implemented |
| 42 | on section entry | stat | lose 2 WP | simple automation | implemented |
| 43 | on section entry | stat | lose 1 WP | simple automation | implemented |
| 47 | on section entry | stat | lose 2 WP | simple automation | implemented |
| 51 | on section entry | stat | lose 2 WP | simple automation | implemented |
| 55 | on section entry | stat | lose 1 WP and 8 END in the Kazim challenge | simple automation | implemented |
| 56 | on section entry | ending | terminal death or failure | simple automation | implemented |
| 58 | on section entry | stat | lose 2 WP | simple automation | implemented |
| 62 | on section entry | stat | lose 2 END from poisonous water | simple automation | implemented |
| 63 | on section entry | stat | lose 2 WP into the Mind Gem | simple automation | implemented |
| 64 | on section entry | stat | lose 1 WP | simple automation | implemented |
| 66 | on section entry | stat | lose 1 WP to Shasarak's dream attack | simple automation | implemented |
| 68 | on section entry | stat | lose 1 WP to strengthen the Shield of Sorcery | simple automation | implemented |
| 69 | on section entry | stat | lose 2 WP | simple automation | implemented |
| 70 | on section entry | ending | terminal death or failure | simple automation | implemented |
| 71 | on section entry | stat | lose 1 END to swamp exhaustion | simple automation | implemented |
| 78 | on section entry | stat | lose 2 END from the fall | simple automation | implemented |
| 80 | on section entry | stat | lose 4 END from the Deathgaunt's touch | simple automation | implemented |
| 86 | on section entry | stat | lose 2 WP | simple automation | implemented |
| 90 | on section entry | ending | terminal death or failure | simple automation | implemented |
| 96 | on section entry | stat | lose 1 WP | simple automation | implemented |
| 98 | on section entry | ending | terminal death or failure | simple automation | implemented |
| 102 | on section entry | ending | terminal death or failure | simple automation | implemented |
| 105 | on section entry | stat | lose 2 WP | simple automation | implemented |
| 110 | on section entry | ending | terminal death or failure | simple automation | implemented |
| 114 | on section entry | stat | lose 8 END from exhaustion | simple automation | implemented |
| 117 | on section entry | stat | lose 2 WP | simple automation | implemented |
| 119 | on section entry | stat | lose 1 WP for Prophecy | simple automation | implemented |
| 120 | on section entry | remove_item, stat | lose 3 WP and use one Azawood Leaf | simple automation | implemented |
| 121 | on section entry | flag | mark Yabari Ointment protection | simple automation | implemented |
| 122 | on section entry | stat | lose 2 WP | simple automation | implemented |
| 127 | on section entry | ending | terminal death or failure | simple automation | implemented |
| 128 | on section entry | ending | terminal death or failure | simple automation | implemented |
| 129 | on section entry | stat | lose 2 END through lack of sleep | simple automation | implemented |
| 132 | on section entry | stat | lose 2 WP | simple automation | implemented |
| 133 | on section entry | stat | restore 1 END and 1 WP | simple automation | implemented |
| 137 | on section entry | stat | lose 3 WP for the protective pentacle | simple automation | implemented |
| 138 | on section entry | remove_item | use one Azawood Leaf | simple automation | implemented |
| 139 | on section entry | stat | lose 4 WP | simple automation | implemented |
| 140 | on section entry | stat | lose 3 END from the crossbow wound | simple automation | implemented |
| 143 | on section entry | stat | lose 2 WP | simple automation | implemented |
| 147 | on section entry | stat | lose 1 WP | simple automation | implemented |
| 148 | on section entry | add_item | add Black Rod if not already recorded | simple automation | implemented |
| 149 | on section entry | gear, stat | Staff and Backpack taken; lose 3 END during captivity | simple automation | implemented |
| 150 | on section entry | meal | consume 1 Meal or lose 3 END | simple automation | implemented |
| 152 | on section entry | ending | terminal death or failure | simple automation | implemented |
| 155 | on section entry | stat | lose 2 WP | simple automation | implemented |
| 159 | on section entry | stat | lose 2 WP | simple automation | implemented |
| 160 | on section entry | stat | lose 2 WP | simple automation | implemented |
| 162 | on section entry | stat | lose 3 WP | simple automation | implemented |
| 163 | on section entry | stat | lose 1 WP | simple automation | implemented |
| 165 | on section entry | stat | lose 4 WP and 1 END | simple automation | implemented |
| 166 | on section entry | stat | lose 1 END | simple automation | implemented |
| 167 | on section entry | ending | terminal death or failure | simple automation | implemented |
| 169 | on section entry | stat | lose 8 END from the Deathgaunt's touch | simple automation | implemented |
| 170 | on section entry | stat | lose 1 WP | simple automation | implemented |
| 171 | on section entry | stat | lose 4 END from the Deathgaunt | simple automation | implemented |
| 172 | on section entry | remove_item | Black Rod thrown to the Kleasa | simple automation | implemented |
| 174 | on section entry | stat | lose 1 WP to activate the Mind Gem | simple automation | implemented |
| 178 | on section entry | stat | lose 1 WP | simple automation | implemented |
| 179 | on section entry | ending | terminal death or failure | simple automation | implemented |
| 181 | on section entry | stat | lose 2 WP | simple automation | implemented |
| 187 | on section entry | stat | lose 1 WP | simple automation | implemented |
| 188 | on section entry | stat | lose 2 WP | simple automation | implemented |
| 189 | on section entry | stat | lose 4 END | simple automation | implemented |
| 192 | on section entry | stat | lose 4 WP | simple automation | implemented |
| 193 | on section entry | ending | terminal death or failure | simple automation | implemented |
| 196 | on section entry | stat | lose 2 WP | simple automation | implemented |
| 198 | on section entry | stat | lose 3 WP for Psychomancy and the Mind Gem effort | simple automation | implemented |
| 200 | on section entry | gear, stat | Staff and Backpack returned; restore 2 END and 1 WP | simple automation | implemented |
| 201 | on section entry | stat | lose 1 WP | simple automation | implemented |
| 202 | on section entry | ending | terminal death or failure | simple automation | implemented |
| 203 | on section entry | stat | lose 2 WP | simple automation | implemented |
| 205 | on section entry | stat | lose 4 WP and 5 END from the Kazim duel | simple automation | implemented |
| 206 | on section entry | stat | lose 1 WP | simple automation | implemented |
| 210 | on section entry | stat | lose 3 WP | simple automation | implemented |
| 213 | on section entry | ending | terminal death or failure | simple automation | implemented |
| 214 | on section entry | meal | consume 1 Meal or lose 3 END | simple automation | implemented |
| 218 | on section entry | remove_item | Black Rod given to the Kleasa | simple automation | implemented |
| 220 | on section entry | ending | terminal death or failure | simple automation | implemented |
| 221 | on section entry | stat | lose 1 END from the fall | simple automation | implemented |
| 223 | on section entry | stat | lose 2 WP | simple automation | implemented |
| 226 | on section entry | stat | lose 4 WP | simple automation | implemented |
| 228 | on section entry | stat | lose 2 END from burns | simple automation | implemented |
| 230 | on section entry | stat | lose 2 WP | simple automation | implemented |
| 231 | on section entry | stat | lose 1 WP | simple automation | implemented |
| 234 | on section entry | stat | lose 2 WP | simple automation | implemented |
| 236 | on section entry | ending | terminal death or failure | simple automation | implemented |
| 239 | on section entry | ending | terminal death or failure | simple automation | implemented |
| 241 | on section entry | stat | lose 2 WP | simple automation | implemented |
| 242 | on section entry | ending | terminal death or failure | simple automation | implemented |
| 244 | on section entry | ending | terminal death or failure | simple automation | implemented |
| 247 | on section entry | add_item | add Chaksu Pipes | simple automation | implemented |
| 249 | on section entry | stat | restore 1 END from Lianor | simple automation | implemented |
| 256 | on section entry | stat | lose 2 WP | simple automation | implemented |
| 258 | on section entry | stat | lose 2 WP | simple automation | implemented |
| 260 | on section entry | ending | terminal death or failure | simple automation | implemented |
| 261 | on section entry | ending | terminal death or failure | simple automation | implemented |
| 262 | on section entry | stat | lose 1 WP | simple automation | implemented |
| 263 | on section entry | ending | terminal death or failure | simple automation | implemented |
| 266 | on section entry | stat | lose 1 WP | simple automation | implemented |
| 269 | on section entry | stat | lose 2 WP | simple automation | implemented |
| 274 | on section entry | stat | lose 2 WP | simple automation | implemented |
| 277 | on section entry | ending | terminal death or failure | simple automation | implemented |
| 278 | on section entry | stat | lose 2 WP | simple automation | implemented |
| 280 | on section entry | ending | terminal death or failure | simple automation | implemented |
| 281 | on section entry | stat | lose 1 WP | simple automation | implemented |
| 282 | on section entry | stat | lose 1 WP | simple automation | implemented |
| 283 | on section entry | stat | lose 3 END | simple automation | implemented |
| 285 | on section entry | stat | lose 2 WP | simple automation | implemented |
| 289 | on section entry | stat | lose 2 WP | simple automation | implemented |
| 291 | on section entry | stat | lose 2 END to fever | simple automation | implemented |
| 292 | on section entry | stat | lose 1 WP | simple automation | implemented |
| 295 | on section entry | stat | lose 3 WP | simple automation | implemented |
| 297 | on section entry | backpack, stat | discard Backpack and contents; lose 1 END | simple automation | implemented |
| 298 | on section entry | stat | lose 1 END and 1 WP during the night | simple automation | implemented |
| 299 | on section entry | remove_item | use one Azawood Leaf | simple automation | implemented |
| 304 | on section entry | stat | lose 1 END | simple automation | implemented |
| 307 | on section entry | stat | lose 1 WP | simple automation | implemented |
| 309 | on section entry | stat | lose 2 END from burns | simple automation | implemented |
| 310 | on section entry | ending | successful Book 2 ending | simple automation | implemented |

## Flow Buttons

| Section | Flow Type | Details | Current App Support | Status |
|---:|---|---|---|---|
| 4 | mechanical choice | 1 combat preset(s) | Choices panel | implemented |
| 5 | mechanical choice | roll helper | Choices panel | implemented |
| 10 | mechanical choice | 1 combat preset(s) | Choices panel | implemented |
| 11 | mechanical choice | 1 combat preset(s) | Choices panel | implemented |
| 20 | mechanical choice | 1 combat preset(s) | Choices panel | implemented |
| 29 | mechanical choice | 3 WP-cost buttons | Choices panel | implemented |
| 32 | mechanical choice | roll helper | Choices panel | implemented |
| 37 | mechanical choice | 1 loot option(s) | Choices panel | implemented |
| 39 | mechanical choice | 2 combat preset(s) | Choices panel | implemented |
| 45 | mechanical choice | 1 loot option(s); roll helper | Choices panel | implemented |
| 61 | mechanical choice | 1 combat preset(s) | Choices panel | implemented |
| 67 | mechanical choice | 1 WP-cost button | Choices panel | implemented |
| 82 | mechanical choice | 1 combat preset(s) | Choices panel | implemented |
| 83 | mechanical choice | 1 combat preset(s) | Choices panel | implemented |
| 89 | mechanical choice | roll helper | Choices panel | implemented |
| 99 | mechanical choice | 1 combat preset(s) | Choices panel | implemented |
| 103 | mechanical choice | 2 loot option(s) | Choices panel | implemented |
| 112 | mechanical choice | 3 WP-cost buttons | Choices panel | implemented |
| 116 | mechanical choice | 1 combat preset(s) | Choices panel | implemented |
| 123 | mechanical choice | 1 combat preset(s) | Choices panel | implemented |
| 133 | mechanical choice | 6 loot option(s) | Choices panel | implemented |
| 134 | mechanical choice | 1 combat preset(s) | Choices panel | implemented |
| 136 | mechanical choice | 2 WP-cost buttons | Choices panel | implemented |
| 146 | mechanical choice | roll helper | Choices panel | implemented |
| 153 | mechanical choice | roll helper | Choices panel | implemented |
| 160 | mechanical choice | roll helper | Choices panel | implemented |
| 163 | mechanical choice | 1 combat preset(s) | Choices panel | implemented |
| 174 | mechanical choice | 2 WP-cost buttons | Choices panel | implemented |
| 176 | mechanical choice | 1 combat preset(s) | Choices panel | implemented |
| 188 | mechanical choice | roll helper | Choices panel | implemented |
| 216 | mechanical choice | 1 loot option(s) | Choices panel | implemented |
| 227 | mechanical choice | 2 WP-cost buttons | Choices panel | implemented |
| 233 | mechanical choice | 1 loot option(s) | Choices panel | implemented |
| 251 | mechanical choice | 1 combat preset(s) | Choices panel | implemented |
| 254 | mechanical choice | 1 combat preset(s) | Choices panel | implemented |
| 266 | mechanical choice | 1 loot option(s) | Choices panel | implemented |
| 268 | mechanical choice | roll helper | Choices panel | implemented |
| 273 | mechanical choice | 1 combat preset(s) | Choices panel | implemented |
| 279 | mechanical choice | 3 WP-cost buttons | Choices panel | implemented |
| 282 | mechanical choice | 1 loot option(s) | Choices panel | implemented |
| 301 | mechanical choice | 1 combat preset(s) | Choices panel | implemented |
| 305 | mechanical choice | 1 loot option(s) | Choices panel | implemented |
