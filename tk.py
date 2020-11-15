#!/usr/bin/env /usr/bin/python3
import tkinter
import os
import sys
from sys import platform as _plt
from tkinter import *
from tkinter import Tk
from tkinter import ttk
from tkinter import messagebox
import tkinter.simpledialog as tksd

# Here, we are creating our class, Window, and inheriting from the Frame
# class. Frame is a class from the tkinter module. (see Lib/tkinter/__init__)
class Window(Frame):

    # Define settings upon initialization. Here you can specify
    def __init__(self, master=None):
        
        # parameters that you want to send through the Frame class. 
        Frame.__init__(self, master)   

        #reference to the master widget, which is the tk window                 
        self.master = master

        #with that, we want to then run init_window, which doesn't yet exist
        self.init_window()

    #Creation of init_window
    def init_window(self):

        # changing the title of our master widget      
        self.master.title("Shutdown Helper")

        # allowing the widget to take the full space of the root window
        self.pack(fill=BOTH, expand=YES)
        # creating a button instance
        label_choose = Label(self, text="Goodbye"+os.getlogin+"Are you sure you are done with this computer?")
        quitButton = Button(self, text="Cancel", command=self.client_exit)
        shutDown = Button(self, text="Shut Down", command=self.turnoff)
        reStart = Button(self, text="Restart", command=self.rebootcomputer)
        lockScreen = Button(self, text="Lock", command=self.lockscreen)
        logOff = Button(self, text="Logoff", command=self.logoffuser)
        lablethesecond = Label(self, text="You can Shut down, Restart, or Log off.", compound=RIGHT)

        # placing the button on my window
        #buttons = quitButton, shutDown, reStart, logOff, lockScreen
        label_choose.pack()
        lablethesecond.pack()
        shutDown.pack(side=LEFT, anchor=W, fill=X, expand=YES)#place(x=253, y=42)
        reStart.pack(side=LEFT, anchor=W, fill=X, expand=YES)#place(x=207, y=42)
        lockScreen.pack(side=LEFT, anchor=W, fill=X, expand=YES)#place(x=10, y=42)
        logOff.pack(side=LEFT, anchor=W, fill=X, expand=YES)#place(x=90, y=42)
        quitButton.pack(side=LEFT, anchor=W, fill=X, expand=YES)#place(x=148, y=42)


    def linuxpm(self):
        _apt = os.path.isfile('/usr/bin/apt')
        _rpm = os.path.isfile('/usr/bin/yum')
        _dnf = os.path.isfile('/usr/bin/dnf')
        _arx = os.path.isfile('/usr/bin/pacman')
        _yes = os.path.isfile('/usr/bin/gnome-screensaver-command')
        if _apt == True and _yes == False:
            userpasswd = tksd.askstring("Password", "[sudo] password for "+os.getlogin()+":", show='*')
            os.system("echo "+userpasswd+" | sudo -S apt -y install gnome-screensaver && gnome-screensaver-command -l && gnome-screensaver-command -a")
        elif _rpm == True and _dnf == False and _yes == False:
            #This on detects if this is rhel or fedora w/ yum
            userpasswd = tksd.askstring("Password", "[sudo] password for "+os.getlogin()+":", show='*')
            os.system("echo "+userpasswd+" | sudo -S yum -y install gnome-screensaver && gnome-screensaver-command -l && gnome-screensaver-command -a")
        elif _dnf == True and _rpm == True and _yes == False:
            #This is fedora with useless yum. It uses dnf instead.
            userpasswd = tksd.askstring("Password", "[sudo] password for "+os.getlogin()+":", show='*')
            os.system("echo "+userpasswd+" | yes | sudo -S dnf install gnome-screensaver && gnome-screensaver-command -l && gnome-screensaver-command -a")
        elif _arx == True and _yes == False:
            userpasswd = tksd.askstring("Password", "[sudo] password for "+os.getlogin()+":", show='*')
            os.system("echo "+userpasswd+" | yes | sudo -S pacman -Sy gnome-screensaver && gnome-screensaver-command -l && gnome-screensaver-command -a")
        elif _dnf == False and _rpm == False and _apt == False and _arx == False and _yes == False:
            messagebox.showerror("Error", "Could not install package because your os is not Debian-based or rpm/dnf based.")
        elif _yes == True:
            os.system("/usr/bin/gnome-screensaver-command -a")    
    def turnoff(self):
        if _plt == "linux" or _plt == "linux2":
            os.system("shutdown now")
        elif _plt == "darwin":
            userpasswd = tksd.askstring("Password", "[sudo] password for "+os.getlogin()+":", show='*')
            os.system("echo "+userpasswd+" | sudo -S shutdown -h")
        elif _plt == "win32":
            os.system("powershell stop-computer")
        elif _plt == "win64":
            os.system("powershell stop-computer")
    def rebootcomputer(self):
        if _plt == "linux" or _plt == "linux2":
            os.system("shutdown -r now")
        elif _plt == "darwin":
            userpasswd = tksd.askstring("Password", "[sudo] password for "+os.getlogin()+":", show='*')
            os.system("echo "+userpasswd+"| sudo -S shutdown -r now")
        elif _plt == "win32":
            os.system("powershell restart-computer")
        elif _plt == "win64":
            os.system("powershell restart-computer")
    def logoffuser(self):
        if _plt == "linux" or _plt == "linux2":
            userpasswd = tksd.askstring("Password", "[sudo] password for "+os.getlogin()+":", show='*')
            os.system("echo "+userpasswd+" | sudo -S skill -KILL -u "+os.getlogin())
        elif _plt == "darwin":
            messagebox.showerror("Error", "Could not log off user.")
        elif _plt == "win32":
            os.system("powershell logoff")
        elif _plt == "win64":
            os.system("powershell logoff")
    def lockscreen(self):
        if _plt == "linux" or _plt == "linux2":
            self.linuxpm(self)
        elif _plt == "darwin":
            os.system("/System/Library/CoreServices/Menu\ Extras/User.menu/Contents/Resources/CGSession -suspend")
        elif _plt == "win32":
            os.system("rundll32.exe user32.dll,LockWorkStation")
        elif _plt == "win64":
            os.system("rundll32.exe user32.dll,LockWorkStation")
    def client_exit(self):
        exit()


# root window created. Here, that would be the only window, but
# you can later have windows within windows.
root = Tk()

#root.geometry("400x80")

root.resizable(width=False, height=False)

if _plt == "linux" or _plt == "linux2":
    #use hicolor fallback because everyone has them.
    wmiconphoto = PhotoImage(file = '/usr/share/icons/hicolor/24x24/actions/system-shutdown.png')
    root.iconphoto(True, wmiconphoto)
    root.wm_iconphoto(True, wmiconphoto)
#elif _plt == "darwin":
    #macOS doesn't have an icon yet because I don't own a Mac.
elif _plt == "win32" or _plt == "win64":
    iconphoto = PhotoImage(file = 'C:/Windows/System32/SecurityAndMaintenance_Error.png')
    root.iconphoto(True, iconphoto)
    root.wm_iconphoto(True, iconphoto)

#creation of an instance
app = Window(root)

root.mainloop()  
