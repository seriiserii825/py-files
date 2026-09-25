import os

from py_libs.Select import Select
from rich import print
from rich.console import Console

from utils.getExcludedDirs import getExcludedDirs
from utils.getReplaceCsv import REPLACE_CSV_PATH, getReplaceRows

console = Console()


def replaceInFiles(str_to_replace, replacement) -> None:
    occurences = _find_all_occurience(str_to_replace)
    selected_files = _choose_files(occurences, str_to_replace)
    if not selected_files:
        print("[red]No files selected for replacement.")
        return
    _replace_in_files(selected_files, str_to_replace, replacement)


def replaceInFilesFromFile(csv_path: str = REPLACE_CSV_PATH) -> None:
    rows = getReplaceRows(csv_path)
    if not rows:
        return

    rows_with_occurences = []
    all_files = set()
    for str_to_replace, replacement in rows:
        print(f"[bold]Looking for '{str_to_replace}'")
        file_paths = _find_all_occurience(str_to_replace)
        if file_paths:
            rows_with_occurences.append((str_to_replace, replacement, file_paths))
            all_files.update(file_paths)

    if not all_files:
        print("[red]No occurrences found for any row.")
        return

    selected_files = set(Select.select_with_fzf(sorted(all_files)))
    if not selected_files:
        print("[red]No files selected for replacement.")
        return

    for str_to_replace, replacement, file_paths in rows_with_occurences:
        files_to_replace = [f for f in file_paths if f in selected_files]
        if not files_to_replace:
            continue
        _replace_in_files(files_to_replace, str_to_replace, replacement)


def _find_all_occurience(str_to_replace) -> list:
    """
    Find all occurrences of a string in files using bash
    and return file paths where the string is found.
    """
    excluded_dirs = getExcludedDirs()
    # Generate multiple --exclude-dir flags
    exclude_flags = " ".join([f"--exclude-dir={d}" for d in excluded_dirs])
    command = f"grep -rl '{str_to_replace}' . {exclude_flags}"

    result = os.popen(command).read()
    file_paths = result.strip().split("\n") if result else []

    if not file_paths or file_paths == [""]:
        print(f"[red]No occurrences found for '{str_to_replace}'")
        return []
    print(f"[green]Occurrences found in {len(file_paths)} files:")
    for file_path in file_paths:
        print(f"- [cyan]{file_path}")

    return file_paths


def _choose_files(file_paths: list, str_to_replace) -> list:
    if not file_paths:
        return []

    for file_path in file_paths:
        command = f"grep -n '{str_to_replace}' {file_path}"
        result = os.popen(command).read()
        if result:
            print(f"[cyan]Occurrences in {file_path}:\n{result}")

    return Select.select_with_fzf(file_paths)


def _replace_in_files(files: list, str_to_replace: str, replacement: str) -> None:
    """
    Replace the string in the selected files.
    """
    for file_path in files:
        with open(file_path, "r") as file:
            content = file.read()

        new_content = content.replace(str_to_replace, replacement)

        with open(file_path, "w") as file:
            file.write(new_content)

        print(f"[green]Replaced '{str_to_replace}' with '{replacement}' in {file_path}")
