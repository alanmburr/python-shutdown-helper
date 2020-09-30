import tkinter
import os
import sys
from sys import platform as _plt
from tkinter import *
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
        lable_choose = StringVar()
        quitButton = Button(self, text="Cancel", command=self.client_exit)
        shutDown = Button(self, text="Shut Down", command=self.turnoff)
        reStart = Button(self, text="Restart", command=self.rebootcomputer)
        lockScreen = Button(self, text="Lock", command=self.lockscreen)
        label = Label(self, textvariable=lable_choose, compound=RIGHT)
        logOff = Button(self, text="Logoff", command=self.logoffuser)
        lablethesecond = Label(self, text="You can Shut down, Restart, or Log off.", compound=RIGHT)

        # placing the button on my window
        buttons = quitButton, shutDown, reStart, logOff, lockScreen
        lable_choose.set("Goodbye, "+ os.getlogin()+". Are you sure you are done with this computer?")
        label.pack()
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
        if _apt == True:
            userpasswd = tksd.askstring("Password", "[sudo] password for "+os.getlogin()+":", show='*')
            os.system("echo "+userpasswd+" | sudo -S apt -y install gnome-screensaver && gnome-screensaver-command -l && gnome-screensaver-command -a")
        elif _rpm == True and _dnf == False:
            userpasswd = tksd.askstring("Password", "[sudo] password for "+os.getlogin()+":", show='*')
            os.system("echo "+userpasswd+" | sudo -S yum -y install gnome-screensaver && gnome-screensaver-command -l && gnome-screensaver-command -a")
        elif _dnf == True and _rpm == True:
            userpasswd = tksd.askstring("Password", "[sudo] password for "+os.getlogin()+":", show='*')
            os.system("echo "+userpasswd+" | yes | sudo -S dnf install gnome-screensaver && gnome-screensaver-command -l && gnome-screensaver-command -a")
        elif _arx == True:
            userpasswd = tksd.askstring("Password", "[sudo] password for "+os.getlogin()+":", show='*')
            os.system("echo "+userpasswd+" | yes | sudo -S pacman -Sy gnome-screensaver && gnome-screensaver-command -l && gnome-screensaver-command -a")
        elif _dnf == False and _rpm == False and _apt == False and _arx == False:
            messagebox.showerror("Error", "Could not install package because your os is not Debian-based or rpm/dnf based.")
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
            linuxpm(self)
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
    root.iconbitmap('shutdown-ico.ico')
    root.wm_iconbitmap('shutdown-ico.ico')
elif _plt == "darwin":
    root.iconbitmap('shutdown-ico.ico')
    root.wm_iconbitmap('shutdown-ico.ico')
elif _plt == "win32":
    root.iconbitmap('shutdown-ico.ico')
    root.wm_iconbitmap('shutdown-ico.ico')
elif _plt == "win64":
    root.iconbitmap('shutdown-ico.ico')
    root.wm_iconbitmap('shutdown-ico.ico')

#creation of an instance
app = Window(root)

root.mainloop()  
