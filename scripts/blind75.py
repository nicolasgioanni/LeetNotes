#!/usr/bin/env python3
"""Build markdown notes and a problem index from a Google Sheets CSV export."""
from __future__ import annotations

import csv
import io
import os
import re
import sys
import urllib.request
from linkify_leetcode import lookup_problem
from collections import defaultdict
from datetime import datetime
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]
NOTES_OUTPUT_PATH = REPO_ROOT / "Notes" / "blind75.md"
PROBLEMS_DIR = REPO_ROOT / "Problems"
PROBLEMS_OUTPUT_PATH = PROBLEMS_DIR / "README.md"
STANDARD_FIELDS = ("Problem", "Category", "Time Complexity", "Space Complexity", "Notes")
NOTE_PREFIXES = ("- ", "* ", "\u2022 ", "\u2022")
CATEGORY_ORDER = [
    "Array & Hashing",
    "Two Pointers",
    "Sliding Window",
    "Stack",
    "Binary Search",
    "Linked List",
    "Trees",
    "Heap / Priority Queue",
    "Backtracking",
    "Tries",
    "Graphs",
    "Advanced Graphs",
    "1-D Dynamic Programming",
    "2-D Dynamic Programming",
    "Greedy",
    "Intervals",
    "Math & Geometry",
    "Bit Manipulation",
]
CATEGORY_ALIASES = {
    "Arrays & Hashing": "Array & Hashing",
    "Binary Tree": "Trees",
    "Binary Trees": "Trees",
}
DEFAULT_CATEGORY = "Uncategorized"


def main() -> int:
    url = os.environ.get("SHEET_CSV_URL")
    if not url:
        print("Environment variable SHEET_CSV_URL is not set.", file=sys.stderr)
        return 1

    try:
        with urllib.request.urlopen(url) as response:
            status = getattr(response, "status", None)
            if status not in (200, None):
                raise RuntimeError(f"unexpected HTTP status code: {status}")
            charset = response.headers.get_content_charset() or "utf-8"
            raw_csv = response.read()
    except Exception as exc:  # pragma: no cover - runtime failure path
        print(f"Failed to download CSV: {exc}", file=sys.stderr)
        return 1

    try:
        csv_text = raw_csv.decode(charset, errors="replace")
    except LookupError:
        csv_text = raw_csv.decode("utf-8", errors="replace")

    reader = csv.DictReader(io.StringIO(csv_text))
    rows = list(reader)
    fieldnames = reader.fieldnames or []

    ensure_problem_folders(rows)

    notes_markdown = build_notes_markdown(fieldnames, rows, url)
    index_markdown = build_problem_index(rows)

    write_if_changed(NOTES_OUTPUT_PATH, notes_markdown)
    write_if_changed(PROBLEMS_OUTPUT_PATH, index_markdown)
    return 0


def ensure_problem_folders(rows: list[dict[str, str]]) -> None:
    for row in rows:
        problem = (row.get("Problem") or "").strip()
        if not problem:
            continue
        slug = slugify(problem)
        if not slug:
            continue
        folder = PROBLEMS_DIR / slug
        folder.mkdir(parents=True, exist_ok=True)
        solution_path = folder / "solution.py"
        if not solution_path.exists():
            placeholder = f"# TODO: implement solution for {problem}\n"
            solution_path.write_text(placeholder, encoding="utf-8")

def build_notes_markdown(fieldnames: list[str], rows: list[dict[str, str]], source_url: str) -> str:
    timestamp = datetime.utcnow().strftime("%Y-%m-%d %H:%M UTC")
    lines: list[str] = [
        "# Blind 75 Notes",
        "",
        "<!-- AUTO-GENERATED FILE. DO NOT EDIT MANUALLY. -->",
        f"*Last updated: {timestamp}*",
        "",
        f"[Source spreadsheet]({source_url})",
        "",
    ]

    if not fieldnames:
        lines.append("_No data available from spreadsheet._")
        lines.append("")
        return "\n".join(lines)

    preferred_order = [field for field in STANDARD_FIELDS if field in fieldnames]
    extra_fields = [field for field in fieldnames if field not in preferred_order]
    ordered_fields = preferred_order + extra_fields

    for row in rows:
        problem = (row.get("Problem") or "Untitled Problem").strip() or "Untitled Problem"
        slug = slugify(problem)
        problem_link = lookup_problem(problem)
        solution_rel_path = f"../Problems/{slug}/solution.py"
        if problem_link:
            links_text = f"*([Problem]({problem_link.url}) | [Solution]({solution_rel_path}))*"
        else:
            links_text = f"*([Solution]({solution_rel_path}))*"
        lines.append(f"## {problem} {links_text}")

        section_lines: list[str] = []

        for field in ordered_fields:
            if field == "Problem":
                continue
            raw_value = row.get(field) or ""
            value = format_cell(raw_value)
            if not value and field != "Notes":
                continue

            if field == "Notes":
                note_lines = format_notes(raw_value)
                if not note_lines:
                    continue
                if len(note_lines) == 1:
                    section_lines.append(f"- **Notes:** {note_lines[0]}")
                else:
                    section_lines.append("- **Notes:**")
                    section_lines.extend(f"  - {note}" for note in note_lines)
                continue

            section_lines.append(f"- **{field}:** {value}")

        if not section_lines:
            section_lines.append("- _No details provided._")

        lines.extend(section_lines)
        lines.append("")

    return "\n".join(lines)


