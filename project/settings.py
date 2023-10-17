import tkinter as tk
import ttkbootstrap as ttk
from tkinter import messagebox
from ttkbootstrap.tooltip import ToolTip
from ttkbootstrap.toast import ToastNotification
from ttkbootstrap.constants import *


class Settings:
    def __init__(self, parent):
        self.master = parent.master  # main window's master
        self.root = ttk.Toplevel()
        self.root.title('Settings')
        self.root.iconbitmap('rsrc/chat.ico')

        # Calculate the center position
        x_position = (self.root.winfo_screenwidth() - 500) // 2  # Adjust the width of the window
        y_position = (self.root.winfo_screenheight() - 400) // 2

        self.root.geometry(f'500x400+{x_position-555}+{y_position}')
        self.root.minsize(500, 400)

        self.root.columnconfigure(0, weight=1)
        self.root.columnconfigure(1, weight=2)

        self.name_entry_text = tk.StringVar(value='None')
        self.email_entry_text = tk.StringVar(value='None')

        if self.master.user:
            self.name_entry_text.set(value=self.master.user.name)
            self.email_entry_text.set(value=self.master.user.email)

        # User name
        name_label = ttk.Label(self.root, text='Name', font=('Microsoft JhengHei Light', 16, 'bold'),
                                    bootstyle='info')
        name_label.grid(row=0, column=0, padx=10, pady=30, sticky='e')
        name_entry = ttk.Entry(self.root, textvariable=self.name_entry_text, width=24,
                               font=('Microsoft JhengHei Light', 9), bootstyle='info')
        name_entry.grid(row=0, column=1, ipady=4)

        # User email
        email_label = ttk.Label(self.root, text='Email', font=('Microsoft JhengHei Light', 16, 'bold'),
                                     bootstyle='info')
        email_label.grid(row=1, column=0, padx=10, pady=20, sticky='e')
        email_entry = ttk.Entry(self.root, state='readonly', textvariable=self.email_entry_text, width=24,
                                     font=('Microsoft JhengHei Light', 9), bootstyle='info')
        email_entry.grid(row=1, column=1, ipady=4)
        ToolTip(email_entry, "You can't change an email", bootstyle='secondary-inverse')

        # Save changes button
        btn_style = ttk.Style()
        btn_style.configure('info.TButton', font=('Microsoft JhengHei Light', 10, 'bold'))

        save_changes_btn = ttk.Button(self.root, text='Save changes', bootstyle='info', width=13,
                                           command=self._save_changes)
        save_changes_btn.grid(row=2, column=1, padx=51, pady=20, ipady=7, ipadx=10, columnspan=2, sticky='se')

        logout_btn = ttk.Button(self.root, text='Log out', bootstyle='info-outline', width=10, command=self._logout)
        logout_btn.grid(row=3, column=1, padx=51, pady=10, ipady=4, columnspan=2, sticky='se')

    def open(self):
        self.root.mainloop()

    def _save_changes(self):
        if not self.master.user:
            messagebox.showerror('You must be logged in', "Please log in or sign up first.")
        else:
            self.master.user.change_name(new_name=self.name_entry_text.get())

    def _logout(self):
        if not self.master.user:
            messagebox.showerror('You must be logged in', "Please log in or sign up first.")
        else:
            yesno = messagebox.askyesno('Logging out', 'Are you sure you want to log out?')
            if yesno:
                self.master.user = None
                self.name_entry_text.set(value='None')
                self.email_entry_text.set(value='None')
