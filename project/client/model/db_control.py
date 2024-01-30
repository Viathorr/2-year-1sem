from .db_command import *


class DBControl:
    """
    Class to control database operations through command objects.

    Attributes:
        check_password_matching_command (CheckPasswordMatchingCommand): Command object to check password matching.
        get_name_command (GetNameByEmailCommand): Command object to get username by email.
        check_email_existence_command (CheckEmailExistenceCommand): Command object to check email existence.
        add_user_command (AddUserCommand): Command object to add a new user.
        change_name_command (ChangeUsernameCommand): Command object to change user's username.

    Methods:
        email_exists(email: str):
            Checks if the given email exists in the database.

        add_user(name: str, email: str, password: str):
            Adds a new user to the database.

        login_check(email: str, password: str) -> str:
            Checks if the provided email and password match a user in the database and returns the user's name.

        change_username(new_name: str, email: str):
            Changes the username of the user with the given email.

        add_new_user(name: str, email: str, password: str):
            Adds a new user to the database.
    """

    def __init__(self, check_password_matching_command: CheckPasswordMatchingCommand,
                 get_name_command: GetNameByEmailCommand, check_email_existence_command: CheckEmailExistenceCommand,
                 add_user_command: AddUserCommand, change_name_command: ChangeUsernameCommand) -> None:
        """
        Initialize a new DBControl object.

        Args:
            check_password_matching_command (CheckPasswordMatchingCommand): Command object to check password matching.
            get_name_command (GetNameByEmailCommand): Command object to get username by email.
            check_email_existence_command (CheckEmailExistenceCommand): Command object to check email existence.
            add_user_command (AddUserCommand): Command object to add a new user.
            change_name_command (ChangeUsernameCommand): Command object to change user's username.
        """
        self._check_password_matching_command = check_password_matching_command
        self._get_name_command = get_name_command
        self._check_email_existence_command = check_email_existence_command
        self._add_user_command = add_user_command
        self._change_name_command = change_name_command

    def email_exists(self, email: str) -> bool:
        """
        Checks if the given email exists in the database.

        Args:
            email (str): The email to check.

        Returns:
            bool: True if such email exists, False otherwise.
        """
        return self._check_email_existence_command.execute(email=email)

    def add_user(self, name: str, email: str, password: str) -> None:
        """
        Adds a new user to the database.

        Args:
            name (str): The name of the user.
            email (str): The email of the user.
            password (str): The password of the user.

        Returns:
            None
        """
        self._add_user_command.execute(name=name, email=email, password=password)

    def login_check(self, email: str, password: str) -> str:
        """
        Checks if the provided email and password match a user in the database and returns the user's name.

        Args:
            email (str): The email to check.
            password (str): The password to check.

        Returns:
            str: The name of the user if login is successful.

        Raises:
            Exception: If login is unsuccessful.
        """
        if self.email_exists(email=email) and self._check_password_matching_command.execute(
                email=email, password=password):
            name = self._get_name_command.execute(email=email)
            return name
        else:
            raise Exception('Invalid email or password. Please try again.')

    def change_username(self, new_name: str, email: str) -> None:
        """
        Changes the username of the user with the given email.

        Args:
            new_name (str): The new username.
            email (str): The email of the user whose username to change.

        Returns:
            None
        """
        self._change_name_command.execute(name=new_name, email=email)
