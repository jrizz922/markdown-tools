# Copy a file with progress and save hash to a different file

~[Copy a file with progress and save hash to a different file](https://www.commandlinefu.com/commands/view/28303/copy-a-file-with-progress-and-save-hash-to-a-different-file)~

`# pv file.txt | tee >(sha1sum > file.sha1) > file-copy.txt`

#macos/dotfiles