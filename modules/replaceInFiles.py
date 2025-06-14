import os
from rich import print
from rich.console import Console
from rich.panel import Panel
from pyfzf.pyfzf import FzfPrompt

from utils.getAttachedDirs import getAttachedDirs
from utils.getExcludedDirs import getExcludedDirs
from utils.getFileData import getFileData
from utils.showOccuriences import showOccuriences
fzf = FzfPrompt()
console = Console()


def replaceInFiles():
    file_extension, search_string, replace_string = getFileData()
    excluded_dirs = getExcludedDirs()
    showOccuriences(file_extension, search_string, excluded_dirs)
    attached_dirs = getAttachedDirs()
    print(Panel(f"[red]excluded_dirs: {excluded_dirs}"))
    print(Panel(f"[blue]attached_dirs: {attached_dirs}"))
    if len(attached_dirs) > 0:
        # find in attached dirs only
        command = (
            f"find {' '.join(attached_dirs)} -type f -name '*{file_extension}' "
            f"-not -path \"{excluded_dirs}\" "
            f"-exec grep -l '{search_string}' {{}} \\; | "
            f"xargs sed -i 's/{search_string}/{replace_string}/g'"
        )
        print(Panel(f"command: {command}"))
        agree = console.input("[blue]Do you want to run the command, (y/n): ")
        if agree.lower() == 'y':
            os.system(command)
        else:
            print(Panel("[red]Command not executed"))
    else:
        command = (
            f"find . -type f -name '*{file_extension}' "
            f"-not -path \"{excluded_dirs}\" "
            f"-exec grep -l '{search_string}' {{}} \\; | "
            f"xargs sed -i 's/{search_string}/{replace_string}/g'"
        )
        print(Panel(f"command: {command}"))
        agree = console.input("[blue]Do you want to run the command, (y/n): ")
        if agree.lower() == 'y':
            os.system(command)
        else:
            print(Panel("[red]Command not executed"))
