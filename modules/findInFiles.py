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
def findInFiles():
    # find all files with the specified extension and exclude directories with bash and grep
    file_extension, search_string, replace_string = getFileData(replace=False)
    excluded_dirs = getExcludedDirs()
    showOccuriences(file_extension, search_string, excluded_dirs)
    excluded_dirs = getExcludedDirs()
    attached_dirs = getAttachedDirs() 
    print(Panel(f"[red]excluded_dirs: {excluded_dirs}"))
    print(Panel(f"[blue]attached_dirs: {attached_dirs}"))

     # Base command
    base_cmd = f"ack --type-add={file_extension}:*.{file_extension} --type={file_extension} -r '{search_string}'"

    # Add attached_dirs if any
    if attached_dirs:
        base_cmd += ' ' + ' '.join(attached_dirs)

    # Add exclusions if any
    if excluded_dirs:
        for dir in excluded_dirs:
            base_cmd += f" --ignore-dir={dir}"

    print(Panel(f"[green]command: {base_cmd}"))
    os.system(base_cmd)
