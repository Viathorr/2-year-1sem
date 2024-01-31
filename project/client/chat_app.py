from main_window import MainWindow
from model.db_command import *
from model.db_control import DBControl
from user import User


class ChatApp:
    """
    Class representing the Chat Application.

    Attributes:
        main_window (MainWindow): The main window of the application.
        db_control (DBControl): Database control object for managing user data.
        user (User): Current user logged into the application.

    Methods:
        run():
            Run the Chat Application.
        _close_window():
            Close the application window.
        set_user(user: User):
            Set the current user of the application.

    """
    def __init__(self):
        """
        Initialize the Chat Application.
        """
        self.main_window = MainWindow(self)
        db = DatabaseUserTable()
        self.db_control = DBControl(CheckPasswordMatchingCommand(db), GetNameByEmailCommand(db),
                                    CheckEmailExistenceCommand(db), AddUserCommand(db), ChangeUsernameCommand(db))
        self.user = None
        self.main_window.root.protocol('WM_DELETE_WINDOW', self._close_window)

    def run(self):
        """
        Run the Chat Application.
        """
        self.main_window.open()

    def _close_window(self):
        """
        Close the application window.
        """
        self.main_window.root.destroy()

    def set_user(self, user: User) -> None:
        """
        Set the current user of the application.

        Args:
            user (User): The user object to set.
        """
        self.user = user


if __name__ == "__main__":
    my_app = ChatApp()
    my_app.run()
