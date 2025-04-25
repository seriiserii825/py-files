import os
from rich import print
from rich.console import Console
from pyfzf.pyfzf import FzfPrompt
from simple_term_menu import TerminalMenu
from rich.panel import Panel

from modules.getListDir import getListDir
fzf = FzfPrompt()
console = Console()
def getAttachedDirs():
    to_exclude = console.input("[blue]Do you want to attach directories, (y/n): ")
    if to_exclude.lower() == 'y':
        dir_list = getListDir(os.getcwd())
        terminal_menu = TerminalMenu(dir_list, title="Select directories to attach", multi_select=True)
        menu_entry_index = terminal_menu.show()
        excluded_dirs = [dir_list[i] for i in menu_entry_index]
        excluded_dirs_str = ' '.join(excluded_dirs)
        print(Panel(f"[green]Attached directories: {excluded_dirs_str}"))
        return excluded_dirs
    else:
        print(Panel("[red]No directories attached"))
        return []
