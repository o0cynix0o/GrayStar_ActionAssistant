#!/usr/bin/env python3
"""Dry-run Book 2 validation for the Grey Star assistant.

These checks avoid the shared save pointer and current-position file. They cover
Book 2 source structure, automation data, flow buttons, combat presets,
achievements, completion, and repeat-book cleanup.
"""

from __future__ import annotations

import contextlib
import io
import json
import re
import sys
from collections import deque
from datetime import datetime
from html.parser import HTMLParser
from pathlib import Path
from typing import Any, Callable


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

import greystar  # noqa: E402


REPORT_PATH = ROOT / "testing" / "logs" / "GSBOOK2_PLAYTEST_REPORT.md"
BOOK_DIR = ROOT / "books" / "gs" / "02tfc"

SUCCESS_ROUTE = [
    1, 126, 257, 78, 235, 105, 61, 149, 200, 275, 144, 266, 276, 250, 53,
    287, 203, 159, 40, 211, 50, 22, 60, 214, 195, 111, 295, 72, 299, 66,
    291, 145, 120, 129, 52, 186, 294, 124, 254, 92, 84, 166, 307, 26, 284,
    76, 108, 38, 168, 240, 54, 103, 170, 148, 267, 23, 273, 85, 157, 272,
    229, 172, 310,
]


class TextParser(HTMLParser):
    def __init__(self) -> None:
        super().__init__()
        self.parts: list[str] = []

    def handle_data(self, data: str) -> None:
        if data.strip():
            self.parts.append(data.strip())


class DryRunAssistant(greystar.GreyStarAssistant):
    def __init__(self) -> None:
        super().__init__(save_dir=ROOT / "testing" / "dry-run-saves", data_dir=ROOT / "data")
        self.saved_state: dict[str, Any] | None = None

    def write_current_position(self) -> None:
        return

    def save_game(self, path_text: str = "", quiet: bool = False) -> bool:
        path = self.resolve_save_path(path_text) if path_text.strip() else self.save_dir / "_dryrun-book2.json"
        self.settings["SavePath"] = str(path)
        self.saved_state = greystar.json_clone(self.state)
        if not quiet:
            print(f"Dry-run save captured: {path}")
        return True


class Result:
    def __init__(self) -> None:
        self.passed: list[str] = []
        self.warnings: list[str] = []
        self.failed: list[str] = []

    def pass_(self, message: str) -> None:
        self.passed.append(message)

    def warn(self, message: str) -> None:
        self.warnings.append(message)

    def fail(self, message: str) -> None:
        self.failed.append(message)

    def check(self, condition: bool, ok: str, bad: str) -> None:
        if condition:
            self.pass_(ok)
        else:
            self.fail(bad)


def capture(func: Callable[[], Any]) -> tuple[Any, str]:
    buffer = io.StringIO()
    with contextlib.redirect_stdout(buffer):
        value = func()
    return value, buffer.getvalue().strip()


def section_text_and_links(section: int) -> tuple[str, list[int]]:
    source = (BOOK_DIR / f"sect{section}.htm").read_text(encoding="utf-8", errors="ignore")
    parser = TextParser()
    parser.feed(source)
    text = re.sub(r"\s+", " ", " ".join(parser.parts)).strip()
    links: list[int] = []
    for match in re.finditer(r"href=[\"']sect(\d+)\.htm", source, flags=re.IGNORECASE):
        target = int(match.group(1))
        if target not in links:
            links.append(target)
    return text, links


