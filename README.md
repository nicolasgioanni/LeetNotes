# LeetCode Progress Tracker

This repo records my Blind 75 grind: problems solved, lessons learned, and code I can revisit quickly. A Google Sheet stays as the single source of truth, and the repo mirrors it through automation.

## Routine and Goals

- Solve or review at least one problem every day and log the result immediately.
- Capture time and space complexity along with key ideas and pitfalls for fast review later.
- Keep every solution in `Problems/<Problem Title>/solution.py` so implementations stay organized.
- Let automation rebuild notes each morning, then skim the diff to stay accountable.

MIT license applies (see `LICENSE`).

## Repository Layout

- `Notes/blind75.md` — auto-generated study notes with direct links back to LeetCode and the local solution file.
- `Problems/` — one directory per problem (for example `Two Sum/solution.py`) where I store code, follow-up notes, or tests.
- `Scripts/` — automation helpers (`blind75.py`, `linkify_leetcode.py`).
- `.github/workflows/notes.yml` — scheduled workflow that updates notes at 5 AM Pacific.
- `README.md` — this overview.

## Navigation Tips

- Use `Problems/README.md` to browse by category; each entry links to its folder.
- Open `Notes/blind75.md` when you want a quick reminder of approach, complexity, or edge cases.
- Every heading in the notes file links both to the LeetCode problem and to the matching solution in this repo.

## Automation Pipeline

1. `Scripts/blind75.py` reads the `SHEET_CSV_URL` (from an env var or GitHub secret) and downloads the Google Sheet as CSV.
2. `linkify_leetcode.py` maps each problem title to its LeetCode slug so the notes include official problem URLs.
3. The script regenerates `Notes/blind75.md` and `Problems/README.md`, writing per-problem sections with complexities, notes, and dual links.
4. It ensures `Problems/<Problem Title>/solution.py` exists, creating a placeholder only when the file is missing.
5. `.github/workflows/notes.yml` runs daily and on manual dispatch: it executes the script and pushes any changed files back to `main`.

### Run Locally

```bash
SHEET_CSV_URL="<csv-url>" python Scripts/blind75.py
```

Update the sheet, run the script (or wait for the workflow), and everything stays current.
