from main_window import *
from database import DatabaseUserTable
from user import User


class ChatApp:
    def __init__(self):
        self.main_window = MainWindow()
        self.db = DatabaseUserTable()
        self.user = None
