"""Orchestration layer for generating notes and indexes."""

from __future__ import annotations

import os
import sys

from . import catalog, config, csv_source, repo, solutions
from .models import MetadataMap, NotesProfile, ProblemMetadata
from .render_index import build_problem_index
from .render_notes import build_notes_markdown


def _sync_solutions_from_url(
    metadata: MetadataMap,
    profile: NotesProfile,
    url: str,
) -> list[dict[str, str]]:
    raw_solutions_csv, solutions_charset = csv_source.fetch_csv(url)
    solutions_text = csv_source.decode_csv(raw_solutions_csv, solutions_charset)
    solution_fieldnames, solution_rows = csv_source.parse_csv(solutions_text)
    return solutions.sync_solutions_from_rows(
        solution_fieldnames,
        solution_rows,
        metadata,
        profile,
    )


def run(
    profile_slug: str | None = None,
    csv_url: str | None = None,
    solutions_csv_url: str | None = None,
) -> int:
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

    solution_rows_for_catalog: list[dict[str, str]] = []
    solutions_url = solutions_csv_url or (
        os.environ.get(profile.solutions_env_var) if profile.solutions_env_var else None
    )

    if solutions_url:
        try:
            solution_rows_for_catalog = _sync_solutions_from_url(metadata, profile, solutions_url)
        except Exception as exc:  # pragma: no cover - runtime failure path
            print(f"Failed to download solutions CSV: {exc}", file=sys.stderr)
            return 1

    notes_markdown = build_notes_markdown(fieldnames, rows, url, metadata, profile)
    repo.write_if_changed(profile.notes_output_path, notes_markdown)

    # Update the shared problem catalog and rebuild the aggregated index.
    problem_catalog = catalog.load_catalog(config.PROBLEMS_CATALOG_PATH)
    catalog_rows = [dict(row) for row in rows]
    if solution_rows_for_catalog:
        existing = {row.get("Problem"): row for row in catalog_rows if row.get("Problem")}
        for extra_row in solution_rows_for_catalog:
            problem_name = extra_row.get("Problem")
            if not problem_name:
                continue
            existing_row = existing.get(problem_name)
            if existing_row is None:
                catalog_rows.append(extra_row)
                existing[problem_name] = extra_row
                continue
            extra_category = (extra_row.get("Category") or "").strip()
            if extra_category and not (existing_row.get("Category") or "").strip():
                existing_row["Category"] = extra_category

    catalog.update_catalog(problem_catalog, catalog_rows, metadata, profile.slug)
    catalog.save_catalog(config.PROBLEMS_CATALOG_PATH, problem_catalog)

    aggregated_rows, aggregated_metadata = catalog.catalog_rows_and_metadata(problem_catalog)
    index_markdown = build_problem_index(aggregated_rows, aggregated_metadata, config.DEFAULT_PROFILE)
    repo.write_if_changed(config.PROBLEMS_INDEX_PATH, index_markdown)
    return 0


def sync_solutions(
    profile_slug: str | None = None,
    csv_url: str | None = None,
) -> int:
    """Synchronise solution files and problem index without regenerating notes."""

    try:
        profile = config.get_profile(profile_slug)
    except ValueError as exc:  # pragma: no cover - defensive path
        print(str(exc), file=sys.stderr)
        return 2

    url = csv_url or (
        os.environ.get(profile.solutions_env_var) if profile.solutions_env_var else None
    )
    if not url:
        if profile.solutions_env_var:
            print(f"Environment variable {profile.solutions_env_var} is not set.", file=sys.stderr)
        else:
            print("No solutions CSV URL configured for this profile.", file=sys.stderr)
        return 1

    problem_catalog = catalog.load_catalog(config.PROBLEMS_CATALOG_PATH)

    existing_rows: dict[str, dict[str, str]] = {}
    metadata: MetadataMap = {}

    for problem, entry in problem_catalog.items():
        if profile.slug in entry.sources:
            existing_rows[problem] = {
                "Problem": problem,
                "Category": ", ".join(entry.categories),
            }
            metadata[problem] = ProblemMetadata(folder_name=entry.folder_name, link=entry.link)

    try:
        solution_rows = _sync_solutions_from_url(metadata, profile, url)
    except Exception as exc:  # pragma: no cover - runtime failure path
        print(f"Failed to download solutions CSV: {exc}", file=sys.stderr)
        return 1

    for row in solution_rows:
        problem_name = (row.get("Problem") or "").strip()
        if not problem_name:
            continue
        category = (row.get("Category") or "").strip()
        current = existing_rows.get(problem_name)
        if current and not category:
            row["Category"] = current.get("Category", "")
        existing_rows[problem_name] = row

    combined_rows = list(existing_rows.values())

    catalog.update_catalog(problem_catalog, combined_rows, metadata, profile.slug)
    catalog.save_catalog(config.PROBLEMS_CATALOG_PATH, problem_catalog)

    aggregated_rows, aggregated_metadata = catalog.catalog_rows_and_metadata(problem_catalog)
    index_markdown = build_problem_index(aggregated_rows, aggregated_metadata, config.DEFAULT_PROFILE)
    repo.write_if_changed(config.PROBLEMS_INDEX_PATH, index_markdown)
    return 0


__all__ = ["run", "sync_solutions"]
