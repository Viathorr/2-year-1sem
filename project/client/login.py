from tkinter import *
from ttkbootstrap.constants import *
import ttkbootstrap as ttk
from tkinter import messagebox
from ttkbootstrap.tooltip import ToolTip
from user import User


class LogIn:
    """
    Class for the sign-up window.

    Attributes:
        _master (ChatApp): The application object.
        root (ttk.Toplevel): Toplevel window with Signup form.
        _email_entry (ttk.Entry): Email field.
        _password_entry (ttk.Entry): Password field.
        _check_var (BooleanVar): The value of show_password checkbox.
        _login_button (ttk.Button): The button to login.

    Methods:
        open(self):
            Opens the signup window.
        _delete_default_text(num: int):
            Deletes the default text in the entry fields.
        _set_default_text(num: int):
            Sets the default text in the entry fields.
        _show_password():
            Toggles the visibility of the password field.
        _clean_entries(num: int = 0):
            Cleans the entry fields.
        _login():
            Handles the login process.

    """
    def __init__(self, master) -> None:
        """
        Initialize the login window.

        Args:
            master (ChatApp): The application object.

        """
        self._master = master  # main window's master
        self.root = ttk.Toplevel()
        self.root.title("Log in")
        self.root.iconbitmap('./rsrc/chat.ico')
        self.root.resizable(False, False)

        label = ttk.Label(self.root, text='Welcome back', font=('Microsoft JhengHei', 17, 'bold'), bootstyle='dark')
        label.place(relx=0.23, rely=0.15)

        # email entry
        self._email_entry = ttk.Entry(self.root, width=25, font=('Ebrima', 10), foreground='gray')
        self._email_entry.insert(0, 'Enter your email')
        self._email_entry.place(relx=0.185, rely=0.32)
        self._email_entry.bind('<FocusIn>', lambda event: self._delete_default_text(1))
        self._email_entry.bind('<FocusOut>', lambda event: self._set_default_text(1))
        ToolTip(self._email_entry, 'Email', bootstyle='secondary-inverse')

        # password entry
        self._password_entry = ttk.Entry(self.root, width=25, font=('Ebrima', 10), foreground='gray')
        self._password_entry.insert(0, 'Enter your password')
        self._password_entry.place(relx=0.185, rely=0.43)
        self._password_entry.bind('<FocusIn>', lambda event: self._delete_default_text(2))
        self._password_entry.bind('<FocusOut>', lambda event: self._set_default_text(2))
        ToolTip(self._password_entry, 'Password', bootstyle='secondary-inverse')

        # checkbutton
        self._check_var = BooleanVar(value=False)
        check_button = ttk.Checkbutton(self.root, text='Show password', variable=self._check_var,
                                       command=self._show_password, bootstyle='info')
        check_button.place(relx=0.5, rely=0.54)

        # login button
        self._login_button = ttk.Button(self.root, text='Log in', bootstyle='info', width=14, command=self._login)
        self._login_button.place(relx=0.29, rely=0.73, anchor='w')

    def open(self):
        """
        Open the login window.
        """
        # Calculate the center position
        x_position = (self.root.winfo_screenwidth() - 450) // 2  # Adjust the width of the window
        y_position = (self.root.winfo_screenheight() - 550) // 2

        self.root.geometry(f'450x550+{x_position}+{y_position - 50}')
        self.root.mainloop()

    def _show_password(self) -> None:
        """
        Toggle the visibility of the password field.
        """
        if self._check_var.get():
            self._password_entry.config(show='')
        elif self._password_entry.get() != 'Enter your password':
            self._password_entry.config(show='•')

    def _delete_default_text(self, num: int) -> None:
        """
        Delete the default text in the entry fields.

        Args:
            num (int): The number indicating which entry field to modify.

        """
        if num == 1:
            self._email_entry.config(foreground='black')
            if self._email_entry.get() == 'Enter your email':
                self._email_entry.delete(0, END)
        elif num == 2:
            self._password_entry.config(foreground='black')
            if self._password_entry.get() == 'Enter your password':
                self._password_entry.delete(0, END)
                if not self._check_var.get():
                    self._password_entry.config(show='•')

    def _set_default_text(self, num: int) -> None:
        """
        Set the default text in the entry fields.

        Args:
            num (int): The number indicating which entry field to modify.

        """
        if num == 1:
            if self._email_entry.get() == '':
                self._email_entry.insert(0, 'Enter your email')
                self._email_entry.config(foreground='gray')
        elif num == 2:
            if self._password_entry.get() == '':
                if not self._check_var.get():
                    self._password_entry.config(show='')
                self._password_entry.insert(0, 'Enter your password')
                self._password_entry.config(foreground='gray')

    def _login(self) -> None:
        """
        Handle the login process.
        """
        email = self._email_entry.get()
        password = self._password_entry.get()

        try:
            username = self._master.db_control.login_check(email, password)
            user = User(username, email)
            self._master.set_user(user)
            # showing the result
            messagebox.showinfo('Success', 'You\'ve successfully logged in!')
            self._clean_entries()
            self._login_button.config(state=DISABLED)
        except Exception as ex:
            messagebox.showerror('Oops... something went wrong!', str(ex))
            self._clean_entries()

    def _clean_entries(self, num: int = 0) -> None:
        """
        Clean the entry fields.

        Args:
            num (int, optional): The number indicating which entry field to clean.
                If not specified, all entry fields will be cleaned.

        """
        if not num or num == 1:
            self._email_entry.delete(0, END)
            self._email_entry.config(foreground='gray')
            self._email_entry.insert(0, 'Enter your email')
        if not num or num == 2:
            self._password_entry.delete(0, END)
            self._password_entry.config(foreground='gray')
            if not self._check_var.get():
                self._password_entry.config(show='')
            self._password_entry.insert(0, 'Enter your password')
