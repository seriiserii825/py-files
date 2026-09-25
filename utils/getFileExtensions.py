from py_libs.InputValidator import InputValidator


def getFileExtensions() -> list:
    """Ask the user for a comma-separated list of file extensions to search in."""
    raw = InputValidator.get_string(
        "Enter the file extensions to search in, comma-separated (e.g., 'py,txt'): "
    )
    return [ext.strip().lstrip(".") for ext in raw.split(",") if ext.strip()]
