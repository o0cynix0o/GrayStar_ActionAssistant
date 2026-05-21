#!/usr/bin/env python3
"""Generate route graph audit reports for Gray Star books."""

from __future__ import annotations

from collections import defaultdict, deque
from dataclasses import dataclass
from datetime import datetime
from html.parser import HTMLParser
from pathlib import Path
import json
import re
import sys
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

import garystar  # noqa: E402


LOG_DIR = ROOT / "testing" / "logs"
TMP_DIR = ROOT / "testing" / "tmp"

NO_INCOMING_NOTES = {
    1: {
        110: "Hidden correct riddle solution for section 264; the local source has no visible section link into it.",
        342: "Footnote says no choice leads here and calls it an oversight. Earlier dry-run smoke used this section manually, so that smoke route needs review.",
    },
    3: {
        190: "Footnote says no choice leads here and calls it an oversight. Section 144 is only reached from this unreachable section, so both should stay documented as source irregularities.",
    }
}

ROUTE_STATUS = {
    1: "machine route-graph baseline plus first named route-family pass. Endpoint classifications and full dry-run branch coverage still need review.",
    3: "machine route-graph baseline plus named route-family pass. Sections 144 and 190 are source irregularities called out by the local footnotes.",
}

BOOK_ROUTE_FAMILIES = {
    1: [
        [
            "Opening Elementalism Split",
            "1 -> 202, 1 -> 168",
            "The first route split from section 1.",
            "Both opening branches are success-capable and merge into the wider graph early. Keep this as a smoke check that both starts can still reach section 350.",
            "No unique achievement yet; use for route reachability testing.",
        ],
        [
            "Early Survival And Travel",
            "2, 3, 58, 59, 78, 168",
            "Early mainland movement, food pressure, rest, and resource recovery/loss.",
            "This family catches Meal handling, END/WP adjustments, Fresh Laumspur handling, and the early \"did the assistant stay in sync?\" checks.",
            "Meal automation, Laumspur use/eat controls, WP/END quick controls.",
        ],
        [
            "Kazim Stone Route",
            "77, 10, 51, 175, 191, 314, 320, 323",
            "The optional Kazim Stone arc and its consequences.",
            "Section 77 adds the Stone. Section 10 detects possession. Section 51 removes it. Sections 314/320/323 apply heavy WP/END costs and gated choices.",
            "`gs1_kazim_claimed`, `gs1_kazim_stolen`; item add/remove automation for Kazim Stone; WP can go negative when forced by the book.",
        ],
        [
            "Shianti / Jnana Blessing Route",
            "87, 126, 161, 49, 274",
            "The benevolent-helper route through Jnana and the Silver Charm.",
            "Section 87 can award the Amulet. Section 161 can award Jnana loot. The Silver Charm modifies the section 49 ravine roll and can lead to the section 274 leap result.",
            "`gs1_priests_amulet`, `gs1_jnanas_blessing`, `gs1_leap_of_faith`; loot picker and random-number modifier testing.",
        ],
        [
            "Alchemy / Yabari / Ezeran Route",
            "65, 72, 151, 193, 297",
            "Alchemy supplies, poison/ointment protection, and Ezeran Acid creation.",
            "Section 193 is the main alchemy cache. Sections 65/72 track Yabari protection. Section 151 checks ingredients; section 297 converts ingredients and an empty vial into Ezeran Acid.",
            "`gs1_yabari_ward`, `gs1_alchemy_cache`, `gs1_ezeran_acid`; recipe conversion and ointment in-use flag.",
        ],
        [
            "Redeemer / Rune Riddle Route",
            "18, 209, 264, hidden 110",
            "The Redeemer item route and the hidden riddle answer route.",
            "Section 209 supplies the Medallion and Pink Liquid. Section 264 consumes the liquid and can route to hidden answer section 110, which has no visible source link.",
            "`gs1_redeemers_tokens`; loot picker, item gate, hidden-section route note.",
        ],
        [
            "Najin Route",
            "58, 101, 126, 130",
            "The Najin approach choice and survival fight.",
            "Section 58 presents attack/wait choices. Section 101 is a survival combat that can resolve to 130. Section 126 can lead toward Jnana instead.",
            "`gs1_najin_standoff`; multi-enemy/survival combat testing.",
        ],
        [
            "Kleasa / Sorcery Shield Route",
            "90, 139, 149, 165",
            "The Sorcery shield setup and the Kleasa limited combat.",
            "Section 139 marks the shield active for section 149. Section 149 drains WP every round and drains less END when the shield is active. Section 165 clears the survival gate.",
            "`gs1_kleasa_survivor`, `gs1_shield_raised`, `gs1_no_shield_no_problem`; combat per-round extras and temporary shield flag.",
        ],
        [
            "Correct Key / Door Route",
            "142, 159, 170, 205, 214, 235, 286",
            "The key/door section cluster and its random-number fork.",
            "Section 286 checks Psychomancy first; otherwise it uses an even/odd random result: even to 214, odd to 205. Several routes in this cluster depend on items, Sorcery, or Prophecy.",
            "`gs1_correct_key`; random-number outcome testing and item/Magick gates.",
        ],
        [
            "Quoku Route",
            "57, 107, 231, 281, 307, 331, 337",
            "Quoku encounters, staff attacks, and the large-Quoku threshold fight.",
            "Section 281 is the special one-round fight: after one round, WP >= 10 routes to 331, otherwise 32. Other Quoku sections test combat modifiers and no-evade fights.",
            "`gs1_quoku_breakthrough`; one-round combat, CS modifiers, WP threshold routing.",
        ],
        [
            "Gear Loss / Recovery Route",
            "Gear loss: 291, 300, 311; recovery: 221, 245; setup: 349",
            "Backpack/Staff unavailable state and later recovery.",
            "The app must snapshot carried gear when the book removes equipment, keep the unavailable state active, and restore it when section 221 or 245 is reached.",
            "`gs1_gear_taken`, `gs1_gear_recovered`; full inventory snapshot/restore testing.",
        ],
        [
            "Shan / Tanith Companion Route",
            "276, 294, 335, 349, 245",
            "Companion separation, sacrifice, and recovery story beats.",
            "Section 276 records Tanith's sacrifice. Sections 294/335 mark the lone-road state. Section 349 can lead into gear recovery through Tanith.",
            "`gs1_tanith_sacrifice`, `gs1_lone_road`; companion-state notes and final-summary coverage.",
        ],
        [
            "Final Ascent Route",
            "340, 298, 350",
            "The late-game success spine into the Book 1 completion screen.",
            "These sections should remain the canonical completion route family for final save summaries, Book 2 handoff, and repeat-book behavior.",
            "`gs1_final_ascent`, `gs1_complete`; complete-book screen, summary, repeat-book reset.",
        ],
        [
            "Failure / Death Endpoint Families",
            "9, 14, 17, 20, 63, 67, 69, 92, 103, 122, 138, 155, 173, 177, 207, 216, 220, 225, 237, 262, 299, 306, 312, 315, 316, 317, 318, 324",
            "The terminal failure leaves detected by the route graph.",
            "Most are death/failure endpoints; sections 92, 262, 315, and 318 still need human text classification before the report should call them final.",
            "Death screen, rewind/repeat handling, route-family endpoint classification.",
        ],
        [
            "Source Irregularities",
            "110, 342",
            "Sections that need special handling outside normal link traversal.",
            "Section 110 is a hidden riddle solution. Section 342 is called out by the source footnote as unreachable by normal choices, so route tests should not treat it as a legal path unless entered manually for oversight handling.",
            "Hidden-route note for 110; unreachable-section marker for 342.",
        ],
    ],
    3: [
        [
            "Opening: Neverness To Crystal Tower",
            "1, 122, 211, 167, 302",
            "The first push across the cloud plain and toward the Crystal Tower.",
            "Both opening choices can still reach the Moonstone. Use this family to make sure the Book 3 start remains playable from either branch.",
            "Opening route links, early Willpower costs, Crystal Tower approach choices.",
        ],
        [
            "Crystal Tower Key Route",
            "56, 10, 150, 197, 240, 242, 252, 287",
            "The five animal keys and the riddle that points to the Serpent Key.",
            "Wrong keys are dangerous but useful replay territory. The Serpent Key opens the tower, while the other keys create story, combat, and item branches.",
            "`gs3_keybearer`, `gs3_serpent_solution`; key loot buttons, poison damage, animal-key combat and route checks.",
        ],
        [
            "Ethetron And Singing City Route",
            "116, 135, 140, 19, 45, 238, 241, 259",
            "The flying-machine route into the realm of the Elessin.",
            "This family covers the Gyronome, Ethetron item choices, landing rolls, and the first real arrival in the Singing City.",
            "`gs3_ethetron_pilot`, `gs3_singing_city`; roll helpers, loot picker, Gyronome item.",
        ],
        [
            "Elessin Judgment And Gear Trouble",
            "191, 107, 182, 344, 278",
            "Weapon confiscation, weapon return, Backpack stashing, and Backpack recovery.",
            "Book 3 separates weapon-only confiscation from Backpack stashing, so route tests need to verify the two states do not overwrite each other.",
            "`gs3_weapons_taken`, `gs3_weapons_returned`, `gs3_ethetron_stash`, `gs3_ethetron_recovery`; weapon and Backpack state automation.",
        ],
        [
            "Screaming God / Guardian Route",
            "4, 22, 44, 55, 115, 182",
            "The route around the statue of the Screaming God and the Guardian's warning.",
            "This is a major story branch and a good replay target. It also creates END-based roll checks while carrying the statue.",
            "`gs3_guardians_song`; END roll helpers, Guardian route notes.",
        ],
        [
            "Chaos-Bird Route",
            "64, 78, 108, 133, 188, 290, 304",
            "The Ethetron attack by Chaos-birds.",
            "This family tests flying combat, Elementalism cost, a WP-based crash roll, and the optional Tanith weapon aid.",
            "`gs3_chaos_bird_survivor`; combat presets, roll helpers, status flag.",
        ],
        [
            "Paradox And Tanith Rescue",
            "12, 67, 207, 213, 253, 276, 288, 314",
            "The strange bargain route and the effort to free Tanith from enchantment.",
            "This is the emotional center of the book. It is also a steady Willpower drain, so it needs careful automation and achievement backfill.",
            "`gs3_paradox_bargain`, `gs3_tanith_rescued`; chained WP costs and route achievements.",
        ],
        [
            "Vale And Healing Route",
            "216, 177, 293, 324, 338",
            "The gentler recovery stretch in the valley.",
            "This family is the best place to verify healing, Senara buds, Senara potions, and rest bonuses.",
            "`gs3_senara_brewer`; healing automations and consumable item use.",
        ],
        [
            "Jahksa / Shadow Brother Route",
            "291, 123, 131, 249, 148, 300, 243, 350",
            "Grey Star's dark double and the final Moonstone fight.",
            "The final combat is unusual: losing the fight can lead to the successful ending. This family needs a dedicated combat test.",
            "`gs3_shadow_brother`, `gs3_final_truth`, `gs3_moonstone_claimed`; defeat-route combat and completion screen.",
        ],
        [
            "Failure / Death Endpoint Families",
            "7, 28, 40, 53, 63, 71, 80, 81, 83, 104, 109, 126, 129, 164, 165, 168, 189, 203, 233, 269, 270, 271, 272, 286, 292, 308, 328, 349",
            "Terminal failure leaves detected in the Book 3 graph.",
            "These are the endpoints the death screen and rewind/repeat flow should handle.",
            "Death/failure automation and route endpoint coverage.",
        ],
        [
            "Source Irregularities",
            "144, 190",
            "Sections called out by the local footnotes as unreachable by normal choices.",
            "Section 190 has no incoming source link, and section 144 is only reached through 190. Keep them documented, but do not treat them as legal route coverage.",
            "Route-audit notes only.",
        ],
    ],
}

