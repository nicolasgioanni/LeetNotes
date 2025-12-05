from __future__ import annotations

from leetnotes import languages


def test_detect_language_prefers_hint_alias() -> None:
    code = "def foo():\n    return 1"
    assert languages.detect_language(code, hint="Py") == "python"
    assert languages.extension_for_language("python") == ".py"


def test_detects_core_languages_by_heuristics() -> None:
    cases = [
        ("#include <stdio.h>\nint main() { return 0; }", None, "c"),
        ("#include <vector>\nusing namespace std;\nint main(){}", None, "cpp"),
        ("public class Solution { public static void main(String[] args) {} }", None, "java"),
        ("const twoSum = (nums, target) => target;", None, "javascript"),
        ("function foo(arr: number[]): number { return arr.length; }", None, "typescript"),
        ("using System;\npublic class Solution {}", None, "csharp"),
        ("def solve():\n    return []", None, "python"),
    ]
    for code, hint, expected in cases:
        assert languages.detect_language(code, hint=hint) == expected


def test_default_language_when_unknown() -> None:
    code = "(* Some pseudo code *)"
    assert languages.detect_language(code, hint=None) == "python"
    assert languages.extension_for_language("unknown") == ".py"
