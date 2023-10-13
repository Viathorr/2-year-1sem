from tkinter import *
from ttkbootstrap.constants import *
import ttkbootstrap as ttk
from tkinter import messagebox
from database import *


class SignUp:
    def __init__(self):
        self.db_table = DatabaseUserTable()

        self.root = ttk.Toplevel()
        self.root.title('Sign up')

        # Get the screen width and height
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()

        # Calculate the center position
        x_position = (screen_width - 450) // 2  # Adjust the width of the window
        y_position = (screen_height - 600) // 2

        self.root.geometry(f'450x600+{x_position}+{y_position}')
        self.root.minsize(450, 650)

        # Main label
        self.label = ttk.Label(self.root, text='Create an account', font=('Ebrima', 17),
                               bootstyle='info')
        self.label.place(relx=0.195, rely=0.13)

        # Name entry
        self.name_entry = ttk.Entry(self.root, width=25, font=('Ebrima', 10), foreground='gray')
        self.name_entry.insert(0, 'Enter your name')
        self.name_entry.place(relx=0.18, rely=0.28)
        self.name_entry.bind('<FocusIn>', lambda event: self._delete_default_text(0))
        self.name_entry.bind('<FocusOut>', lambda event: self._set_default_text(0))

        # Email entry
        self.email_entry = ttk.Entry(self.root, width=25, font=('Ebrima', 10), foreground='gray')
        self.email_entry.insert(0, 'Enter your email')
        self.email_entry.place(relx=0.18, rely=0.38)
        self.email_entry.bind('<FocusIn>', lambda event: self._delete_default_text(1))
        self.email_entry.bind('<FocusOut>', lambda event: self._set_default_text(1))

        # Password entry
        self.password_entry = ttk.Entry(self.root, width=25, font=('Ebrima', 10), foreground='gray')
        self.password_entry.insert(0, 'Enter your password')
        self.password_entry.place(relx=0.18, rely=0.48)
        self.password_entry.bind('<FocusIn>', lambda event: self._delete_default_text(2))
        self.password_entry.bind('<FocusOut>', lambda event: self._set_default_text(2))

        # Password confirmation entry
        self.confirm_password_entry = ttk.Entry(self.root, width=25, font=('Ebrima', 10), foreground='gray')
        self.confirm_password_entry.insert(0, 'Confirm your password')
        self.confirm_password_entry.place(relx=0.18, rely=0.58)
        self.confirm_password_entry.bind('<FocusIn>', lambda event: self._delete_default_text(3))
        self.confirm_password_entry.bind('<FocusOut>', lambda event: self._set_default_text(3))

        # Show password checkbutton
        self.check_var = BooleanVar(value=True)
        self.show_password_check = ttk.Checkbutton(self.root, text='Show password', variable=self.check_var,
                                                   bootstyle='info', command=self.show_password)
        self.show_password_check.place(relx=0.5, rely=0.67)

        # Sign up button
        self.signup_button = ttk.Button(self.root, text='Sign up', bootstyle='info', width=15, command=self.signup)
        self.signup_button.place(relx=0.3, rely=0.825, anchor='w')

    def run(self):
        self.root.mainloop()

    def _delete_default_text(self, num):
        if num == 0:
            self.name_entry.config(foreground='black')
            if self.name_entry.get() == 'Enter your name':
                self.name_entry.delete(0, END)
        elif num == 1:
            self.email_entry.config(foreground='black')
            if self.email_entry.get() == 'Enter your email':
                self.email_entry.delete(0, END)
        elif num == 2:
            self.password_entry.config(foreground='black')
            if self.password_entry.get() == 'Enter your password':
                self.password_entry.delete(0, END)
        elif num == 3:
            self.confirm_password_entry.config(foreground='black')
            if self.confirm_password_entry.get() == 'Confirm your password':
                self.confirm_password_entry.delete(0, END)

    def _set_default_text(self, num):
        if num == 0:
            if self.name_entry.get() == '':
                self.clean_entries(0)
        elif num == 1:
            if self.email_entry.get() == '':
                self.clean_entries(1)
        elif num == 2:
            if self.password_entry.get() == '':
                self.clean_entries(2)
        elif num == 3:
            if self.confirm_password_entry.get() == '':
                self.clean_entries(3)

    def show_password(self):
        if self.check_var.get():
            self.confirm_password_entry.config(show='')
            self.password_entry.config(show='')
        else:
            self.confirm_password_entry.config(show='*')
            self.password_entry.config(show='*')

    def clean_entries(self, num=0):
        if not num or num == 0:
            self.name_entry.delete(0, END)
            self.name_entry.config(foreground='gray')
            self.name_entry.insert(0, 'Enter your name')
        if not num or num == 1:
            self.email_entry.delete(0, END)
            self.email_entry.config(foreground='gray')
            self.email_entry.insert(0, 'Enter your email')
        if not num or num == 2:
            self.password_entry.delete(0, END)
            self.password_entry.config(foreground='gray')
            self.password_entry.insert(0, 'Enter your password')
        if not num or num == 3:
            self.confirm_password_entry.delete(0, END)
            self.confirm_password_entry.config(foreground='gray')
            self.confirm_password_entry.insert(0, 'Confirm your password')

    def signup(self):
        name = self.name_entry.get()
        email = self.email_entry.get()
        password = self.password_entry.get()
        confirm_password = self.confirm_password_entry.get()
        self.db_table.connect()

        if password != confirm_password:
            messagebox.showerror('Error', 'Passwords do not match. Please try again.')
            self.clean_entries(2)
            self.clean_entries(3)
            return
        if self.db_table.check_email_existence(email):
            messagebox.showwarning('Warning', '''An account with this email already exists. 
                                    Please use a different email or proceed to login.''')
            return
        else:
            self.db_table.add_user(name, email, password)
            messagebox.showinfo('Success', 'Registration completed successfully!')
            self.clean_entries()
