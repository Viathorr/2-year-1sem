from main_window import MainWindow
from model.db_command import *
from model.db_control import DBControl


class ChatApp:
    def __init__(self):
        self.main_window = MainWindow(self)
        db = DatabaseUserTable()
        self.db_control = DBControl(CheckPasswordMatchingCommand(db), GetNameByEmailCommand(db),
                                    CheckEmailExistenceCommand(db), AddUserCommand(db), ChangeUsernameCommand(db))
        self.user = None
        self.main_window.root.protocol('WM_DELETE_WINDOW', self._close_window)

    def run(self):
        self.main_window.open()

    def _close_window(self):
        self.main_window.root.destroy()

    def set_user(self, user):
        self.user = user


if __name__ == "__main__":
    my_app = ChatApp()
    my_app.run()
