#!/usr/bin/env python3
"""Dry-run Book 1 playtests for the Grey Star assistant.

These checks deliberately avoid the live save pointer and current-position file.
They exercise Book 1 section automation, flow buttons, combat presets, and the
successful completion transition with disposable in-memory assistant instances.
"""

from __future__ import annotations

import contextlib
import io
import json
import sys
from datetime import datetime
from pathlib import Path
from typing import Any, Callable


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

import greystar  # noqa: E402


REPORT_PATH = ROOT / "testing" / "logs" / "GSBOOK1_PLAYTEST_REPORT.md"

SUCCESS_ROUTE = [
    1, 202, 140, 112, 84, 224, 127, 40, 223, 195, 82, 339, 217, 105, 131,
    300, 289, 175, 116, 226, 295, 320, 187, 230, 291, 178, 160, 301, 247,
    62, 7, 270, 201, 172, 211, 250, 326, 87, 125, 137, 92, 142, 286, 214,
    176, 153, 185, 80, 25, 77, 147, 221, 292, 346, 199, 31, 75, 3, 85, 18,
    134, 58, 342, 101, 130, 126, 161, 193, 15, 218, 39, 55, 70, 88, 189,
    215, 2, 24, 33, 10, 51, 102, 149, 165, 192, 276, 52, 152, 277, 252,
    327, 78, 29, 54, 278, 184, 325, 136, 345, 61, 186, 86, 266, 330, 256,
    281, 331, 307, 249, 282, 148, 233, 337, 44, 335, 294, 319, 344, 43,
    143, 118, 268, 8, 19, 35, 59, 65, 72, 22, 334, 222, 239, 267, 340,
    298, 263, 146, 232, 154, 4, 350,
]


class DryRunAssistant(greystar.GreyStarAssistant):
    """Assistant variant that never writes the shared save pointer."""

    def __init__(self) -> None:
        super().__init__(save_dir=ROOT / "testing" / "dry-run-saves", data_dir=ROOT / "data")
        self.saved_state: dict[str, Any] | None = None

    def write_current_position(self) -> None:  # keep live campaign untouched
        return

    def save_game(self, path_text: str = "", quiet: bool = False) -> bool:
        path = self.resolve_save_path(path_text) if path_text.strip() else self.save_dir / "_dryrun.json"
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


