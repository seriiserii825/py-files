import os


def getListDir(base_path):
    """
    List all directories in a given path.
    """
    # Get the list of directories
    return [d for d in os.listdir(base_path)
            if os.path.isdir(os.path.join(base_path, d))]
