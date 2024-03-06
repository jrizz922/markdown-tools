# Display Disk Partition Sizes

\# Display Disk Partition Sizes

`$ lsblk -o name,size`



`$ lsblk | grep -v part | awk '{print $1 "\t" $4}'`

0m0,007s user 0m0,011s sys 0m0,000s


#macos/dotfiles	