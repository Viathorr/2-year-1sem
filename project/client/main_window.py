from tkinter import messagebox
from ttkbootstrap.constants import *
import ttkbootstrap as ttk
from signup import SignUp
from client.login import LogIn
from settings import Settings
from client.chat_window import ClientChatWindow


class MainWindow:
    """
    Class representing the main window of the chat application.

    Attributes:
        master (ChatApp): The application object.
        root (ttk.Window): The main window of the application.
        login_btn (ttk.Button): Button to open the login window.
        signup_btn (ttk.Button): Button to open the signup window.
        settings_window (Settings): Reference to the settings window.

    Methods:
        open():
            Opens the main window.
        close_window():
            Closes the main window.
        reopen_window():
            Reopens the main window after being minimized.
        _open_chat_window():
            Opens the chat window if the user is logged in.
        _close_chat_window():
            Closes the chat window.
        _open_login_window():
            Opens the login window.
        _close_login_window():
            Closes the login window.
        _open_signup_window():
            Opens the signup window.
        _close_signup_window():
            Closes the signup window.
        _open_settings():
            Opens the settings window.
        _close_settings_window():
            Closes the settings window.
        change_buttons_state(disable: bool):
            Changes the state of login and signup buttons based on the user's login status.
    """
    def __init__(self, parent, theme='minty') -> None:
        """
        Initialize the main window of the chat application.

        Args:
            parent (ChatApp): The parent application object.
            theme (str, optional): The theme of the window. Defaults to 'minty'.
        """
        self.master = parent  # chat app

        # Main Window
        self.root = ttk.Window(themename=theme)
        self.root.title('Chat')
        self.root.iconbitmap('./rsrc/chat.ico')
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

    def open(self) -> None:
        """
        Open the main window.
        """
        self.root.mainloop()

    def close_window(self) -> None:
        """
        Close the main window.
        """
        self.root.withdraw()

    def reopen_window(self) -> None:
        """
        Reopen the main window after being minimized.
        """
        self.root.deiconify()

    def _open_chat_window(self) -> None:
        """
        Open the chat window.
        """
        if not self.master.user:
            messagebox.showwarning('You must be logged in', "Please log in or sign up first.")
        else:
            self.root.withdraw()
            self.chat_window = ClientChatWindow(self)
            self.chat_window.root.protocol('WM_DELETE_WINDOW', self._close_chat_window)
            try:
                self.chat_window.connect()
            except Exception as ex:
                self.chat_window.root.destroy()
                self.root.deiconify()
                messagebox.showerror(title='Error', message=str(ex))

    def _close_chat_window(self) -> None:
        """
        Close the chat window.
        """
        print('in close window method')
        self.chat_window.socket.close()
        self.chat_window.destroy()
        self.root.deiconify()

    def _open_login_window(self) -> None:
        """
        Open the login window
        """
        self.root.withdraw()
        self.login_window = LogIn(self)
        self.login_window.root.protocol('WM_DELETE_WINDOW', self._close_login_window)
        self.login_window.open()

    def _close_login_window(self) -> None:
        """
        Close the login window
        """
        if self.master.user:
            self.change_buttons_state(True)
        self.login_window.root.destroy()
        self.root.deiconify()

    def _open_signup_window(self) -> None:
        """
        Open the signup window
        """
        self.root.withdraw()
        self.signup_window = SignUp(self)
        self.signup_window.root.protocol('WM_DELETE_WINDOW', self._close_signup_window)
        self.signup_window.open()

    def _close_signup_window(self) -> None:
        """
        Close the signup window
        """
        if self.master.user:
            self.change_buttons_state(True)
        self.signup_window.root.destroy()
        self.root.deiconify()

    def _open_settings(self) -> None:
        """
        Open the settings window
        """
        self.root.withdraw()
        self.settings_window = Settings(self)
        self.settings_window.root.protocol('WM_DELETE_WINDOW', self._close_settings_window)
        self.settings_window.open()

    def _close_settings_window(self) -> None:
        """
        Close the settings window.
        """
        if not self.master.user:
            self.change_buttons_state(False)
        self.settings_window.root.destroy()
        self.root.deiconify()

    def change_buttons_state(self, disable: bool) -> None:
        """
        Change the state of login and signup buttons.

        Args:
            disable (bool): True to disable buttons, False to enable.
        """
        self.login_btn.config(state=NORMAL if not disable else DISABLED)
        self.signup_btn.config(state=NORMAL if not disable else DISABLED)