BOOK_ROUTE_TESTING_NOTES = {
    1: [
        "The named families above should drive playtest scripts: each family needs at least one success-capable dry run and, where practical, one failure/alternate run.",
        "The old Book 1 success-route smoke is useful for mechanics, but it is not a source-link proof because it used manual jumps through sections such as 342. Rebuild that smoke from this route-family table before using it as route evidence.",
        "Branches in this book are merge-heavy. A route family can share most of its later path with another family, so coverage should track sections, state changes, achievements, and endpoint behavior rather than only one complete route string.",
    ],
    3: [
        "Both opening branches can reach section 350, but the path merges often. Use route-family coverage plus mechanic coverage rather than trying to name every possible full path.",
        "Sections 144 and 190 are source irregularities from the local footnotes and should not be counted as missed legal player routes.",
        "The final combat at section 243 needs special testing because combat defeat routes to the successful ending at section 350.",
    ],
}


class TextParser(HTMLParser):
    def __init__(self) -> None:
        super().__init__()
        self.parts: list[str] = []

    def handle_data(self, data: str) -> None:
        stripped = data.strip()
        if stripped:
            self.parts.append(stripped)


@dataclass(frozen=True)
class SectionInfo:
    section: int
    exists: bool
    text: str
    links: tuple[int, ...]
    tags: tuple[str, ...]


