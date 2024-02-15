from tkinter import messagebox
from ttkbootstrap.constants import *
import ttkbootstrap as ttk
from .imediator import IMediator


class MainWindow:
    """
    Class representing the main window of the chat application.

    Attributes:
        _mediator (IMediator): The mediator that handles needed events.
        root (ttk.Window): The main window of the application.
        _login_btn (ttk.Button): Button to open the login window.
        _signup_btn (ttk.Button): Button to open the signup window.

    Methods:
        open():
            Opens the main window.
        close_window():
            Closes the main window.
        reopen_window():
            Reopens the main window after being minimized.
        destroy_window():
            Destroys the main window.
        _open_chat_window():
            Opens the chat window if the user is logged in.
        show_err(err: str):
            Takes an error message and displays it.
        change_buttons_state(disable: bool):
            Changes the state of login and signup buttons based on the user's login status.
    """
    def __init__(self, mediator: IMediator, theme='minty') -> None:
        """
        Initialize the main window of the chat application.

        Args:
            mediator (IMediator): The mediator that handles all needed events.
            theme (str, optional): The theme of the window. Defaults to 'minty'.
        """
        self._mediator = mediator  # mediator class

        # Main Window
        self.root = ttk.Window(themename=theme)
        self.root.title('Chat')
        self.root.iconbitmap('./rsrc/chat.ico')
        self.root.resizable(False, False)
        # self.root.protocol('WM_DELETE_WINDOW', self.destroy_window)

        # Calculate the center position
        x_position = (self.root.winfo_screenwidth() - 550) // 2  # Adjust the width of the window
        y_position = (self.root.winfo_screenheight() - 600) // 2

        self.root.geometry(f'550x600+{x_position}+{y_position - 30}')
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

        # Log in button
        self._login_btn = ttk.Button(text='Log in', bootstyle='info', width=17,
                                     command=self._mediator.open_login_window)
        self._login_btn.grid(row=2, column=1, ipady=10)

        # Sign up button
        self._signup_btn = ttk.Button(text='Sign up', bootstyle='info', width=17,
                                      command=self._mediator.open_signup_window)
        self._signup_btn.grid(row=3, column=1, ipady=10)
        # Settings button
        settings_btn = ttk.Button(text='Settings', bootstyle='dark-outline', width=17,
                                  command=self._mediator.open_settings)
        settings_btn.grid(row=4, column=1, ipady=3, pady=15, sticky='n')

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

    def destroy_window(self) -> None:
        """
        Destroys the main window.
        """
        self.root.destroy()

    def _open_chat_window(self) -> None:
        """
        Open the chat window.
        """
        if not self._mediator.user:
            messagebox.showwarning('You must be logged in', "Please log in or sign up first.")
        else:
            self.close_window()
            self._mediator.open_chat_window()

    def show_error(self, err: str):
        """
        Displays given err message.

        Args:
            err (str): The err message to display.
        """
        messagebox.showerror(title='Error', message=err)

    def change_buttons_state(self, disable: bool) -> None:
        """
        Change the state of login and signup buttons.

        Args:
            disable (bool): True to disable buttons, False to enable.
        """
        self._login_btn.config(state=NORMAL if not disable else DISABLED)
        self._signup_btn.config(state=NORMAL if not disable else DISABLED)
