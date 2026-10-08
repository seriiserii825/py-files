import re
import shlex
import subprocess

from py_libs.Select import Select
from rich import print
from rich.markup import escape
from rich.panel import Panel


def showOccurrences(file_extensions, search_string, excluded_dirs):
    include_flags = [f"--include=*.{ext}" for ext in file_extensions]
    exclude_flags = [f"--exclude-dir={d}" for d in excluded_dirs]
    # -F: search the literal string (no regex), args are passed without a shell,
    # so quotes/brackets/$ etc. in search_string need no escaping.
    # -w only makes sense when the string starts and ends with a word char,
    # otherwise e.g. "('products')" inside "get_field('products')" is never matched.
    word_flag = ["-w"] if re.fullmatch(r"\w(.*\w)?", search_string, re.S) else []

    list_command = ["grep", "-rlIF", *word_flag, *include_flags, *exclude_flags, "-e", search_string, "."]
    print(Panel(f"[green]command: {escape(shlex.join(list_command))}"))

    result = subprocess.run(list_command, capture_output=True, text=True).stdout
    file_paths = result.strip().split("\n") if result.strip() else []

    if not file_paths:
        print(f"[red]No occurrences found for '{escape(search_string)}'")
        return

    print(f"[green]Occurrences found in {len(file_paths)} files:")
    for file_path in file_paths:
        print(f"- [cyan]{escape(file_path)}")

    selected_files = Select.select_with_fzf(file_paths)
    if not selected_files:
        print("[red]No files selected.")
        return

    for file_path in selected_files:
        command = ["grep", "-nF", *word_flag, "-e", search_string, "--", file_path]
        result = subprocess.run(command, capture_output=True, text=True).stdout
        print(Panel(f"[cyan]{escape(file_path)}[/cyan]\n{escape(result)}"))
