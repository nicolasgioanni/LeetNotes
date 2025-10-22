"""Markdown renderers for study note documents."""

from __future__ import annotations

import os
from datetime import datetime
from pathlib import Path
from typing import Any
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


def _build_note_tree(entries: list[normalize.NoteEntry]) -> list[dict[str, Any]]:
    """Convert flat note entries into a parent/child hierarchy."""

    root: dict[str, Any] = {"level": -1, "text": "", "ordered": False, "children": []}
    stack: list[dict[str, Any]] = [root]

    for entry in entries:
        level = entry.level
        while stack and level <= stack[-1]["level"]:
            stack.pop()
        parent = stack[-1]
        node: dict[str, Any] = {
            "level": level,
            "text": entry.text,
            "ordered": entry.ordered,
            "children": [],
        }
        parent["children"].append(node)
        stack.append(node)

    return root["children"]


def _render_note_nodes(nodes: list[dict[str, Any]], base_indent: int) -> list[str]:
    """Render note nodes as Markdown/HTML lines anchored at base_indent."""

    lines: list[str] = []
    idx = 0
    while idx < len(nodes):
        ordered = bool(nodes[idx]["ordered"])
        group: list[dict[str, Any]] = []
        while idx < len(nodes) and bool(nodes[idx]["ordered"]) == ordered:
            group.append(nodes[idx])
            idx += 1
        if ordered:
            lines.extend(_render_ordered_group(group, base_indent))
        else:
            lines.extend(_render_bullet_group(group, base_indent))
    return lines


def _render_bullet_group(group: list[dict[str, Any]], base_indent: int) -> list[str]:
    indent = "  " * base_indent
    lines: list[str] = [f"{indent}<ul>"]
    for node in group:
        item_indent = "  " * (base_indent + 1)
        children = node["children"]
        if children:
            lines.append(f"{item_indent}<li>{node['text']}")
            lines.extend(_render_note_nodes(children, base_indent + 2))
            lines.append(f"{item_indent}</li>")
        else:
            lines.append(f"{item_indent}<li>{node['text']}</li>")
    lines.append(f"{indent}</ul>")
    return lines


def _render_ordered_group(group: list[dict[str, Any]], base_indent: int) -> list[str]:
    indent = "  " * base_indent
    lines: list[str] = [f"{indent}<ol type=\"1\">"]
    for node in group:
        item_indent = "  " * (base_indent + 1)
        children = node["children"]
        if children:
            lines.append(f"{item_indent}<li>{node['text']}")
            lines.extend(_render_note_nodes(children, base_indent + 2))
            lines.append(f"{item_indent}</li>")
        else:
            lines.append(f"{item_indent}<li>{node['text']}</li>")
    lines.append(f"{indent}</ol>")
    return lines


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

    category_entries: dict[str, dict[str, tuple[str, list[str]]]] = {}

    for row in rows:
        problem = (row.get("Problem") or "Untitled Problem").strip() or "Untitled Problem"
        problem_meta = metadata.get(problem)
        folder_name = problem_meta.folder_name if problem_meta else folder_name_from_title(problem)
        link = problem_meta.link if problem_meta else None
        solution_filenames = list(problem_meta.solutions) if problem_meta and problem_meta.solutions else []
        solution_count = len(solution_filenames) if solution_filenames else 1
        solution_label = "Solutions" if solution_count != 1 else "Solution"
        solution_rel_path = _relative_solution_url(
            profile.notes_output_path.parent,
            profile.problems_dir / folder_name,
        )
        solution_link = f"[{solution_label}]({solution_rel_path})"
        link_entries: list[str] = [solution_link]
        if link:
            link_entries = [f"[Problem]({link.url})", solution_link]
        links_text = f"*({' | '.join(link_entries)})*"
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
                if (
                    len(note_entries) == 1
                    and note_entries[0].level == 0
                    and not note_entries[0].ordered
                ):
                    section_lines.append(f"- **Notes:** {note_entries[0].text}")
                else:
                    section_lines.append("- **Notes:**")
                    tree = _build_note_tree(note_entries)
                    section_lines.extend(_render_note_nodes(tree, base_indent=1))
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
            bucket = category_entries.setdefault(canonical, {})
            existing = bucket.get(folder_name)
            if existing:
                existing_line, existing_details = existing
                replace_entry = False
                if len(section_lines) > len(existing_details):
                    replace_entry = True
                elif len(section_lines) == len(existing_details):
                    if "[Problem]" in problem_line and "[Problem]" not in existing_line:
                        replace_entry = True
                if replace_entry:
                    bucket[folder_name] = (problem_line, section_lines.copy())
            else:
                bucket[folder_name] = (problem_line, section_lines.copy())

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

    rendered_folders: set[str] = set()

    for category in ordered_categories:
        bucket = category_entries.get(category, {})
        entries = sorted(
            bucket.items(),
            key=lambda item: item[1][0].lower(),
        )
        category_lines: list[str] = []
        for folder_name, (problem_line, detail_lines) in entries:
            if folder_name in rendered_folders:
                continue
            rendered_folders.add(folder_name)
            category_lines.append(problem_line)
            category_lines.extend(detail_lines)
            category_lines.append("")
        if category_lines:
            lines.append(f"## {category}")
            lines.append("")
            lines.extend(category_lines)

    while lines and lines[-1] == "":
        lines.pop()

    return "\n".join(lines)


__all__ = ["build_notes_markdown"]

