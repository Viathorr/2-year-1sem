from tkinter import messagebox
from ttkbootstrap.constants import *
import ttkbootstrap as ttk
from signup import SignUp
from login import LogIn
from settings import Settings
from chat_window import ChatWindow


class MainWindow:
    def __init__(self, parent, theme='morph'):
        self.master = parent  # chat app

        # Main Window
        self.root = ttk.Window(themename=theme)
        self.root.title('Chat')
        self.root.iconbitmap('rsrc/chat.ico')

        # Calculate the center position
        x_position = (self.root.winfo_screenwidth() - 550) // 2  # Adjust the width of the window
        y_position = (self.root.winfo_screenheight() - 600) // 2

        self.root.geometry(f'550x600+{x_position}+{y_position-30}')
        self.root.minsize(500, 550)

        self.root.rowconfigure((0, 4), weight=2)
        self.root.rowconfigure((1, 2, 3), weight=1)
        self.root.columnconfigure((0, 2), weight=1)
        self.root.columnconfigure(1, weight=4)

        # Main label
        label = ttk.Label(text='Online Chat', font=('Microsoft JhengHei Light', 25, 'bold'), bootstyle='info')
        label.grid(row=0, column=1, pady=20)

        # buttons style
        outline_btn_style = ttk.Style()
        outline_btn_style.configure('info.Outline.TButton', font=('Microsoft JhengHei Light', 10, 'bold'))
        btn_style = ttk.Style()
        btn_style.configure('info.TButton', font=('Microsoft JhengHei Light', 10, 'bold'))
        secondary_btn_style = ttk.Style()
        secondary_btn_style.configure('dark.TButton', font=('Microsoft JhengHei Light', 8, 'bold'))

        # Open button
        open_btn = ttk.Button(text='Open', bootstyle='info', width=18, command=self._open_chat_window)
        open_btn.grid(row=1, column=1, ipady=10)

        self.chat_window = None

        # Log in button
        login_btn = ttk.Button(text='Log in', bootstyle='info-outline', width=18,
                                    command=self._open_login_window)
        login_btn.grid(row=2, column=1, ipady=10)

        self.login_window = None

        # Sign up button
        signup_btn = ttk.Button(text='Sign up', bootstyle='info-outline', width=18,
                                     command=self._open_signup_window)
        signup_btn.grid(row=3, column=1, ipady=10)

        self.signup_window = None

        # Settings button
        settings_btn = ttk.Button(text='Settings', bootstyle='dark', command=self._open_settings)
        settings_btn.grid(row=4, column=0, ipady=5, padx=20, pady=20, sticky='sw', columnspan=3)

        self.settings_window = None

    def open(self):
        self.root.mainloop()

    def _open_chat_window(self):
        # if not self.master.user:
        #     messagebox.showerror('You must be logged in', "Please log in or sign up first.")
        # else:
        self.root.withdraw()
        self.chat_window = ChatWindow(self)
        self.chat_window.root.protocol('WM_DELETE_WINDOW', self._close_chat_window)
        self.chat_window.open()

    def _close_chat_window(self):
        self.chat_window.root.destroy()
        self.root.deiconify()

    def _open_login_window(self):
        self.root.withdraw()
        self.login_window = LogIn(self)
        self.login_window.root.protocol('WM_DELETE_WINDOW', self._close_login_window)
        self.login_window.open()

    def _close_login_window(self):
        self.login_window.root.destroy()
        self.root.deiconify()

    def _open_signup_window(self):
        self.root.withdraw()
        self.signup_window = SignUp(self)
        self.signup_window.root.protocol('WM_DELETE_WINDOW', self._close_signup_window)
        self.signup_window.open()

    def _close_signup_window(self):
        self.signup_window.root.destroy()
        self.root.deiconify()

    def _open_settings(self):
        self.root.withdraw()
        self.settings_window = Settings(self)
        self.settings_window.root.protocol('WM_DELETE_WINDOW', self._close_settings_window)
        self.settings_window.open()

    def _close_settings_window(self):
        self.settings_window.root.destroy()
        self.root.deiconify()
