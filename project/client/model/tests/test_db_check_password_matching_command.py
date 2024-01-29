import pytest
from unittest.mock import MagicMock, patch
from ..db_command import CheckPasswordMatchingCommand


@pytest.fixture
def database_mock():
    return MagicMock()


def test_check_password_matching_correct(database_mock):
    # Mocking database response
    database_mock.execute_and_return_result.return_value = "cGFzc3dvcmQ="  # base64 encoded password

    # Mocking bcrypt check
    with patch('bcrypt.checkpw') as bcrypt_checkpw:
        bcrypt_checkpw.return_value = True

        # Creating instance of CheckPasswordMatchingCommand
        command = CheckPasswordMatchingCommand(database_mock)

        # Calling execute method
        result = command.execute(email="test@example.com", password="password123")

        # Asserting result
        assert result is True

        # Asserting database method called with correct query
        database_mock.execute_and_return_result.assert_called_once_with("SELECT password FROM user WHERE email = 'test@example.com'")

        # Asserting bcrypt check called with correct arguments
        bcrypt_checkpw.assert_called_once_with(b'password123', b'password')  # Assuming bcrypt result is b'password'


def test_check_password_matching_incorrect(database_mock):
    # Mocking database response
    database_mock.execute_and_return_result.return_value = "cGFzc3dvcmQ="

    # Mocking bcrypt check
    with patch('bcrypt.checkpw') as bcrypt_checkpw:
        bcrypt_checkpw.return_value = False

        # Creating instance of CheckPasswordMatchingCommand
        command = CheckPasswordMatchingCommand(database_mock)

        # Calling execute method
        result = command.execute(email="test@example.com", password="wrongpassword")

        # Asserting result
        assert result is False

        # Asserting bcrypt check called with correct arguments
        bcrypt_checkpw.assert_called_once_with(b'wrongpassword', b'password')


def test_check_password_matching_missing_email(database_mock):
    with pytest.raises(TypeError):
        command = CheckPasswordMatchingCommand(database_mock)
        command.execute(password="password123")


def test_check_password_matching_missing_password(database_mock):
    with pytest.raises(TypeError):
        command = CheckPasswordMatchingCommand(database_mock)
        command.execute(email="test@example.com")


if __name__ == "__main__":
    pytest.main()
