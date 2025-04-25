import os
from rich import print
def getListDir(base_path):
    """
    List all directories in a given path.
    """
    from rich.console import Console
    from pyfzf.pyfzf import FzfPrompt

    # Get the list of directories
    return [d for d in os.listdir(base_path) if os.path.isdir(os.path.join(base_path, d))]
