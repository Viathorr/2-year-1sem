from tkinter import messagebox
from ttkbootstrap.constants import *
import ttkbootstrap as ttk
from signup import SignUp
from login import LogIn
from settings import Settings


class MainWindow:
    def __init__(self, parent):
        self.master = parent  # chat app

        # Main Window
        self.root = ttk.Window(themename='morph')
        self.root.title('Chat')
        self.root.iconbitmap('rsrc/chat.ico')

        # Calculate the center position
        x_position = (self.root.winfo_screenwidth() - 600) // 2  # Adjust the width of the window
        y_position = (self.root.winfo_screenheight() - 650) // 2

        self.root.geometry(f'600x650+{x_position}+{y_position}')
        self.root.minsize(500, 550)

        self.root.rowconfigure((0, 4), weight=3)
        self.root.rowconfigure((1, 2, 3), weight=1)
        self.root.columnconfigure((0, 2), weight=1)
        self.root.columnconfigure(1, weight=4)

        # Main label
        self.label = ttk.Label(text='Online Chat', font=('Microsoft JhengHei Light', 25, 'bold'), bootstyle='info')
        self.label.grid(row=0, column=1)

        # buttons style
        outline_btn_style = ttk.Style()
        outline_btn_style.configure('info.Outline.TButton', font=('Microsoft JhengHei Light', 10, 'bold'))
        btn_style = ttk.Style()
        btn_style.configure('info.TButton', font=('Microsoft JhengHei Light', 10, 'bold'))
        secondary_btn_style = ttk.Style()
        secondary_btn_style.configure('dark.TButton', font=('Microsoft JhengHei Light', 8, 'bold'))

        # Open button
        self.open_btn = ttk.Button(text='Open', bootstyle='info', width=18, command=self._open_chat_window)
        self.open_btn.grid(row=1, column=1, ipady=10)

        # Log in button
        self.login_btn = ttk.Button(text='Log in', bootstyle='info-outline', width=18,
                                    command=self._open_login_window)
        self.login_btn.grid(row=2, column=1, ipady=10)

        # Sign up button
        self.signup_btn = ttk.Button(text='Sign up', bootstyle='info-outline', width=18,
                                     command=self._open_signup_window)
        self.signup_btn.grid(row=3, column=1, ipady=10)

        # Settings button
        self.settings_btn = ttk.Button(text='Settings', bootstyle='dark', command=self._open_settings)
        self.settings_btn.grid(row=4, column=0, ipady=5, padx=20, pady=20, sticky='sw', columnspan=3)

    def open(self):
        self.root.mainloop()

    def _open_chat_window(self):
        if not self.master.user:
            messagebox.showerror('You must be logged in', "Please log in or sign up first.")
        else:
            return

    def _open_login_window(self):
        login = LogIn(self)
        login.open()

    def _open_signup_window(self):
        signup = SignUp(self)
        signup.open()

    def _open_settings(self):
        settings = Settings(self)
        settings.open()
