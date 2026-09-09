import os

from pyfzf.pyfzf import FzfPrompt
from rich import print
from rich.console import Console
from rich.panel import Panel
from simple_term_menu import TerminalMenu

from modules.getListDir import getListDir

fzf = FzfPrompt()
console = Console()

_cached_excluded_dirs = None


def getExcludedDirs():
    global _cached_excluded_dirs
    if _cached_excluded_dirs is not None:
        return _cached_excluded_dirs

    default_exclude_dirs = list(
        set(
            [
                ".git",
                "__pycache__",
                "venv",
                "node_modules",
                "dist",
                "build",
                ".idea",
                ".vscode",
                "vendor",
                ".mypy_cache",
            ]
        )
    )

    print(Panel(f"These directories will be excluded by default: {default_exclude_dirs}"))
    to_exclude = console.input(
        "[blue]The directories above will be excluded automatically. "
        "Do you want to exclude any additional ones, (y/n): "
    )
    if to_exclude.lower() == "y":
        dir_list = getListDir(os.getcwd())
        terminal_menu = TerminalMenu(
            dir_list, title="Select directories to exclude", multi_select=True
        )
        menu_entry_index = terminal_menu.show()
        excluded_dirs = [dir_list[i] for i in menu_entry_index]
        excluded_dirs.extend(default_exclude_dirs)
        excluded_dirs_str = " ".join(excluded_dirs)
        print(Panel(f"[green]Excluded directories: {excluded_dirs_str}"))
        _cached_excluded_dirs = excluded_dirs
    else:
        print(
            f"[green]No additional directories excluded, "
            f"except these by default: {default_exclude_dirs}"
        )
        _cached_excluded_dirs = default_exclude_dirs

    return _cached_excluded_dirs
