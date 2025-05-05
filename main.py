
from modules.findInFiles import findInFiles
from modules.renameFiles import renameFiles
from modules.replaceInFiles import replaceInFiles
from pyfzf.pyfzf import FzfPrompt
fzf = FzfPrompt()

menu_items = ['Find in files', 'Replace in files', 'Rename files', 'Exit']

choice = fzf.prompt(menu_items)
if choice:
    print(f"You selected: {choice[0]}")

if choice[0] == 'Find in files':
    findInFiles()
elif choice[0] == 'Replace in files':
    replaceInFiles()
elif choice[0] == 'Rename files':
    renameFiles()
elif choice[0] == 'Exit':
    print("Exiting...")
    exit(0)

def menu():
    pass
