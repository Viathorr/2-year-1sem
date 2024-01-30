class User:
    """
        Represents a user with a name and email address.

        Attributes:
            name (str): The name of the user.
            email (str): The email address of the user.

        Methods:
            name:
                Getter and setter property for the user's name.
            email:
                Getter and setter property for the user's email address.

        Example:
            >>> user = User('John Doe', 'john@example.com')
            >>> user.name
            'John Doe'
            >>> user.email
            'john@example.com'
        """
    def __init__(self, name: str = '', email: str = ''):
        """
        Initialize a new User object.

        Args:
            name (str, optional): The name of the user. Defaults to an empty string.
            email (str, optional): The email address of the user. Defaults to an empty string.
        """
        self._name = name
        self._email = email

    @property
    def name(self) -> str:
        """
        Get or set the name of the user.

        Returns:
            str: The name of the user.
        """
        return self._name

    @name.setter
    def name(self, new_name: str) -> None:
        """
        Set the name of the user.

        Args:
            new_name (str): The new name for the user.
        """
        self._name = new_name

    @property
    def email(self) -> str:
        """
        Get or set the email address of the user.

        Returns:
            str: The email address of the user.
        """
        return self._email

    @email.setter
    def email(self, new_email: str) -> None:
        """
        Set the email address of the user.

        Args:
            new_email (str): The new email address for the user.
        """
        self._email = new_email
