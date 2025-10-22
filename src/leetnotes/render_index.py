"""Markdown renderer for the Problems index."""

from __future__ import annotations

import os
import re

from datetime import datetime
from pathlib import Path
from urllib.parse import quote

from . import config, normalize
from .models import MetadataMap, NotesProfile, ProblemLink
from .repo import folder_name_from_title

def _relative_solution_url(from_dir: Path, solution_path: Path) -> str:
    """Return a percent-encoded relative path from from_dir to solution_path."""

    rel = Path(os.path.relpath(solution_path, start=from_dir))
    encoded = "/".join(quote(part) for part in rel.parts)
    if not encoded.startswith((".", "/")):
        encoded = f"./{encoded}"
    return encoded

def build_problem_index(
    rows: list[dict[str, str]],
    metadata: MetadataMap,
    profile: NotesProfile,
) -> str:
    """Render the Problems/README.md index."""

    timestamp = datetime.utcnow().strftime("%Y-%m-%d %H:%M UTC")
    lines: list[str] = [
        f"# {profile.index_title}",
        "",
        "<!-- AUTO-GENERATED FILE. DO NOT EDIT MANUALLY. -->",
        f"*Last updated: {timestamp}*",
        "",
        "This index lists every problem I've solved, organized by category, with links to the problem and my solutions.",
        "",
        "",
    ]

    category_map: dict[str, dict[str, dict[str, object]]] = {}

    for row in rows:
        problem = (row.get("Problem") or "Untitled Problem").strip() or "Untitled Problem"
        problem_meta = metadata.get(problem)
        folder_name = problem_meta.folder_name if problem_meta else folder_name_from_title(problem)
        link = problem_meta.link if problem_meta else None
        display_name = problem_display_name(problem, link, folder_name)
        solution_filenames = list(problem_meta.solutions) if problem_meta and problem_meta.solutions else []
        solution_count = len(solution_filenames) if solution_filenames else 1
        solution_label = "Solutions" if solution_count != 1 else "Solution"
        solution_rel = _relative_solution_url(
            profile.problems_index_path.parent,
            profile.problems_dir / folder_name,
        )
        solution_link = f"[{solution_label}]({solution_rel})"
        category_raw = (row.get("Category") or "").strip()
        categories = normalize.split_categories(category_raw)
        if not categories:
            categories = [config.DEFAULT_CATEGORY]
        for category in categories:
            canonical = config.CATEGORY_ALIASES.get(category, category) or config.DEFAULT_CATEGORY
            bucket = category_map.setdefault(canonical, {})
            existing = bucket.get(folder_name)
            if existing:
                if not existing["link"] and link:
                    existing["link"] = link
                continue
            bucket[folder_name] = {
                "display": display_name,
                "link": link,
                "solution_link": solution_link,
                "folder": folder_name,
            }

    ordered_categories = config.CATEGORY_ORDER + [
        category
        for category in sorted(category_map)
        if category not in config.CATEGORY_ORDER and category != config.DEFAULT_CATEGORY
    ]

    rendered_folders: set[str] = set()

    for category in ordered_categories:
        bucket = category_map.get(category)
        if not bucket:
            continue
        entries = sorted(
            bucket.values(),
            key=lambda item: item["display"].lower(),
        )
        category_lines: list[str] = []
        for entry in entries:
            folder_name = entry["folder"]
            if folder_name in rendered_folders:
                continue
            rendered_folders.add(folder_name)
            display_name = entry["display"]
            link_obj = entry["link"]
            solution_link = entry["solution_link"]
            title_text = normalize.escape_ordered_list_prefix(display_name)
            links: list[str] = []
            if link_obj:
                links.append(f"[Problem]({link_obj.url})")
            links.append(solution_link)
            links_text = " | ".join(links)
            category_lines.append(f"- {title_text} ({links_text})")
        if category_lines:
            lines.append(f"## {category}")
            lines.extend(category_lines)
            lines.append("")

    uncategorized_bucket = category_map.get(config.DEFAULT_CATEGORY, {})
    uncategorized_entries = sorted(
        uncategorized_bucket.values(),
        key=lambda item: item["display"].lower(),
    )
    uncategorized_lines: list[str] = []
    for entry in uncategorized_entries:
        folder_name = entry["folder"]
        if folder_name in rendered_folders:
            continue
        rendered_folders.add(folder_name)
        display_name = entry["display"]
        link_obj = entry["link"]
        solution_link = entry["solution_link"]
        title_text = normalize.escape_ordered_list_prefix(display_name)
        links: list[str] = []
        if link_obj:
            links.append(f"[Problem]({link_obj.url})")
        links.append(solution_link)
        links_text = " | ".join(links)
        uncategorized_lines.append(f"- {title_text} ({links_text})")
    if uncategorized_lines:
        lines.append(f"## {config.DEFAULT_CATEGORY}")
        lines.extend(uncategorized_lines)
        lines.append("")

    if len(lines) == 7:
        lines.append("_No problems found in the spreadsheet._")
        lines.append("")

    return "\n".join(lines)


def problem_display_name(problem: str, link: ProblemLink | None, folder_name: str) -> str:
    """Return the display name for a problem, including its number if known."""

    if link and link.frontend_id:
        number = normalize.canonical_problem_number(link.frontend_id)
        return f"{number}. {problem}"
    match = re.match(r"^(\d+)\.\s+", folder_name)
    if match:
        number = normalize.canonical_problem_number(match.group(1))
        return f"{number}. {problem}"
    return problem


__all__ = ["build_problem_index", "problem_display_name"]
