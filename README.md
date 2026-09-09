# py-files

Interactive CLI (fzf-driven menu) for finding, renaming and bulk-replacing text across files in a directory tree.

## Features

- **Find file by filename** — walk the current directory tree and list files whose name contains a given substring.
- **Find in files by select** — search for a string across files filtered by extension, excluding chosen directories (`.git`, `venv`, `node_modules`, etc. excluded by default), then pick which matches to inspect via fzf.
- **Replace in files by extension** — find all files containing a string, preview the matching lines, pick files via fzf, and replace the string in them.
- **Replace in files from file** — batch replace using pairs read from `~/Downloads/replace.csv` (columns: `original,to-replace`; the file is auto-created with a header if missing). Wrap a value in double quotes if it contains a comma, e.g. `"var(--White, #fff)",#fff`.
- **Rename files by select** / **Replace and Rename files** — rename a chosen file, optionally replacing its old name with the new one across the codebase first.

## Setup

```bash
uv sync
uv run main.py
```
