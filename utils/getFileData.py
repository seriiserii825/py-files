import os
from rich import print
from rich.console import Console
from pyfzf.pyfzf import FzfPrompt
fzf = FzfPrompt()
console = Console()
def getFileData(replace=True, ):
    file_extension = console.input("[green]Enter the file extension (e.g., txt,php,js): ")
    if not file_extension:
        print("[red]Please enter a valid file extension")
        exit(1)
    search_string = console.input("[blue]Enter the string to search for: ")
    if not search_string:
        print("[red]Please enter a valid search string.")
        exit(1)
    if replace:
        replace_string = console.input("[blue]Enter the string to replace with: ")
        if not replace_string:
            print("[red]Please enter a valid replacement string.")
            exit(1)
    else:
        replace_string = None

    return file_extension, search_string, replace_string

