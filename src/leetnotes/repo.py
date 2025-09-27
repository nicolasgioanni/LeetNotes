"""Filesystem operations for the leetnotes package."""

from __future__ import annotations

import re
import shutil
from pathlib import Path
from typing import Optional

from . import config, normalize
from .leetcode import lookup_problem
from .models import MetadataMap, NotesProfile, ProblemMetadata


def ensure_problem_folders(rows: list[dict[str, str]], profile: NotesProfile) -> MetadataMap:
    """Ensure a directory and placeholder solution exists for each problem."""

    metadata: MetadataMap = {}
    base_dir = profile.problems_dir
    for row in rows:
        problem = (row.get("Problem") or "").strip()
        if not problem:
            continue

        link = lookup_problem(problem)
        frontend_id = (link.frontend_id or "").strip()
        folder_title = problem
        legacy_numbered_title: Optional[str] = None
        if frontend_id:
            padded_id = normalize.format_frontend_id(frontend_id)
            folder_title = f"{padded_id}. {problem}"
            if padded_id != frontend_id:
                legacy_numbered_title = f"{frontend_id}. {problem}"

        folder_name = folder_name_from_title(folder_title)
        target_folder = base_dir / folder_name

        legacy_candidates = [
            base_dir / normalize.slugify(problem),
            base_dir / folder_name_from_title(problem),
        ]
        if legacy_numbered_title:
            legacy_candidates.append(
                base_dir / folder_name_from_title(legacy_numbered_title)
            )

        for legacy in legacy_candidates:
            if legacy.exists() and legacy != target_folder:
                migrate_folder_contents(legacy, target_folder)

        target_folder.mkdir(parents=True, exist_ok=True)

        solution_path = target_folder / "solution.py"
        if not solution_path.exists():
            placeholder = f"# TODO: implement solution for {problem}\n"
            solution_path.write_text(placeholder, encoding="utf-8")

        if link.frontend_id:
            for legacy in legacy_candidates:
                if legacy != target_folder:
                    remove_directory(legacy)

        metadata[problem] = ProblemMetadata(folder_name=folder_name, link=link)

    return metadata


def migrate_folder_contents(source: Path, target: Path) -> None:
    """Move legacy folder contents into the target directory."""

    target.mkdir(parents=True, exist_ok=True)
    for item in list(source.iterdir()):
        destination = target / item.name
        if destination.exists():
            if destination.is_file() and item.is_file():
                if destination.name == "solution.py":
                    try:
                        dest_text = destination.read_text(encoding="utf-8")
                    except OSError:
                        dest_text = ""
                    try:
                        src_text = item.read_text(encoding="utf-8")
                    except OSError:
                        src_text = ""
                    if dest_text.startswith("# TODO") and src_text and not src_text.startswith("# TODO"):
                        destination.write_text(src_text, encoding="utf-8")
                try:
                    item.unlink()
                except FileNotFoundError:
                    pass
            elif item.is_dir():
                migrate_folder_contents(item, destination)
                try:
                    item.rmdir()
                except OSError:
                    pass
            continue
        item.rename(destination)
    try:
        source.rmdir()
    except OSError:
        shutil.rmtree(source, ignore_errors=True)


def folder_name_from_title(title: str) -> str:
    """Derive a normalised folder name from a problem title."""

    name = title.strip()
    if not name:
        return "Untitled Problem"
    for char in config.INVALID_FOLDER_CHARS:
        name = name.replace(char, " ")
    name = re.sub(r"\s+", " ", name)
    return name.strip()


def remove_directory(path: Path) -> None:
    """Remove a directory tree, tolerating missing paths."""

    if not path.exists():
        return
    if path.is_symlink():
        try:
            path.unlink()
        except OSError:
            pass
        return
    shutil.rmtree(path, ignore_errors=True)
    if path.exists():
        try:
            path.rmdir()
        except OSError:
            pass


def write_if_changed(path: Path, content: str) -> None:
    """Write content to disk if it differs from the existing file."""

    path.parent.mkdir(parents=True, exist_ok=True)
    if path.exists():
        existing = path.read_text(encoding="utf-8")
        if existing == content:
            return
    path.write_text(content, encoding="utf-8")


__all__ = [
    "ensure_problem_folders",
    "folder_name_from_title",
    "migrate_folder_contents",
    "remove_directory",
    "write_if_changed",
]
