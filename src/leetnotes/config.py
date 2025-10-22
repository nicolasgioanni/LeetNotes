"""Central configuration for the leetnotes package."""

from __future__ import annotations

from pathlib import Path

from .models import NotesProfile

REPO_ROOT = Path(__file__).resolve().parents[2]

NOTES_DIR = REPO_ROOT / "Notes"
PROBLEMS_DIR = REPO_ROOT / "Problems"
CATALOG_DIR = REPO_ROOT / "var"
PROBLEMS_CATALOG_PATH = CATALOG_DIR / "catalog.json"

STD_CATEGORY_ORDER = [
    "Array & Hashing",
    "Two Pointers",
    "Sliding Window",
    "Stack",
    "Binary Search",
    "Linked List",
    "Trees",
    "Heap / Priority Queue",
    "Backtracking",
    "Tries",
    "Graphs",
    "Advanced Graphs",
    "1-D Dynamic Programming",
    "2-D Dynamic Programming",
    "Greedy",
    "Intervals",
    "Math & Geometry",
    "Bit Manipulation",
]

CATEGORY_ORDER = STD_CATEGORY_ORDER  # Backwards-compat alias

STANDARD_FIELDS = (
    "Problem",
    "Category",
    "Time Complexity",
    "Space Complexity",
    "Notes",
)

NOTE_PREFIXES = ("- ", "* ", "\u2022 ", "\u2022")

CATEGORY_ALIASES = {
    "Arrays & Hashing": "Array & Hashing",
    "Binary Tree": "Trees",
    "Binary Trees": "Trees",
}

DEFAULT_CATEGORY = "Uncategorized"
INVALID_FOLDER_CHARS = '<>:"/\\|?*'

BLIND75_PROFILE = NotesProfile(
    slug="blind75",
    name="Blind 75",
    env_var="SHEET_CSV_URL",
    notes_output_path=NOTES_DIR / "blind75.md",
    problems_dir=PROBLEMS_DIR,
    problems_index_path=PROBLEMS_DIR / "README.md",
    notes_title="Blind 75 Notes",
    index_title="My Solved LeetCode Problem Index",
    solutions_env_var="SOLUTIONS_CSV_URL",
)

NEETCODE150_PROFILE = NotesProfile(
    slug="neetcode150",
    name="NeetCode 150",
    env_var="SHEET_CSV_URL_NEETCODE150",
    notes_output_path=NOTES_DIR / "neetcode150.md",
    problems_dir=PROBLEMS_DIR,
    problems_index_path=PROBLEMS_DIR / "README.md",
    notes_title="NeetCode 150 Notes",
    index_title=BLIND75_PROFILE.index_title,
    solutions_env_var="SOLUTIONS_CSV_URL_NEETCODE150",
)

_PROFILES = {
    profile.slug: profile
    for profile in (
        BLIND75_PROFILE,
        NEETCODE150_PROFILE,
    )
}

DEFAULT_PROFILE = BLIND75_PROFILE
ENV_SHEET_CSV_URL = DEFAULT_PROFILE.env_var
NOTES_OUTPUT_PATH = DEFAULT_PROFILE.notes_output_path
PROBLEMS_INDEX_PATH = DEFAULT_PROFILE.problems_index_path


def available_profiles() -> list[str]:
    """Return the slugs for all configured note profiles."""

    return sorted(_PROFILES)


def get_profile(slug: str | None = None) -> NotesProfile:
    """Look up a note profile by slug, defaulting to the Blind 75 profile."""

    if slug is None:
        return DEFAULT_PROFILE
    try:
        return _PROFILES[slug]
    except KeyError as exc:  # pragma: no cover - defensive path
        available = ", ".join(available_profiles())
        raise ValueError(f"Unknown profile '{slug}'. Available profiles: {available}") from exc


__all__ = [
    "available_profiles",
    "BLIND75_PROFILE",
    "CATEGORY_ALIASES",
    "CATEGORY_ORDER",
    "DEFAULT_CATEGORY",
    "DEFAULT_PROFILE",
    "ENV_SHEET_CSV_URL",
    "INVALID_FOLDER_CHARS",
    "NEETCODE150_PROFILE",
    "NOTES_DIR",
    "NOTES_OUTPUT_PATH",
    "NOTE_PREFIXES",
    "PROBLEMS_CATALOG_PATH",
    "PROBLEMS_DIR",
    "PROBLEMS_INDEX_PATH",
    "REPO_ROOT",
    "STANDARD_FIELDS",
    "STD_CATEGORY_ORDER",
    "get_profile",
]
