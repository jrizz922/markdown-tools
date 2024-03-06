# Copy a file with progress and save hash to a different file

~Copy a file with progress and save hash to a different file~

`# pv file.txt | tee >(sha1sum > file.sha1) > file-copy.txt`

#macos/dotfiles