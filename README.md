# markdown-tools

rm_md_extras.py is a Python script that is used to manipulate markdown files in a specified directory. It provides the functionality to remove images and hyperlinks from these files. This is achieved using regular expressions to find and remove the specified elements. The script accepts command-line arguments to specify the directory and the type of elements to remove. It can remove images, hyperlinks, or both. Additionally, it can convert exported markdown files to shell scripts.

The directory can be provided as a command-line argument or input by the user when the script is run.

* To remove images: `python rm_md_extras.py -d /path/to/directory -i`
* To remove hyperlinks: `python rm_md_extras.py -d /path/to/directory -l`
* To remove both: `python rm_md_extras.py -d /path/to/directory -i -l`
* To convert exported markdown files to shell scripts: `python rm_md_extras.py -d /path/to/directory -c`