def section_path(book_number: int, section: int) -> Path:
    book = garystar.BOOKS[book_number]
    return ROOT / "books" / "gs" / book["Folder"] / f"sect{section}.htm"


def clean_text(source: str) -> str:
    parser = TextParser()
    parser.feed(source)
    return re.sub(r"\s+", " ", " ".join(parser.parts)).strip()


def unique_links(source: str) -> tuple[int, ...]:
    links: list[int] = []
    for match in re.finditer(r"href=[\"']sect(\d+)\.htm", source, flags=re.IGNORECASE):
        target = int(match.group(1))
        if target not in links:
            links.append(target)
    return tuple(links)


def tags_for_text(text: str, links: tuple[int, ...]) -> tuple[str, ...]:
    lower = text.lower()
    tags: list[str] = []
    checks = [
        ("branch", len(links) >= 2),
        ("leaf", not links),
        ("combat", "you must fight" in lower or ("combat skill" in lower and "endurance" in lower)),
        ("random", "random number table" in lower),
        ("magick_check", "magical power" in lower or "power of" in lower),
        ("item_gate", any(phrase in lower for phrase in ("if you possess", "if you have", "if you do not have", "if you lack"))),
        ("wp", "willpower" in lower),
        ("endurance", "endurance" in lower),
        ("meal", "meal" in lower or "provision" in lower),
        ("loot", any(phrase in lower for phrase in ("mark ", "add ", "you may take", "you find", "record "))),
        ("gear_loss", any(word in lower for word in ("confiscat", "discard", "lose your backpack", "lost your backpack", "stored"))),
    ]
    for tag, condition in checks:
        if condition:
            tags.append(tag)
    return tuple(tags)


