from model.db_command import *
from model.db_control import DBControl
from gui.mediator import Mediator


class ChatApp:
    """
    Class representing the Chat Application.

    Attributes:
        _mediator (Mediator): The mediator that handles all needed events.

    Methods:
        run():
            Run the Chat Application.

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
