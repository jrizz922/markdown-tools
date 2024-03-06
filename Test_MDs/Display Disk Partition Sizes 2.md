# Display Disk Partition Sizes

[\# Display Disk Partition Sizes](https://www.commandlinefu.com/commands/browse/25/50/75)

`$ lsblk -o name,size`



`$ lsblk | grep -v part | awk '{print $1 "\t" $4}'`

0m0,007s user 0m0,011s sys 0m0,000s


#macos/dotfiles	