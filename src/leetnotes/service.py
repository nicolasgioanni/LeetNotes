"""Orchestration layer for generating notes and indexes."""

from __future__ import annotations

import os
import sys

from . import catalog, config, csv_source, repo
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
    repo.write_if_changed(profile.notes_output_path, notes_markdown)

    # Update the shared problem catalog and rebuild the aggregated index.
    problem_catalog = catalog.load_catalog(config.PROBLEMS_CATALOG_PATH)
    catalog.update_catalog(problem_catalog, rows, metadata, profile.slug)
    catalog.save_catalog(config.PROBLEMS_CATALOG_PATH, problem_catalog)

    aggregated_rows, aggregated_metadata = catalog.catalog_rows_and_metadata(problem_catalog)
    index_markdown = build_problem_index(aggregated_rows, aggregated_metadata, config.DEFAULT_PROFILE)
    repo.write_if_changed(config.PROBLEMS_INDEX_PATH, index_markdown)
    return 0


__all__ = ["run"]