"""Synchronise solution source files from a solutions CSV."""

from __future__ import annotations

import re
from dataclasses import replace
from pathlib import Path
from typing import Iterable, Sequence

from . import repo
from .models import MetadataMap, NotesProfile

_CODE_FENCE_RE = re.compile(r"^\s*```(?P<lang>[A-Za-z0-9+#-]*)\s*\n(?P<body>.*)\n```\s*$", re.DOTALL)
_BRACKET_LANG_RE = re.compile(r"^\s*\[(?P<lang>[^\]]+)\]\s*$")
_PREFIX_LANG_RE = re.compile(r"^\s*(?:language\s*[:=]\s*)?(?P<lang>[A-Za-z0-9+#]+)\s*$", re.IGNORECASE)
_SOLUTION_HEADER_PREFIX = re.compile(r"^\s*solution", re.IGNORECASE)
_SOLUTION_COLUMN_INDEX = re.compile(r"(\d+)")

_LANGUAGE_ALIASES = {
    "py": "python",
    "python": "python",
    "python3": "python",
    "java": "java",
    "cpp": "cpp",
    "c++": "cpp",
    "c": "c",
    "js": "javascript",
    "javascript": "javascript",
    "ts": "typescript",
    "typescript": "typescript",
    "go": "go",
    "golang": "go",
    "rust": "rust",
    "swift": "swift",
    "kotlin": "kotlin",
    "scala": "scala",
    "ruby": "ruby",
    "c#": "csharp",
    "csharp": "csharp",
}

_LANGUAGE_EXTENSIONS = {
    "python": ".py",
    "java": ".java",
    "cpp": ".cpp",
    "c": ".c",
    "javascript": ".js",
    "typescript": ".ts",
    "go": ".go",
    "rust": ".rs",
    "swift": ".swift",
    "kotlin": ".kt",
    "scala": ".scala",
    "ruby": ".rb",
    "csharp": ".cs",
}

_EMPTY_TOKENS = {"", "na", "n/a", "none", "-", "--", "todo", "tbd"}


def sync_solutions_from_rows(
    fieldnames: Sequence[str],
    rows: Iterable[dict[str, str]],
    metadata: MetadataMap,
    profile: NotesProfile,
) -> list[dict[str, str]]:
    """Sync solution code from the CSV rows, updating metadata in place."""

    solution_columns = _ordered_solution_columns(fieldnames)
    if not solution_columns:
        return []

    ensure_rows: list[dict[str, str]] = []
    row_refs: list[tuple[dict[str, str], dict[str, str]]] = []
    for row in rows:
        problem_name = _extract_problem_name(row)
        if not problem_name:
            continue
        ensure_row = {
            "Problem": problem_name,
            "Category": (row.get("Category") or "").strip(),
        }
        ensure_rows.append(ensure_row)
        row_refs.append((row, ensure_row))

    if ensure_rows:
        new_metadata = repo.ensure_problem_folders(ensure_rows, profile)
        metadata.update(new_metadata)

    sanitized_rows: dict[str, dict[str, str]] = {}

    for original_row, ensured_row in row_refs:
        sanitized_problem = ensured_row.get("Problem", "").strip()
        if not sanitized_problem:
            continue
        category = (ensured_row.get("Category") or original_row.get("Category") or "").strip()

        sanitized_rows.setdefault(
            sanitized_problem,
            {"Problem": sanitized_problem, "Category": category},
        )
        if category and not (sanitized_rows[sanitized_problem].get("Category") or "").strip():
            sanitized_rows[sanitized_problem]["Category"] = category

        problem_meta = metadata.get(sanitized_problem)
        if problem_meta is None:
            continue
        folder = profile.problems_dir / problem_meta.folder_name

        parsed_solutions: list[tuple[str, str]] = []
        for column in solution_columns:
            raw_value = original_row.get(column, "")
            if not _has_solution_content(raw_value):
                continue
            code_body, lang_hint = _parse_solution_cell(raw_value)
            if not code_body.strip():
                continue
            language = _detect_language(code_body, lang_hint)
            extension = _LANGUAGE_EXTENSIONS.get(language, ".py")
            parsed_solutions.append((extension, _ensure_trailing_newline(code_body)))

        if not parsed_solutions:
            # Leave existing solution files untouched.
            continue

        repo.clear_solution_files(folder)
        filenames: list[str] = []
        for index, (extension, code_body) in enumerate(parsed_solutions, start=1):
            filename = f"solution{index}{extension}"
            repo.write_if_changed(folder / filename, code_body)
            filenames.append(filename)

        placeholder_path = folder / "solution.py"
        if placeholder_path.exists():
            try:
                contents = placeholder_path.read_text(encoding="utf-8")
            except OSError:
                contents = ""
            if contents.strip().startswith("# TODO") or not contents.strip():
                try:
                    placeholder_path.unlink()
                except OSError:
                    pass

        metadata[sanitized_problem] = replace(
            problem_meta,
            solutions=tuple(filenames),
        )

    # Ensure metadata for all problems has an up-to-date solution file listing.
    for problem, meta in list(metadata.items()):
        folder = profile.problems_dir / meta.folder_name
        filenames = repo.list_solution_files(folder)
        placeholder_path = folder / "solution.py"
        if "solution.py" in filenames and len(filenames) > 1:
            if placeholder_path.exists():
                try:
                    placeholder_path.unlink()
                except OSError:
                    pass
            filenames = [name for name in filenames if name != "solution.py"]
        if not filenames:
            filenames = ["solution.py"]
        metadata[problem] = replace(meta, solutions=tuple(filenames))

    return list(sanitized_rows.values())


