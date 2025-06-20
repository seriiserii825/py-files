import os
from rich import print
from rich.console import Console
from rich.panel import Panel
from classes.Select import Select
from utils.getExcludedDirs import getExcludedDirs
console = Console()


def find_file() -> str:
    # filename = console.input("[blue]Enter the file name to rename: ")
    fzf_cmd = (
        "fzf --height 40% --reverse --inline-info "
        "--preview 'bat --style=numbers --color=always {}'"
    )
    file_path = os.popen(fzf_cmd).read().strip()
    filename = os.path.basename(file_path)
    # filename without extension
    return filename.split('.')[0]


def renameFiles(filename: str) -> None:
    newfilename = _get_new_file_name()
    files = _find_files(filename)
    selected_files = _check_file_to_rename(files)
    _rename_files(selected_files, newfilename)


def _get_new_file_name() -> str:
    new_file_name = console.input(
        "[blue]Enter the new file name, without extension: ")
    if not new_file_name:
        print(Panel("[red]New file name cannot be empty."))
        return _get_new_file_name()
    return new_file_name


def _find_files(filename: str) -> list:
    """Find files with the given filename."""
    excluded_dirs = getExcludedDirs()
    command = f'find . -type f -name "*{filename}*" -not -path "{excluded_dirs}"'
    files = os.popen(command).read().strip().splitlines()
    return files if files else []


def _check_file_to_rename(files: list) -> list:
    files_to_rename = Select.select_with_fzf(files)
    if not files_to_rename:
        print(Panel("[red]No files selected for renaming."))
        return []
    return files_to_rename


def _rename_files(files: list, newfilename: str) -> None:
    """Rename the selected files to the new filename."""
    new_file_extension = _get_file_with_extenstion_from_list(files, newfilename)
    was_renamed = False
    for file in files:
        new_file_name = file.replace(os.path.basename(file), new_file_extension)
        print(f"new_file_name: {new_file_name}")
        print(f'{file}: file')
        # new_file already exists
        if os.path.exists(new_file_name):
            print(
                Panel(f"[red]File {new_file_name} already exists. Skipping."))
            continue
        was_renamed = True
        os.rename(file, new_file_name)
        print(f"Renamed {file} to {new_file_name}")
    if not was_renamed:
        print(Panel("[red]No files were renamed."))
    else:
        print(Panel("[green]Files renamed successfully."))


def _get_file_with_extenstion_from_list(list_of_files: list, filename: str) -> str:
    list_extension = list_of_files[0].split('.')[-1]
    return f"{filename}.{list_extension}"
