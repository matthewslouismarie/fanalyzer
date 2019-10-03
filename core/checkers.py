from os import walk
from os.path import split

def is_folder_name_valid(path: str) -> bool:
    """Verify rule 1."""
    (head, tail) = split(path)
    return tail == 'fnc3'

def does_folder_only_contain_files(path: str) -> bool:
    """Verify rule 2."""
    (dirpath, dirnames, dirfiles) = next(walk(path))
    return dirnames == []
