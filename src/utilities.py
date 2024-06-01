from pathlib import Path

def validate_extension(file_path, valid_extensions=['.md', '.txt']):
    return Path(file_path).suffix in valid_extensions

def expand_user_path(path):
    """Expand the '~' in the file path to the user's home directory."""
    return Path(path).expanduser()

def progress(iterable, prefix='', suffix='', decimals=1, length=50, fill='█', print_end="\r"):
    total = len(iterable)
    def print_progress_bar(iteration):
        percent = ("{0:." + str(decimals) + "f}").format(100 * (iteration / float(total)))
        filled_length = int(length * iteration // total)
        bar = fill * filled_length + '-' * (length - filled_length)
        print(f'\r{prefix} |{bar}| {percent}% {suffix}', end=print_end)
    for i, item in enumerate(iterable, 1):
        yield item
        print_progress_bar(i)
    print()
