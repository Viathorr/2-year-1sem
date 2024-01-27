from .database import DatabaseUserTable
from abc import ABC, abstractmethod
import bcrypt
import base64
from typing import Union


class ICommand(ABC):
    def __init__(self, db: DatabaseUserTable) -> None:
        self._db = db

    @abstractmethod
    def execute(self, *args, **kwargs) -> Union[bool, str, None]:
        pass


class CheckPasswordMatchingCommand(ICommand):
    def execute(self, *args, **kwargs) -> bool:
        query = f"SELECT password FROM user WHERE email = '{kwargs.get('email')}'"
        real_password = self._db.execute_and_return_result(query)
        bin_password = base64.b64decode(real_password)
        if bcrypt.checkpw(kwargs.get('password').encode('utf-8'), bin_password):
            return True
        return False


class GetNameByEmailCommand(ICommand):
    def execute(self, *args, **kwargs) -> str:
        query = f"SELECT name FROM user WHERE email = '{kwargs.get('email')}'"
        name = self._db.execute_and_return_result(query)
        return name


class CheckEmailExistenceCommand(ICommand):
    def execute(self, *args, **kwargs) -> bool:
        query = f"SELECT COUNT(*) FROM user WHERE email = '{kwargs.get('email')}'"
        result = self._db.execute_and_return_result(query)
        if not result:
            return False
        return True


class AddUserCommand(ICommand):
    def execute(self, *args, **kwargs) -> None:
        hashed_password = bcrypt.hashpw(kwargs.get('password').encode('utf-8'), bcrypt.gensalt())
        str_hashed_password = base64.b64encode(hashed_password).decode('utf-8')
        query = f"INSERT INTO user (name, email, password) VALUES ('{kwargs.get('name')}', '{kwargs.get('email')}', '{str_hashed_password}')"
        self._db.execute_query(query)


class ChangeUsernameCommand(ICommand):
    def execute(self, *args, **kwargs) -> None:
        query = f"UPDATE user SET name = '{kwargs.get('name')}' WHERE email = '{kwargs.get('email')}'"
        self._db.execute_query(query)
