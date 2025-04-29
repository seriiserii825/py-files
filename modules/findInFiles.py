import os
from rich import print
from rich.console import Console
from rich.panel import Panel
from pyfzf.pyfzf import FzfPrompt

from utils.getAttachedDirs import getAttachedDirs
from utils.getExcludedDirs import getExcludedDirs
from utils.getFileData import getFileData
fzf = FzfPrompt()
console = Console()
def findInFiles():
    file_extenstion, search_string, replace_string = getFileData()
    excluded_dirs = getExcludedDirs()
    attached_dirs = getAttachedDirs() 
    print(Panel(f"[red]excluded_dirs: {excluded_dirs}"))
    print(Panel(f"[blue]attached_dirs: {attached_dirs}"))
    if len(attached_dirs) > 0:
        ## find in attached dirs only with grep and bash
        command = f"grep -rnw {' '.join(attached_dirs)} -e '{search_string}' --include '*.{file_extenstion}'"       
        print(Panel(f"[green]command: {command}"))
        os.system(command)
    else:
        command = f"grep -rnw {' '.join(excluded_dirs)} -e '{search_string}' --include '*.{file_extenstion}'"
        print(Panel(f"[green]command: {command}"))
        os.system(command)
