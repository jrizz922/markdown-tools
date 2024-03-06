import os
import argparse
import re

# 1. Import the necessary libraries: os for directory and file operations, argparse for command line argument parsing, and re for regular expressions.
# 2. Define a function to remove hyperlinks from a markdown file. This function will use regular expressions to find and replace hyperlinks.
# 3. Define a function to scan a directory for markdown files. This function will use os.walk to traverse the directory and its subdirectories.
# 4. Use argparse to parse command line arguments. If a directory is not provided, prompt the user for one.
# 5. Call the directory scanning function with the provided or prompted directory.
# 6. For each markdown file found, call the hyperlink removal function and save the file.

def remove_hyperlinks(file_path):
    with open(file_path, 'r') as file:
        content = file.read()
    content = re.sub(r'\[(.*?)\]\((.*?)\)', r'\1', content)
    with open(file_path, 'w') as file:
        file.write(content)

def scan_directory(directory):
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith('.md'):
                remove_hyperlinks(os.path.join(root, file))

parser = argparse.ArgumentParser()
parser.add_argument('-d', '--directory', help='Directory to scan for markdown files')
args = parser.parse_args()

if args.directory:
    directory = args.directory
else:
    directory = input('Please enter the directory to scan: ')

try:
    scan_directory(directory)
except Exception as e:
    print(f'An error occurred: {e}')