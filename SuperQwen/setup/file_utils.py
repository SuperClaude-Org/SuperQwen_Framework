import importlib.resources
from pathlib import Path

QWEN_DIR = Path.home() / ".qwen"

def get_package_files(subfolder: str):
    """Helper to get files from a package subfolder."""
    try:
        package_name = 'SuperQwen'
        # Data folders are not packages, so we get the path to the main package
        # and then navigate to the subfolder.
        data_dir = importlib.resources.files(package_name) / subfolder.capitalize()
        return [file for file in data_dir.iterdir() if file.is_file()]
    except (ModuleNotFoundError, FileNotFoundError):
        return []