def prime(section: int = 1, *, cs: int = 40, end: int = 120, wp: int = 120) -> DryRunAssistant:
    assistant = DryRunAssistant()
    assistant.state = greystar.normalize_state(greystar.default_state())
    assistant.character["Name"] = "QA Grey Star"
    assistant.character["BookNumber"] = 1
    assistant.character["CombatSkillBase"] = cs
    assistant.character["CombatSkillCurrent"] = cs
    assistant.character["EnduranceMax"] = end
    assistant.character["EnduranceCurrent"] = end
    assistant.character["WillpowerCurrent"] = wp
    assistant.character["WillpowerBase"] = wp
    assistant.character["LesserMagicks"] = list(greystar.LESSER_MAGICKS)
    assistant.inventory["Weapons"] = ["Wizard's Staff", "Broadsword"]
    assistant.inventory["BackpackItems"] = [
        "Meal", "Meal", "Meal", "Meal", "Meal", "Meal", "Meal", "Meal",
        "Kazim Stone", "Calacena Mushrooms", "Coil of Rope", "Tinderbox", "Torch",
    ]
    assistant.inventory["SpecialItems"] = [
        "Map of the Shadakine Empire",
        "Magic Talisman",
        "Jewelled Dagger",
        "Silver Charm of Jnana the Wise",
        "Amulet of the Shianti priest",
        "Medallion of the Redeemer",
        "Yabari Ointment",
        "Tarama Seed",
    ]
    assistant.inventory["HasHerbPouch"] = True
    assistant.inventory["HerbPouchItems"] = [
        "Empty Vial",
        "Empty Vial",
        "Vial of Saltpetre",
        "Vial of Sulphur",
        "Ezeran Crystals",
        "Vial of Pink Liquid",
        "Potion of Laumspur",
        "Potion of Rendalim's Elixir",
    ]
    assistant.state["SectionHistory"] = []
    assistant.state["CurrentBookStats"] = {
        "BookNumber": 1,
        "BookTitle": greystar.BOOKS[1]["Title"],
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
    use_staff = assistant.combat_uses_magical_staff()
    if use_staff:
        return ["combat", "round", str(wp), str(roll)]
    return ["combat", "round", str(roll)]


def run_simple_automation_sweep(result: Result) -> None:
    assistant = prime()
    entries = assistant.section_automation.get("1", {})
    tested = 0
    for raw_section in sorted(entries.keys(), key=lambda item: int(item)):
        section = int(raw_section)
        local = prime()
        try:
            capture(lambda section=section, local=local: local.set_section(section))
            tested += 1
        except Exception as exc:  # pragma: no cover - report-driven script
            result.fail(f"Section {section} simple automation raised {type(exc).__name__}: {exc}")
    result.check(tested == len(entries), f"Simple automation sweep covered {tested} sections.", "Simple automation sweep did not cover every entry.")


def run_flow_surface_sweep(result: Result) -> None:
    assistant = prime()
    flows = assistant.section_flows.get("1", {})
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
            if not isinstance(option, dict):
                continue
            local = prime(section)
            try:
                capture(lambda local=local, option=option: local.apply_flow_loot(str(option.get("id") or "")))
                loot_tests += 1
            except Exception as exc:
                result.fail(f"Section {section} loot {option.get('id')} raised {type(exc).__name__}: {exc}")
        for status in greystar.as_list(flow.get("status")):
            if not isinstance(status, dict):
                continue
            local = prime(section)
            try:
                capture(lambda local=local, status=status: local.set_status_flag(str(status.get("key") or ""), True))
                status_tests += 1
            except Exception as exc:
                result.fail(f"Section {section} status {status.get('key')} raised {type(exc).__name__}: {exc}")
        if isinstance(flow.get("wpCost"), dict):
            local = prime(section)
            try:
                capture(lambda local=local, flow=flow: local.pay_willpower_cost(int(flow["wpCost"].get("cost") or 0)))
                wp_tests += 1
            except Exception as exc:
                result.fail(f"Section {section} WP cost raised {type(exc).__name__}: {exc}")
        for combat in greystar.as_list(flow.get("combat")):
            if not isinstance(combat, dict):
                continue
            local = prime(section)
            combat_id = str(combat.get("id") or "")
            try:
                capture(lambda local=local, combat_id=combat_id: local.start_section_combat(combat_id))
                if not local.combat.get("Active"):
                    result.fail(f"Section {section} combat {combat_id} did not become active.")
                else:
                    combat_tests += 1
            except Exception as exc:
                result.fail(f"Section {section} combat {combat_id} raised {type(exc).__name__}: {exc}")
    result.pass_(f"Flow sweep: {roll_tests} roll outcomes, {loot_tests} loot buttons, {status_tests} status toggles, {wp_tests} WP costs, {combat_tests} combat presets.")


def run_focused_combat_checks(result: Result) -> None:
    for shield, expected_extra_end in [(False, 2), (True, 1)]:
        local = prime(149, cs=30, end=80, wp=30)
        local.automation_flags["sorceryShieldActiveFor149"] = shield
        capture(lambda: local.start_section_combat("149-kleasa"))
        capture(lambda: local.combat_round(combat_round_tokens(local, roll=5, wp=1)))
        log = greystar.as_list(local.combat.get("Log"))
        last = log[-1] if log else {}
        result.check(
            bool(last.get("SpecialEffects")),
            f"Section 149 records per-round special effects with shield={shield}.",
            f"Section 149 did not record per-round special effects with shield={shield}.",
        )
        result.check(
            int(last.get("FinalPlayerEnd", -999)) == max(0, int(last.get("PlayerEnd", 0)) - expected_extra_end),
            f"Section 149 shield={shield} applies the correct extra END loss.",
            f"Section 149 shield={shield} extra END loss was not correct.",
        )

    local = prime(259, cs=10, end=10, wp=5)
    capture(lambda: local.start_section_combat("259-darkling-room"))
    fixed_before = int(local.combat.get("FixedPlayerCombatSkill") or 0)
    capture(lambda: local.combat_round(combat_round_tokens(local, roll=5, wp=1)))
    fixed_after = int(local.combat.get("FixedPlayerCombatSkill") or 0)
    result.check(
        fixed_before == 15 and fixed_after == fixed_before,
        "Section 259 mental Combat Skill stays fixed after round damage.",
        f"Section 259 fixed mental Combat Skill changed unexpectedly ({fixed_before}->{fixed_after}).",
    )

    for wp, route in [(20, 331), (5, 32)]:
        local = prime(281, cs=18, end=80, wp=wp)
        capture(lambda: local.start_section_combat("281-large-quoku"))
        capture(lambda: local.combat_round(combat_round_tokens(local, roll=5, wp=1)))
        result.check(
            int(local.state["CurrentSection"]) == route,
            f"Section 281 one-round WP threshold routes to {route} from WP {wp}.",
            f"Section 281 WP {wp} routed to {local.state['CurrentSection']} instead of {route}.",
        )


def run_weapon_ruling_checks(result: Result) -> None:
    local = prime(1, cs=18, end=30, wp=0)
    capture(lambda: local.start_combat(["combat", "start", "Training Foe", "10", "10"]))
    result.check(
        local.combat_active_weapon() == "Wizard's Staff" and local.combat_skill_for_round() == 18,
        "Wizard's Staff can be used as a normal weapon at 0 WP without the -6 penalty.",
        f"0-WP Staff combat skill was {local.combat_skill_for_round()} with weapon {local.combat_active_weapon()}.",
    )

    local = prime(1, cs=18, end=30, wp=20)
    local.inventory["Weapons"] = []
    local.inventory["SpecialItems"] = []
    capture(lambda: local.start_combat(["combat", "start", "Training Foe", "10", "10"]))
    result.check(
        local.combat_active_weapon() == "" and local.combat_skill_for_round() == 10,
        "No weapon applies the explicit -8 CS penalty.",
        f"Unarmed combat skill was {local.combat_skill_for_round()} with weapon {local.combat_active_weapon()}.",
    )

    local = prime(1, cs=18, end=30, wp=20)
    local.inventory["Weapons"] = ["Broadsword"]
    capture(lambda: local.start_combat(["combat", "start", "Training Foe", "10", "10"]))
    result.check(
        local.combat_active_weapon() == "Broadsword" and local.combat_skill_for_round() == 12,
        "No Staff plus another weapon applies the Staff-unavailable -6 CS penalty.",
        f"No-Staff weapon combat skill was {local.combat_skill_for_round()} with weapon {local.combat_active_weapon()}.",
    )

    local = prime(1, cs=18, end=30, wp=20)
    capture(lambda: local.start_combat(["combat", "start", "Training Foe", "10", "10"]))
    capture(lambda: local.set_combat_weapon("Jewelled Dagger", save=False))
    result.check(
        local.combat_active_weapon() == "Jewelled Dagger" and local.combat_skill_for_round() == 19,
        "Jewelled Dagger gives +1 CS only when selected as the combat weapon.",
        f"Jewelled Dagger combat skill was {local.combat_skill_for_round()} with weapon {local.combat_active_weapon()}.",
    )


def run_gear_restore_checks(result: Result) -> None:
    for loss_section, restore_section in [(291, 221), (300, 221), (311, 245)]:
        local = prime(1)
        before_backpack = list(local.inventory["BackpackItems"])
        capture(lambda: local.set_section(loss_section))
        result.check(
            not local.automation_flags.get("staffAvailable", True) and not local.inventory["BackpackItems"],
            f"Section {loss_section} stores unavailable gear.",
            f"Section {loss_section} did not store gear correctly.",
        )
        capture(lambda: local.set_section(restore_section))
        result.check(
            local.automation_flags.get("staffAvailable", False)
            and "Wizard's Staff" in local.inventory["Weapons"]
            and before_backpack[:3] == local.inventory["BackpackItems"][:3],
            f"Section {restore_section} restores gear from section {loss_section}.",
            f"Section {restore_section} did not restore gear from section {loss_section}.",
        )


def run_completion_check(result: Result) -> None:
    local = prime(1, cs=18, end=28, wp=0)
    capture(lambda: local.set_section(350))
    completion = local.book_completion_payload()
    result.check(
        bool(completion.get("Active")) and int(completion.get("Summary", {}).get("BookNumber") or 0) == 1,
        "Section 350 activates the Book 1 completion payload.",
        "Section 350 did not activate the Book 1 completion payload.",
    )
    capture(lambda: local.continue_completed_book(lesser_magick="Psychomancy"))
    result.check(
        int(local.character["BookNumber"]) == 2
        and int(local.state["CurrentSection"]) == 1
        and 1 in [int(item) for item in greystar.as_list(local.character["CompletedBooks"])]
        and "Psychomancy" in greystar.as_list(local.character["LesserMagicks"]),
        "Book 1 continue flow advances to Book 2 and carries completion state.",
        "Book 1 continue flow did not advance cleanly to Book 2.",
    )

    repeat = prime(1, cs=18, end=28, wp=26)
    capture(lambda: repeat.set_section(350))
    repeat.character["EnduranceCurrent"] = 4
    repeat.character["WillpowerCurrent"] = 1
    capture(lambda: repeat.repeat_completed_book())
    result.check(
        int(repeat.character["BookNumber"]) == 1
        and int(repeat.state["CurrentSection"]) == 1
        and int(repeat.character["EnduranceCurrent"]) == 28
        and int(repeat.character["WillpowerCurrent"]) == 26
        and not repeat.book_completion_payload().get("Active"),
        "Book repeat restarts the completed book with END/WP reset and the same character.",
        "Book repeat did not reset the completed book cleanly.",
    )


def run_achievement_checks(result: Result) -> None:
    local = prime(1, cs=60, end=220, wp=220)
    for section in SUCCESS_ROUTE:
        capture(lambda section=section: local.set_section(section))
    local.sync_achievements(save=False)
    unlocked = {
        str(entry.get("Id"))
        for entry in greystar.as_list(local.achievement_state().get("Unlocked"))
        if isinstance(entry, dict)
    }
    expected = {
        "gs1_complete",
        "gs1_long_road",
        "gs1_kazim_claimed",
        "gs1_kazim_stolen",
        "gs1_priests_amulet",
        "gs1_jnanas_blessing",
        "gs1_yabari_ward",
        "gs1_alchemy_cache",
        "gs1_prophetic_climb",
        "gs1_najin_standoff",
        "gs1_kleasa_survivor",
        "gs1_no_shield_no_problem",
        "gs1_correct_key",
        "gs1_quoku_breakthrough",
        "gs1_gear_taken",
        "gs1_gear_recovered",
        "gs1_tanith_sacrifice",
        "gs1_lone_road",
        "gs1_final_ascent",
    }
    missing = sorted(expected - unlocked)
    result.check(
        not missing and "gs1_shield_raised" not in unlocked,
        "Book 1 achievement sync backfills route and story unlocks from history.",
        f"Achievement sync mismatch. Missing: {', '.join(missing)}; shield={ 'gs1_shield_raised' in unlocked }.",
    )


def run_route_smoke_playthrough(result: Result) -> None:
    local = prime(1, cs=60, end=220, wp=220)
    visited = 0
    for section in SUCCESS_ROUTE:
        try:
            capture(lambda section=section: local.set_section(section))
            flow = local.current_section_flow_entry() or {}
            for combat in greystar.as_list(flow.get("combat")):
                if not isinstance(combat, dict):
                    continue
                combat_id = str(combat.get("id") or "")
                capture(lambda combat_id=combat_id: local.start_section_combat(combat_id))
                rounds = 0
                while local.combat.get("Active") and rounds < 8:
                    capture(lambda: local.combat_round(combat_round_tokens(local, roll=9, wp=2)))
                    rounds += 1
            visited += 1
        except Exception as exc:
            result.fail(f"Successful-route smoke failed at section {section}: {type(exc).__name__}: {exc}")
            break
    result.check(
        visited == len(SUCCESS_ROUTE) and 350 in greystar.as_list(local.state["CurrentBookStats"].get("VisitedSections")),
        f"Successful-route smoke reached section 350 across {visited} route stops.",
        f"Successful-route smoke stopped after {visited} route stops.",
    )


def run_route_link_check(result: Result) -> None:
    missing: list[str] = []
    bad_ranges: list[str] = []
    for section in range(1, greystar.BOOKS[1]["MaxSection"] + 1):
        source = ROOT / "books" / "gs" / greystar.BOOKS[1]["Folder"] / f"sect{section}.htm"
        if not source.exists():
            missing.append(str(section))
            continue
        local = prime(section)
        for route in local.section_source_routes(1, section):
            target = ROOT / "books" / "gs" / greystar.BOOKS[1]["Folder"] / f"sect{route}.htm"
            if route < 1 or route > greystar.BOOKS[1]["MaxSection"] or not target.exists():
                bad_ranges.append(f"{section}->{route}")
    result.check(not missing, "All 350 Book 1 section HTML files exist.", f"Missing section files: {', '.join(missing[:12])}")
    result.check(not bad_ranges, "All Book 1 source links point to existing sections.", f"Bad section links: {', '.join(bad_ranges[:12])}")


def write_report(result: Result) -> None:
    lines = [
        "# GS Book 1 Playtest Report",
        "",
        f"Generated: {datetime.now().isoformat(timespec='seconds')}",
        "",
        "Scope: dry-run route, automation, combat, gear restore, and completion checks. The script uses in-memory saves and does not touch the live campaign pointer.",
        "",
        f"Passed checks: {len(result.passed)}",
        f"Warnings: {len(result.warnings)}",
        f"Failures: {len(result.failed)}",
        "",
        "## Passed",
        "",
    ]
    lines.extend(f"- {item}" for item in result.passed)
    if result.warnings:
        lines.extend(["", "## Warnings", ""])
        lines.extend(f"- {item}" for item in result.warnings)
    if result.failed:
        lines.extend(["", "## Failures", ""])
        lines.extend(f"- {item}" for item in result.failed)
    lines.append("")
    REPORT_PATH.parent.mkdir(parents=True, exist_ok=True)
    REPORT_PATH.write_text("\n".join(lines), encoding="utf-8")


def main() -> int:
    result = Result()
    run_route_link_check(result)
    run_simple_automation_sweep(result)
    run_flow_surface_sweep(result)
    run_focused_combat_checks(result)
    run_weapon_ruling_checks(result)
    run_gear_restore_checks(result)
    run_completion_check(result)
    run_achievement_checks(result)
    run_route_smoke_playthrough(result)
    write_report(result)
    print(f"Passed: {len(result.passed)}")
    print(f"Warnings: {len(result.warnings)}")
    print(f"Failures: {len(result.failed)}")
    print(f"Report: {REPORT_PATH}")
    for item in result.failed:
        print(f"FAIL: {item}")
    return 1 if result.failed else 0


if __name__ == "__main__":
    raise SystemExit(main())
