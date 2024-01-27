from tkinter import *
from ttkbootstrap.constants import *
import ttkbootstrap as ttk
from tkinter import messagebox
from ttkbootstrap.tooltip import ToolTip
from user import User


class LogIn:
    def __init__(self, parent):
        self.master = parent.master  # main window's master
        self.root = ttk.Toplevel()
        self.root.title("Log in")
        self.root.iconbitmap('./rsrc/chat.ico')
        self.root.resizable(False, False)

        label = ttk.Label(self.root, text='Welcome back', font=('Microsoft JhengHei', 17, 'bold'), bootstyle='dark')
        label.place(relx=0.23, rely=0.15)

        # email entry
        self.email_entry = ttk.Entry(self.root, width=25, font=('Ebrima', 10), foreground='gray')
        self.email_entry.insert(0, 'Enter your email')
        self.email_entry.place(relx=0.185, rely=0.32)
        self.email_entry.bind('<FocusIn>', lambda event: self._delete_default_text(1))
        self.email_entry.bind('<FocusOut>', lambda event: self._set_default_text(1))
        ToolTip(self.email_entry, 'Email', bootstyle='secondary-inverse')

        # password entry
        self.password_entry = ttk.Entry(self.root, width=25, font=('Ebrima', 10), foreground='gray')
        self.password_entry.insert(0, 'Enter your password')
        self.password_entry.place(relx=0.185, rely=0.43)
        self.password_entry.bind('<FocusIn>', lambda event: self._delete_default_text(2))
        self.password_entry.bind('<FocusOut>', lambda event: self._set_default_text(2))
        ToolTip(self.password_entry, 'Password', bootstyle='secondary-inverse')

        # checkbutton
        self.check_var = BooleanVar(value=False)
        check_button = ttk.Checkbutton(self.root, text='Show password', variable=self.check_var,
                                       command=self._show_password, bootstyle='info')
        check_button.place(relx=0.5, rely=0.54)

        # login button
        self.login_button = ttk.Button(self.root, text='Log in', bootstyle='info', width=14, command=self._login)
        self.login_button.place(relx=0.29, rely=0.73, anchor='w')

    def open(self):
        # Calculate the center position
        x_position = (self.root.winfo_screenwidth() - 450) // 2  # Adjust the width of the window
        y_position = (self.root.winfo_screenheight() - 550) // 2

        self.root.geometry(f'450x550+{x_position}+{y_position - 50}')
        self.root.mainloop()

    def _show_password(self):
        if self.check_var.get():
            self.password_entry.config(show='')
        elif self.password_entry.get() != 'Enter your password':
            self.password_entry.config(show='•')

    def _delete_default_text(self, num):
        if num == 1:
            self.email_entry.config(foreground='black')
            if self.email_entry.get() == 'Enter your email':
                self.email_entry.delete(0, END)
        elif num == 2:
            self.password_entry.config(foreground='black')
            if self.password_entry.get() == 'Enter your password':
                self.password_entry.delete(0, END)
                if not self.check_var.get():
                    self.password_entry.config(show='•')

    def _set_default_text(self, num):
        if num == 1:
            if self.email_entry.get() == '':
                self.email_entry.insert(0, 'Enter your email')
                self.email_entry.config(foreground='gray')
        elif num == 2:
            if self.password_entry.get() == '':
                if not self.check_var.get():
                    self.password_entry.config(show='')
                self.password_entry.insert(0, 'Enter your password')
                self.password_entry.config(foreground='gray')

    def _login(self):
        email = self.email_entry.get()
        password = self.password_entry.get()

        try:
            username = self.master.db_control.login_check(email, password)
            user = User(username, email)
            self.master.set_user(user)
            # showing the result
            messagebox.showinfo('Success', 'You\'ve successfully logged in!')
            self._clean_entries()
            self.login_button.config(state=DISABLED)
        except Exception as ex:
            messagebox.showerror('Oops... something went wrong!', str(ex))
            self._clean_entries()

    def _clean_entries(self, num=0):
        if not num or num == 1:
            self.email_entry.delete(0, END)
            self.email_entry.config(foreground='gray')
            self.email_entry.insert(0, 'Enter your email')
        if not num or num == 2:
            self.password_entry.delete(0, END)
            self.password_entry.config(foreground='gray')
            if not self.check_var.get():
                self.password_entry.config(show='')
            self.password_entry.insert(0, 'Enter your password')
