import os

from rich import print
from rich.panel import Panel

from classes.Select import Select


def showOccurrences(file_extensions, search_string, excluded_dirs):
    include_flags = " ".join([f"--include='*.{ext}'" for ext in file_extensions])
    exclude_flags = " ".join([f"--exclude-dir={d}" for d in excluded_dirs])

    list_command = f"grep -rlw {include_flags} {exclude_flags} -e '{search_string}' ."
    print(Panel(f"[green]command: {list_command}"))

    result = os.popen(list_command).read()
    file_paths = result.strip().split("\n") if result else []

    if not file_paths or file_paths == [""]:
        print(f"[red]No occurrences found for '{search_string}'")
        return

    print(f"[green]Occurrences found in {len(file_paths)} files:")
    for file_path in file_paths:
        print(f"- [cyan]{file_path}")

    selected_files = Select.select_with_fzf(file_paths)
    if not selected_files:
        print("[red]No files selected.")
        return

    for file_path in selected_files:
        command = f"grep -nw -e '{search_string}' '{file_path}'"
        result = os.popen(command).read()
        print(Panel(f"[cyan]{file_path}[/cyan]\n{result}"))
