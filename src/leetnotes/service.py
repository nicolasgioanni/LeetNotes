"""Orchestration layer for generating notes and indexes."""

from __future__ import annotations

import os
import sys

from . import config, csv_source, repo
from .render_index import build_problem_index
from .render_notes import build_notes_markdown


def run(profile_slug: str | None = None, csv_url: str | None = None) -> int:
    """Execute the notes generation workflow for the selected profile."""

    try:
        profile = config.get_profile(profile_slug)
    except ValueError as exc:  # pragma: no cover - defensive path
        print(str(exc), file=sys.stderr)
        return 2

    url = csv_url or os.environ.get(profile.env_var)
    if not url:
        print(f"Environment variable {profile.env_var} is not set.", file=sys.stderr)
        return 1

    try:
        raw_csv, charset = csv_source.fetch_csv(url)
    except Exception as exc:  # pragma: no cover - runtime failure path
        print(f"Failed to download CSV: {exc}", file=sys.stderr)
        return 1

    csv_text = csv_source.decode_csv(raw_csv, charset)
    fieldnames, rows = csv_source.parse_csv(csv_text)

    metadata = repo.ensure_problem_folders(rows, profile)

    notes_markdown = build_notes_markdown(fieldnames, rows, url, metadata, profile)
    index_markdown = build_problem_index(rows, metadata, profile)

    repo.write_if_changed(profile.notes_output_path, notes_markdown)
    repo.write_if_changed(profile.problems_index_path, index_markdown)
    return 0


__all__ = ["run"]
