#!/usr/bin/env python3
"""Helpers for resolving LeetCode problem URLs."""
from __future__ import annotations

import re
from dataclasses import dataclass

# Manual overrides for titles whose slug differs from the simple heuristic.
KNOWN_SLUGS: dict[str, str] = {
    "1 Bit and 2 Bit Characters": "1-bit-and-2-bit-characters",  # example pattern
}


@dataclass(frozen=True)
class ProblemLink:
    """Resolved LeetCode problem metadata."""

    title: str
    slug: str

    @property
    def url(self) -> str:
        return f"https://leetcode.com/problems/{self.slug}/"


def slugify(title: str) -> str:
    """Translate a problem title into a LeetCode-style slug."""

    value = title.lower()
    value = re.sub(r"[^a-z0-9\s-]", "", value)
    value = re.sub(r"[\s_-]+", "-", value).strip("-")
    return value


def lookup_problem(title: str) -> ProblemLink:
    """Best-effort resolution of a LeetCode problem title."""

    slug = KNOWN_SLUGS.get(title)
    if not slug:
        slug = slugify(title)
    return ProblemLink(title=title, slug=slug)
