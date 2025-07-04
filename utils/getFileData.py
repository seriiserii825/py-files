from pyfzf.pyfzf import FzfPrompt
from rich import print
from rich.console import Console

fzf = FzfPrompt()
console = Console()


def getFileData() -> str:
    replace_string = console.input("[blue]Enter the string to replace with: ")
    if not replace_string:
        print("[red]Please enter a valid replacement string.")
        exit(1)
    return replace_string
