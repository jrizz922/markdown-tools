# CLI Tree of Sub-Directories & Files w/o exa

CLI Tree of Sub-Directories & Files w/o exa

```
% find . -print | sed -e 's;[^/]*/;|-- ;g;s;-- |; |;g'
```



#macos/dotfiles	