"""Markdown renderer for the Problems index."""

from __future__ import annotations

import os
import re

from collections import defaultdict
from datetime import datetime
from pathlib import Path
from urllib.parse import quote

from . import config, normalize
from .models import MetadataMap, NotesProfile, ProblemLink
from .repo import folder_name_from_title
from .solutions import solution_link_labels

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

    category_map: dict[str, list[tuple[str, ProblemLink | None, list[str]]]] = defaultdict(list)

    for row in rows:
        problem = (row.get("Problem") or "Untitled Problem").strip() or "Untitled Problem"
        problem_meta = metadata.get(problem)
        folder_name = problem_meta.folder_name if problem_meta else folder_name_from_title(problem)
        link = problem_meta.link if problem_meta else None
        display_name = problem_display_name(problem, link, folder_name)
        solution_filenames = list(problem_meta.solutions) if problem_meta and problem_meta.solutions else []
        solution_links: list[str] = []
        for label, filename in solution_link_labels(solution_filenames):
            solution_rel = _relative_solution_url(
                profile.problems_index_path.parent,
                profile.problems_dir / folder_name / filename,
            )
            solution_links.append(f"[{label}]({solution_rel})")
        if not solution_links:
            solution_rel = _relative_solution_url(
                profile.problems_index_path.parent,
                profile.problems_dir / folder_name / "solution.py",
            )
            solution_links.append(f"[Solution]({solution_rel})")
        category_raw = (row.get("Category") or "").strip()
        categories = normalize.split_categories(category_raw)
        if not categories:
            categories = [config.DEFAULT_CATEGORY]
        for category in categories:
            canonical = config.CATEGORY_ALIASES.get(category, category) or config.DEFAULT_CATEGORY
            category_map[canonical].append((display_name, link, solution_links))

    ordered_categories = config.CATEGORY_ORDER + [
        category
        for category in sorted(category_map)
        if category not in config.CATEGORY_ORDER and category != config.DEFAULT_CATEGORY
    ]

    for category in ordered_categories:
        problems = category_map.get(category, [])
        if not problems:
            continue
        lines.append(f"## {category}")
        for display_name, link_obj, solution_link_entries in sorted(problems, key=lambda item: item[0].lower()):
            title_text = normalize.escape_ordered_list_prefix(display_name)
            links: list[str] = []
            if link_obj:
                links.append(f"[Problem]({link_obj.url})")
            links.extend(solution_link_entries)
            links_text = " | ".join(links)
            lines.append(f"- {title_text} ({links_text})")
        lines.append("")

    uncategorized = category_map.get(config.DEFAULT_CATEGORY, [])
    if uncategorized:
        lines.append(f"## {config.DEFAULT_CATEGORY}")
        for display_name, link_obj, solution_link_entries in sorted(uncategorized, key=lambda item: item[0].lower()):
            title_text = normalize.escape_ordered_list_prefix(display_name)
            links: list[str] = []
            if link_obj:
                links.append(f"[Problem]({link_obj.url})")
            links.extend(solution_link_entries)
            links_text = " | ".join(links)
            lines.append(f"- {title_text} ({links_text})")
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
