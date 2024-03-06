# Create Console Clock Job

[Create Console Clock Job](https://www.commandlinefu.com/commands/browse/25/50/75/100/125/150/175/200/225/250)

```
% while sleep 1; do tput sc; tput cup 0 $(($(tput cols)-29)); date; tput rc; done &
```


To kill by job #:
```
buffer-endeavouros% jobs 
[1]  + running    while sleep 1; do; tput sc; tput cup 0 $(($(tput cols)-29)); date; tput rc;
buffer-endeavouros% kill %1 
buffer-endeavouros% [1]  + terminated  while sleep 1; do; tput sc; tput cup 0 $(($(tput cols)-29)); date; tput rc; 
```



#macos/dotfiles	