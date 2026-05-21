#!/usr/bin/env python3
"""Dry-run Book 4 validation for the Grey Star assistant."""

from __future__ import annotations

import contextlib
import io
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


REPORT_PATH = ROOT / "testing" / "logs" / "GSBOOK4_PLAYTEST_REPORT.md"
BOOK_DIR = ROOT / "books" / "gs" / "04wotw"
SUCCESS_ROUTE = [
    1, 348, 326, 50, 239, 172, 257, 81, 169, 9, 217, 99, 201, 260, 298,
    10, 29, 76, 90, 98, 118, 193, 175, 252, 321, 282, 354, 343, 312, 300,
    254, 358, 242, 324, 347, 275, 351, 328, 191, 39, 92, 131, 180, 316, 360,
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
        path = self.resolve_save_path(path_text) if path_text.strip() else self.save_dir / "_dryrun-book4.json"
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


def prime(section: int = 1, *, cs: int = 42, end: int = 150, wp: int = 180) -> DryRunAssistant:
    assistant = DryRunAssistant()
    assistant.state = greystar.normalize_state(greystar.default_state())
    assistant.character["Name"] = "QA Grey Star"
    assistant.character["BookNumber"] = 4
    assistant.character["CombatSkillBase"] = cs
    assistant.character["CombatSkillCurrent"] = cs
    assistant.character["EnduranceMax"] = end
    assistant.character["EnduranceCurrent"] = end
    assistant.character["WillpowerCurrent"] = wp
    assistant.character["WillpowerBase"] = wp
    assistant.character["LesserMagicks"] = list(greystar.LESSER_MAGICKS)
    assistant.character["HigherMagicks"] = list(greystar.HIGHER_MAGICKS)
    assistant.inventory["Weapons"] = ["Wizard's Staff", "Broadsword"]
    assistant.inventory["BackpackItems"] = [
        "Meal",
        "Meal",
        "Coil of Rope",
        "Tinderbox",
        "Pestle and Mortar",
        "Empty Vial",
    ]
    assistant.inventory["SpecialItems"] = [
        "Map of the Shadakine Empire",
        "Magic Talisman",
        "Silver Charm of Jnana the Wise",
        "Jewelled Dagger",
        "Mind Gem",
        "Moonstone",
    ]
    assistant.inventory["HasHerbPouch"] = True
    assistant.inventory["HerbPouchItems"] = [
        "Empty Vial",
        "Potion of Invulnerability",
        "Potion of Laumspur (+6 END)",
    ]
    assistant.state["SectionHistory"] = []
    assistant.state["CurrentBookStats"] = {
        "BookNumber": 4,
        "BookTitle": greystar.BOOKS[4]["Title"],
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


def combat_round_tokens(assistant: DryRunAssistant, roll: int = 9, wp: int = 1) -> list[str]:
    if assistant.combat_uses_magical_staff():
        return ["combat", "round", str(wp), str(roll)]
    return ["combat", "round", str(roll)]


def run_source_integrity(result: Result) -> None:
    missing = [section for section in range(1, 361) if not (BOOK_DIR / f"sect{section}.htm").exists()]
    result.check(not missing, "All 360 Book 4 section files exist.", f"Missing section files: {missing}")

    bad_links: list[str] = []
    graph: dict[int, list[int]] = {}
    for section in range(1, 361):
        _, links = section_text_and_links(section)
        graph[section] = links
        for target in links:
            if target < 1 or target > 360 or not (BOOK_DIR / f"sect{target}.htm").exists():
                bad_links.append(f"{section}->{target}")
    result.check(not bad_links, "Every Book 4 source link points to an existing section.", f"Bad links: {bad_links[:10]}")

    seen = {1}
    queue: deque[int] = deque([1])
    while queue:
        current = queue.popleft()
        for target in graph[current]:
            if target not in seen:
                seen.add(target)
                queue.append(target)
    unreachable = sorted(set(range(1, 361)) - seen)
    result.check(not unreachable, "All Book 4 sections are reachable from section 1 in the source graph.", f"Unexpected unreachable sections: {unreachable}")


def run_data_surface(result: Result) -> None:
    assistant = prime()
    result.check("4" in assistant.section_automation, "Book 4 automation data loads.", "Book 4 automation data did not load.")
    result.check("4" in assistant.section_flows, "Book 4 flow data loads.", "Book 4 flow data did not load.")

    combat_sections: list[int] = []
    roll_sections: list[int] = []
    for section in range(1, 361):
        text, _ = section_text_and_links(section)
        if re.search(r"COMBAT SKILL\s+\d+\s+ENDURANCE\s+\d+", text, flags=re.IGNORECASE):
            combat_sections.append(section)
        if "Random Number Table" in text or "pick a number" in text.lower():
            roll_sections.append(section)

    flow = assistant.section_flows.get("4", {})
    missing_combat = [section for section in combat_sections if not flow.get(str(section), {}).get("combat")]
    missing_rolls = [section for section in roll_sections if not flow.get(str(section), {}).get("roll")]
    result.check(not missing_combat, f"All {len(combat_sections)} detected Book 4 combat sections have presets.", f"Missing combat presets: {missing_combat}")
    result.check(not missing_rolls, f"All {len(roll_sections)} detected Book 4 roll sections have helpers.", f"Missing roll helpers: {missing_rolls}")

    loot_buttons = sum(len(entry.get("loot", [])) for entry in flow.values() if isinstance(entry, dict))
    wp_buttons = sum(len(entry.get("wpCosts", [])) for entry in flow.values() if isinstance(entry, dict))
    result.check(loot_buttons >= 35, f"Book 4 exposes {loot_buttons} loot/item buttons.", f"Expected at least 35 loot buttons, found {loot_buttons}.")
    result.check(wp_buttons >= 20, f"Book 4 exposes {wp_buttons} WP-cost buttons.", f"Expected at least 20 WP-cost buttons, found {wp_buttons}.")


def run_simple_automations(result: Result) -> None:
    assistant = prime()
    entries = assistant.section_automation.get("4", {})
    failures: list[str] = []
    for section_text in sorted(entries, key=lambda value: int(value)):
        section = int(section_text)
        test = prime(section)
        messages, _ = capture(lambda test=test: test.apply_section_automation(force=True, visit_changed=True))
        if not messages:
            failures.append(section_text)
    result.check(not failures, f"Swept {len(entries)} Book 4 simple automation entries.", f"Automation entries produced no output: {failures[:12]}")


def run_rolls_and_items(result: Result) -> None:
    assistant = prime(4, end=20, wp=25)
    roll = assistant.evaluate_roll_flow(assistant.section_flow_entry(4, 4) or {}, 4)
    result.check(roll.get("Total") == 49 and roll.get("Route") == 16, "Section 4 WP+END roll routes to the six-pod result at total 49.", f"Unexpected section 4 roll: {roll}")
    roll = assistant.evaluate_roll_flow(assistant.section_flow_entry(4, 4) or {}, 5)
    result.check(roll.get("Total") == 50 and roll.get("Route") == 11, "Section 4 WP+END roll routes to the nine-pod result at total 50.", f"Unexpected section 4 roll: {roll}")

    assistant = prime(148)
    roll = assistant.evaluate_roll_flow(assistant.section_flow_entry(4, 148) or {}, 0)
    result.check(roll.get("Total", 0) >= 7 and roll.get("Route") == 55, "Section 148 applies item and Magick roll modifiers.", f"Unexpected section 148 roll: {roll}")

    assistant = prime(84)
    before = len(assistant.inventory["HerbPouchItems"])
    _, output = capture(lambda: assistant.apply_section_automation(force=True, visit_changed=True))
    result.check(
        assistant.automation_flags.get("invulnerabilityActive") is True
        and not assistant.has_item("Potion of Invulnerability", ["herb", "backpack"], "contains")
        and assistant.has_item("Empty Vial", ["herb", "backpack"], "contains"),
        "Potion of Invulnerability use removes the potion, returns a vial, and sets the protection flag.",
        f"Potion automation failed from {before} herb items: {output}",
    )

    assistant = prime(355)
    assistant.inventory["HerbPouchItems"].append("Phinomel Pods (9)")
    before_cs = assistant.character["CombatSkillCurrent"]
    _, output = capture(lambda: assistant.apply_flow_loot("leafwater-9"))
    result.check(
        assistant.character["CombatSkillCurrent"] == before_cs + 9
        and not assistant.has_item("Phinomel Pods", ["herb", "backpack"], "contains"),
        "Leafwater button removes Phinomel Pods and raises Combat Skill.",
        f"Leafwater failed: {output}",
    )

    assistant = prime(331, end=100)
    assistant.character["EnduranceCurrent"] = 80
    _, output = capture(lambda: assistant.apply_flow_loot("laumspur-potions"))
    result.check(
        assistant.has_item("Potion of Laumspur", ["herb", "backpack"], "contains"),
        "Book 4 herb-cache buttons add Laumspur potions.",
        f"Laumspur loot failed: {output}",
    )
    _, output = capture(lambda: assistant.use_item("herb", "Potion of Laumspur (+6 END)"))
    result.check(
        assistant.character["EnduranceCurrent"] == 86,
        "Potion of Laumspur (+6 END) restores 6 END when used.",
        f"Laumspur use failed: {output}",
    )


def run_combat_behaviour(result: Result) -> None:
    assistant = prime(111, cs=20, end=100, wp=100)
    _, output = capture(lambda: assistant.start_section_combat("111-winged"))
    assistant.combat["UseStaff"] = False
    found_roll = None
    for roll in range(10):
        ratio = assistant.combat_skill_for_round(1) - assistant.combat_effective_enemy_combat_skill()
        _, enemy_raw, player_raw = assistant.get_crt_result(ratio, roll)
        enemy_loss = assistant.loss_value(enemy_raw, int(assistant.combat["EnemyEnduranceCurrent"]))
        player_loss = assistant.loss_value(player_raw, int(assistant.character["EnduranceCurrent"]))
        if enemy_loss > player_loss > 0:
            found_roll = roll
            break
    if found_roll is None:
        result.fail("Could not find a CRT result to test conditional fly-by loss ignoring.")
    else:
        _, output = capture(lambda: assistant.combat_round(["combat", "round", str(found_roll)]))
        log = assistant.combat.get("Log", [{}])[-1]
        result.check(
            int(log.get("IgnoredPlayerLoss") or 0) > 0 and int(log.get("GreyStarLoss") or 0) == 0,
            "Fly-by combat can ignore Grey Star END loss when enemy loss is higher.",
            f"Conditional fly-by loss failed: {log} / {output}",
        )

    assistant = prime(270, cs=10, end=500, wp=100)
    _, output = capture(lambda: assistant.start_section_combat("270-demon-master"))
    assistant.combat["UseStaff"] = False
    for _ in range(4):
        if not assistant.combat.get("Active"):
            break
        capture(lambda: assistant.combat_round(["combat", "round", "0"]))
    result.check(
        int(assistant.state["CurrentSection"]) == 276,
        "Demon Master combat routes to section 276 when it lasts four rounds.",
        f"Demon Master route failed: section {assistant.state['CurrentSection']} / {output}",
    )

    assistant = prime(180)
    _, output = capture(lambda: assistant.apply_section_automation(force=True, visit_changed=True))
    result.check(
        "Wizard's Staff" not in assistant.inventory["Weapons"] and assistant.automation_flags.get("staffAvailable") is False,
        "Final Shasarak route removes the shattered Wizard's Staff.",
        f"Staff removal failed: {output}",
    )


def run_completion_and_achievements(result: Result) -> None:
    assistant = prime()
    for section in SUCCESS_ROUTE[1:]:
        capture(lambda section=section: assistant.set_section(section))
    result.check(assistant.book_completed(4), "Book 4 success route completes Book 4.", "Book 4 was not marked complete.")
    payload = assistant.book_completion_payload()
    result.check(payload.get("Active") is True and payload.get("CanContinue") is False, "Book 4 completion payload is final-book aware.", f"Unexpected completion payload: {payload}")

    unlocks = assistant.sync_achievements()
    unlocked_ids = {entry["Id"] for entry in unlocks} | assistant.achievement_unlocked_ids()
    expected = {"gs4_complete", "gs4_moonstone_bearer", "gs4_staff_shattered", "gs4_agarash_defied", "gs4_wizard_regent"}
    result.check(expected <= unlocked_ids, "Book 4 achievement sync/backfill unlocks final-route achievements.", f"Missing achievements: {sorted(expected - unlocked_ids)}")

    capture(lambda: assistant.repeat_completed_book())
    result.check(
        int(assistant.character["BookNumber"]) == 4
        and int(assistant.state["CurrentSection"]) == 1
        and int(assistant.character["EnduranceCurrent"]) == int(assistant.character["EnduranceMax"]),
        "Repeat Book 4 resets the final book to section 1 with restored END.",
        "Repeat Book 4 did not reset as expected.",
    )


def write_report(result: Result) -> None:
    lines = [
        "# GS Book 4 Playtest Report",
        "",
        f"Generated: {datetime.now().isoformat(timespec='seconds')}",
        "",
        "## Summary",
        "",
        f"- Passed: {len(result.passed)}",
        f"- Warnings: {len(result.warnings)}",
        f"- Failures: {len(result.failed)}",
        "",
    ]
    for title, values in (("Passed", result.passed), ("Warnings", result.warnings), ("Failures", result.failed)):
        lines.extend([f"## {title}", ""])
        if values:
            lines.extend(f"- {value}" for value in values)
        else:
            lines.append("- None")
        lines.append("")
    REPORT_PATH.write_text("\n".join(lines), encoding="utf-8")


def main() -> int:
    result = Result()
    run_source_integrity(result)
    run_data_surface(result)
    run_simple_automations(result)
    run_rolls_and_items(result)
    run_combat_behaviour(result)
    run_completion_and_achievements(result)
    write_report(result)
    print(f"Book 4 playtest report: {REPORT_PATH}")
    print(f"Passed: {len(result.passed)} | Warnings: {len(result.warnings)} | Failures: {len(result.failed)}")
    if result.failed:
        for failure in result.failed:
            print(f"FAIL: {failure}")
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
