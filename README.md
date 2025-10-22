# LeetNotes: Automated LeetCode Notes

A structured workspace for solving LeetCode problems and maintaining high-quality study notes. The repository couples a simple Python CLI with a Google Sheets source to keep solutions, notes, and indexes synchronized.

## Objectives

- Solve or review at least one problem every day and log the result immediately.
- Maintain a clear, navigable record of solved problems.  
- Capture approach, edge cases, and time/space complexity for easy review.  
- Keep folders and indexes consistent through automated generation.
- Let automation rebuild notes each morning, then skim the diff to stay accountable.

## Repository Structure

- **Notes/**  
  - `blind75.md`: Auto-generated study notes based on the **Notes Sheet**.  
- **Problems/**  
  - `<Problem Title>/solution.py`: Generated from the **Solutions Sheet** for that problem title.  
- **src/leetnotes/**  
  - CLI and helper scripts for reading the sheets, normalizing titles/slugs, generating notes, and writing solution files.  
- **tests/**  
  - Unit tests for the renderers and utilities.  
- **.github/workflows/**  
  - `notes.yml`: Workflow that runs on a schedule to update notes and solution files.  
- **pyproject.toml**  
  - Build metadata for the CLI package.  
- **README.md**  
  - Documentation for the repository.  

## How the Sync Works

1. Two CSV inputs per list:  
   - Notes Sheet (CSV) — problem title, category, approach, time/space complexity, and study notes.  
   - Solutions Sheet (CSV) — problem title and **solution code** in a `solution` column (plain text).  
2. The CLI resolves each **problem title** to the official LeetCode slug/URL and **normalizes the repository layout** so every problem has a dedicated folder.  
3. The CLI **writes `solution.py`** using the code found in the **Solutions Sheet** for that problem. If multiple variants are provided (e.g., “Two Pointers”, “Heap”), files are suffixed accordingly.  
4. The CLI generates the notes file under `Notes/` (for example `Notes/blind75.md`) from the **Notes Sheet**.  
5. A GitHub Actions workflow (`.github/workflows/notes.yml`) runs the CLI on a schedule and commits any changes (new notes or updated solution files).  

## Conventions

- Each problem has its own directory under `Problems/` using the official title (optionally prefixed by its problem number).  
- The **canonical implementation** is written to `solution.py` from the **Solutions Sheet**. Additional variants can be added as `solution_<variant>.py`.  
- Complexity analysis and narrative notes are stored in the generated Markdown under `Notes/`, not inside the solution code.  
- The CLI preserves code formatting from the sheet and aligns with LeetCode-style function signatures.  

## Adding a New Problem

1. **Solve the problem on LeetCode.**  
2. **Update the Notes Sheet** (CSV) with: problem title, category, approach, time complexity, space complexity, and notes.  
3. **Add the solution code to the Solutions Sheet** (CSV):  
   - Use the exact **problem title** in the title column.  
   - Put your **Python solution code** in the `solution` column (plain text; no code fences).  
4. **Run the CLI** locally or wait for the GitHub Actions workflow to run. The CLI will:  
   - Create/update `Problems/<Problem Title>/solution.py` **from the Solutions Sheet**.  
   - Regenerate `Notes/blind75.md` **from the Notes Sheet**.  

## Additional Note Sets

This repository supports **multiple curated lists**, each with its own pair of sheets (Notes + Solutions). Examples include Blind 75, NeetCode 150, or any custom set you design.

### How to Add Another Note Set

1. Prepare **two Google Sheets** for the new list with the same schema as above:  
   - **Notes Sheet**: problem title, category, approach, time/space complexity, notes.  
   - **Solutions Sheet**: problem title, `solution` (Python code).  
2. Publish both sheets to CSV and copy their URLs.  
3. Set environment variables for the new list (example: NeetCode 150):  
   ```bash
   export SHEET_CSV_URL_NEETCODE150_NOTES="<csv-url-notes>"
   export SHEET_CSV_URL_NEETCODE150_SOLUTIONS="<csv-url-solutions>"
   ```
4. Run the CLI with a matching profile name:  
   ```bash
   leetnotes --profile neetcode150
   ```

### What Happens

- Notes are generated at: `Notes/neetcode150.md`  
- Solutions are written under: `Problems/NeetCode150/`  
- The profile mapping for the two CSV URLs is defined in `src/leetnotes/config.py`. You can add as many profiles as you need.  

### Example

For a custom “Dynamic Programming 50” set:  
```bash
export SHEET_CSV_URL_DP50_NOTES="<csv-url-notes>"
export SHEET_CSV_URL_DP50_SOLUTIONS="<csv-url-solutions>"
leetnotes --profile dp50
```

This will generate:  
- `Notes/dp50.md`  
- `Problems/DP50/`  

The scheduled workflow will keep both notes and solution files up to date whenever you change either sheet.

## License
This project is licensed under the MIT License. see the LICENSE file for details.
