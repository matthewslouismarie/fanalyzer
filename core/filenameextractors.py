import re


def trim_extension(filename: str) -> str:
    split_filename = filename.split('.')
    if len(split_filename) == 1:
        """There is no extension."""
        return filename
    elif len(split_filename) == 2:
        """There is one extension."""
        return split_filename[0]

    """A dot can only be used to separate the Name of File from the file
    extension (inferred from 4, 5, 6, 14), and there can either be 0 or 1
    extension. (4)
    """
    raise ValueError()

def extract_name(filename: str) -> tuple([str, str]):
    """Accept only extension-trimmed filenames."""
    split_filename = filename.split('_')
    name = split_filename[0]
    new_filename_index = len(name)
    if len(split_filename) > 1:
        new_filename_index += 1
    return (name, filename[new_filename_index:])

def extract_date_str(filename: str) -> str:
    regex_s = f'(_s(\d+)?)'
    regex_mte = f'(_mte(\d+){regex_s}?)'
    regex_h = f'(_h(\d+){regex_mte}?)'
    regex_d = f'(_d(\d+){regex_h}?)'
    regex_m = f'(_m(\d+){regex_d}?)'
    regex_y = f'(y(\d+){regex_m})'
    return re.search(f'\A{regex_y}', filename, re.IGNORECASE).group(1)

def extract_date_from_date_str(date_str: str):