def build_problem_index(rows: list[dict[str, str]]) -> str:
    timestamp = datetime.utcnow().strftime("%Y-%m-%d %H:%M UTC")
    lines: list[str] = [
        "# Problem Index",
        "",
        "<!-- AUTO-GENERATED FILE. DO NOT EDIT MANUALLY. -->",
        f"*Last updated: {timestamp}*",
        "",
        "This index shows every problem folder grouped by category. Make sure the folder",
        "names match the generated links (lowercase with dashes).",
        "",
    ]

    category_map: dict[str, list[tuple[str, str]]] = defaultdict(list)

    for row in rows:
        problem = (row.get("Problem") or "Untitled Problem").strip() or "Untitled Problem"
        category_raw = (row.get("Category") or "").strip()
        categories = split_categories(category_raw)
        if not categories:
            categories = [DEFAULT_CATEGORY]
        slug = slugify(problem)
        for category in categories:
            canonical = CATEGORY_ALIASES.get(category, category) or DEFAULT_CATEGORY
            category_map[canonical].append((problem, slug))

    ordered_categories = CATEGORY_ORDER + [
        category
        for category in sorted(category_map)
        if category not in CATEGORY_ORDER and category != DEFAULT_CATEGORY
    ]

    for category in ordered_categories:
        problems = category_map.get(category, [])
        if not problems:
            continue
        lines.append(f"## {category}")
        for problem, slug in sorted(problems, key=lambda item: item[0].lower()):
            lines.append(f"- [{problem}](./{slug}/)")
        lines.append("")

    uncategorized = category_map.get(DEFAULT_CATEGORY, [])
    if uncategorized:
        lines.append(f"## {DEFAULT_CATEGORY}")
        for problem, slug in sorted(uncategorized, key=lambda item: item[0].lower()):
            lines.append(f"- [{problem}](./{slug}/)")
        lines.append("")

    if len(lines) == 7:  # Only header content, no problems
        lines.append("_No problems found in the spreadsheet._")
        lines.append("")

    return "\n".join(lines)


def split_categories(raw: str) -> list[str]:
    if not raw:
        return []
    parts = re.split(r"[,/]|\n", raw)
    cleaned = [part.strip() for part in parts if part.strip()]
    return cleaned


def slugify(value: str) -> str:
    value = value.lower()
    value = re.sub(r"[^a-z0-9\s-]", "", value)
    value = re.sub(r"[\s_-]+", "-", value).strip("-")
    return value or "untitled-problem"


def format_cell(value: str) -> str:
    text = (value or "").strip()
    if not text:
        return ""

    lowered = text.lower()
    if lowered.startswith("http://") or lowered.startswith("https://"):
        return f"[link]({text})"

    return " ".join(text.split())


def format_notes(value: str) -> list[str]:
    text = (value or "").replace("<br>", "\n")
    text = text.replace("\r\n", "\n").replace("\r", "\n")
    parts = [part.strip() for part in text.split("\n")]
    cleaned: list[str] = []
    for part in parts:
        if not part:
            continue
        stripped = part
        for prefix in NOTE_PREFIXES:
            if stripped.startswith(prefix):
                stripped = stripped[len(prefix):].strip()
                break
        formatted = format_cell(stripped)
        if formatted:
            cleaned.append(formatted)
    return cleaned


def write_if_changed(path: Path, content: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    if path.exists():
        existing = path.read_text(encoding="utf-8")
        if existing == content:
            return
    path.write_text(content, encoding="utf-8")


if __name__ == "__main__":
    sys.exit(main())









