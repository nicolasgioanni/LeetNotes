"""Smoke tests for leetnotes renderers."""

from __future__ import annotations

from leetnotes import config
from leetnotes.models import ProblemLink, ProblemMetadata
from leetnotes.normalize import clean_problem_title
from leetnotes.render_index import build_problem_index
from leetnotes.render_notes import build_notes_markdown


BLIND75 = config.get_profile("blind75")
NEETCODE150 = config.get_profile("neetcode150")


def test_build_notes_markdown_includes_problem_links() -> None:
    fieldnames = ["Problem", "Category", "Notes"]
    rows = [
        {
            "Problem": "Two Sum",
            "Category": "Array & Hashing",
            "Notes": "Remember to use a hash map.",
        }
    ]
    link = ProblemLink(title="Two Sum", slug="two-sum", frontend_id="1")
    metadata = {
        "Two Sum": ProblemMetadata(folder_name="0001. Two Sum", link=link, solutions=("solution.py",)),
    }

    result = build_notes_markdown(fieldnames, rows, "https://example.com", metadata, BLIND75)

    assert "**Two Sum**" in result
    assert "[Problem](https://leetcode.com/problems/two-sum/)" in result
    assert "[Solution](../Problems/0001.%20Two%20Sum)" in result
    assert "Remember to use a hash map." in result


def test_build_problem_index_groups_by_category() -> None:
    rows = [
        {
            "Problem": "Two Sum",
            "Category": "Array & Hashing",
        },
        {
            "Problem": "Binary Search",
            "Category": "Binary Search",
        },
    ]
    metadata = {
        "Two Sum": ProblemMetadata(folder_name="0001. Two Sum", link=None, solutions=("solution.py",)),
        "Binary Search": ProblemMetadata(folder_name="0704. Binary Search", link=None, solutions=("solution.py",)),
    }

    result = build_problem_index(rows, metadata, BLIND75)

    assert "## Array & Hashing" in result
    assert "## Binary Search" in result
    assert "./0001.%20Two%20Sum" in result
    assert "./0704.%20Binary%20Search" in result


def test_alternate_profile_updates_solution_links() -> None:
    fieldnames = ["Problem", "Category"]
    rows = [
        {
            "Problem": "LRU Cache",
            "Category": "Linked List",
        }
    ]
    metadata = {
        "LRU Cache": ProblemMetadata(folder_name="NeetCode150/0146. LRU Cache", link=None, solutions=("solution.py",)),
    }

    notes_output = build_notes_markdown(fieldnames, rows, "https://example.com", metadata, NEETCODE150)
    index_output = build_problem_index(rows, metadata, NEETCODE150)

    assert "../Problems/NeetCode150/0146.%20LRU%20Cache" in notes_output
    assert "./NeetCode150/0146.%20LRU%20Cache" in index_output
    assert "# NeetCode 150 Notes" in notes_output
    assert "# My Solved LeetCode Problem Index" in index_output


def test_renderers_include_multiple_solution_links() -> None:
    rows = [
        {
            "Problem": "Two Sum",
            "Category": "Array & Hashing",
        }
    ]
    metadata = {
        "Two Sum": ProblemMetadata(
            folder_name="0001. Two Sum",
            link=None,
            solutions=("solution1.py", "solution2.java"),
        )
    }

    notes_output = build_notes_markdown(["Problem", "Category"], rows, "https://example.com", metadata, BLIND75)
    index_output = build_problem_index(rows, metadata, BLIND75)

    assert "[Solutions](../Problems/0001.%20Two%20Sum)" in notes_output
    assert "[Solutions](./0001.%20Two%20Sum)" in index_output


def test_problem_index_deduplicates_duplicate_rows() -> None:
    rows = [
        {"Problem": "Two Sum", "Category": "Array & Hashing"},
        {"Problem": "Two Sum ", "Category": "Array & Hashing"},
    ]
    metadata = {
        "Two Sum": ProblemMetadata(folder_name="0001. Two Sum", link=None, solutions=("solution.py",)),
    }

    result = build_problem_index(rows, metadata, BLIND75)
    assert result.count("./0001.%20Two%20Sum") == 1


def test_notes_markdown_deduplicates_duplicate_rows() -> None:
    fieldnames = ["Problem", "Category"]
    rows = [
        {"Problem": "Two Sum", "Category": "Array & Hashing"},
        {"Problem": "Two Sum", "Category": "Array & Hashing"},
    ]
    metadata = {
        "Two Sum": ProblemMetadata(folder_name="0001. Two Sum", link=None, solutions=("solution.py",)),
    }

    result = build_notes_markdown(fieldnames, rows, "https://example.com", metadata, BLIND75)
    assert result.count("**Two Sum**") == 1


def test_clean_problem_title_strips_annotations() -> None:
    assert clean_problem_title("Same Tree (DFS)") == "Same Tree"
    assert clean_problem_title("Word Search (Backtracking)") == "Word Search"
