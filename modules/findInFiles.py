from py_libs.InputValidator import InputValidator
from pyfzf.pyfzf import FzfPrompt
from rich.console import Console

from utils.getExcludedDirs import getExcludedDirs
from utils.getFileExtensions import getFileExtensions
from utils.showOccurrences import showOccurrences

fzf = FzfPrompt()
console = Console()


def findInFiles():
    """find all files with the specified extensions
    and exclude directories with bash and grep, then let the user
    select which matching files to inspect"""
    string_to_search = InputValidator.get_string(
        "Enter the string to search for: ")

    file_extensions = getFileExtensions()

    excluded_dirs = getExcludedDirs()
    showOccurrences(file_extensions, string_to_search, excluded_dirs)
