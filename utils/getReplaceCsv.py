import csv
import os

from rich import print

CSV_HEADER = ["original", "to-replace"]
REPLACE_CSV_PATH = os.path.expanduser("~/Downloads/replace.tsv")


def ensureReplaceCsv(csv_path: str = REPLACE_CSV_PATH) -> bool:
    """
    Create replace.tsv with the expected header if it doesn't exist yet.
    Returns True if the file was just created.
    """
    if os.path.exists(csv_path):
        return False

    os.makedirs(os.path.dirname(csv_path), exist_ok=True)
    with open(csv_path, "w", newline="") as file:
        csv.writer(file, delimiter="\t").writerow(CSV_HEADER)
    print(f"[yellow]{csv_path} not found — created a new empty file.")
    return True


def getReplaceRows(csv_path: str = REPLACE_CSV_PATH) -> list:
    """
    Read the original/to-replace pairs from replace.tsv (in ~/Downloads),
    skipping incomplete rows.
    """
    if ensureReplaceCsv(csv_path):
        return []

    with open(csv_path, "r", newline="") as file:
        lines = file.readlines()

    if len(lines) <= 1:
        print(f"[yellow]{csv_path} is empty (only the header row).")
        return []

    rows = []
    with open(csv_path, "r", newline="") as file:
        reader = csv.DictReader(file, delimiter="\t")
        for row in reader:
            original = (row.get("original") or "").strip()
            to_replace = (row.get("to-replace") or "").strip()
            if original and to_replace:
                rows.append((original, to_replace))

    if not rows:
        print(f"[red]No valid rows found in {csv_path}")

    return rows
