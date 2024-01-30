import re


class EmailValidation:
    """
    Utility class for validating email addresses.

    Provides a static method `is_valid_email` to check if a given email address
    is valid according to the specified regex pattern.

    Attributes:
        None

    Methods:
        is_valid_email(email: str) -> bool:
            Checks if the given email address is valid.
    """

    @staticmethod
    def is_valid_email(email: str) -> bool:
        """
        Check if the given email address is valid.

        Args:
            email (str): The email address to validate.

        Returns:
            bool: True if the email address is valid, False otherwise.

        Example:
            >>> EmailValidation.is_valid_email('example@example.com')
            True
        """
        email_regex = re.compile(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$', re.VERBOSE)
        return bool(email_regex.match(email))
