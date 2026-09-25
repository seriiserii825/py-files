import os

from py_libs.CsvFile import CsvFile
from rich import print

CSV_HEADER = ["original", "to-replace"]
REPLACE_CSV_PATH = os.path.expanduser("~/Downloads/replace.csv")


def ensureReplaceCsv(csv_path: str = REPLACE_CSV_PATH) -> bool:
    """
    Create replace.csv with the expected header if it doesn't exist yet.
    Returns True if the file was just created.
    """
    if os.path.exists(csv_path):
        return False

    os.makedirs(os.path.dirname(csv_path), exist_ok=True)
    CsvFile(csv_path).write_csv([], fieldnames=CSV_HEADER)
    print(f"[yellow]{csv_path} not found — created a new empty file.")
    return True


def getReplaceRows(csv_path: str = REPLACE_CSV_PATH) -> list:
    """
    Read the original/to-replace pairs from replace.csv (in ~/Downloads),
    skipping incomplete rows. Wrap a value in double quotes if it contains
    a comma, e.g. "var(--White, #fff)",#fff
    """
    if ensureReplaceCsv(csv_path):
        return []

    rows = CsvFile(csv_path).read_csv() or []
    if not rows:
        print(f"[yellow]{csv_path} is empty (only the header row).")
        return []

    result = []
    for row in rows:
        original = (row.get("original") or "").strip()
        to_replace = (row.get("to-replace") or "").strip()
        if original and to_replace:
            result.append((original, to_replace))

    if not result:
        print(f"[red]No valid rows found in {csv_path}")

    return result
