from client.gui.main_window import MainWindow
from model.db_command import *
from model.db_control import DBControl
from user.user import User
from gui.mediator import Mediator


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
        db = DatabaseUserTable()
        db_control = DBControl(CheckPasswordMatchingCommand(db), GetNameByEmailCommand(db),
                               CheckEmailExistenceCommand(db), AddUserCommand(db), ChangeUsernameCommand(db))
        self._mediator = Mediator(db_control)

    def run(self) -> None:
        """
        Run the Chat Application.
        """
        self._mediator.run()


if __name__ == "__main__":
    my_app = ChatApp()
    my_app.run()
