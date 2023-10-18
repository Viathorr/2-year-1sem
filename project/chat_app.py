from main_window import MainWindow
from chat_window import ChatWindow
from database import DatabaseUserTable

# TODO
# 1. Modify main window appearance
# 2. If you want, modify the name entry in settings window, so that when the focus is on it, font color changes to black
# and vice versa


class ChatApp:
    def __init__(self):
        self.main_window = MainWindow(self)
        self.db = DatabaseUserTable()
        self.user = None

        self.main_window.root.protocol('WM_DELETE_WINDOW', self._close_window)
        self.db.connect()

    def run(self):
        self.main_window.open()

    def _open_chat_window(self):
        # if not self.master.user:
        #     messagebox.showerror('You must be logged in', "Please log in or sign up first.")
        # else:
        chat_window = ChatWindow(self)
        chat_window.open()

    def _close_window(self):
        self.db.close_connection()
        self.main_window.root.destroy()

    def set_user(self, user):
        self.user = user


if __name__ == "__main__":
    my_app = ChatApp()
    my_app.run()
