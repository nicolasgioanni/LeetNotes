"""Data structures used throughout the leetnotes package."""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
from typing import Dict, Optional


@dataclass(frozen=True)
class ProblemLink:
    """Resolved LeetCode problem metadata."""

    title: str
    slug: str
    frontend_id: Optional[str] = None

    @property
    def url(self) -> str:
        return f"https://leetcode.com/problems/{self.slug}/"


@dataclass(frozen=True)
class ProblemMetadata:
    """Local repository metadata for a problem."""

    folder_name: str
    link: Optional[ProblemLink]


@dataclass(frozen=True)
class NotesProfile:
    """Configuration describing how to generate a particular note set."""

    slug: str
    name: str
    env_var: str
    notes_output_path: Path
    problems_dir: Path
    problems_index_path: Path
    notes_title: str
    index_title: str


MetadataMap = Dict[str, ProblemMetadata]

__all__ = [
    "MetadataMap",
    "NotesProfile",
    "ProblemLink",
    "ProblemMetadata",
]