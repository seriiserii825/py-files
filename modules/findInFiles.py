from rich.console import Console
from pyfzf.pyfzf import FzfPrompt

from classes.InputValidator import InputValidator
from utils.getExcludedDirs import getExcludedDirs
from utils.showOccuriences import showOccuriences
fzf = FzfPrompt()
console = Console()


def findInFiles():
    """find all files with the specified extension
        and exclude directories with bash and grep"""
    string_to_search = InputValidator.get_string(
        "Enter the string to search for: ")

    file_extension = InputValidator.get_string(
        "Enter the file extension to search in (e.g., 'py', 'txt'): ")

    excluded_dirs = getExcludedDirs()
    showOccuriences(file_extension, string_to_search, excluded_dirs)
