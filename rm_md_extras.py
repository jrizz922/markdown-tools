#!/usr/bin/env python3

import re
import argparse
from pathlib import Path

def read_file(file_path):
    """
    Reads a file and returns its content.

    Parameters:
    file_path (str): The path to the file.

    Returns:
    str: The content of the file.
    """
    with open(file_path, 'r', encoding='utf-8') as file:
        return file.read()

def write_file(file_path, content):
    """
    Writes content to a file.

    Parameters:
    file_path (str): The path to the file.
    content (str): The content to write to the file.
    """
    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(content)

def remove_images(content):
    """
    Removes image markdown from the content.

    Parameters:
    content (str): The content to process.

    Returns:
    str: The content with image markdown removed.
    """
    return re.sub(r"!\[.*?\]\(.*?\)", "", content)

def remove_hyperlinks(content):
    """
    Removes hyperlink markdown from the content.

    Parameters:
    content (str): The content to process.

    Returns:
    str: The content with hyperlink markdown removed.
    """
    return re.sub(r'\[(.*?)\]\((.*?)\)', r'\1', content)

def remove_all_except_header_and_code(content):
    """
    Removes all lines from the content except headers and code blocks.

    Parameters:
    content (str): The content to process.

    Returns:
    str: The content with only headers and code blocks.
    """
    lines = content.split('\n')
    updated_content = []
    inside_code_block = False
    inside_inline_code_block = False

    for line in lines:
        if line.strip() == '```':
            inside_code_block = not inside_code_block
            continue

        if '`' in line:
            inside_inline_code_block = not inside_inline_code_block
            line = line.replace('`', '')

        if (inside_code_block or inside_inline_code_block) and line.lstrip().startswith(('#', '$')):
            line = line.lstrip()[1:]

        if line.strip() == '':
            continue

        if (line.startswith('#') and not inside_code_block) or inside_code_block or inside_inline_code_block:
            updated_content.append(line)

    return '\n'.join(updated_content)

def remove_specific_line(content):
    """
    Removes any line that contains "#macos/dotfiles".

    Parameters:
    content (str): The content to process.

    Returns:
    str: The content with the lines containing "#macos/dotfiles" removed.
    """
    lines = content.split('\n')
    lines = [line for line in lines if "#macos/dotfiles" not in line]
    return '\n'.join(lines)

def process_files_in_directory(directory, output_directory, process_function):
    """
    Processes all markdown files in a directory using a specified function.

    Parameters:
    directory (str): The directory to process.
    output_directory (str): The directory to output the processed files.
    process_function (function): The function to process the files.
    """
    directory_path = Path(directory)
    output_directory_path = Path(output_directory)

    if not output_directory_path.exists():
        output_directory_path.mkdir(parents=True)

    for file_path in directory_path.glob('**/*.md'):
        content = read_file(file_path)
        content = remove_specific_line(content)
        updated_content = process_function(content)
        new_file_path = output_directory_path / file_path.with_suffix('.sh').name
        write_file(new_file_path, updated_content)

        print(f"Processed file: {file_path.name}")
        if process_function == remove_images:
            print("Images were removed from the file.")
        elif process_function == remove_hyperlinks:
            print("Hyperlinks were removed from the file.")
        elif process_function == remove_all_except_header_and_code:
            print("All lines except headers and code blocks were removed from the file.")

def main():
    """
    Main function to parse arguments and call the appropriate processing function.
    """
    parser = argparse.ArgumentParser(description='Remove images and/or hyperlinks from markdown files in a specified directory. Will also convert markdown files to shell scripts.')
    parser.add_argument('-d', '--directory', type=str, required=True, help='The directory where the markdown files are located.')
    parser.add_argument('-o', '--output', type=str, help='The directory where the processed files will be saved. If not specified, a directory named "outputs" will be created in the directory where the markdown files are located.')
    parser.add_argument('-i', '--images', action='store_true', help='Remove images from the markdown files.')
    parser.add_argument('-l', '--links', action='store_true', help='Remove hyperlinks from the markdown files.')
    parser.add_argument('-c', '--convert', action='store_true', help='Convert markdown files to shell scripts.')
    args = parser.parse_args()

    output_directory = args.output if args.output else Path(args.directory) / "outputs"

    if args.images:
        process_files_in_directory(args.directory, output_directory, remove_images)
    if args.links:
        process_files_in_directory(args.directory, output_directory, remove_hyperlinks)
    if args.convert:
        process_files_in_directory(args.directory, output_directory, remove_all_except_header_and_code)

if __name__ == "__main__":
    main()