# markdown-tools

This script is used to remove images and hyperlinks from markdown files in a specified directory. It uses regular expressions to find and remove the images and hyperlinks. rm_mdimages.py and rm_mdlinks.py are just the functions broken out.

The directory can be provided as a command-line argument or input by the user when the script is run.

* To remove images: `python rm_md_extras.py -d /path/to/directory -i`
* To remove hyperlinks: `python rm_md_extras.py -d /path/to/directory -l`
* To remove both: `python rm_md_extras.py -d /path/to/directory -i -l`
* To convert exported markdown files to shell scripts: 'python rm_md_extras.py -c /path/to/directory -c'
