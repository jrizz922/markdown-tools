# Add a New User to All Groups the Default User is in

Quickly add a new user to all groups the default user is in Using groups, sudo, tail, xargs

This is a standard procedure for me, whenever I set up a new Raspberry Pi system. Because the default user is "pi", I quickly replace it with my own (e.g. "kostis"), but I have to substitute that user to all of pi's groups first, before deleting the default account. xargs helps a lot with that in a single line, while avoiding boring "for" loops. For everything trickier, there's always "parallel" :)

`# groups pi | xargs -n 1 | tail -n +4 | xargs -n 1 sudo adduser kostis`

#macos/dotfiles