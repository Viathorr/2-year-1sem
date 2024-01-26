from main_window import MainWindow
from client.model.database import DatabaseUserTable


class ChatApp:
    def __init__(self):
        self.main_window = MainWindow(self)
        self.db = DatabaseUserTable()
        self.user = None

        self.main_window.root.protocol('WM_DELETE_WINDOW', self._close_window)
        self.db.connect()

    def run(self):
        self.main_window.open()

    def _close_window(self):
        self.db.close_connection()
        self.main_window.root.destroy()

    def set_user(self, user):
        self.user = user


if __name__ == "__main__":
    my_app = ChatApp()
    my_app.run()