def prime(section: int = 1, *, cs: int = 40, end: int = 120, wp: int = 140) -> DryRunAssistant:
    assistant = DryRunAssistant()
    assistant.state = greystar.normalize_state(greystar.default_state())
    assistant.character["Name"] = "QA Grey Star"
    assistant.character["BookNumber"] = 2
    assistant.character["CombatSkillBase"] = cs
    assistant.character["CombatSkillCurrent"] = cs
    assistant.character["EnduranceMax"] = end
    assistant.character["EnduranceCurrent"] = end
    assistant.character["WillpowerCurrent"] = wp
    assistant.character["WillpowerBase"] = wp
    assistant.character["LesserMagicks"] = list(greystar.LESSER_MAGICKS)
    assistant.inventory["Weapons"] = ["Wizard's Staff", "Broadsword"]
    assistant.inventory["BackpackItems"] = ["Meal", "Meal", "Meal", "Coil of Rope", "Empty Vial"]
    assistant.inventory["SpecialItems"] = [
        "Map of the Shadakine Empire",
        "Magic Talisman",
        "Silver Charm of Jnana the Wise",
        "Black Rod",
        "Mind Gem",
        "Chaksu Pipes",
    ]
    assistant.inventory["HasHerbPouch"] = True
    assistant.inventory["HerbPouchItems"] = ["Empty Vial", "Azawood Leaf", "Azawood Leaf", "Azawood Leaf"]
    assistant.state["SectionHistory"] = []
    assistant.state["CurrentBookStats"] = {
        "BookNumber": 2,
        "BookTitle": greystar.BOOKS[2]["Title"],
        "StartSection": section,
        "LastSection": section,
        "SectionsVisited": 0,
        "VisitedSections": [],
        "StartingEnduranceMax": end,
        "StartingWillpower": wp,
    }
    assistant.state["CurrentSection"] = section
    assistant.record_section_visit()
    assistant.save_section_checkpoint("ready")
    return assistant


def run_source_integrity(result: Result) -> None:
    missing = [section for section in range(1, 311) if not (BOOK_DIR / f"sect{section}.htm").exists()]
    result.check(not missing, "All 310 Book 2 section files exist.", f"Missing section files: {missing}")

    bad_links: list[str] = []
    graph: dict[int, list[int]] = {}
    for section in range(1, 311):
        _, links = section_text_and_links(section)
        graph[section] = links
        for target in links:
            if target < 1 or target > 310 or not (BOOK_DIR / f"sect{target}.htm").exists():
                bad_links.append(f"{section}->{target}")
    result.check(not bad_links, "Every Book 2 source link points to an existing section.", f"Bad links: {bad_links[:10]}")

    seen = {1}
    queue: deque[int] = deque([1])
    while queue:
        current = queue.popleft()
        for target in graph[current]:
            if target not in seen:
                seen.add(target)
                queue.append(target)
    result.check(len(seen) == 310, "All 310 sections are reachable from section 1 through source links.", f"Reachable sections: {len(seen)}/310")


def run_data_surface(result: Result) -> None:
    assistant = prime()
    result.check("2" in assistant.section_automation, "Book 2 automation data loads.", "Book 2 automation data did not load.")
    result.check("2" in assistant.section_flows, "Book 2 flow data loads.", "Book 2 flow data did not load.")
    result.check("1" in assistant.section_automation and "1" in assistant.section_flows, "Book 1 data still loads after multi-book merge.", "Book 1 data missing after multi-book merge.")

    combat_sections = []
    roll_sections = []
    for section in range(1, 311):
        text, _ = section_text_and_links(section)
        if re.search(r"COMBAT SKILL\s+\d+\s+ENDURANCE\s+\d+", text, flags=re.IGNORECASE):
            combat_sections.append(section)
        if "Random Number Table" in text or "pick a number" in text.lower():
            roll_sections.append(section)
    flow = assistant.section_flows.get("2", {})
    missing_combat = [section for section in combat_sections if not flow.get(str(section), {}).get("combat")]
    missing_rolls = [section for section in roll_sections if not flow.get(str(section), {}).get("roll")]
    result.check(not missing_combat, f"All {len(combat_sections)} detected combat sections have combat presets.", f"Missing combat presets: {missing_combat}")
    result.check(not missing_rolls, f"All {len(roll_sections)} detected roll sections have roll helpers.", f"Missing roll helpers: {missing_rolls}")


