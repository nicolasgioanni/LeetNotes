# LeetCode Progress Tracker

This repo records my Blind 75 grind: problems solved, lessons learned, and code I can revisit quickly. A Google Sheet stays as the single source of truth, and the repo mirrors it through automation.

## Routine and Goals

- Solve or review at least one problem every day and log the result immediately.
- Capture time and space complexity along with key ideas and pitfalls for fast review later.
- Keep every solution in `Problems/<Problem Title>/solution.py` so implementations stay organized.
- Let automation rebuild notes each morning, then skim the diff to stay accountable.

## Repository Layout

- `Notes/blind75.md` - auto-generated study notes with direct links back to LeetCode and the local solution file.
- `Problems/` - one directory per problem (for example `Two Sum/solution.py`) where I store code, follow-up notes, or tests.
- `src/leetnotes/` - Python package housing the CLI entry point and supporting modules.
- `tests/` - smoke tests that keep the renderers honest as the package evolves.
- `.github/workflows/notes.yml` - scheduled workflow that updates notes at 5 AM Pacific.
- `README.md` - this overview.


## Navigation Tips

- Use `Problems/README.md` to browse by category; each entry links to its folder.
- Open `Notes/blind75.md` when you want a quick reminder of approach, complexity, or edge cases.
- Every heading in the notes file links both to the LeetCode problem and to the matching solution in this repo.

## Automation Pipeline

1. The `leetnotes` CLI reads `SHEET_CSV_URL` (from an env var or GitHub secret) and downloads the Google Sheet as CSV.
2. `leetnotes.leetcode` resolves each problem title to a LeetCode slug so the notes include official problem URLs.
3. `leetnotes.repo` normalizes problem folders and ensures a placeholder `solution.py` exists when needed.
4. `leetnotes.render_notes` and `leetnotes.render_index` rebuild `Notes/blind75.md` and `Problems/README.md` from the spreadsheet data.
5. `.github/workflows/notes.yml` installs the package, runs the CLI daily, and pushes any committed changes.

### Run Locally

```bash
python -m pip install --upgrade pip
python -m pip install .

SHEET_CSV_URL="<csv-url>" leetnotes
```

### Additional Note Sets

Need another curated list? Set the appropriate CSV URL and pick a profile when running the CLI.

```bash
SHEET_CSV_URL_NEETCODE150="<csv-url>" leetnotes --profile neetcode150
```

That profile writes to `Notes/neetcode150.md` and mirrors solutions in `Problems/NeetCode150/`. Feel free to add more profiles in `src/leetnotes/config.py` as your study plans grow.

Update the sheet, run the script (or wait for the workflow), and everything stays current.

## License
This project is licensed under the MIT License. see the LICENSE file for details.
