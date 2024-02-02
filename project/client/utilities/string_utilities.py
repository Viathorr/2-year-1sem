class StringUtilities:
    """
    Utility class for common string operations.

    Provides static methods for checking if a string is empty or contains newline characters.

    Methods:
        is_empty_string(string: str) -> bool:
            Checks if the given string is empty or consists only of whitespace characters.

        contains_newline_char(string: str) -> bool:
            Checks if the given string contains newline characters.
    """
    @staticmethod
    def is_empty_string(string: str) -> bool:
        """
       Check if the given string is empty or consists only of whitespace characters.

       Args:
           string (str): The string to check.

       Returns:
           bool: True if the string is empty or consists only of whitespace characters, False otherwise.
       """
        return all(char.isspace() for char in string)

    @staticmethod
    def contains_newline_char(string: str) -> bool:
        """
        Check if the given string contains newline characters.

        Args:
            string (str): The string to check.

        Returns:
            bool: True if the string contains newline characters, False otherwise.
        """
        return '\n' in string
