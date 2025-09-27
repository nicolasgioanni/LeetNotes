"""Helpers for resolving LeetCode problem URLs."""

from __future__ import annotations

import json
import re
import threading
import urllib.error
import urllib.request
from typing import Optional

from .models import ProblemLink

KNOWN_SLUGS: dict[str, str] = {
    "1 Bit and 2 Bit Characters": "1-bit-and-2-bit-characters",
    "Three Sum": "3sum",
    "Maximum Depth of Binary Tree (DFS)": "maximum-depth-of-binary-tree",
    "Same Tree (DFS)": "same-tree",
    "Subtree of Another Tree (DFS)": "subtree-of-another-tree",
}

_GRAPHQL_URL = "https://leetcode.com/graphql"
_GRAPHQL_QUERY = (
    "query questionData($titleSlug: String!) {\n"
    "  question(titleSlug: $titleSlug) {\n"
    "    questionId\n"
    "    questionFrontendId\n"
    "  }\n"
    "}\n"
)
_CACHE_LOCK = threading.Lock()
_QUESTION_CACHE: dict[str, Optional[str]] = {}


def lookup_problem(title: str) -> ProblemLink:
    """Best-effort resolution of a LeetCode problem title."""

    slug = KNOWN_SLUGS.get(title)
    if not slug:
        slug = _slugify(title)

    frontend_id = _question_frontend_id(slug)
    return ProblemLink(title=title, slug=slug, frontend_id=frontend_id)


def _slugify(value: str) -> str:
    value = value.lower()
    value = re.sub(r"[^a-z0-9\s-]", "", value)
    value = re.sub(r"[\s_-]+", "-", value).strip("-")
    return value or "untitled-problem"


def _question_frontend_id(slug: str) -> Optional[str]:
    with _CACHE_LOCK:
        if slug in _QUESTION_CACHE:
            return _QUESTION_CACHE[slug]

    payload = json.dumps(
        {
            "operationName": "questionData",
            "variables": {"titleSlug": slug},
            "query": _GRAPHQL_QUERY,
        }
    ).encode("utf-8")

    request = urllib.request.Request(
        _GRAPHQL_URL,
        data=payload,
        headers={
            "Content-Type": "application/json",
            "Referer": f"https://leetcode.com/problems/{slug}/",
            "User-Agent": "Mozilla/5.0 (compatible; LeetCodeNotesBot/1.0)",
        },
    )

    result: Optional[str] = None
    try:
        with urllib.request.urlopen(request, timeout=15) as response:
            data = json.load(response)
        question = data.get("data", {}).get("question")
        if question:
            result = question.get("questionFrontendId") or question.get("questionId")
    except urllib.error.URLError:
        result = None

    with _CACHE_LOCK:
        _QUESTION_CACHE[slug] = result
    return result


__all__ = ["KNOWN_SLUGS", "lookup_problem"]
