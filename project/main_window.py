from tkinter import messagebox
from ttkbootstrap.constants import *
import ttkbootstrap as ttk
from signup import SignUp
from login import LogIn
from settings import Settings
from chat_window import ClientChatWindow


class MainWindow:
    def __init__(self, parent, theme='minty'):
        self.master = parent  # chat app

        # Main Window
        self.root = ttk.Window(themename=theme)
        self.root.title('Chat')
        self.root.iconbitmap('rsrc/chat.ico')
        self.root.resizable(False, False)

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
        label = ttk.Label(text='Online Chat', font=('Microsoft JhengHei', 25, 'bold'), bootstyle='dark')
        label.grid(row=0, column=1, pady=20)

        # buttons style
        btn_style = ttk.Style()
        btn_style.configure('info.TButton', font=('Microsoft JhengHei', 10, 'bold'))
        dark_btn_style = ttk.Style()
        dark_btn_style.configure('dark.Outline.TButton', font=('Microsoft JhengHei', 10, 'bold'))

        # Open button
        open_btn = ttk.Button(text='Open', bootstyle='info', width=17, command=self._open_chat_window)
        open_btn.grid(row=1, column=1, ipady=10)

        self.chat_window = None

        # Log in button
        self.login_btn = ttk.Button(text='Log in', bootstyle='info', width=17,
                                    command=self._open_login_window)
        self.login_btn.grid(row=2, column=1, ipady=10)
        self.login_window = None

        # Sign up button
        self.signup_btn = ttk.Button(text='Sign up', bootstyle='info', width=17,
                                     command=self._open_signup_window)
        self.signup_btn.grid(row=3, column=1, ipady=10)
        self.signup_window = None

        # Settings button
        settings_btn = ttk.Button(text='Settings', bootstyle='dark-outline', width=17, command=self._open_settings)
        settings_btn.grid(row=4, column=1, ipady=3, pady=15, sticky='n')

        self.settings_window = None

    def open(self):
        self.root.mainloop()

    def _open_chat_window(self):
        if not self.master.user:
            messagebox.showwarning('You must be logged in', "Please log in or sign up first.")
        else:
            self.root.withdraw()
            self.chat_window = ClientChatWindow(self)
            self.chat_window.root.protocol('WM_DELETE_WINDOW', self._close_chat_window)
            try:
                self.chat_window.open()
            except Exception as ex:
                self.chat_window.root.destroy()
                self.root.deiconify()
                messagebox.showerror(title='Error', message=str(ex))

    def _close_chat_window(self):
        self.chat_window.socket.close()
        self.chat_window.root.destroy()
        self.root.deiconify()

    def _open_login_window(self):
        self.root.withdraw()
        self.login_window = LogIn(self)
        self.login_window.root.protocol('WM_DELETE_WINDOW', self._close_login_window)
        self.login_window.open()

    def _close_login_window(self):
        if self.master.user:
            self.login_btn.config(state=DISABLED)
            self.signup_btn.config(state=DISABLED)
        self.login_window.root.destroy()
        self.root.deiconify()

    def _open_signup_window(self):
        self.root.withdraw()
        self.signup_window = SignUp(self)
        self.signup_window.root.protocol('WM_DELETE_WINDOW', self._close_signup_window)
        self.signup_window.open()

    def _close_signup_window(self):
        if self.master.user:
            self.login_btn.config(state=DISABLED)
            self.signup_btn.config(state=DISABLED)
        self.signup_window.root.destroy()
        self.root.deiconify()

    def _open_settings(self):
        self.root.withdraw()
        self.settings_window = Settings(self)
        self.settings_window.root.protocol('WM_DELETE_WINDOW', self._close_settings_window)
        self.settings_window.open()

    def _close_settings_window(self):
        if not self.master.user:
            self.login_btn.config(state=NORMAL)
            self.signup_btn.config(state=NORMAL)
        self.settings_window.root.destroy()
        self.root.deiconify()