def death_or_failure_text(text: str) -> bool:
    lower = text.lower()
    phrases = [
        "your life and your quest end",
        "your life and adventure end",
        "your life and adventure ends",
        "your life and your adventure end",
        "your life and your adventure ends",
        "your adventure ends",
        "your quest ends",
        "your quest and your life end",
        "your quest and your life are now over",
        "your life and quest end",
        "your quest and your adventure end",
        "your life and your quest are now over",
        "your life and your quest are over",
        "your quest has failed and your adventure is over",
        "your quest is over",
        "you have failed",
        "you are dead",
        "you die",
        "you perish",
        "death is instantaneous",
        "you fall to your death",
    ]
    return any(phrase in lower for phrase in phrases)


def classify_endpoint(book_number: int, info: SectionInfo) -> str:
    if info.links:
        return "not_endpoint"
    max_section = int(garystar.BOOKS[book_number]["MaxSection"])
    lower = info.text.lower()
    if info.section == max_section:
        return "success"
    if "the forbidden city" in lower and book_number == 1:
        return "success"
    if "beyond the nightmare gate" in lower and book_number == 2:
        return "success"
    if death_or_failure_text(info.text):
        return "death_or_failure"
    return "needs_classification"


def read_book(book_number: int) -> dict[int, SectionInfo]:
    max_section = int(garystar.BOOKS[book_number]["MaxSection"])
    result: dict[int, SectionInfo] = {}
    for section in range(1, max_section + 1):
        path = section_path(book_number, section)
        if not path.exists():
            result[section] = SectionInfo(section, False, "", tuple(), ("missing",))
            continue
        source = path.read_text(encoding="utf-8", errors="ignore")
        links = unique_links(source)
        text = clean_text(source)
        result[section] = SectionInfo(section, True, text, links, tags_for_text(text, links))
    return result


