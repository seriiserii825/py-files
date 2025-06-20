import os
from rich import print
from rich.console import Console
from rich.panel import Panel
from pyfzf.pyfzf import FzfPrompt

from utils.getExcludedDirs import getExcludedDirs

fzf = FzfPrompt()
console = Console()


def replaceInFiles(str_to_replace, replacement) -> None:
    occurences = _find_all_occurience(str_to_replace)
    selected_files = _choose_files(occurences, str_to_replace)
    if not selected_files:
        console.print(Panel(
            "[red]No files selected for replacement.[/red]", title="Error"))
        return
    _replace_in_files(selected_files, str_to_replace, replacement)


def _find_all_occurience(str_to_replace) -> list:
    """
    Find all occurrences of a string in files using bash and return file paths where the string is found.
    """
    excluded_dirs = getExcludedDirs()
    # Generate multiple --exclude-dir flags
    exclude_flags = ' '.join([f"--exclude-dir={d}" for d in excluded_dirs])
    command = f"grep -rl '{str_to_replace}' . {exclude_flags}"

    result = os.popen(command).read()
    file_paths = result.strip().split('\n') if result else []

    if not file_paths or file_paths == ['']:
        console.print(Panel(
            f"No occurrences found for '{str_to_replace}'", title="Result", style="bold red"))
        return []

    console.print(Panel(
        f"Occurrences found in {len(file_paths)} files:", title="Result", style="bold green"))
    for file_path in file_paths:
        console.print(f"- [cyan]{file_path}[/cyan]")

    return file_paths


def _choose_files(file_paths: list, str_to_replace) -> list:
    selected_files = []

    for file_path in file_paths:
        # display string to replace in file with grep
        command = f"grep -n '{str_to_replace}' {file_path}"
        result = os.popen(command).read()
        if result:
            console.print(Panel(
                f"Occurrences in [bold cyan]{file_path}[/bold cyan]:\n{result}",
                title="Occurrences Found",
                style="bold yellow"
            ))

            to_replace = input(
                f"Do you want to replace '{str_to_replace}' in [bold cyan]{file_path}[/bold cyan]? (y/n): "
            )
            if to_replace.lower() == 'y':
                selected_files.append(file_path)

    return selected_files


def _replace_in_files(files: list, str_to_replace: str, replacement: str) -> None:
    """
    Replace the string in the selected files.
    """
    for file_path in files:
        with open(file_path, 'r') as file:
            content = file.read()

        new_content = content.replace(str_to_replace, replacement)

        with open(file_path, 'w') as file:
            file.write(new_content)

        console.print(
            f"[green]Replaced '{str_to_replace}' with '{replacement}' in {file_path}[/green]")
