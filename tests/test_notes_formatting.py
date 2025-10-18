"""Unit tests for ordered and nested notes rendering."""

from __future__ import annotations

from leetnotes.config import DEFAULT_PROFILE
from leetnotes.normalize import format_notes
from leetnotes.render_notes import build_notes_markdown


def test_format_notes_detects_numbered_markers() -> None:
    raw = (
        "Idea: Use recursion\n"
        "1) Visit the node\n"
        "2) Traverse neighbors\n"
        "Question: Complexity?"
    )

    entries = format_notes(raw)

    assert entries[0].ordered is False
    assert entries[0].level == 0

    assert entries[1].ordered is True
    assert entries[1].level == 1
    assert entries[1].marker == "1)"

    assert entries[2].ordered is True
    assert entries[2].level == 1
    assert entries[2].order_bump == 1
    assert entries[2].marker == "2)"

    assert entries[3].ordered is False
    assert entries[3].level == 0


def test_build_notes_markdown_renders_ordered_lists_with_html() -> None:
    raw_notes = (
        "Two ways to solve this:\n"
        "- 1) Hash map for counts\n"
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

    assert "<ol type=\"1\">" in markdown
    assert "Hash map for counts" in markdown
    assert "ASCII diff array" in markdown


def test_single_numbered_entry_stays_unordered() -> None:
    raw = "- test\n- 1) only step\n- test"

    entries = format_notes(raw)

    assert [entry.ordered for entry in entries] == [False, False, False]
    assert entries[1].text.startswith("1)")

    markdown = build_notes_markdown(
        ["Problem", "Category", "Notes"],
        [
            {
                "Problem": "Single Ordered",
                "Category": "Misc",
                "Notes": raw,
            }
        ],
        "https://example.com",
        {},
        DEFAULT_PROFILE,
    )

    assert "<ol type=\"1\">" not in markdown
    assert "1) only step" in markdown
    assert markdown.count("<ul>") >= 1


def test_numbered_heading_with_nested_bullets() -> None:
    raw = (
        "1) Edge case, 2) determine head node, 3) merge loop, 4) attach rest\n"
        "- Edge case if lists are None\n"
        "- Compare list.val and set as head and tail, move to next node in list we took node from\n"
        "- Loop while both lists have nodes, attaching smaller node to tail.next and updating tail to tail.next\n"
        "- Tail.next is the node that is not None"
    )

    entries = format_notes(raw)

    assert entries[0].ordered is False
    assert entries[0].level == 0
    assert entries[0].text.startswith("1)")
    assert all(entry.level == 1 for entry in entries[1:])

    markdown = build_notes_markdown(
        ["Problem", "Category", "Notes"],
        [
            {
                "Problem": "Merge Lists",
                "Category": "Linked List",
                "Notes": raw,
            }
        ],
        "https://example.com",
        {},
        DEFAULT_PROFILE,
    )

    assert "<ol type=\"1\">" not in markdown
    assert "1) Edge case" in markdown
    assert markdown.count("<ul>") >= 1


def test_ordered_sections_with_nested_children() -> None:
    raw = (
        "Base Check: If the number of edges isn't equal to the number of nodes minus one, the graph can't be a valid tree\n"
        "Reason: After the first node, each added node needs exactly one new edge to connect them to be a valid tree\n"
        "1) Data Structures:\n"
        "  - Adjacency List: Map nodes to neighbors and back\n"
        "  - Visited Set: Store every node visited for iteration/recursion using dfs/bfs\n"
        "2) Run DFS on any node passing a current node and previous node as parameters:\n"
        "  - Base case: Check if node is in visited\n"
        "  - For every neighbor the current node has, i\n"
        "    - If the neighbor is the previous node, skip it\n"
        "    - If the DFS call on the neighbor nodes is false, return false (caught a cycle)\n"
        "  - If the for loop performed without failing, return True\n"
        "3) Return the boolean result of both (and): \n"
        "  - The DFS call\n"
        "  - Whether or not the number of visited nodes equals the total number of nodes (n)"
    )

    entries = format_notes(raw)

    ordered_levels = [entry.level for entry in entries if entry.marker in {"1)", "2)", "3)"}]
    assert ordered_levels == [1, 1, 1]

    markdown = build_notes_markdown(
        ["Problem", "Category", "Notes"],
        [
            {
                "Problem": "Valid Tree",
                "Category": "Graphs",
                "Notes": raw,
            }
        ],
        "https://example.com",
        {},
        DEFAULT_PROFILE,
    )

    assert markdown.count('<ol type="1">') == 1
    assert '<li>Return the boolean result of both (and):' in markdown
    assert markdown.find('<li>Return the boolean result of both (and):') > markdown.find('<ol type="1">')




