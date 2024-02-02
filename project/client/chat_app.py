from main_window import MainWindow
from model.db_command import *
from model.db_control import DBControl
from user import User


class ChatApp:
    """
    Class representing the Chat Application.

    Attributes:
        _main_window (MainWindow): The main window of the application.
        db_control (DBControl): Database control object for managing user data.
        _user (User): Current user logged into the application.

    Methods:
        run():
            Run the Chat Application.
        _close_window():
            Close the application window.
        deiconify_main_window():
            Reopen main window.
        set_user(user: User):
            Set the current user of the application.

    """
    def __init__(self) -> None:
        """
        Initialize the Chat Application.
        """
        self._main_window = MainWindow(self)
        db = DatabaseUserTable()
        self.db_control = DBControl(CheckPasswordMatchingCommand(db), GetNameByEmailCommand(db),
                                     CheckEmailExistenceCommand(db), AddUserCommand(db), ChangeUsernameCommand(db))
        self._user = None
        self._main_window.root.protocol('WM_DELETE_WINDOW', self._close_window)

    @property
    def user(self) -> None:
        return self._user

    def run(self) -> None:
        """
        Run the Chat Application.
        """
        self._main_window.open()

    def deiconify_main_window(self):
        self._main_window.root.deiconify()

    def _close_window(self) -> None:
        """
        Close the application window.
        """
        self._main_window.root.destroy()

    def set_user(self, user: User) -> None:
        """
        Set the current user of the application.

        Args:
            user (User): The user object to set.
        """
        self._user = user


if __name__ == "__main__":
    my_app = ChatApp()
    my_app.run()
