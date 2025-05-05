import os
from rich import print
from rich.console import Console
from rich.panel import Panel
from utils.getExcludedDirs import getExcludedDirs
console = Console()

def renameFiles():
    # filename = console.input("[blue]Enter the file name to rename: ")
    file_path = os.popen("fzf --height 40% --reverse --inline-info --preview 'bat --style=numbers --color=always {}'").read().strip()
    filename = os.path.basename(file_path)
    # filename without extension
    filename = filename.split('.')[0]
    print(f'filename: {filename}')
    newfilename = console.input("[blue]Enter the new file name: ")
    excluded_dirs = getExcludedDirs()
    # Create the command to find files
    command = f'find . -type f -name "*{filename}*" -not -path "{excluded_dirs}"'
    print(Panel(f"command: {command}"))

    # Run the find command to list the files
    files = os.popen(command).read()  # Using os.popen to capture the output of the find command
    print(Panel(f"Files found: {files}"))

    # Ask for confirmation to run the rename command
    agree = console.input("[blue]Do you want to run the command, (y/n): ")
    if agree.lower() == 'y':
        if files:
            # Loop through the files and rename them
            for file in files.splitlines():
                new_file_name = file.replace(filename, newfilename)
                os.rename(file, new_file_name)
                print(f"Renamed {file} to {new_file_name}")
        else:
            print(Panel("[red]No files found to rename."))
    else:
        print(Panel("[red]Command not executed"))
