"""Markdown renderers for study note documents."""

from __future__ import annotations

import os
from datetime import datetime
from pathlib import Path
from urllib.parse import quote

from . import config, normalize
from .models import MetadataMap, NotesProfile
from .repo import folder_name_from_title

def _relative_solution_url(from_dir: Path, solution_path: Path) -> str:
    """Return a percent-encoded relative path from from_dir to solution_path."""

    rel = Path(os.path.relpath(solution_path, start=from_dir))
    encoded = "/".join(quote(part) for part in rel.parts)
    if not encoded.startswith((".", "/")):
        encoded = f"./{encoded}"
    return encoded

def build_notes_markdown(
    fieldnames: list[str],
    rows: list[dict[str, str]],
    source_url: str,
    metadata: MetadataMap,
    profile: NotesProfile,
) -> str:
    """Render the notes markdown document for the provided profile."""

    timestamp = datetime.utcnow().strftime("%Y-%m-%d %H:%M UTC")
    lines: list[str] = [
        f"# {profile.notes_title}",
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

    preferred_order = [field for field in config.STANDARD_FIELDS if field in fieldnames]
    extra_fields = [field for field in fieldnames if field not in preferred_order]
    ordered_fields = preferred_order + extra_fields

    category_entries: dict[str, list[tuple[str, list[str]]]] = {}

    for row in rows:
        problem = (row.get("Problem") or "Untitled Problem").strip() or "Untitled Problem"
        problem_meta = metadata.get(problem)
        folder_name = problem_meta.folder_name if problem_meta else folder_name_from_title(problem)
        link = problem_meta.link if problem_meta else None
        solution_rel_path = _relative_solution_url(
            profile.notes_output_path.parent,
            profile.problems_dir / folder_name / "solution.py",
        )
        if link:
            links_text = f"*([Problem]({link.url}) | [Solution]({solution_rel_path}))*"
        else:
            links_text = f"*([Solution]({solution_rel_path}))*"
        problem_title = normalize.escape_ordered_list_prefix(problem)
        heading_text = f"**{problem_title}**"
        problem_line = f"{heading_text} {links_text}".strip()

        section_lines: list[str] = []

        for field in ordered_fields:
            if field in {"Problem", "Category"}:
                continue
            raw_value = row.get(field) or ""
            value = normalize.format_cell(raw_value)
            if not value and field != "Notes":
                continue

            if field == "Notes":
                note_entries = normalize.format_notes(raw_value)
                if not note_entries:
                    continue
                if len(note_entries) == 1 and note_entries[0][0] == 0:
                    section_lines.append(f"- **Notes:** {note_entries[0][1]}")
                else:
                    section_lines.append("- **Notes:**")
                    for level, note in note_entries:
                        indent = "  " * (level + 1)
                        section_lines.append(f"{indent}- {note}")
                continue

            section_lines.append(f"- **{field}:** {value}")

        if not section_lines:
            section_lines.append("- _No details provided._")

        category_raw = (row.get("Category") or "").strip()
        categories = normalize.split_categories(category_raw)
        if not categories:
            categories = [config.DEFAULT_CATEGORY]

        for category in categories:
            canonical = config.CATEGORY_ALIASES.get(category, category) or config.DEFAULT_CATEGORY
            category_entries.setdefault(canonical, []).append((problem_line, section_lines.copy()))

    if not category_entries:
        return "\n".join(lines)

    ordered_categories = [
        category
        for category in config.CATEGORY_ORDER
        if category in category_entries and category != config.DEFAULT_CATEGORY
    ]
    ordered_categories.extend(
        category
        for category in category_entries
        if category not in config.CATEGORY_ORDER and category != config.DEFAULT_CATEGORY
    )
    if config.DEFAULT_CATEGORY in category_entries:
        ordered_categories.append(config.DEFAULT_CATEGORY)

    for category in ordered_categories:
        lines.append(f"## {category}")
        lines.append("")
        for problem_line, detail_lines in category_entries[category]:
            lines.append(problem_line)
            lines.extend(detail_lines)
            lines.append("")

    if lines and lines[-1] == "":
        lines.pop()

    return "\n".join(lines)


__all__ = ["build_notes_markdown"]
