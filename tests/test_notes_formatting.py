"""Unit tests for ordered and nested notes rendering."""

from __future__ import annotations

from leetnotes.config import DEFAULT_PROFILE
from leetnotes.normalize import NoteEntry, format_notes
from leetnotes.render_notes import build_notes_markdown


def test_format_notes_detects_numbered_markers() -> None:
    raw = (
        "Idea: Use recursion
"
        "1) Visit the node
"
        "2) Traverse neighbors
"
        "Question: Complexity?"
    )

    entries = format_notes(raw)

    assert entries[0] == NoteEntry(level=0, text="Idea: Use recursion", ordered=False)
    assert entries[1] == NoteEntry(level=1, text="Visit the node", ordered=True)
    assert entries[2] == NoteEntry(level=1, text="Traverse neighbors", ordered=True)
    assert entries[3] == NoteEntry(level=0, text="Question: Complexity?", ordered=False)


def test_build_notes_markdown_renders_ordered_lists_with_html() -> None:
    raw_notes = (
        "Two ways to solve this:
"
        "- 1) Hash map for counts
"
        "- 2) ASCII diff array"
    )

    markdown = build_notes_markdown(
        ["Problem", "Category", "Notes"],
        [
            {
                "Problem": "Anagram Check",
                "Category": "Hashing",
                "Notes": raw_notes,
            }
        ],
        "https://example.com",
        {},
        DEFAULT_PROFILE,
    )

    assert "<ol type="1">" in markdown
    assert "Hash map for counts" in markdown
    assert "ASCII diff array" in markdown
    assert "<ul>" in markdown
