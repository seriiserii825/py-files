from pyfzf.pyfzf import FzfPrompt

from modules.findInFiles import findInFiles
from modules.renameFiles import find_file, get_new_file_name, renameFiles
from modules.replaceInFiles import replaceInFiles

fzf = FzfPrompt()

menu_items = [
    "Find in files",
    "Replace in files",
    "Rename files",
    "Replace and Rename files",
    "Exit",
]

choice = fzf.prompt(menu_items)
if choice:
    print(f"You selected: {choice[0]}")

if choice[0] == "Find in files":
    findInFiles()
elif choice[0] == "Replace in files":
    str_to_replace = input("Enter the string to replace: ")
    replacement = input("Enter the replacement string: ")
    replaceInFiles(str_to_replace=str_to_replace, replacement=replacement)
    pass
elif choice[0] == "Rename files":
    filename = find_file()
    newfilename = get_new_file_name()
    renameFiles(filename=filename, newfilename=newfilename)
elif choice[0] == "Replace and Rename files":
    filename = find_file()
    newfilename = get_new_file_name()
    replaceInFiles(str_to_replace=filename, replacement=newfilename)
    newfilename = renameFiles(filename=filename, newfilename=newfilename)
elif choice[0] == "Exit":
    print("Exiting...")
    exit(0)


def menu():
    pass
