"""Download and parse CSV content from external sources."""

from __future__ import annotations

import csv
import io
import sys
import time
import urllib.request
from typing import Tuple


def _set_read_timeout(response: urllib.response.addinfourl, read_timeout: float) -> None:
    """Reset the socket timeout for the response read phase."""

    try:
        fp = getattr(response, "fp", None)
        raw = getattr(fp, "raw", None)
        sock = getattr(raw, "_sock", None)
        if sock:
            sock.settimeout(read_timeout)
    except Exception:
        # Soft-fail: if we cannot tweak the socket, keep going with the default timeout.
        return


def fetch_csv(
    url: str,
    *,
    label: str | None = None,
    connect_timeout: float = 10,
    read_timeout: float = 120,
    max_attempts: int = 4,
    backoff_factor: float = 2.0,
) -> Tuple[bytes, str]:
    """Download CSV data from the provided URL with retries and backoff."""

    target_label = label or url
    attempts = max(1, max_attempts)

    last_error: Exception | None = None
    for attempt in range(1, attempts + 1):
        try:
            with urllib.request.urlopen(url, timeout=connect_timeout) as response:  # type: ignore[arg-type]
                status = getattr(response, "status", None)
                if status not in (200, None):
                    raise RuntimeError(f"unexpected HTTP status code: {status}")
                charset = response.headers.get_content_charset() or "utf-8"
                _set_read_timeout(response, read_timeout)
                raw_csv = response.read()
            return raw_csv, charset
        except Exception as exc:  # pragma: no cover - network/runtime failures
            last_error = exc
            if attempt >= attempts:
                break
            delay = backoff_factor ** (attempt - 1)
            print(
                f"Retrying download for {target_label} "
                f"(attempt {attempt}/{attempts - 1} failed: {exc!s}); sleeping {delay:.1f}s.",
                file=sys.stderr,
            )
            time.sleep(delay)

    raise RuntimeError(f"Failed to download {target_label} after {attempts} attempts: {last_error}")


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