def bfs(start: int, graph: dict[int, tuple[int, ...]]) -> set[int]:
    seen = {start}
    queue: deque[int] = deque([start])
    while queue:
        node = queue.popleft()
        for target in graph.get(node, tuple()):
            if target not in seen:
                seen.add(target)
                queue.append(target)
    return seen


def shortest_path(start: int, target: int, graph: dict[int, tuple[int, ...]]) -> list[int]:
    queue: deque[int] = deque([start])
    parents: dict[int, int | None] = {start: None}
    while queue:
        node = queue.popleft()
        if node == target:
            break
        for nxt in graph.get(node, tuple()):
            if nxt not in parents:
                parents[nxt] = node
                queue.append(nxt)
    if target not in parents:
        return []
    path: list[int] = []
    node: int | None = target
    while node is not None:
        path.append(node)
        node = parents[node]
    return list(reversed(path))


def reverse_graph(graph: dict[int, tuple[int, ...]]) -> dict[int, tuple[int, ...]]:
    incoming: dict[int, list[int]] = defaultdict(list)
    for source, targets in graph.items():
        for target in targets:
            incoming[target].append(source)
    return {key: tuple(value) for key, value in incoming.items()}


def dominators(start: int, reachable: set[int], graph: dict[int, tuple[int, ...]]) -> dict[int, set[int]]:
    reverse = reverse_graph(graph)
    dom: dict[int, set[int]] = {node: set(reachable) for node in reachable}
    dom[start] = {start}
    changed = True
    while changed:
        changed = False
        for node in sorted(reachable):
            if node == start:
                continue
            preds = [pred for pred in reverse.get(node, tuple()) if pred in reachable]
            if not preds:
                new_value = {node}
            else:
                common = set(dom[preds[0]])
                for pred in preds[1:]:
                    common &= dom[pred]
                new_value = common | {node}
            if new_value != dom[node]:
                dom[node] = new_value
                changed = True
    return dom


def compact_list(values: list[int] | tuple[int, ...], limit: int = 24) -> str:
    items = list(values)
    if not items:
        return "None"
    if len(items) <= limit:
        return ", ".join(str(item) for item in items)
    head = ", ".join(str(item) for item in items[:limit])
    return f"{head}, ... (+{len(items) - limit} more)"


def table_rows(rows: list[list[Any]]) -> list[str]:
    return ["| " + " | ".join(str(cell) for cell in row) + " |" for row in rows]


def branch_row(section: int, info: SectionInfo, success_reachable: set[int]) -> list[Any]:
    success_targets = [target for target in info.links if target in success_reachable]
    dead_targets = [target for target in info.links if target not in success_reachable]
    return [
        section,
        ", ".join(str(target) for target in info.links),
        "yes" if section in success_reachable else "no",
        compact_list(success_targets, 8),
        compact_list(dead_targets, 8),
        ", ".join(info.tags),
    ]


