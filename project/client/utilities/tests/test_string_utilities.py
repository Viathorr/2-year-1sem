import pytest
from ..string_utilities import StringUtilities


class TestStringUtilities:
    def test_is_empty_string(self):
        # Test empty string
        result = StringUtilities.is_empty_string('')
        assert result  # True

        # Test string with only whitespace characters
        result = StringUtilities.is_empty_string('  \t  \n  ')
        assert result  # True

        # Test non-empty string
        result = StringUtilities.is_empty_string('Hello, Wolrd!')
        assert not result  # False

    def test_contains_newline_char(self):
        # Test string with newline character
        result = StringUtilities.contains_newline_char('Hello\nworld')
        assert result  # True

        # Test string without newline character
        result = StringUtilities.contains_newline_char('Hello, Wolrd!')
        assert not result  # False

        # Test empty string
        result = StringUtilities.contains_newline_char('')
        assert not result  # False
