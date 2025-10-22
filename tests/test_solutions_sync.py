from __future__ import annotations

from pathlib import Path

import pytest

from leetnotes import repo, solutions
from leetnotes.models import MetadataMap, NotesProfile, ProblemLink


def _profile(tmp_path: Path) -> NotesProfile:
    return NotesProfile(
        slug="test",
        name="Test Profile",
        env_var="TEST_SHEET",
        notes_output_path=tmp_path / "Notes" / "test.md",
        problems_dir=tmp_path / "Problems",
        problems_index_path=tmp_path / "Problems" / "README.md",
        notes_title="Test Notes",
        index_title="Test Index",
        solutions_env_var="TEST_SOLUTIONS",
    )


def _stub_lookup_problem(title: str) -> ProblemLink:
    slug = title.lower().replace(" ", "-")
    return ProblemLink(title=title, slug=slug, frontend_id="123")


def test_sync_creates_language_specific_files(monkeypatch: pytest.MonkeyPatch, tmp_path: Path) -> None:
    profile = _profile(tmp_path)
    profile.problems_dir.mkdir(parents=True, exist_ok=True)
    monkeypatch.setattr(repo, "lookup_problem", _stub_lookup_problem)

    rows = [{"Problem": "Grid Traveler", "Category": "Dynamic Programming"}]
    metadata: MetadataMap = repo.ensure_problem_folders(rows, profile)

    solution_fieldnames = ["Problems", "Category", "Solution 1", "Solution 2"]
    solution_rows = [
        {
            "Problems": "Grid Traveler",
            "Category": "Dynamic Programming",
            "Solution 1": "```python\nclass Solution:\n    def solve(self):\n        return 1\n```",
            "Solution 2": "```java\nclass Solution {\n    int solve() {\n        return 1;\n    }\n}\n```",
        }
    ]

    sanitized_rows = solutions.sync_solutions_from_rows(
        solution_fieldnames,
        solution_rows,
        metadata,
        profile,
    )

    assert sanitized_rows == [
        {"Problem": "Grid Traveler", "Category": "Dynamic Programming"},
    ]

    problem_folder = profile.problems_dir / "0123. Grid Traveler"
    assert (problem_folder / "solution1.py").read_text(encoding="utf-8").startswith("class Solution:")
    assert (problem_folder / "solution2.java").read_text(encoding="utf-8").startswith("class Solution {")
    assert not (problem_folder / "solution.py").exists()

    meta = metadata["Grid Traveler"]
    assert meta.solutions == ("solution1.py", "solution2.java")

    # Simulate a subsequent ensure pass and confirm placeholder is not recreated.
    repo.ensure_problem_folders(
        [{"Problem": "Grid Traveler", "Category": "Dynamic Programming"}],
        profile,
    )
    assert not (problem_folder / "solution.py").exists()


def test_sync_skips_empty_solutions(monkeypatch: pytest.MonkeyPatch, tmp_path: Path) -> None:
    profile = _profile(tmp_path)
    profile.problems_dir.mkdir(parents=True, exist_ok=True)
    monkeypatch.setattr(repo, "lookup_problem", _stub_lookup_problem)

    rows = [{"Problem": "Three Sum", "Category": "Array"}]
    metadata: MetadataMap = repo.ensure_problem_folders(rows, profile)

    solution_fieldnames = ["Problems", "Category", "Solution 1"]
    solution_rows = [
        {"Problems": "Three Sum", "Category": "Array", "Solution 1": "  "},
    ]

    solutions.sync_solutions_from_rows(
        solution_fieldnames,
        solution_rows,
        metadata,
        profile,
    )

    problem_folder = profile.problems_dir / "0123. Three Sum"
    assert (problem_folder / "solution.py").exists()

    meta = metadata["Three Sum"]
    assert meta.solutions == ("solution.py",)


def test_sync_detects_cpp_extension(monkeypatch: pytest.MonkeyPatch, tmp_path: Path) -> None:
    profile = _profile(tmp_path)
    profile.problems_dir.mkdir(parents=True, exist_ok=True)
    monkeypatch.setattr(repo, "lookup_problem", _stub_lookup_problem)

    rows = [{"Problem": "Graph Paths", "Category": "Graphs"}]
    metadata: MetadataMap = repo.ensure_problem_folders(rows, profile)

    cpp_code = "#include <vector>\nusing namespace std;\nint solve(vector<int>& nums) {\n    return nums.size();\n}"

    solution_fieldnames = ["Problems", "Category", "Solution 1"]
    solution_rows = [
        {"Problems": "Graph Paths", "Category": "Graphs", "Solution 1": cpp_code},
    ]

    solutions.sync_solutions_from_rows(
        solution_fieldnames,
        solution_rows,
        metadata,
        profile,
    )

    problem_folder = profile.problems_dir / "0123. Graph Paths"
    assert (problem_folder / "solution1.cpp").exists()
    assert metadata["Graph Paths"].solutions == ("solution1.cpp",)