def _ordered_solution_columns(fieldnames: Sequence[str]) -> list[str]:
    columns: list[tuple[int, int, str]] = []
    for index, name in enumerate(fieldnames):
        if not name:
            continue
        if not _SOLUTION_HEADER_PREFIX.match(name):
            continue
        numeric = _SOLUTION_COLUMN_INDEX.search(name)
        order = int(numeric.group(1)) if numeric else 0
        columns.append((order, index, name))
    columns.sort()
    return [column for _, _, column in columns]


def _extract_problem_name(row: dict[str, str]) -> str:
    for key in ("Problem", "Problems"):
        value = row.get(key)
        if value and value.strip():
            return value.strip()
    return ""


def _has_solution_content(value: str) -> bool:
    text = (value or "").strip()
    return text.lower() not in _EMPTY_TOKENS and bool(text)


def _parse_solution_cell(raw_value: str) -> tuple[str, str | None]:
    text = (raw_value or "").replace("\r\n", "\n").replace("\r", "\n").strip()
    if not text:
        return "", None

    fence_match = _CODE_FENCE_RE.match(text)
    if fence_match:
        lang = fence_match.group("lang") or None
        body = fence_match.group("body")
        return body.strip("\n"), lang

    lines = text.split("\n")
    if lines:
        bracket_match = _BRACKET_LANG_RE.match(lines[0])
        if bracket_match and len(lines) > 1:
            return "\n".join(lines[1:]).strip("\n"), bracket_match.group("lang")
        prefix_match = _PREFIX_LANG_RE.match(lines[0])
        if prefix_match and len(lines) > 1:
            return "\n".join(lines[1:]).strip("\n"), prefix_match.group("lang")

    return text.strip("\n"), None


def _detect_language(code_body: str, hint: str | None) -> str:
    if hint:
        normalised = _LANGUAGE_ALIASES.get(hint.strip().lower(), hint.strip().lower())
        if normalised in _LANGUAGE_EXTENSIONS:
            return normalised

    snippet = code_body.strip()
    lowered = snippet.lower()

    if "import java" in lowered or "public class" in snippet or "System.out" in snippet:
        return "java"
    if "#include" in lowered or "std::" in snippet or "using namespace std" in lowered:
        return "cpp"
    if "#include <stdio" in lowered or "printf(" in snippet:
        return "c"
    if lowered.startswith("def ") or lowered.startswith("class ") or "def " in lowered:
        return "python"
    if "fun main(" in lowered or "val " in lowered:
        return "kotlin"
    if "func " in lowered and "->" in snippet:
        return "swift"
    if "console.log" in lowered or lowered.startswith("function "):
        return "javascript"

    return "python"


def _ensure_trailing_newline(text: str) -> str:
    return text if text.endswith("\n") else f"{text}\n"


__all__ = ["sync_solutions_from_rows"]