def run_automation_sweep(result: Result) -> None:
    assistant = prime()
    entries = assistant.section_automation.get("2", {})
    tested = 0
    for raw_section in sorted(entries.keys(), key=lambda item: int(item)):
        local = prime()
        try:
            capture(lambda raw_section=raw_section, local=local: local.set_section(int(raw_section)))
            tested += 1
        except Exception as exc:
            result.fail(f"Section {raw_section} automation raised {type(exc).__name__}: {exc}")
    result.check(tested == len(entries), f"Simple automation sweep covered {tested} Book 2 sections.", "Simple automation sweep did not cover every entry.")


def run_flow_sweep(result: Result) -> None:
    assistant = prime()
    flows = assistant.section_flows.get("2", {})
    roll_tests = loot_tests = wp_tests = combat_tests = 0
    for raw_section, flow in sorted(flows.items(), key=lambda item: int(item[0])):
        section = int(raw_section)
        if isinstance(flow.get("roll"), dict):
            for raw in range(10):
                local = prime(section)
                try:
                    capture(lambda local=local, raw=raw: local.roll_current_section(raw))
                    roll_tests += 1
                except Exception as exc:
                    result.fail(f"Section {section} roll {raw} raised {type(exc).__name__}: {exc}")
        for option in greystar.as_list(flow.get("loot")):
            local = prime(section)
            try:
                capture(lambda local=local, option=option: local.apply_flow_loot(str(option.get("id") or "")))
                loot_tests += 1
            except Exception as exc:
                result.fail(f"Section {section} loot {option.get('id')} raised {type(exc).__name__}: {exc}")
        costs = greystar.as_list(flow.get("wpCosts"))
        if isinstance(flow.get("wpCost"), dict):
            costs.append(flow["wpCost"])
        for cost in costs:
            local = prime(section)
            try:
                capture(lambda local=local, cost=cost: local.pay_willpower_cost(int(cost.get("cost") or 0)))
                wp_tests += 1
            except Exception as exc:
                result.fail(f"Section {section} WP cost {cost.get('cost')} raised {type(exc).__name__}: {exc}")
        for preset in greystar.as_list(flow.get("combat")):
            local = prime(section)
            try:
                capture(lambda local=local, preset=preset: local.start_section_combat(str(preset.get("id") or "")))
                if local.combat.get("Active"):
                    combat_tests += 1
                else:
                    result.fail(f"Section {section} combat {preset.get('id')} did not start.")
            except Exception as exc:
                result.fail(f"Section {section} combat {preset.get('id')} raised {type(exc).__name__}: {exc}")

    result.check(roll_tests == 90, f"Roll helper sweep covered {roll_tests} outcomes.", f"Unexpected roll test count: {roll_tests}")
    result.check(loot_tests >= 15, f"Loot sweep covered {loot_tests} buttons.", f"Loot sweep only covered {loot_tests} buttons.")
    result.check(wp_tests >= 16, f"Willpower-cost sweep covered {wp_tests} buttons.", f"Willpower-cost sweep only covered {wp_tests} buttons.")
    result.check(combat_tests >= 19, f"Combat sweep started {combat_tests} presets.", f"Combat sweep only started {combat_tests} presets.")