def audit_book(book_number: int) -> tuple[str, dict[str, Any]]:
    book = garystar.BOOKS[book_number]
    max_section = int(book["MaxSection"])
    infos = read_book(book_number)
    graph = {section: info.links for section, info in infos.items() if info.exists}
    existing = sorted(section for section, info in infos.items() if info.exists)
    missing = sorted(section for section, info in infos.items() if not info.exists)
    bad_links = sorted(
        (section, target)
        for section, links in graph.items()
        for target in links
        if target < 1 or target > max_section or target not in infos or not infos[target].exists
    )
    reachable = bfs(1, graph) if 1 in graph else set()
    unreachable = sorted(set(existing) - reachable)
    reverse = reverse_graph(graph)
    no_incoming = sorted(section for section in existing if section != 1 and not reverse.get(section))
    endpoints = [(section, classify_endpoint(book_number, infos[section])) for section in existing if not infos[section].links]
    success_sections = [section for section, kind in endpoints if kind == "success"]
    success = success_sections[0] if success_sections else max_section
    success_path = shortest_path(1, success, graph)
    can_reach_success = bfs(success, reverse) if success in graph else set()
    success_reachable = reachable & can_reach_success
    branch_points = sorted(section for section in reachable if len(graph.get(section, tuple())) >= 2)
    success_branch_points = [section for section in branch_points if section in success_reachable]
    doms = dominators(1, reachable, graph) if reachable else {}
    success_dominators = sorted(doms.get(success, set())) if success in reachable else []
    opening_branches: list[list[Any]] = []
    for target in graph.get(1, tuple()):
        target_reachable = bfs(target, graph)
        target_endpoints = sorted(section for section, _ in endpoints if section in target_reachable)
        shared_with_other_opening = set()
        for other in graph.get(1, tuple()):
            if other == target:
                continue
            shared_with_other_opening |= target_reachable & bfs(other, graph)
        opening_branches.append(
            [
                f"1 -> {target}",
                len(target_reachable),
                "yes" if success in target_reachable else "no",
                compact_list(target_endpoints, 16),
                compact_list(sorted(shared_with_other_opening)[:16], 16),
            ]
        )

    report: list[str] = []
    report.append(f"# GS Book {book_number} Route Audit")
    report.append("")
    report.append(f"Generated: {datetime.now().isoformat(timespec='seconds')}")
    report.append("")
    report.append(f"Book: {book['Title']}")
    report.append("")
    report.append(
        "Status: "
        + ROUTE_STATUS.get(
            book_number,
            "machine route-graph baseline. Human route-family names and story classifications still need review.",
        )
    )
    report.append("")
    report.append("## Summary")
    report.append("")
    summary_rows = [
        ["Metric", "Value"],
        ["Expected sections", max_section],
        ["Existing section files", len(existing)],
        ["Missing section files", compact_list(missing)],
        ["Source edges", sum(len(links) for links in graph.values())],
        ["Bad source links", compact_list([f"{source}->{target}" for source, target in bad_links])],
        ["Reachable from section 1", f"{len(reachable)}/{len(existing)}"],
        ["Unreachable from section 1", compact_list(unreachable)],
        ["No incoming links", compact_list(no_incoming)],
        ["Endpoint sections", len(endpoints)],
        ["Branch points", len(branch_points)],
        ["Success-capable branch points", len(success_branch_points)],
        ["Detected success section", success],
    ]
    report.extend(table_rows(summary_rows[:1]))
    report.append("|---|---|")
    report.extend(table_rows(summary_rows[1:]))
    report.append("")
    report.append("## Shortest Success Path")
    report.append("")
    if success_path:
        report.append(f"- Length: {len(success_path)} sections")
        report.append(f"- Path: {compact_list(success_path, 80)}")
    else:
        report.append("- No source-link path to the detected success section was found.")
    report.append("")
    report.append("## Mandatory Success Chokepoints")
    report.append("")
    report.append("These sections dominate the detected success endpoint in the source-link graph. They are route-graph chokepoints, not proof that every legal state can pass through them.")
    report.append("")
    report.append(f"- Count: {len(success_dominators)}")
    report.append(f"- Sections: {compact_list(success_dominators, 80)}")
    report.append("")
    report.append("## Opening Branches")
    report.append("")
    report.extend(table_rows([["Branch", "Reachable Sections", "Can Reach Success", "Reachable Endpoints", "Early Merge Examples"]]))
    report.append("|---|---:|---|---|---|")
    report.extend(table_rows(opening_branches))
    report.append("")
    if no_incoming:
        report.append("## No-Incoming Review Notes")
        report.append("")
        notes = NO_INCOMING_NOTES.get(book_number, {})
        report.extend(table_rows([["Section", "Route Audit Note"]]))
        report.append("|---:|---|")
        for section in no_incoming:
            report.extend(table_rows([[section, notes.get(section, "Needs human review.")]]))
        report.append("")
    route_families = BOOK_ROUTE_FAMILIES.get(book_number, [])
    if route_families:
        report.append("## Player-Facing Route Families")
        report.append("")
        report.append(
            "These names collapse the success-capable branch points into routes a player or tester can reason about. "
            "A family is not always a single exclusive path; many branches merge back into the main graph, "
            "so these are route themes with important entry sections, state changes, and test hooks."
        )
        report.append("")
        report.extend(
            table_rows(
                [
                    [
                        "Route Family",
                        "Entry / Trigger Sections",
                        "What It Represents",
                        "Route Stakes / Notes",
                        "Achievement / App Hooks",
                    ]
                ]
            )
        )
        report.append("|---|---|---|---|---|")
        report.extend(table_rows(route_families))
        report.append("")
        route_testing_notes = BOOK_ROUTE_TESTING_NOTES.get(book_number, [])
        if route_testing_notes:
            report.append("## Route Testing Notes")
            report.append("")
            for note in route_testing_notes:
                report.append(f"- {note}")
            report.append("")
    report.append("## Endpoint Inventory")
    report.append("")
    report.extend(table_rows([["Section", "Classification", "Reachable", "Tags", "Shortest Path"]]))
    report.append("|---:|---|---|---|---|")
    endpoint_rows: list[list[Any]] = []
    for section, kind in endpoints:
        path = shortest_path(1, section, graph) if section in reachable else []
        endpoint_rows.append(
            [
                section,
                kind,
                "yes" if section in reachable else "no",
                ", ".join(infos[section].tags),
                compact_list(path, 24) if path else "None",
            ]
        )
    report.extend(table_rows(endpoint_rows))
    report.append("")
    report.append("## Success-Capable Branch Points")
    report.append("")
    report.append("These are branch sections reachable from section 1 that can still reach the detected success ending.")
    report.append("")
    report.extend(table_rows([["Section", "Targets", "Can Reach Success", "Success Targets", "Non-success Targets", "Tags"]]))
    report.append("|---:|---|---|---|---|---|")
    report.extend(table_rows([branch_row(section, infos[section], success_reachable) for section in success_branch_points]))
    report.append("")
    report.append("## Other Reachable Branch Points")
    report.append("")
    other_branches = [section for section in branch_points if section not in success_reachable]
    if other_branches:
        report.extend(table_rows([["Section", "Targets", "Can Reach Success", "Success Targets", "Non-success Targets", "Tags"]]))
        report.append("|---:|---|---|---|---|---|")
        report.extend(table_rows([branch_row(section, infos[section], success_reachable) for section in other_branches]))
    else:
        report.append("- None")
    report.append("")
    if route_families:
        report.append("## Route-Family Maintenance Notes")
        report.append("")
        report.append("- Keep the named route-family table in sync with section audit changes and assistant automation data.")
        report.append("- Rebuild route-smoke scripts from the named families before treating them as source-link proof.")
        report.append("- Endpoint rows marked `needs_classification` remain mandatory human-review stops.")
        report.append("- Route-only choices can stay on the book page; mechanical branches need support data or explicit manual notes.")
    else:
        report.append("## Route-Family Starter Notes")
        report.append("")
        report.append("- Treat each section 1 target as an opening route family until human review gives it a story name.")
        report.append("- Treat success-capable branch points as the first checklist for route-family classification.")
        report.append("- Treat endpoint rows marked `needs_classification` as mandatory human-review stops.")
        report.append("- Route-only choices can stay on the book page; mechanical branches need support data or explicit manual notes.")
    report.append("")
    while report and not report[-1]:
        report.pop()

    artifact = {
        "bookNumber": book_number,
        "bookTitle": book["Title"],
        "maxSection": max_section,
        "existing": existing,
        "missing": missing,
        "badLinks": bad_links,
        "reachable": sorted(reachable),
        "unreachable": unreachable,
        "noIncoming": no_incoming,
        "endpoints": [{"section": section, "classification": kind} for section, kind in endpoints],
        "success": success,
        "successPath": success_path,
        "successDominators": success_dominators,
        "branchPoints": branch_points,
        "successBranchPoints": success_branch_points,
        "graph": {str(section): list(links) for section, links in sorted(graph.items())},
        "tags": {str(section): list(info.tags) for section, info in sorted(infos.items()) if info.exists},
    }
    return "\n".join(report), artifact


def main(argv: list[str]) -> int:
    if argv:
        books = [int(value) for value in argv]
    else:
        books = [1, 2]
    LOG_DIR.mkdir(parents=True, exist_ok=True)
    TMP_DIR.mkdir(parents=True, exist_ok=True)
    for book_number in books:
        report, artifact = audit_book(book_number)
        report_path = LOG_DIR / f"GSBOOK{book_number}_ROUTE_AUDIT.md"
        artifact_path = TMP_DIR / f"gsbook{book_number}_route_graph.json"
        report_path.write_text(report + "\n", encoding="utf-8")
        artifact_path.write_text(json.dumps(artifact, indent=2) + "\n", encoding="utf-8")
        print(f"Book {book_number} route audit: {report_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
