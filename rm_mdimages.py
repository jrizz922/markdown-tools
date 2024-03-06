import os
import re
import argparse

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

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Remove images from markdown files in a specified directory.')
    parser.add_argument('-d', '--directory', type=str, help='The directory where the markdown files are located.')

    args = parser.parse_args()

    # If the directory was not provided as a command-line argument, ask the user for it
    if args.directory is None:
        args.directory = input("Please enter the directory where the markdown files are located: ")

    # Call the function to remove images from the markdown files
    remove_images_from_markdown(args.directory)