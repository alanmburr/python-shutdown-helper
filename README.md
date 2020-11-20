# Shutdown Helper for 
- [Ubuntu](#ubuntu)
- [Windows](#windows)
## Ubuntu
Requires: [curl](https://curl.se/download.html), [make](#installing-tk)
### Download Installer
```bash
#!/bin/bash
$ mkdir $HOME/Downloads/shutdown-helper
$ curl https://raw.githubusercontent.com/wackyblackie/python-shutdown-helper/master/Makefile -O $HOME/Downloads/shutdown-helper/Makefile
```
### Run Installer
#### Download and Install Components
```bash
$ make download install -C $HOME/Downloads/shutdown-helper
```
#### ONLY Download Components
```bash
$ make download -C $HOME/Downloads/shutdown-helper
```
#### ONLY Install Components
```bash
$ make install -C $HOME/Downloads/shutdown-helper
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
Requires: [git](https://git-scm.com/download/win), [python3](https://www.python.org/ftp/python/3.9.0/python-3.9.0-amd64.exe), tkinter: ```pip3 install tk```
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
