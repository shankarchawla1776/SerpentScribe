from pathlib import Path

class FileHandler:
    def __init__(self):
        pass

    def read_files(self, file_paths):
        notes = []
        for file_path in file_paths:
            with open(file_path, 'r') as file:
                notes.append(file.read())
        return notes

    def write_files(self, file_paths, contents):
        for file_path, content in zip(file_paths, contents):
            with open(file_path, 'w') as file:
                file.write(content)

    def get_files_in_directory(self, dir_path, extensions=['.md', '.txt']):
        path = Path(dir_path)
        return [file for file in path.iterdir() if file.suffix in extensions]
