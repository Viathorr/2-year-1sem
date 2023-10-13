from tkinter import *
from ttkbootstrap.constants import *
import ttkbootstrap as ttk
# from PIL import ImageTk, Image
from signup import SignUp
from login import LogIn


class MainWindow:
    def __init__(self):
        # Main Window
        self.root = ttk.Window(themename='morph')
        self.root.title('Main')

        # Get the screen width and height
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()

        # Calculate the center position
        x_position = (screen_width - 600) // 2  # Adjust the width of the window
        y_position = (screen_height - 650) // 2

        self.root.geometry(f'600x650+{x_position}+{y_position}')
        self.root.minsize(500, 550)

        self.root.rowconfigure((0, 4), weight=3)
        self.root.rowconfigure((1, 2, 3), weight=1)
        self.root.columnconfigure((0, 2), weight=1)
        self.root.columnconfigure(1, weight=4)

        # Main label
        self.label = ttk.Label(text='Online Chat', font=('Microsoft JhengHei Light', 20), bootstyle='info')
        self.label.grid(row=0, column=1)

        # buttons style
        outline_btn_style = ttk.Style()
        outline_btn_style.configure('info.Outline.TButton', font=('Microsoft JhengHei Light', 10))
        btn_style = ttk.Style()
        btn_style.configure('info.TButton', font=('Microsoft JhengHei Light', 10))

        # Open button
        self.open_btn = ttk.Button(text='Open', bootstyle='info', width=18)
        self.open_btn.grid(row=1, column=1, ipady=10)

        # Log in button
        self.login_btn = ttk.Button(text='Log in', bootstyle='info-outline', width=18,
                                    command=self.open_login_window)
        self.login_btn.grid(row=2, column=1, ipady=10)

        # Sign up button
        self.signup_btn = ttk.Button(text='Sign up', bootstyle='info-outline', width=18,
                                     command=self.open_signup_window)
        self.signup_btn.grid(row=3, column=1, ipady=10)

        # Settings button (implement)

    def run(self):
        self.root.mainloop()

    @staticmethod
    def open_login_window():
        login = LogIn()
        login.run()

    @staticmethod
    def open_signup_window():
        signup = SignUp()
        signup.run()


instance = MainWindow()
instance.run()

