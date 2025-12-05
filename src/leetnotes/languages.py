"""Language detection and extension helpers for solution files."""

from __future__ import annotations

import re
from typing import Optional

LANGUAGE_ALIASES = {
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

LANGUAGE_EXTENSIONS = {
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

_DEFAULT_LANGUAGE = "python"

_TS_TYPE_ANNOTATION_RE = re.compile(
    r":\s*(?:number|string|boolean|any|unknown|never|void|Promise<|Array<|ReadonlyArray<|Record<|Map<|Set<)",
    re.IGNORECASE,
)
_TS_DECLARATION_RE = re.compile(r"\b(?:interface|type|enum)\s+\w+", re.IGNORECASE)
_TS_ACCESS_MODIFIER_RE = re.compile(
    r"\b(?:public|private|protected|readonly)\s+\w+\s*:", re.IGNORECASE
)


def normalise_language_hint(hint: Optional[str]) -> Optional[str]:
    """Normalise a language hint to a canonical identifier, if recognised."""

    if not hint:
        return None
    cleaned = hint.strip().lower()
    return LANGUAGE_ALIASES.get(cleaned, cleaned if cleaned in LANGUAGE_EXTENSIONS else None)


def extension_for_language(language: str) -> str:
    """Return the preferred file extension for a detected language."""

    return LANGUAGE_EXTENSIONS.get(language, LANGUAGE_EXTENSIONS[_DEFAULT_LANGUAGE])


def detect_language(code_body: str, hint: Optional[str] = None) -> str:
    """Detect the most likely language for a code snippet."""

    normalised_hint = normalise_language_hint(hint)
    if normalised_hint:
        return normalised_hint

    snippet = (code_body or "").strip()
    lowered = snippet.lower()

    if _looks_like_csharp(snippet, lowered):
        return "csharp"
    if _looks_like_java(snippet, lowered):
        return "java"
    if _looks_like_cpp(snippet, lowered):
        return "cpp"
    if _looks_like_c(snippet, lowered):
        return "c"
    if _looks_like_typescript(snippet, lowered):
        return "typescript"
    if _looks_like_javascript(snippet, lowered):
        return "javascript"
    if _looks_like_go(snippet, lowered):
        return "go"
    if _looks_like_rust(snippet, lowered):
        return "rust"
    if _looks_like_swift(snippet, lowered):
        return "swift"
    if _looks_like_kotlin(snippet, lowered):
        return "kotlin"
    if _looks_like_python(snippet, lowered):
        return "python"

    return _DEFAULT_LANGUAGE


def _looks_like_csharp(snippet: str, lowered: str) -> bool:
    return (
        "using system" in lowered
        or ("namespace " in lowered and "namespace std" not in lowered)
        or "console.write" in lowered
        or "ienumerable<" in lowered
        or "ilist<" in lowered
        or "task<" in lowered
        or "async task" in lowered
    )


def _looks_like_java(snippet: str, lowered: str) -> bool:
    return (
        "import java" in lowered
        or "system.out" in lowered
        or "public static void main" in lowered
        or "public class" in lowered
        or (
            "class " in lowered
            and ("boolean" in lowered or "string" in lowered or "list<" in snippet or "@override" in lowered)
        )
    )


def _looks_like_cpp(snippet: str, lowered: str) -> bool:
    if "std::" in snippet or "using namespace std" in lowered:
        return True
    if "cout <<" in lowered or "cin >>" in lowered:
        return True
    if "vector<" in snippet or "unordered_map<" in snippet or "unordered_set<" in snippet:
        return True
    return bool(
        re.search(r"#include\s*<\s*(?:bits/stdc\+\+\.h|iostream|string|vector|queue|stack|map|set|unordered_map|unordered_set)>", lowered)
    )


def _looks_like_c(snippet: str, lowered: str) -> bool:
    if "std::" in snippet or "using namespace std" in lowered or "vector<" in snippet:
        return False
    return (
        "#include <stdio" in lowered
        or "#include <stdlib" in lowered
        or "printf(" in lowered
        or "scanf(" in lowered
        or "malloc(" in lowered
    )


def _looks_like_typescript(snippet: str, lowered: str) -> bool:
    return bool(
        _TS_DECLARATION_RE.search(snippet)
        or _TS_TYPE_ANNOTATION_RE.search(snippet)
        or _TS_ACCESS_MODIFIER_RE.search(snippet)
        or "import type" in lowered
        or "export type" in lowered
        or "implements" in lowered
        or "readonly " in lowered
    )


def _looks_like_javascript(snippet: str, lowered: str) -> bool:
    return (
        "console.log" in lowered
        or lowered.startswith("function ")
        or lowered.startswith("const ")
        or lowered.startswith("let ")
        or lowered.startswith("var ")
        or " => " in snippet
        or "=>{" in snippet
        or "module.exports" in lowered
        or "export default" in lowered
        or re.search(r"\bfunction\s+\w+\s*\(", lowered) is not None
    )


def _looks_like_go(snippet: str, lowered: str) -> bool:
    return (
        lowered.startswith("package ")
        or "package main" in lowered
        or ("func " in lowered and "fmt." in lowered)
    )


def _looks_like_rust(snippet: str, lowered: str) -> bool:
    return (
        lowered.startswith("fn main()")
        or "println!" in lowered
        or "let mut" in lowered
        or re.search(r"\bfn\s+\w+\s*\(", lowered) is not None
    )


def _looks_like_swift(snippet: str, lowered: str) -> bool:
    return (lowered.startswith("import ") and "foundation" in lowered) or (
        "func " in lowered and "->" in snippet
    )


def _looks_like_kotlin(snippet: str, lowered: str) -> bool:
    return (
        "fun main(" in lowered
        or lowered.startswith("fun ")
        or "val " in lowered
    )


def _looks_like_python(snippet: str, lowered: str) -> bool:
    return bool(
        re.search(r"^\s*def\s+\w+", lowered, re.MULTILINE)
        or re.search(r"^\s*class\s+\w+\s*:", lowered, re.MULTILINE)
    )


__all__ = [
    "detect_language",
    "extension_for_language",
    "LANGUAGE_ALIASES",
    "LANGUAGE_EXTENSIONS",
    "normalise_language_hint",
]
