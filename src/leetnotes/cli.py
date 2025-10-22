"""Command-line interface for leetnotes."""

from __future__ import annotations

import argparse
import sys
from typing import Sequence

from . import config
from .service import run


def main(argv: Sequence[str] | None = None) -> int:
    """Entry point used by the console script."""

    parser = argparse.ArgumentParser(prog="leetnotes", description="Generate notes from a LeetCode spreadsheet.")
    parser.add_argument(
        "--profile",
        choices=config.available_profiles(),
        default=config.DEFAULT_PROFILE.slug,
        help="Note profile to generate (default: %(default)s)",
    )
    parser.add_argument(
        "--csv-url",
        help="Override the configured environment variable with an explicit CSV URL.",
    )
    parser.add_argument(
        "--solutions-csv-url",
        help="Override the configured solutions environment variable with an explicit CSV URL.",
    )
    args = parser.parse_args(list(argv) if argv is not None else None)

    return run(
        profile_slug=args.profile,
        csv_url=args.csv_url,
        solutions_csv_url=args.solutions_csv_url,
    )


if __name__ == "__main__":
    sys.exit(main())


__all__ = ["main"]
