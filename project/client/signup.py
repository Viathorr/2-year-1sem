from tkinter import *
from ttkbootstrap.constants import *
import ttkbootstrap as ttk
from tkinter import messagebox
from ttkbootstrap.tooltip import ToolTip
from user import User
from utilities.email_validation import EmailValidation
from utilities.string_utilities import StringUtilities


class SignUp:
    """
    Class for the sign-up window.

    Attributes:
        master (ChatApp): The application object.
        root (ttk.Toplevel): Toplevel window with Signup form.
        name_entry (ttk.Entry): Name field.
        email_entry (ttk.Entry): Email field.
        password_entry (ttk.Entry): Password field.
        confirm_password_entry (ttk.Entry): Confirm password field.
        check_var (BooleanVar): The value of show_password checkbox.
        signup_button (ttk.Button): The button to signup.

    Methods:
        open(self):
            Opens the signup window.
        _delete_default_text(num: int):
            Deletes the default text in the entry fields.
        _set_default_text(num: int):
            Sets the default text in the entry fields.
        _show_password():
            Toggles the visibility of the password fields.
        _clean_entries(num: int = 0):
            Cleans the entry fields.
        _signup():
            Handles the sign-up process.

    """
    def __init__(self, parent) -> None:
        """Initialize the sign-up window.

        Args:
            parent (MainWindow): The parent window.

        """
        self.master = parent.master  # main window's master
        self.root = ttk.Toplevel()
        self.root.title('Sign up')
        self.root.iconbitmap('./rsrc/chat.ico')
        self.root.resizable(False, False)

        # Calculate the center position
        x_position = (self.root.winfo_screenwidth() - 450) // 2  # Adjust the width of the window
        y_position = (self.root.winfo_screenheight() - 600) // 2

        self.root.geometry(f'450x600+{x_position}+{y_position - 50}')

        # Main label
        label = ttk.Label(self.root, text='Create an account', font=('Microsoft JhengHei', 17, 'bold'),
                               bootstyle='dark')
        label.place(relx=0.17, rely=0.13)

        # Name entry
        self.name_entry = ttk.Entry(self.root, width=25, font=('Ebrima', 10), foreground='gray')
        self.name_entry.insert(0, 'Enter your name')
        self.name_entry.place(relx=0.18, rely=0.28)
        self.name_entry.bind('<FocusIn>', lambda event: self._delete_default_text(1))
        self.name_entry.bind('<FocusOut>', lambda event: self._set_default_text(1))
        ToolTip(self.name_entry, 'Name', bootstyle='secondary-inverse')

        # Email entry
        self.email_entry = ttk.Entry(self.root, width=25, font=('Ebrima', 10), foreground='gray')
        self.email_entry.insert(0, 'Enter your email')
        self.email_entry.place(relx=0.18, rely=0.38)
        self.email_entry.bind('<FocusIn>', lambda event: self._delete_default_text(2))
        self.email_entry.bind('<FocusOut>', lambda event: self._set_default_text(2))
        ToolTip(self.email_entry, 'Email', bootstyle='secondary-inverse')

        # Password entry
        self.password_entry = ttk.Entry(self.root, width=25, font=('Ebrima', 10), foreground='gray')
        self.password_entry.insert(0, 'Enter your password')
        self.password_entry.place(relx=0.18, rely=0.48)
        self.password_entry.bind('<FocusIn>', lambda event: self._delete_default_text(3))
        self.password_entry.bind('<FocusOut>', lambda event: self._set_default_text(3))
        ToolTip(self.password_entry, 'Password', bootstyle='secondary-inverse')

        # Password confirmation entry
        self.confirm_password_entry = ttk.Entry(self.root, width=25, font=('Ebrima', 10), foreground='gray')
        self.confirm_password_entry.insert(0, 'Confirm your password')
        self.confirm_password_entry.place(relx=0.18, rely=0.58)
        self.confirm_password_entry.bind('<FocusIn>', lambda event: self._delete_default_text(4))
        self.confirm_password_entry.bind('<FocusOut>', lambda event: self._set_default_text(4))
        ToolTip(self.confirm_password_entry, 'Confirm password', bootstyle='secondary-inverse')

        # Show password checkbutton
        self.check_var = BooleanVar(value=False)
        show_password_check = ttk.Checkbutton(self.root, text='Show password', variable=self.check_var,
                                                   bootstyle='info', command=self._show_password)
        show_password_check.place(relx=0.5, rely=0.67)

        # Sign up button
        self.signup_button = ttk.Button(self.root, text='Sign up', bootstyle='info', width=15, command=self._signup)
        self.signup_button.place(relx=0.275, rely=0.825, anchor='w')

    def open(self) -> None:
        """
        Open the sign-up window.
        """
        self.root.mainloop()

    def _delete_default_text(self, num: int) -> None:
        """
        Delete the default text in the entry fields.

        Args:
            num (int): The number indicating which entry field to modify.

        """
        if num == 1:
            self.name_entry.config(foreground='black')
            if self.name_entry.get() == 'Enter your name':
                self.name_entry.delete(0, END)
        elif num == 2:
            self.email_entry.config(foreground='black')
            if self.email_entry.get() == 'Enter your email':
                self.email_entry.delete(0, END)
        elif num == 3:
            self.password_entry.config(foreground='black')
            if self.password_entry.get() == 'Enter your password':
                self.password_entry.delete(0, END)
                if not self.check_var.get():
                    self.password_entry.config(show='•')
        elif num == 4:
            self.confirm_password_entry.config(foreground='black')
            if self.confirm_password_entry.get() == 'Confirm your password':
                self.confirm_password_entry.delete(0, END)
                if not self.check_var.get():
                    self.confirm_password_entry.config(show='•')

    def _set_default_text(self, num: int) -> None:
        """
        Set the default text in the entry fields.

        Args:
            num (int): The number indicating which entry field to modify.

        """
        if num == 1:
            if self.name_entry.get() == '':
                self._clean_entries(1)
        elif num == 2:
            if self.email_entry.get() == '':
                self._clean_entries(2)
        elif num == 3:
            if self.password_entry.get() == '':
                self._clean_entries(3)
        elif num == 4:
            if self.confirm_password_entry.get() == '':
                self._clean_entries(4)

    def _show_password(self) -> None:
        """
        Toggle the visibility of the password fields.
        """
        if self.check_var.get():
            self.confirm_password_entry.config(show='')
            self.password_entry.config(show='')
        else:
            if self.confirm_password_entry.get() != 'Confirm your password':
                self.confirm_password_entry.config(show='•')
            if self.password_entry.get() != 'Enter your password':
                self.password_entry.config(show='•')

    def _clean_entries(self, num: int = 0) -> None:
        """
        Clean the entry fields.

        Args:
            num (int, optional): The number indicating which entry field to clean.
                If not specified, all entry fields will be cleaned.

        """
        if not num or num == 1:
            self.name_entry.delete(0, END)
            self.name_entry.config(foreground='gray')
            self.name_entry.insert(0, 'Enter your name')
        if not num or num == 2:
            self.email_entry.delete(0, END)
            self.email_entry.config(foreground='gray')
            self.email_entry.insert(0, 'Enter your email')
        if not num or num == 3:
            self.password_entry.delete(0, END)
            if not self.check_var.get():
                self.password_entry.config(show='')
            self.password_entry.config(foreground='gray')
            self.password_entry.insert(0, 'Enter your password')
        if not num or num == 4:
            self.confirm_password_entry.delete(0, END)
            if not self.check_var.get():
                self.confirm_password_entry.config(show='')
            self.confirm_password_entry.config(foreground='gray')
            self.confirm_password_entry.insert(0, 'Confirm your password')

    def _signup(self) -> None:
        """
        Handle the sign-up process.
        """
        name = self.name_entry.get()
        email = self.email_entry.get()
        if name == 'Enter your name' or StringUtilities.is_empty_string(name):
            messagebox.showerror('Error', 'Please enter your name.')
            return
        elif StringUtilities.contains_newline_char(name):
            messagebox.showerror('Error', 'The use of special characters, such as newline, is not allowed in names. '
                                          'Please enter a name without special characters.')
            return

        if not EmailValidation.is_valid_email(email):
            messagebox.showerror('Error', 'Invalid email. Try again.')
            return

        password = self.password_entry.get()
        confirm_password = self.confirm_password_entry.get()

        if password != confirm_password:
            messagebox.showerror('Error', 'Passwords do not match. Please try again.')
            self._clean_entries(3)
            self._clean_entries(4)
            return
        elif StringUtilities.is_empty_string(password):
            messagebox.showerror('Error', 'Please enter valid password.')
            return
        if self.master.db_control.email_exists(email):
            messagebox.showwarning('Warning', '''An account with this email already exists.\n'''
                                              '''Please use a different email or proceed to login.''')
            return
        else:
            self.master.db_control.add_user(name, email, password)
            user = User(name, email)
            self.master.set_user(user)

            messagebox.showinfo('Success', 'Registration has completed successfully!')
            self._clean_entries()
            self.signup_button.config(state=DISABLED)
