#!/usr/bin/env python3
import os, sys, time, hashlib
from tkinter import *
from tkinter.ttk import *
from tkinter import messagebox

class Login(Tk):
    def __init__(self):
        Tk.__init__(self)
        self.title(string = "Login")
        self.resizable(0,0)
        #self.style = Style()
        #self.style.theme_use("clam")
        self.configure(background = 'white')
        icon = PhotoImage(file='icon.png')
        self.tk.call('wm', 'iconphoto', self._w, icon)
        self.eval('tk::PlaceWindow %s center' % self.winfo_pathname(self.winfo_id()))

        self.bind("<Escape>", self.exit) # Press ESC to quit app


        self.options = {
            'username' : StringVar(),
            'pwd' : StringVar(),
        }

        photo = PhotoImage(file='login_img.png')
        #photo = photo.zoom(2)
        photo = photo.subsample(1)
        label = Label(self, image=photo, background = 'white')
        label.image = photo # keep a reference!
        label.grid(row = 0, column = 0, columnspan = 2)

        Label(self, text = 'Username', background = 'white', foreground = 'black', font='Helvetica 12 bold').grid(row = 1, column = 0)
        self.a = Entry(self, textvariable = self.options['username'], width = 30)
        self.a.grid(row = 2, column = 0, columnspan = 2)
        self.a.focus()

        Label(self, text = 'Password', background = 'white', foreground = 'black', font='Helvetica 12 bold').grid(row = 3, column = 0)
        Entry(self, textvariable = self.options['pwd'], show = '*', width = 30).grid(row = 4, column = 0, columnspan = 2)

        login_clk = Button(self, text = 'Login', command = self.login, width = 30).grid(row = 5, column = 0, columnspan = 2)
        register_clk = Button(self, text = 'Register', command = self.reg, width = 30).grid(row = 6, column = 0, columnspan = 2)
        close = Button(self, text = 'Exit', command = self.destroy, width = 30).grid(row = 7, column = 0, columnspan = 2)
        self.bind("<Return>", self.login_event) # Press ESC to quit app

    def login_event(self, event):
        self.login() # Redirect to login on event (hotkey is bound to <Return>)

    def login(self):
        # Check username and password
        if self.options['username'].get() == 'root' and hashlib.sha256(self.options['pwd'].get().encode('utf-8')).hexdigest() == '4813494d137e1631bba301d5acab6e7bb7aa74ce1185d456565ef51d737677b2':
            pass # Continue
        else:
            messagebox.showwarning("ERROR", "Invalid username or password")
            self.options['username'].set('')
            self.options['pwd'].set('')
            self.a.focus()
            return # Error, invalid username/password

        self.destroy()
        main = MainWindow(self.options['username'].get(), self.options['pwd'].get())
        main.mainloop()

    def exit(self, event):
        sys.exit(0)

    def reg(self):
        self.register = Toplevel()
        self.register.title(string = 'Register')
        self.register.configure(background = 'white')
        self.register.resizable(0,0)

        # textbar
        self.options['frame'] = Text(self.register, background = 'black', foreground = 'white', height = 32, width = 80)
        self.options['frame'].grid(row = 0, column = 1)



class MainWindow(Tk):
    def __init__(self, username, pwd):
        Tk.__init__(self)
        self.title(string = "Welcome, %s" % username)
        self.resizable(0,0)
        #self.style = Style()
        #self.style.theme_use("clam")
        self.configure(background = 'white')
        icon = PhotoImage(file='icon.png')
        self.tk.call('wm', 'iconphoto', self._w, icon)
        self.eval('tk::PlaceWindow %s center' % self.winfo_pathname(self.winfo_id()))

        self.bind("<Escape>", self.exit) # Press ESC to quit app


        self.options = {
            'username' : StringVar(),
            'pwd' : StringVar(),
        }

        photo = PhotoImage(file='login_img.png')
        #photo = photo.zoom(2)
        photo = photo.subsample(1)
        label = Label(self, image=photo, background = 'white')
        label.image = photo # keep a reference!
        label.grid(row = 0, column = 0, columnspan = 2)

    def exit(self, event):
        sys.exit(0)

logon = Login()
logon.mainloop()
