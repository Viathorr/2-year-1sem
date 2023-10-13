from tkinter import *
from ttkbootstrap.constants import *
import ttkbootstrap as ttk
from tkinter import messagebox
from database import *


class LogIn:
    def __init__(self):
        self.db_table = DatabaseUserTable()

        self.root = ttk.Toplevel()
        self.root.title("Log in")
        self.root.geometry('450x550')
        self.root.minsize(450, 400)

        self.label = ttk.Label(self.root, text='Welcome back!', font=('Ebrima', 16),
                          bootstyle='info')  # modify the font if you find
        self.label.place(relx=0.253, rely=0.15)

        # email entry
        self.email_entry = ttk.Entry(self.root, width=25, font=('Ebrima', 10), foreground='gray')
        self.email_entry.insert(0, 'Enter your email')
        self.email_entry.place(relx=0.185, rely=0.32)
        self.email_entry.bind('<FocusIn>', lambda event: self._delete_default_text(1))
        self.email_entry.bind('<FocusOut>', lambda event: self._set_default_text(1))

        # password entry
        self.password_entry = ttk.Entry(self.root, width=25, font=('Ebrima', 10), foreground='gray')
        self.password_entry.insert(0, 'Enter your password')
        self.password_entry.place(relx=0.185, rely=0.43)
        self.password_entry.bind('<FocusIn>', lambda event: self._delete_default_text(2))
        self.password_entry.bind('<FocusOut>', lambda event: self._set_default_text(2))

        # checkbutton
        self.check_var = BooleanVar(value=True)
        self.check_button = ttk.Checkbutton(self.root, text='Show password', variable=self.check_var,
                                            command=self.show_password, bootstyle='info')
        self.check_button.place(relx=0.5, rely=0.54)

        # login button
        self.login_button = ttk.Button(self.root, text='Log in', bootstyle='info', width=14, command=self.login)
        self.login_button.place(relx=0.315, rely=0.73, anchor='w')

    def run(self):
        self.root.mainloop()

    def show_password(self):
        if self.check_var.get():
            self.password_entry.config(show='')
        else:
            self.password_entry.config(show='*')

    def _delete_default_text(self, num):
        if num == 1:
            self.email_entry.config(foreground='black')
            if self.email_entry.get() == 'Enter your email':
                self.email_entry.delete(0, END)
        elif num == 2:
            self.password_entry.config(foreground='black')
            if self.password_entry.get() == 'Enter your password':
                self.password_entry.delete(0, END)

    def _set_default_text(self, num):
        if num == 1:
            if self.email_entry.get() == '':
                self.email_entry.insert(0, 'Enter your email')
                self.email_entry.config(foreground='gray')
        elif num == 2:
            if self.password_entry.get() == '':
                self.password_entry.insert(0, 'Enter your password')
                self.password_entry.config(foreground='gray')

    def login(self):
        email = self.email_entry.get()
        password = self.password_entry.get()
        self.db_table.connect()
        if self.db_table.check_email_existence(email):
            if self.db_table.check_password_matching(email, password):
                print('yes')
                messagebox.showinfo('Success', 'You successfully logged in!')
                self.clean_entries()
            else:
                print('no')
                messagebox.showwarning('Oops... something went wrong!', 'Invalid email or password. Please try again.')
                self.clean_entries(2)
        else:
            messagebox.showwarning('Oops... something went wrong!', 'Invalid email or password. Please try again.')
            self.clean_entries()

    def clean_entries(self, num=0):
        if not num or num == 1:
            self.email_entry.delete(0, END)
            self.email_entry.config(foreground='gray')
            self.email_entry.insert(0, 'Enter your email')
        if not num or num == 2:
            self.password_entry.delete(0, END)
            self.password_entry.config(foreground='gray')
            self.password_entry.insert(0, 'Enter your password')

    def close(self):
        self.root.destroy()
