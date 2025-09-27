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


def escape_ordered_list_prefix(text: str) -> str:
    """Escape leading ordered-list markers so Markdown keeps numbering."""

    return re.sub(r"^(\\d+)\\.", r"\\1\\.", text)

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


def format_notes(value: str) -> list[str]:
    """Normalise a freeform notes field into individual bullet points."""

    text = (value or "").replace("<br>", "\n")
    text = text.replace("\r\n", "\n").replace("\r", "\n")
    parts = [part.strip() for part in text.split("\n")]

    cleaned: list[str] = []
    for part in parts:
        if not part:
            continue
        stripped = part
        for prefix in config.NOTE_PREFIXES:
            if stripped.startswith(prefix):
                stripped = stripped[len(prefix):].strip()
                break
        formatted = format_cell(stripped)
        if formatted:
            cleaned.append(formatted)
    return cleaned


__all__ = [
    "canonical_problem_number",
    "escape_ordered_list_prefix",
    "format_cell",
    "format_frontend_id",
    "format_notes",
    "slugify",
    "split_categories",
]
