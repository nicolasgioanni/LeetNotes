"""String normalisation helpers."""

from __future__ import annotations

import re
from dataclasses import dataclass

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


_ORDERED_PREFIX_RE = re.compile(r"^(?:\(\d+\)|\d+[.)])\s+")


@dataclass(frozen=True)
class NoteEntry:
    """Normalized note line with indentation metadata and ordering flag."""

    level: int
    text: str
    ordered: bool = False
    order_bump: int = 0
    marker: str = ""


def format_notes(value: str) -> list[NoteEntry]:
    """Normalise a freeform notes field into bullet lines with indentation metadata."""

    text = (value or "").replace("<br>", "\n")
    text = text.replace("\r\n", "\n").replace("\r", "\n")
    raw_lines = text.split("\n")

    entries: list[NoteEntry] = []

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
            matched_prefix = False
            for prefix in config.NOTE_PREFIXES:
                if content.startswith(prefix):
                    content = content[len(prefix):]
                    marker_level += 1
                    matched_prefix = True
                    break
            if not matched_prefix:
                break
            content = content.lstrip(" ")

        ordered = False
        order_bump = 0
        marker = ""
        while True:
            match = _ORDERED_PREFIX_RE.match(content)
            if not match:
                break
            if not marker:
                marker = match.group(0).rstrip()
            ordered = True
            content = content[match.end():]
            content = content.lstrip(" ")
            if marker_level == 0:
                marker_level = 1
                order_bump = 1

        total_level = indent_level + marker_level
        formatted = format_cell(content.strip())
        if formatted:
            entries.append(NoteEntry(total_level, formatted, ordered, order_bump, marker))

    if not entries:
        return []

    normalized: list[NoteEntry] = []
    idx = 0
    length = len(entries)
    while idx < length:
        entry = entries[idx]
        if entry.ordered:
            level = entry.level
            run: list[NoteEntry] = []
            while idx < length and entries[idx].ordered and entries[idx].level == level:
                run.append(entries[idx])
                idx += 1
            if len(run) == 1:
                only = run[0]
                adjusted_level = only.level
                if only.order_bump and adjusted_level >= only.order_bump:
                    adjusted_level -= only.order_bump
                restored_text = only.text
                if only.marker:
                    restored_text = f"{only.marker} {restored_text}" if restored_text else only.marker
                normalized.append(NoteEntry(adjusted_level, restored_text, False, 0, ""))
            else:
                normalized.extend(run)
            continue
        normalized.append(entry)
        idx += 1

    entries = normalized

    min_level = min(entry.level for entry in entries)
    if min_level > 0:
        entries = [
            NoteEntry(entry.level - min_level, entry.text, entry.ordered, entry.order_bump, entry.marker)
            for entry in entries
        ]
    return entries


__all__ = [
    "canonical_problem_number",
    "clean_problem_title",
    "escape_ordered_list_prefix",
    "format_cell",
    "format_frontend_id",
    "NoteEntry",
    "format_notes",
    "slugify",
    "split_categories",
]
