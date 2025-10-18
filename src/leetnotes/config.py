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

NOTE_BULLET_LEVEL_STYLES = (
    {
        "style": "list-style-type: disc;",
    },
    {
        "style": "list-style-type: circle;",
    },
    {
        "style": "list-style-type: square;",
    },
    {
        "style": (
            "list-style-type: none; "
            "list-style-image: url('data:image/svg+xml,%3Csvg%20xmlns%3D%22http://www.w3.org/2000/svg%22%20"
            "viewBox%3D%220%200%2016%2016%22%3E%3Cpolygon%20points%3D%228%2C1%2015%2C8%208%2C15%201%2C8%22%20"
            "fill%3D%22%23000%22/%3E%3C/svg%3E');"
        ),
        "marker": "◆",
    },
    {
        "style": (
            "list-style-type: none; "
            "list-style-image: url('data:image/svg+xml,%3Csvg%20xmlns%3D%22http://www.w3.org/2000/svg%22%20"
            "viewBox%3D%220%200%2016%2016%22%3E%3Cpolygon%20points%3D%223%2C2%2013%2C8%203%2C14%22%20"
            "fill%3D%22%23000%22/%3E%3C/svg%3E');"
        ),
        "marker": "▶",
    },
    {
        "style": (
            "list-style-type: none; "
            "list-style-image: url('data:image/svg+xml,%3Csvg%20xmlns%3D%22http://www.w3.org/2000/svg%22%20"
            "viewBox%3D%220%200%2016%2016%22%3E%3Cpolygon%20points%3D%223%2C2%2013%2C2%2015%2C8%2013%2C14%203%2C14%201%2C8%22%20"
            "fill%3D%22%23000%22/%3E%3C/svg%3E');"
        ),
        "marker": "▹",
    },
)

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
    "NOTE_BULLET_LEVEL_STYLES",
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
