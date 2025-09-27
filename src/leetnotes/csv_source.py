"""Download and parse CSV content from external sources."""

from __future__ import annotations

import csv
import io
import urllib.request
from typing import Tuple


def fetch_csv(url: str) -> Tuple[bytes, str]:
    """Download CSV data from the provided URL."""

    with urllib.request.urlopen(url) as response:  # type: ignore[arg-type]
        status = getattr(response, "status", None)
        if status not in (200, None):
            raise RuntimeError(f"unexpected HTTP status code: {status}")
        charset = response.headers.get_content_charset() or "utf-8"
        raw_csv = response.read()
    return raw_csv, charset


def decode_csv(raw_csv: bytes, charset: str) -> str:
    """Decode raw CSV bytes using the provided charset with a UTF-8 fallback."""

    try:
        return raw_csv.decode(charset, errors="replace")
    except LookupError:
        return raw_csv.decode("utf-8", errors="replace")


def parse_csv(csv_text: str) -> Tuple[list[str], list[dict[str, str]]]:
    """Parse CSV text into fieldnames and row dictionaries."""

    reader = csv.DictReader(io.StringIO(csv_text))
    rows = list(reader)
    fieldnames = list(reader.fieldnames or [])
    return fieldnames, rows


__all__ = ["decode_csv", "fetch_csv", "parse_csv"]
