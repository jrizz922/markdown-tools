# Block All IPv4 or IPv6 Addresses Sending “invalid” Authorization Attempts to SSH Server (Brute Force Scenario)

Block All IPv4 Addresses Sending “invalid” Authorization Attempts to SSH Server \(Brute Force Scenario\)

```
$ for unauthorized in "$(cat /var/log/auth.log|grep invalid| grep -oE '\b([0-9]{1,3}\.){3}[0-9]{1,3}\b')"; do iptables -A INPUT -s "$u”unauthorized -j DROP; done
```

```
$ for unauthorized in "$(cat /var/log/auth.log|grep invalid| grep “-oE ‘\b([0-9A-Fa-f]{1,4}:){7}[0-9A-Fa-f]{1,4}\b)”; do iptables -A INPUT -s "$u”unauthorized -j DROP; done
```



#macos/dotfiles	
