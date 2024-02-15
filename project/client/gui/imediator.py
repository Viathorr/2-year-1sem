from abc import ABC, abstractmethod
from client.user.user import User
from client.model.db_control import DBControl


class IMediator(ABC):
    def __init__(self, db_control: DBControl):
        self._db_control = db_control
        self._user = None

    @property
    def user(self) -> User | None:
        return self._user

    @abstractmethod
    def run(self) -> None:
        pass

    @abstractmethod
    def deiconify_main_window(self) -> None:
        pass

    def set_user(self, user: User | None) -> None:
        """
        Set the current user of the application.

        Args:
            user (User): The user object to set.
        """
        self._user = user

    @abstractmethod
    def open_settings(self) -> None:
        pass

    @abstractmethod
    def save_set_changes(self, new_name: str) -> None:
        pass

    @abstractmethod
    def open_chat_window(self) -> None:
        pass

    @abstractmethod
    def connect(self) -> None:
        pass

    @abstractmethod
    def send_msg(self, msg: str) -> None:
        pass

    @abstractmethod
    def display_msg(self, msg: str) -> None:
        pass

    @abstractmethod
    def change_participants_label(self, label: str) -> None:
        pass

    @abstractmethod
    def handle_server_err(self) -> None:
        pass

    @abstractmethod
    def close_chat_window(self) -> None:
        pass

    @abstractmethod
    def open_login_window(self) -> None:
        pass

    @abstractmethod
    def login_check(self, email: str, password: str) -> str:
        pass

    @abstractmethod
    def open_signup_window(self) -> None:
        pass

    @abstractmethod
    def check_email(self, email: str) -> bool:
        pass

    @abstractmethod
    def add_user(self, name: str, email: str, password: str) -> None:
        pass
