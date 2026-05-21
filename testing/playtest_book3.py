#!/usr/bin/env python3
"""Dry-run Book 3 validation for the Grey Star assistant.

The checks use disposable in-memory saves and avoid the live campaign pointer.
They cover source structure, automation data, flow buttons, Book 3-specific
gear handling, final-combat routing, achievements, completion, and repeat-book
cleanup.
"""

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


REPORT_PATH = ROOT / "testing" / "logs" / "GSBOOK3_PLAYTEST_REPORT.md"
BOOK_DIR = ROOT / "books" / "gs" / "03btng"

SUCCESS_ROUTE = [
    1, 211, 167, 302, 70, 264, 217, 246, 172, 91, 17, 250, 282, 116, 135,
    140, 19, 13, 26, 45, 238, 241, 259, 245, 182, 278, 314, 14, 187, 94,
    309, 20, 249, 148, 300, 216, 293, 324, 228, 201, 183, 169, 330, 338,
    247, 215, 194, 51, 33, 75, 78, 304, 325, 341, 47, 275, 243, 350,
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
        path = self.resolve_save_path(path_text) if path_text.strip() else self.save_dir / "_dryrun-book3.json"
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


def prime(section: int = 1, *, cs: int = 40, end: int = 140, wp: int = 160) -> DryRunAssistant:
    assistant = DryRunAssistant()
    assistant.state = greystar.normalize_state(greystar.default_state())
    assistant.character["Name"] = "QA Grey Star"
    assistant.character["BookNumber"] = 3
    assistant.character["CombatSkillBase"] = cs
    assistant.character["CombatSkillCurrent"] = cs
    assistant.character["EnduranceMax"] = end
    assistant.character["EnduranceCurrent"] = end
    assistant.character["WillpowerCurrent"] = wp
    assistant.character["WillpowerBase"] = wp
    assistant.character["LesserMagicks"] = list(greystar.LESSER_MAGICKS)
    assistant.inventory["Weapons"] = ["Wizard's Staff", "Broadsword"]
    assistant.inventory["BackpackItems"] = [
        "Meal",
        "Meal",
        "Meal",
        "Meal",
        "Coil of Rope",
        "Tinderbox",
        "Pestle and Mortar",
        "Ezeran Salts",
    ]
    assistant.inventory["SpecialItems"] = [
        "Map of the Shadakine Empire",
        "Magic Talisman",
        "Silver Charm of Jnana the Wise",
        "Jewelled Dagger",
        "Mind Gem",
    ]
    assistant.inventory["HasHerbPouch"] = True
    assistant.inventory["HerbPouchItems"] = [
        "Empty Vial",
        "Empty Vial",
        "Vial of Saltpetre",
        "Vial of Sulphur",
        "Senara Potion (+5 WP)",
    ]
    assistant.state["SectionHistory"] = []
    assistant.state["CurrentBookStats"] = {
        "BookNumber": 3,
        "BookTitle": greystar.BOOKS[3]["Title"],
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
    missing = [section for section in range(1, 351) if not (BOOK_DIR / f"sect{section}.htm").exists()]
    result.check(not missing, "All 350 Book 3 section files exist.", f"Missing section files: {missing}")

    bad_links: list[str] = []
    graph: dict[int, list[int]] = {}
    for section in range(1, 351):
        _, links = section_text_and_links(section)
        graph[section] = links
        for target in links:
            if target < 1 or target > 350 or not (BOOK_DIR / f"sect{target}.htm").exists():
                bad_links.append(f"{section}->{target}")
    result.check(not bad_links, "Every Book 3 source link points to an existing section.", f"Bad links: {bad_links[:10]}")

    seen = {1}
    queue: deque[int] = deque([1])
    while queue:
        current = queue.popleft()
        for target in graph[current]:
            if target not in seen:
                seen.add(target)
                queue.append(target)
    unreachable = sorted(set(range(1, 351)) - seen)
    result.check(
        unreachable == [144, 190],
        "Reachability matches the known Book 3 source irregularities: 144 and 190.",
        f"Unexpected unreachable sections: {unreachable}",
    )


def run_data_surface(result: Result) -> None:
    assistant = prime()
    result.check("3" in assistant.section_automation, "Book 3 automation data loads.", "Book 3 automation data did not load.")
    result.check("3" in assistant.section_flows, "Book 3 flow data loads.", "Book 3 flow data did not load.")
    result.check("1" in assistant.section_flows and "2" in assistant.section_flows, "Book 1 and 2 flow data still load.", "Earlier book flow data missing.")

    combat_sections: list[int] = []
    roll_sections: list[int] = []
    for section in range(1, 351):
        text, _ = section_text_and_links(section)
        if re.search(r"COMBAT SKILL\s+\d+\s+ENDURANCE\s+\d+", text, flags=re.IGNORECASE):
            combat_sections.append(section)
        if "Random Number Table" in text or "pick a number" in text.lower():
            roll_sections.append(section)
    flow = assistant.section_flows.get("3", {})
    missing_combat = [section for section in combat_sections if not flow.get(str(section), {}).get("combat")]
    missing_rolls = [section for section in roll_sections if not flow.get(str(section), {}).get("roll")]
    result.check(not missing_combat, f"All {len(combat_sections)} detected combat sections have combat presets.", f"Missing combat presets: {missing_combat}")
    result.check(not missing_rolls, f"All {len(roll_sections)} detected roll sections have roll helpers.", f"Missing roll helpers: {missing_rolls}")


def run_automation_sweep(result: Result) -> None:
    entries = prime().section_automation.get("3", {})
    tested = 0
    for raw_section in sorted(entries.keys(), key=lambda item: int(item)):
        local = prime()
        try:
            capture(lambda raw_section=raw_section, local=local: local.set_section(int(raw_section)))
            tested += 1
        except Exception as exc:
            result.fail(f"Section {raw_section} automation raised {type(exc).__name__}: {exc}")
    result.check(tested == len(entries), f"Simple automation sweep covered {tested} Book 3 sections.", "Simple automation sweep did not cover every Book 3 entry.")


def run_flow_sweep(result: Result) -> None:
    flows = prime().section_flows.get("3", {})
    roll_tests = loot_tests = status_tests = wp_tests = combat_tests = 0
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
        for status in greystar.as_list(flow.get("status")):
            local = prime(section)
            try:
                capture(lambda local=local, status=status: local.set_status_flag(str(status.get("key") or ""), True))
                status_tests += 1
            except Exception as exc:
                result.fail(f"Section {section} status {status.get('key')} raised {type(exc).__name__}: {exc}")
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
    result.check(roll_tests == 140, f"Roll helper sweep covered {roll_tests} outcomes.", f"Unexpected roll test count: {roll_tests}")
    result.check(loot_tests >= 20, f"Loot sweep covered {loot_tests} buttons.", f"Loot sweep only covered {loot_tests} buttons.")
    result.check(status_tests >= 1, f"Status sweep covered {status_tests} toggles.", "No status toggles were tested.")
    result.check(wp_tests >= 4, f"Willpower-cost sweep covered {wp_tests} buttons.", f"Willpower-cost sweep only covered {wp_tests} buttons.")
    result.check(combat_tests >= 16, f"Combat sweep started {combat_tests} presets.", f"Combat sweep only started {combat_tests} presets.")


def run_mechanic_edge_checks(result: Result) -> None:
    low = prime(4, end=10)
    low_roll, _ = capture(lambda: low.roll_current_section(0))
    high = prime(4, end=25)
    high_roll, _ = capture(lambda: high.roll_current_section(0))
    result.check(
        int(low_roll.get("Route") or 0) == 65 and int(high_roll.get("Route") or 0) == 59,
        "Dynamic END roll modifiers route section 4 correctly.",
        f"Section 4 roll routes were low={low_roll.get('Route')} high={high_roll.get('Route')}.",
    )

    local = prime(1)
    original = list(local.inventory["BackpackItems"])
    capture(lambda: local.set_section(344))
    stashed = not local.inventory["BackpackItems"] and not local.automation_flags.get("backpackAvailable")
    capture(lambda: local.set_section(278))
    restored = original[:3] == local.inventory["BackpackItems"][:3] and local.automation_flags.get("backpackAvailable")
    result.check(stashed and restored, "Book 3 Backpack stash and recovery preserve Backpack Items.", "Backpack stash/recovery failed.")

    local = prime(1)
    capture(lambda: local.set_section(191))
    weapons_stored = not local.inventory["Weapons"] and local.inventory["BackpackItems"]
    capture(lambda: local.set_section(182))
    weapons_restored = "Wizard's Staff" in local.inventory["Weapons"] and "Broadsword" in local.inventory["Weapons"]
    result.check(weapons_stored and weapons_restored, "Book 3 weapon-only confiscation preserves Backpack Items and restores weapons.", "Weapon-only confiscation failed.")

    local = prime(322, cs=18)
    capture(lambda: local.start_section_combat("322-elessi-leader-dagger"))
    result.check(
        local.combat_active_weapon() == "" and local.combat_skill_for_round() == 12,
        "Jewelled Dagger section preset forces unarmed combat with the reduced -6 CS penalty.",
        f"Section 322 dagger preset CS={local.combat_skill_for_round()} weapon={local.combat_active_weapon()!r}.",
    )

    local = prime(243, cs=1, end=1, wp=0)
    capture(lambda: local.start_section_combat("243-jahksa-final"))
    capture(lambda: local.combat_round(combat_round_tokens(local, roll=1, wp=1)))
    result.check(
        int(local.state["CurrentSection"]) == 350 and bool(local.book_completion_payload().get("Active")),
        "Final Jahksa combat defeat routes to section 350 and activates completion.",
        f"Final combat routed to {local.state['CurrentSection']} with completion={local.book_completion_payload().get('Active')}.",
    )

    local = prime(1, wp=2)
    before = int(local.character["WillpowerCurrent"])
    capture(lambda: local.use_item("herb", "Senara Potion (+5 WP)"))
    result.check(int(local.character["WillpowerCurrent"]) == before + 5, "Senara Potion use restores 5 WP.", "Senara Potion did not restore WP.")


def run_completion_and_achievements(result: Result) -> None:
    local = prime(cs=80, end=240, wp=240)
    for section in SUCCESS_ROUTE:
        capture(lambda section=section: local.set_section(section))
    result.check(3 in greystar.as_list(local.character["CompletedBooks"]), "Success-route smoke completes Book 3.", "Book 3 did not complete on success-route smoke.")
    local.sync_achievements(save=False)
    unlocked = local.achievement_unlocked_ids()
    expected = {
        "gs3_complete",
        "gs3_moonstone_claimed",
        "gs3_final_truth",
        "gs3_daemonak_slayer",
        "gs3_ethetron_pilot",
        "gs3_singing_city",
        "gs3_guardians_song",
        "gs3_paradox_bargain",
        "gs3_chaos_bird_survivor",
    }
    result.check(expected.issubset(unlocked), f"Achievement sync/backfill unlocked expected Book 3 route set.", f"Missing expected achievements: {sorted(expected - unlocked)}")

    before_count = len(unlocked)
    capture(lambda: local.repeat_completed_book())
    result.check(
        int(local.character["BookNumber"]) == 3
        and int(local.state["CurrentSection"]) == 1
        and len(local.achievement_unlocked_ids()) >= before_count,
        "Repeat Book 3 resets to section 1 and preserves achievements.",
        "Repeat Book 3 cleanup failed.",
    )


def write_report(result: Result) -> None:
    REPORT_PATH.parent.mkdir(parents=True, exist_ok=True)
    lines = [
        "# GS Book 3 Playtest Report",
        "",
        f"Generated: {datetime.now().isoformat(timespec='seconds')}",
        "",
        "Scope: dry-run source, automation, flow, Book 3 edge mechanics, completion, achievements, and repeat-book checks. The script uses in-memory saves and does not touch the live campaign pointer.",
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
    print(f"Book 3 playtest report: {REPORT_PATH}")
    print(f"Passed: {len(result.passed)} | Warnings: {len(result.warnings)} | Failures: {len(result.failed)}")
    for failure in result.failed:
        print(f"FAIL: {failure}")
    return 1 if result.failed else 0


if __name__ == "__main__":
    raise SystemExit(main())
