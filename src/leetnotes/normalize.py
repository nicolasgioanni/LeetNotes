"""String normalisation helpers."""

from __future__ import annotations

import re

from . import config


def format_frontend_id(frontend_id: str) -> str:
    """Pad numeric frontend identifiers with leading zeros."""

    cleaned = frontend_id.strip()
    if cleaned.isdigit():
        return f"{int(cleaned):04d}"
    return cleaned


def canonical_problem_number(value: str) -> str:
    """Normalise problem numbers by stripping leading zeros."""

    cleaned = value.strip()
    if cleaned.isdigit():
        return str(int(cleaned))
    return cleaned


def clean_problem_title(title: str) -> str:
    """Remove trailing annotations in parentheses from a problem title."""

    cleaned = title.strip()
    return re.sub(r"\s*\([^)]*\)\s*$", "", cleaned)


def escape_ordered_list_prefix(text: str) -> str:
    """Escape leading ordered-list markers so Markdown keeps numbering."""

    return re.sub(r'^(\d+)\.', r'\1\.', text)


def split_categories(raw: str) -> list[str]:
    """Split category strings on commas, slashes, or newlines."""

    if not raw:
        return []
    parts = re.split(r"[,/]|\n", raw)
    return [part.strip() for part in parts if part.strip()]


def slugify(value: str) -> str:
    """Convert text into a filesystem-friendly slug."""

    value = value.lower()
    value = re.sub(r"[^a-z0-9\s-]", "", value)
    value = re.sub(r"[\s_-]+", "-", value).strip("-")
    return value or "untitled-problem"


def format_cell(value: str) -> str:
    """Normalise CSV cell content for Markdown rendering."""

    text = (value or "").strip()
    if not text:
        return ""

    lowered = text.lower()
    if lowered.startswith("http://") or lowered.startswith("https://"):
        return f"[link]({text})"

    return " ".join(text.split())


def format_notes(value: str) -> list[tuple[int, str]]:
    """Normalise a freeform notes field into bullet lines with indentation metadata."""

    text = (value or "").replace("<br>", "\n")
    text = text.replace("\r\n", "\n").replace("\r", "\n")
    raw_lines = text.split("\n")

    entries: list[tuple[int, str]] = []

    for raw_line in raw_lines:
        if not raw_line.strip():
            continue
        expanded = raw_line.expandtabs(2).rstrip()
        if not expanded:
            continue
        stripped = expanded.lstrip(" ")
        indent_width = len(expanded) - len(stripped)
        indent_level = indent_width // 2
        content = stripped
        marker_level = 0
        while True:
            for prefix in config.NOTE_PREFIXES:
                if content.startswith(prefix):
                    content = content[len(prefix):]
                    marker_level += 1
                    break
            else:
                break
            content = content.lstrip(" ")
        formatted = format_cell(content.strip())
        if formatted:
            entries.append((indent_level + marker_level, formatted))

    if not entries:
        return []

    min_level = min(level for level, _ in entries)
    return [(level - min_level, text) for level, text in entries]



__all__ = [
    "canonical_problem_number",
    "clean_problem_title",
    "escape_ordered_list_prefix",
    "format_cell",
    "format_frontend_id",
    "format_notes",
    "slugify",
    "split_categories",
]
