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
    }
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
        "your adventure ends",
        "your quest ends",
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
    report.append("Status: machine route-graph baseline. Human route-family names and story classifications still need review.")
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
    report.append("## Route-Family Starter Notes")
    report.append("")
    report.append("- Treat each section 1 target as an opening route family until human review gives it a story name.")
    report.append("- Treat success-capable branch points as the first checklist for route-family classification.")
    report.append("- Treat endpoint rows marked `needs_classification` as mandatory human-review stops.")
    report.append("- Route-only choices can stay on the book page; mechanical branches need support data or explicit manual notes.")
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
