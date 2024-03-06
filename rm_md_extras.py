# This script is used to remove images and hyperlinks from markdown files in a specified directory. 
# It uses regular expressions to find and remove the images and hyperlinks. 
# The directory can be provided as a command-line argument or input by the user when the script is run.

# * To remove images: python rm_md_extras.py -d /path/to/directory -i
# * To remove hyperlinks: python rm_md_extras.py -d /path/to/directory -l
# * To remove both: python rm_md_extras.py -d /path/to/directory -i -l

import os
import re
import argparse

# Function to remove images from markdown files in a specified directory
def remove_images_from_markdown(directory):
    try:
        # Get a list of all markdown files in the directory
        markdown_files = [file for file in os.listdir(directory) if file.endswith(".md")]

        # Iterate over each markdown file
        for file in markdown_files:
            file_path = os.path.join(directory, file)

            # Read the contents of the markdown file
            with open(file_path, "r") as f:
                content = f.read()

            # Remove the images from the markdown file using regular expressions
            updated_content = re.sub(r"!\[.*?\]\(.*?\)", "", content)

            # Save the updated content back to the markdown file
            with open(file_path, "w") as f:
                f.write(updated_content)

            print(f"Images removed from {file}")
    except FileNotFoundError:
        print(f"Directory {directory} not found.")
    except Exception as e:
        print(f"An error occurred: {str(e)}")

# Function to remove hyperlinks from a markdown file
def remove_hyperlinks(file_path):
    with open(file_path, 'r') as file:
        content = file.read()
    content = re.sub(r'\[(.*?)\]\((.*?)\)', r'\1', content)
    with open(file_path, 'w') as file:
        file.write(content)

# Function to scan a directory and remove hyperlinks from all markdown files in it
def scan_directory(directory):
    for root, _, files in os.walk(directory):
        for file in files:
            if file.endswith('.md'):
                remove_hyperlinks(os.path.join(root, file))

# Main function
def main():
    parser = argparse.ArgumentParser(description='Remove images and/or hyperlinks from markdown files in a specified directory.')
    parser.add_argument('-d', '--directory', type=str, required=True, help='The directory where the markdown files are located.')
    parser.add_argument('-i', '--images', action='store_true', help='Remove images from the markdown files.')
    parser.add_argument('-l', '--links', action='store_true', help='Remove hyperlinks from the markdown files.')

    args = parser.parse_args()

    # If the user wants to remove images
    if args.images:
        remove_images_from_markdown(args.directory)

    # If the user wants to remove hyperlinks
    if args.links:
        scan_directory(args.directory)

# Entry point of the script
if __name__ == "__main__":
    main()