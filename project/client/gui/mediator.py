from .imediator import IMediator
from .main_window import MainWindow
from .login import LogIn
from .signup import SignUp
from .settings import Settings
from .chat_window import ClientChatWindow
from client.client_socket.client_socket import ClientSocket


class Mediator(IMediator):
    def __init__(self, db_control):
        super(Mediator, self).__init__(db_control)
        self._main_window = MainWindow(self)
        self._main_window.root.protocol('WM_DELETE_WINDOW', self._close_window)
        self._chat_window = None
        self._login_window = None
        self._signup_window = None
        self._settings_window = None
        self._socket = None

    @property
    def participants(self):
        return self._socket.participants

    def connect(self) -> None:
        self._socket.connect()

    def run(self) -> None:
        """
        Run the Chat Application.
        """
        self._main_window.open()

    def deiconify_main_window(self):
        self._main_window.reopen_window()

    def _close_window(self) -> None:
        """
        Close the application window.
        """
        self._main_window.destroy_window()

    def open_settings(self):
        self._main_window.close_window()
        self._settings = Settings(self)
        self._settings.root.protocol('WM_DELETE_WINDOW', self._close_settings)
        self._settings.open()

    def save_set_changes(self, new_name: str) -> None:
        self.user.name = new_name
        self._db_control.change_username(new_name, self.user.email)

    def _close_settings(self):
        self._settings.root.destroy()
        if not self.user:
            self._main_window.change_buttons_state(False)
        self._main_window.reopen_window()

    def open_login_window(self) -> None:
        """
        Open the login window
        """
        self._main_window.close_window()
        self._login_window = LogIn(self)
        self._login_window.root.protocol('WM_DELETE_WINDOW', self._close_login_window)
        self._login_window.open()

    def login_check(self, email: str, password: str) -> str:
        return self._db_control.login_check(email, password)

    def _close_login_window(self) -> None:
        """
        Close the login window
        """
        if self.user:
            self._main_window.change_buttons_state(True)
        self._login_window.root.destroy()
        self._main_window.reopen_window()

    def open_signup_window(self) -> None:
        """
        Open the signup window
        """
        self._main_window.close_window()
        self._signup_window = SignUp(self)
        self._signup_window.root.protocol('WM_DELETE_WINDOW', self._close_signup_window)
        self._signup_window.open()

    def check_email(self, email: str) -> bool:
        return self._db_control.email_exists(email)

    def add_user(self, name: str, email: str, password: str) -> None:
        self._db_control.add_user(name, email, password)

    def _close_signup_window(self) -> None:
        """
        Close the signup window
        """
        if self.user:
            self._main_window.change_buttons_state(True)
        self._signup_window.root.destroy()
        self._main_window.reopen_window()

    def open_chat_window(self) -> None:
        self._socket = ClientSocket(self)
        self._chat_window = ClientChatWindow(self)
        self._chat_window.root.protocol('WM_DELETE_WINDOW', self.close_chat_window)
        try:
            self._socket.connect()
            self._chat_window.open()
        except Exception as ex:
            self._chat_window.destroy()
            self.deiconify_main_window()
            self._main_window.show_error(str(ex))

    def send_msg(self, msg: str):
        self._socket.send(msg)

    def display_msg(self, msg: str) -> None:
        self._chat_window.add_message(msg)

    def change_participants_label(self, label: str) -> None:
        self._chat_window.set_participants_label(label)

    def handle_server_err(self):
        self.close_chat_window()
        self._chat_window.show_server_error()

    def close_chat_window(self) -> None:
        self._socket.close()
        self._chat_window.destroy()
        self.deiconify_main_window()
