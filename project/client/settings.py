import tkinter as tk
import ttkbootstrap as ttk
from tkinter import messagebox
from ttkbootstrap.tooltip import ToolTip
from ttkbootstrap.constants import *
from utilities.string_utilities import StringUtilities


class Settings:
    """
    Class for the settings window.

    Attributes:
        _master (ChatApp): The application object.
        root (ttk.Toplevel): Toplevel window with Signup form.
        _name_entry_text (tk.StringVal): The value of name entry.
        _email_entry_text (tk.StringVal): The value of email entry.

    Methods:
        open(self):
            Opens the settings window.
        _save_changes():
            Saves the changes of the username, if there are any.
        _logout():
            Handles the logout process.

    """
    def __init__(self, master) -> None:
        """
        Initialize the settings window.

        Args:
            master (ChatApp): The application object.
        """
        self._master = master
        self.root = ttk.Toplevel()
        self.root.title('Settings')
        self.root.iconbitmap('./rsrc/chat.ico')
        self.root.resizable(False, False)

        self.root.columnconfigure(0, weight=1)
        self.root.columnconfigure(1, weight=2)

        self._name_entry_text = tk.StringVar(value='None')
        self._email_entry_text = tk.StringVar(value='None')

        if self._master.user:
            self._name_entry_text.set(value=self._master.user.name)
            self._email_entry_text.set(value=self._master.user.email)

        # User name
        name_label = ttk.Label(self.root, text='Name', font=('Microsoft JhengHei', 16),
                               bootstyle='dark')
        name_label.grid(row=0, column=0, padx=10, pady=17, sticky='se')
        name_entry = ttk.Entry(self.root, textvariable=self._name_entry_text, width=26,
                               font=('Microsoft JhengHei Light', 9), bootstyle='info', foreground='gray')
        name_entry.grid(row=0, column=1, ipady=4, pady=15, sticky='s')

        # User email
        email_label = ttk.Label(self.root, text='Email', font=('Microsoft JhengHei', 16),
                                bootstyle='dark')
        email_label.grid(row=1, column=0, padx=10, pady=15, sticky='e')
        email_entry = ttk.Entry(self.root, state='readonly', textvariable=self._email_entry_text, width=26,
                                font=('Microsoft JhengHei Light', 9), bootstyle='info', foreground='gray')
        email_entry.grid(row=1, column=1, ipady=4)
        ToolTip(email_entry, "You can't change an email", bootstyle='secondary-inverse')

        # Save changes button
        btn_style = ttk.Style()
        btn_style.configure('info.TButton', font=('Microsoft JhengHei', 10, 'bold'))

        save_changes_btn = ttk.Button(self.root, text='Save changes', bootstyle='info', width=13,
                                      command=self._save_changes)
        save_changes_btn.grid(row=2, column=1, padx=51, pady=20, ipady=7, ipadx=10, columnspan=2, sticky='se')

        logout_btn = ttk.Button(self.root, text='Log out', bootstyle='dark-outline', width=10)
        if self._master.user:
            logout_btn.config(state=NORMAL, command=self._logout)
        else:
            logout_btn.config(state=DISABLED)
        logout_btn.grid(row=3, column=1, padx=51, pady=10, ipady=4, columnspan=2, sticky='se')

    def open(self) -> None:
        """
        Open the settings window.
        """
        # Calculate the center position
        x_position = (self.root.winfo_screenwidth() - 500) // 2  # Adjust the width of the window
        y_position = (self.root.winfo_screenheight() - 350) // 2

        self.root.geometry(f'500x350+{x_position}+{y_position - 50}')
        self.root.mainloop()

    def _save_changes(self) -> None:
        """
        Save the changes of the username, if there are any.
        """
        if not self._master.user:
            messagebox.showerror('You must be logged in', "Please log in or sign up first.")
        else:
            new_name = self._name_entry_text.get()
            if not StringUtilities.contains_newline_char(self._name_entry_text.get()) and not StringUtilities.is_empty_string(self._name_entry_text.get()):
                self._master.user.name = new_name
                self._master.db_control.change_username(new_name, self._master.user.email)
            elif StringUtilities.is_empty_string(self._name_entry_text.get()):
                messagebox.showerror('Error', 'Please enter a non-empty name.')
            else:
                messagebox.showerror('Error', 'The use of special characters, such as newline, is not allowed in names.'
                                              ' Please enter a name without special characters.')

    def _logout(self) -> None:
        """
        Handle the logout process.
        """
        if not self._master.user:
            messagebox.showerror('You must be logged in', "Please log in or sign up first.")
        else:
            yesno = messagebox.askyesno('Logging out', 'Are you sure you want to log out?')
            if yesno:
                self._master.set_user(None)
                self._name_entry_text.set(value='None')
                self._email_entry_text.set(value='None')
