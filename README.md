# Shutdown Helper for 
- [Ubuntu](#ubuntu)
- [Windows](#windows)
## Ubuntu
Requires: curl, make
### Downloading
```bash
#!/bin/bash
$ mkdir $HOME/Downloads/shutdown-helper
$ curl https://raw.githubusercontent.com/wackyblackie/python-shutdown-helper/master/Makefile -O $HOME/Downloads/shutdown-helper/Makefile
```
### Downloading and Installing
```bash
$ make download install -C $HOME/Downloads/shutdown-helper
```
### Uninstalling/Removing
Uninstalling executables, and NOT manpages:
```bash
$ make uninstall -C $HOME/Downloads/shutdown-helper
```
Uninstalling ALL components:
```bash
$ make remove -C $HOME/Downloads/shutdown-helper
```
## Windows
Requires:
```bash
#!%systemtroot%\Windows\System32\cmd.exe OR %systemroot%\Windows\System32\WindowsPowerShell\v1.0\powershell.exe
> git clone https://github.com/wackyblackie/python-shutdown-helper %USERPROFILE%\Downloads\shutdown-helper
> cd %USERPROFILE%\Downloads\shutdown-helper
> python3 -m tk.py
```
### Uninstalling
```bash
#!%systemtroot%\Windows\System32\cmd.exe OR %systemroot%\Windows\System32\WindowsPowerShell\v1.0\powershell.exe
> rmdir %USERPROFILE%\Downloads\shutdown-helper
```
