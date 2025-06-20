import os
from rich import print
from rich.console import Console
from rich.panel import Panel
from pyfzf.pyfzf import FzfPrompt

fzf = FzfPrompt()
console = Console()


def replaceInFiles(search_string):
    str_to_replace = input("[blue]Enter the string to replace: ")
    if not str_to_replace:
        print("[red]Please enter a valid replacement string.")
        exit(1)
    print(f'{str_to_replace}: str_to_replace')
