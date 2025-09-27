"""Aggregate metadata across profiles for problem index generation."""

from __future__ import annotations

import json
from dataclasses import dataclass
from pathlib import Path
from typing import Dict, Iterable

from . import config
from .models import MetadataMap, ProblemLink, ProblemMetadata
from .normalize import split_categories


@dataclass
class CatalogEntry:
    folder_name: str
    categories: list[str]
    sources: set[str]
    link: ProblemLink | None


Catalog = Dict[str, CatalogEntry]


def load_catalog(path: Path) -> Catalog:
    if not path.exists():
        return {}
    data = json.loads(path.read_text(encoding="utf-8"))
    catalog: Catalog = {}
    for problem, entry in data.items():
        link_data = entry.get("link")
        link = ProblemLink(**link_data) if link_data else None
        catalog[problem] = CatalogEntry(
            folder_name=entry["folder_name"],
            categories=list(entry.get("categories", [])),
            sources=set(entry.get("sources", [])),
            link=link,
        )
    return catalog


def save_catalog(path: Path, catalog: Catalog) -> None:
    serialisable = {}
    for problem, entry in catalog.items():
        link_dict = (
            {
                "title": entry.link.title,
                "slug": entry.link.slug,
                "frontend_id": entry.link.frontend_id,
            }
            if entry.link
            else None
        )
        serialisable[problem] = {
            "folder_name": entry.folder_name,
            "categories": sorted(set(entry.categories), key=str.lower),
            "sources": sorted(entry.sources),
            "link": link_dict,
        }
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(serialisable, indent=2, sort_keys=True), encoding="utf-8")


def update_catalog(
    catalog: Catalog,
    rows: Iterable[dict[str, str]],
    metadata: MetadataMap,
    profile_slug: str,
) -> None:
    row_map = {}
    for row in rows:
        name = (row.get("Problem") or "").strip()
        if name:
            row_map[name] = row

    current_problems = set()
    for problem, meta in metadata.items():
        row = row_map.get(problem, {})
        raw_categories = row.get("Category") or ""
        categories = split_categories(raw_categories)
        if not categories:
            categories = [config.DEFAULT_CATEGORY]

        entry = catalog.get(problem)
        if entry is None:
            entry = CatalogEntry(
                folder_name=meta.folder_name,
                categories=categories,
                sources={profile_slug},
                link=meta.link,
            )
            catalog[problem] = entry
        else:
            entry.folder_name = meta.folder_name
            entry.link = meta.link or entry.link
            entry.categories = sorted(
                set(entry.categories).union(categories),
                key=str.lower,
            )
            entry.sources.add(profile_slug)
        current_problems.add(problem)

    for problem, entry in list(catalog.items()):
        if profile_slug in entry.sources and problem not in current_problems:
            entry.sources.remove(profile_slug)
            if not entry.sources:
                catalog.pop(problem)


def catalog_rows_and_metadata(catalog: Catalog) -> tuple[list[dict[str, str]], MetadataMap]:
    rows: list[dict[str, str]] = []
    metadata: MetadataMap = {}
    for problem, entry in sorted(catalog.items()):
        rows.append(
            {
                "Problem": problem,
                "Category": ", ".join(entry.categories),
            }
        )
        metadata[problem] = ProblemMetadata(folder_name=entry.folder_name, link=entry.link)
    return rows, metadata
