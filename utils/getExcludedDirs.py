import os
from rich import print
from rich.console import Console
from pyfzf.pyfzf import FzfPrompt
from simple_term_menu import TerminalMenu
from rich.panel import Panel

from modules.getListDir import getListDir
fzf = FzfPrompt()
console = Console()


def getExcludedDirs():
    default_exclude_dirs = list(set([
        '.git', '__pycache__', 'venv', 'node_modules',
        'dist', 'build', '.idea', '.vscode', 'vendor'
    ]))

    print(Panel(f"default_exclude_dirs: {default_exclude_dirs}"))
    to_exclude = console.input(
        "[blue]Do you want to exclude directories, (y/n): ")
    if to_exclude.lower() == 'y':
        dir_list = getListDir(os.getcwd())
        terminal_menu = TerminalMenu(
            dir_list, title="Select directories to exclude", multi_select=True)
        menu_entry_index = terminal_menu.show()
        excluded_dirs = [dir_list[i] for i in menu_entry_index]
        excluded_dirs.extend(default_exclude_dirs)
        excluded_dirs_str = ' '.join(excluded_dirs)
        print(Panel(f"[green]Excluded directories: {excluded_dirs_str}"))
        return excluded_dirs
    else:
        print("[green]No directories excluded")
        return default_exclude_dirs
