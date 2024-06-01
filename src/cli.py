import argparse
from pathlib import Path
from getpass import getpass
import os

from src.handler import FileHandler
from src.format import Formatter
from src.utilities import expand_user_path, validate_extension, progress

def get_api_key():
    """Prompt the user for an API key and save it in a file."""
    api_key = getpass("Please enter your OpenAI API key: ")
    home = Path.home()
    api_key_file = home / ".serpentscribe"
    with open(api_key_file, 'w') as f:
        f.write(api_key)
    return api_key

def load_api_key():
    """Load the API key from the file."""
    home = Path.home()
    api_key_file = home / ".serpentscribe"
    if api_key_file.exists():
        with open(api_key_file, 'r') as f:
            return f.read().strip()
    return None

def main():
    parser = argparse.ArgumentParser(description="Convert academic notes to the Cornell note-taking system.")
    parser.add_argument('path', type=str, help='Path to the .md or .txt file or directory containing the notes')
    parser.add_argument('--summarize', action='store_true', help='Summarize the notes instead of formatting them')
    parser.add_argument('--outline', action='store_true', help='Create an outline of the notes')
    parser.add_argument('--highlight', action='store_true', help='Highlight key points in the notes')
    args = parser.parse_args()

    api_key = load_api_key()
    if not api_key:
        print("API key not found.")
        api_key = get_api_key()

    file_handler = FileHandler()
    formatter = Formatter(api_key)
    
    # Ensure the path is expanded correctly
    path = expand_user_path(args.path)
    if path.is_file():
        files = [path]
    elif path.is_dir():
        files = file_handler.get_files_in_directory(path)
    else:
        print("Invalid path. Please provide a valid file or directory path.")
        return

    notes = file_handler.read_files(files)
    formatted_notes = []

    if args.summarize:
        for note in progress(notes, prefix='Summarizing notes'):
            formatted_notes.append(formatter.summarize_notes(note))
    elif args.outline:
        for note in progress(notes, prefix='Creating outlines'):
            formatted_notes.append(formatter.create_outline(note))
    elif args.highlight:
        for note in progress(notes, prefix='Highlighting key points'):
            formatted_notes.append(formatter.highlight_key_points(note))
    else:
        for note in progress(notes, prefix='Formatting notes'):
            formatted_notes.append(formatter.format_notes_to_cornell(note))

    output_files = [file.stem + ('_summary' if args.summarize else '_outline' if args.outline else '_highlight' if args.highlight else '_cornell') + file.suffix for file in files]
    output_paths = [Path(file).parent / output_file for file, output_file in zip(files, output_files)]
    file_handler.write_files(output_paths, formatted_notes)

    for output_path in output_paths:
        print(f"Formatted notes have been saved to {output_path}")

if __name__ == "__main__":
    main()
