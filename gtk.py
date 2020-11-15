#!/usr/bin/env /usr/bin/python3
from os import name
import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, Gio
import os
import getpass as pwd
from sys import platform as _plt

down = Gtk.PositionType.BOTTOM

#slowly migrating from tk to gtk.
class Window(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self, title="Shutdown Helper")
        Gtk.Window.set_default_icon_name("system-shutdown")

        self.set_size_request(200, 300)

        hb = Gtk.HeaderBar()
        hb.set_show_close_button(True)
        hb.props.title = "Shutdown Helper"
        #hb.props.subtitle = "Are you sure you're done?"
        hb.set_decoration_layout(":close")
        self.set_titlebar(hb)

        grid = Gtk.Grid()
        self.add(grid)

        #main_label = Gtk.Label(label= '                                             ')
        #main_label.connect("hilighted", self.egg)
        #main_label.set_justify(Gtk.Justification.CENTER)

        stop = Gtk.Button.new_with_mnemonic("_Shut _Down")
        stop.connect("clicked", self.off)
        stop.set_hexpand(True)
        stop.set_vexpand(True)

        redo = Gtk.Button.new_with_mnemonic("_Reboot")
        redo.connect("clicked", self.repwr)
        redo.set_hexpand(True)
        redo.set_vexpand(True)
        
        slp = Gtk.Button.new_with_mnemonic("_Sleep")
        slp.connect("clicked", self.sleep)
        slp.set_hexpand(True)
        slp.set_vexpand(True)

        lock = Gtk.Button.new_with_mnemonic("_Lock")
        lock.connect("clicked", self.padlock)
        lock.set_hexpand(True)
        lock.set_vexpand(True)

        lgout = Gtk.Button.new_with_mnemonic("_Log _Out")
        lgout.connect("clicked", self.skill)
        lgout.set_hexpand(True)
        lgout.set_vexpand(True)

        quit = Gtk.Button.new_with_mnemonic("_Cancel")
        quit.connect("clicked", self.done)
        quit.set_hexpand(True)
        quit.set_vexpand(True)

        mini_btns = Gtk.IconSize.BUTTON

        stop_mini = Gtk.Button()
        stop_mini_icon = Gio.ThemedIcon(name="system-shutdown")
        stop_mini_img = Gtk.Image.new_from_gicon(stop_mini_icon, mini_btns)
        stop_mini.add(stop_mini_img)
        stop_mini.connect("clicked", self.off)

        redo_mini = Gtk.Button()
        redo_mini_icon = Gio.ThemedIcon(name="system-restart")
        redo_mini_img = Gtk.Image.new_from_gicon(redo_mini_icon, mini_btns)
        redo_mini.add(redo_mini_img)
        redo_mini.connect("clicked", self.repwr)

        slp_mini = Gtk.Button()
        slp_mini_icon = Gio.ThemedIcon(name="sleep")
        slp_mini_img = Gtk.Image.new_from_gicon(slp_mini_icon, mini_btns)
        slp_mini.add(slp_mini_img)
        slp_mini.connect("clicked", self.sleep)

        lock_mini = Gtk.Button()
        lock_mini_icon = Gio.ThemedIcon(name="lock")
        lock_mini_img = Gtk.Image.new_from_gicon(lock_mini_icon, mini_btns)
        lock_mini.add(lock_mini_img)
        lock_mini.connect("clicked", self.padlock)

        lgout_mini = Gtk.Button()
        lgout_mini_icon = Gio.ThemedIcon(name="system-log-out")
        lgout_mini_img = Gtk.Image.new_from_gicon(lgout_mini_icon, mini_btns)
        lgout_mini.add(lgout_mini_img)
        lgout_mini.connect("clicked", self.skill)

        hb.pack_start(stop_mini)
        hb.pack_start(redo_mini)
        hb.pack_start(slp_mini)
        hb.pack_start(lock_mini)
        hb.pack_start(lgout_mini)

        grid.add(stop)
        grid.attach_next_to(redo, stop, down, 1, 2)
        grid.attach_next_to(slp, redo, down, 1, 2)
        grid.attach_next_to(lock, slp, down, 1, 2)
        grid.attach_next_to(lgout, lock, down, 1, 2)
        grid.attach_next_to(quit, lgout, down, 1, 2)


    def padlock(self, lock):
        _yes = os.path.isfile('/usr/bin/gnome-screensaver-command')
        if _yes == False:
            os.system("notify-send -i 'system-shutdown' '`gnome-screensaver-command` is not installed. Open a terminal (Ctrl+Alt+T) and type: man python-shutdown-helper.'")
        elif _yes == True:
            os.system("/usr/bin/gnome-screensaver-command -a")    
    def off(self, stop):
        os.system("shutdown now")
    def repwr(self, redo):
        os.system("shutdown -r now")
    def skill(self, skill):
        user = str(pwd.getuser())
        os.system("skill -KILL -u "+user)
    def sleep(self, slp):
        os.system("systemctl suspend -i")
    def egg(self, main_label):
        os.system("zenity --info --text 'You have found the Easter Egg!' --title 'Easter Egg!'")
        os.system("xmessage -center 'You Found The Easter Egg!' -title 'Easter Egg Found!'")
        os.system("notify-send -i 'error-app' 'You have found an easter egg!'")
    def done(self, quit):
        Gtk.main_quit()

window = Window()
window.connect("destroy", Gtk.main_quit)
window.show_all()
Gtk.main()  