def run_mechanic_edge_checks(result: Result) -> None:
    local = prime(99, cs=10, end=40, wp=40)
    capture(lambda: local.start_section_combat("99-shadakine-warrior"))
    capture(lambda: local.combat_round(["combat", "round", "1", "0"]))
    log = greystar.as_list(local.combat.get("Log"))
    result.check(bool(log) and int(log[-1].get("GreyStarLoss") or 0) == 0, "Section 99 ignores Grey Star END loss in round 1.", "Section 99 did not ignore round 1 END loss.")

    local = prime()
    local.inventory["BackpackItems"] = ["Meal", "Coil of Rope"]
    capture(lambda: local.set_section(297))
    result.check(not local.inventory["BackpackItems"] and not local.automation_flags.get("backpackAvailable"), "Section 297 discards Backpack contents and marks Backpack unavailable.", "Section 297 Backpack discard failed.")

    local = prime()
    capture(lambda: local.set_section(149))
    staff_missing = "Wizard's Staff" not in local.inventory["Weapons"]
    capture(lambda: local.set_section(200))
    staff_restored = "Wizard's Staff" in local.inventory["Weapons"]
    result.check(staff_missing and staff_restored, "Capture and release store and restore Staff/Backpack gear.", "Gear store/restore failed.")

    local = prime(45, end=20, wp=30)
    capture(lambda: local.apply_flow_loot("karmo-potion"))
    capture(lambda: local.use_item("herb", "Karmo Potion"))
    doubled = (
        int(local.character["EnduranceCurrent"]) == 40
        and int(local.character["WillpowerCurrent"]) == 60
        and bool(local.automation_flags.get("karmoPotionActive"))
        and bool(local.automation_flags.get("karmoSideEffectPending"))
        and local.has_item("Empty Vial", ["herb", "backpack"])
    )
    capture(lambda: local.roll_current_section(4))
    capture(lambda: local.apply_karmo_side_effect())
    capture(lambda: local.finish_karmo_potion())
    resolved = (
        int(local.character["EnduranceCurrent"]) == 18
        and int(local.character["WillpowerCurrent"]) == 30
        and not bool(local.automation_flags.get("karmoPotionActive"))
        and not bool(local.automation_flags.get("karmoSideEffectPending"))
    )
    result.check(
        doubled and resolved,
        "Karmo Potion use doubles END/WP, applies the side-effect roll, returns a vial, and halves after combat.",
        "Karmo Potion use/finish flow failed.",
    )


def run_completion_and_achievements(result: Result) -> None:
    local = prime()
    for section in SUCCESS_ROUTE:
        capture(lambda section=section: local.set_section(section))
    result.check(2 in greystar.as_list(local.character["CompletedBooks"]), "Success-route smoke completes Book 2.", "Book 2 did not complete on success-route smoke.")
    unlocks = local.sync_achievements(save=False)
    unlocked = local.achievement_unlocked_ids()
    expected = {"gs2_complete", "gs2_shadow_gate", "gs2_gear_taken", "gs2_gear_returned", "gs2_slave_breaker", "gs2_samu_oath"}
    result.check(expected.issubset(unlocked), f"Achievement sync/backfill unlocked expected Book 2 route set ({len(unlocks)} new in smoke).", f"Missing expected achievements: {sorted(expected - unlocked)}")

    before_count = len(unlocked)
    capture(lambda: local.repeat_completed_book())
    result.check(
        int(local.character["BookNumber"]) == 2
        and int(local.state["CurrentSection"]) == 1
        and len(local.achievement_unlocked_ids()) >= before_count,
        "Repeat Book 2 resets to section 1 and preserves achievements.",
        "Repeat Book 2 cleanup failed.",
    )


def write_report(result: Result) -> None:
    REPORT_PATH.parent.mkdir(parents=True, exist_ok=True)
    lines = [
        "# GS Book 2 Playtest Report",
        "",
        f"Generated: {datetime.now().isoformat(timespec='seconds')}",
        "",
        f"Passed: {len(result.passed)}",
        f"Warnings: {len(result.warnings)}",
        f"Failures: {len(result.failed)}",
        "",
        "## Passed",
        "",
    ]
    lines.extend(f"- {item}" for item in result.passed)
    lines.extend(["", "## Warnings", ""])
    lines.extend(f"- {item}" for item in result.warnings or ["None"])
    lines.extend(["", "## Failures", ""])
    lines.extend(f"- {item}" for item in result.failed or ["None"])
    lines.append("")
    REPORT_PATH.write_text("\n".join(lines), encoding="utf-8")


def main() -> int:
    result = Result()
    run_source_integrity(result)
    run_data_surface(result)
    run_automation_sweep(result)
    run_flow_sweep(result)
    run_mechanic_edge_checks(result)
    run_completion_and_achievements(result)
    write_report(result)
    print(f"Book 2 playtest report: {REPORT_PATH}")
    print(f"Passed: {len(result.passed)} | Warnings: {len(result.warnings)} | Failures: {len(result.failed)}")
    for failure in result.failed:
        print(f"FAIL: {failure}")
    return 1 if result.failed else 0


if __name__ == "__main__":
    raise SystemExit(main())
