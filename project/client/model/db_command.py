from .database import DatabaseUserTable
from abc import ABC, abstractmethod
import bcrypt
import base64
from typing import Union


class ICommand(ABC):
    """
    Abstract base class for defining command objects.

    Attributes:
        db (DatabaseUserTable): The database object used by the command.

    Methods:
        execute(**kwargs) -> Union[bool, str, None]:
            Executes the command with optional arguments and keyword arguments.
    """
    def __init__(self, db: DatabaseUserTable) -> None:
        """
        Initialize a new ICommand object.

        Args:
            db (DatabaseUserTable): The database object used by the command.
        """
        self._db = db

    @abstractmethod
    def execute(self, **kwargs) -> Union[bool, str, None]:
        """
        Abstract method to be implemented by concrete command subclasses.

        Args:
            **kwargs: Optional keyword arguments.

        Returns:
            Union[bool, str, None]: The result of the command execution.
        """
        pass


class CheckPasswordMatchingCommand(ICommand):
    """
    Command to check if the provided password matches the stored password for a given email.

    Inherits from ICommand.

    Methods:
        execute(**kwargs) -> bool:
            Executes the command to check password matching.
    """
    def execute(self, **kwargs) -> bool:
        """
        Executes the command to check if the provided password matches the stored password.

        Args:
            **kwargs: Keyword arguments containing 'email' and 'password'.

        Returns:
            bool: True if the password matches, False otherwise.
        """
        query = f"SELECT password FROM user WHERE email = '{kwargs.get('email')}'"
        real_password = self._db.execute_and_return_result(query)
        bin_password = base64.b64decode(real_password)
        if bcrypt.checkpw(kwargs.get('password').encode('utf-8'), bin_password):
            return True
        return False


class GetNameByEmailCommand(ICommand):
    """
    Command to get a name from database by a provided email.

    Inherits from ICommand.

    Methods:
        execute(**kwargs) -> str:
            Executes the command to get a name from db.
    """
    def execute(self, **kwargs) -> str:
        """
        Executes the command to get a name from database.

        Args:
            **kwargs: Keyword arguments containing 'email'.

        Returns:
            str: name from database by a provided email.
        """
        query = f"SELECT name FROM user WHERE email = '{kwargs.get('email')}'"
        name = self._db.execute_and_return_result(query)
        return name


class CheckEmailExistenceCommand(ICommand):
    """
    Command to check if the provided email exists in database.

    Inherits from ICommand.

    Methods:
        execute(**kwargs) -> bool:
            Executes the command to check email existence.
    """
    def execute(self, **kwargs) -> bool:
        """
        Executes the command to check email existence.

        Args:
            **kwargs: Keyword arguments containing 'email'.

        Returns:
            bool: True if the email exists, False otherwise.
        """
        query = f"SELECT COUNT(*) FROM user WHERE email = '{kwargs.get('email')}'"
        result = self._db.execute_and_return_result(query)
        if not result:
            return False
        return True


class AddUserCommand(ICommand):
    """
    Command to add a new user to the database.

    Inherits from ICommand.

    Methods:
        execute(**kwargs) -> None:
            Executes the command to add new user to the database.
    """
    def execute(self, **kwargs) -> None:
        """
        Executes the command to add a new user to the database.

        Args:
            **kwargs: Keyword arguments containing 'name', 'email' and 'password'.

        Returns:
            None
        """
        hashed_password = bcrypt.hashpw(kwargs.get('password').encode('utf-8'), bcrypt.gensalt())
        str_hashed_password = base64.b64encode(hashed_password).decode('utf-8')
        query = f"INSERT INTO user (name, email, password) VALUES ('{kwargs.get('name')}', '{kwargs.get('email')}', '{str_hashed_password}')"
        self._db.execute_query(query)


class ChangeUsernameCommand(ICommand):
    """
    Command to change a particular username in the database.

    Inherits from ICommand.

    Methods:
        execute(**kwargs) -> None:
            Executes the command to change a particular username in the database.
    """
    def execute(self, **kwargs) -> None:
        """
        Executes the command to change a particular username in the database.

        Args:
            **kwargs: Keyword arguments containing 'name' and 'email'.

        Returns:
            None
        """
        query = f"UPDATE user SET name = '{kwargs.get('name')}' WHERE email = '{kwargs.get('email')}'"
        self._db.execute_query(query)
