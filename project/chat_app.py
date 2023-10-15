from main_window import *
from database import DatabaseUserTable
# from user import User


class ChatApp:
    def __init__(self):
        self.main_window = MainWindow(self)
        self.db = DatabaseUserTable()
        self.user = None

        self.main_window.root.protocol('WM_DELETE_WINDOW', self.close_window)
        self.db.connect()

    def close_window(self):
        self.db.close_connection()
        self.main_window.root.destroy()

    def open(self):
        self.main_window.run()

    def set_user(self, user):
        self.user = user


my_app = ChatApp()
my_app.open()
