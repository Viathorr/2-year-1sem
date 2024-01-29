import pytest
from unittest.mock import MagicMock, patch
from ..db_command import AddUserCommand
import bcrypt


@pytest.fixture
def database_mock():
    return MagicMock()


def test_add_user_command_correct(database_mock):
    with patch('bcrypt.hashpw') as bcrypt_hashpw, patch('base64.b64encode') as base64_b64encode, patch('bcrypt.gensalt') as bcrypt_gensalt:
        bcrypt_hashpw.return_value = b'hashed_password'
        base64_b64encode.return_value = b'str_hashed_password'
        bcrypt_gensalt.return_value = b'$2b$12$mHPgc/vQij81jqMQhL/VJe'

        # Creating instance of AddUserCommand
        command = AddUserCommand(database_mock)

        # Calling execute method
        command.execute(name="John Doe", email="john@example.com", password="password123")

        # Asserting database method called with correct query
        database_mock.execute_query.assert_called_once_with(
            "INSERT INTO user (name, email, password) VALUES ('John Doe', 'john@example.com', 'str_hashed_password')")

        # Asserting bcrypt hashpw called with correct arguments
        bcrypt_hashpw.assert_called_once_with(b'password123', b'$2b$12$mHPgc/vQij81jqMQhL/VJe')

        # Asserting base64 b64encode called with correct arguments
        base64_b64encode.assert_called_once_with(b'hashed_password')
