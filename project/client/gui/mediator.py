from .imediator import IMediator
from .main_window import MainWindow
from .login import LogIn
from .signup import SignUp
from .settings import Settings
from .chat_window import ClientChatWindow
from client.client_socket.client_socket import ClientSocket
from typing import List


class Mediator(IMediator):
    """
    Mediator class that handles all interactions between different windows.

    Attributes:
        _main_window (MainWindow): The main window of the application.
        _chat_window (ClientChatWindow): Reference to the chat window.
        _login_window (LogIn): Reference to the login form window.
        _signup_window (SignUp): Reference to the signup form window.
        _settings_window (Settings): Reference to the settings window.
        _socket (ClientSocket): The client socket object for communication with the server.

    Methods:
        run():
            Run the Chat Application.
        _close_window():
            Close the application window.
        deiconify_main_window():
            Reopen main window.
        set_user(user: User):
            Set the current user of the application.
        open_chat_window():
            Opens the chat window if the user is logged in.
        send_msg(msg: str):
            Sends a message to the server.
        display_msg(msg: str):
            Displays the received from server message.
        change_participants_label(label: str):
            Changes the label that shows the number of participants.
        handle_server_err():
            Handles the server error occurence.
        close_chat_window():
            Closes the chat window.
        open_login_window():
            Opens the login window.
        login_check(email: str, password: str):
            Validates user credentials.
        _close_login_window():
            Closes the login window.
        open_signup_window():
            Opens the signup window.
        check_email(email: str):
            Checks whether the given email already exists or not.
        add_user(name: str, email: str, password: str):
            Adds user to the database.
        _close_signup_window():
            Closes the signup window.
        open_settings():
            Opens the settings window.
        _close_settings_window():
            Closes the settings window.

    """
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
    def participants(self) -> List[str]:
        """
        Getter of participants
        Returns:
            List[str]
        """
        return self._socket.participants

    def connect(self) -> None:
        """
        Connects socket to the server.
        """
        self._socket.connect()

    def run(self) -> None:
        """
        Run the Chat Application.
        """
        self._main_window.open()

    def deiconify_main_window(self) -> None:
        """
        Reopens the main application window.
        """
        self._main_window.reopen_window()

    def _close_window(self) -> None:
        """
        Close the application window.
        """
        self._main_window.destroy_window()

    def open_settings(self) -> None:
        """
        Opens the settings window.
        """
        self._main_window.close_window()
        self._settings = Settings(self)
        self._settings.root.protocol('WM_DELETE_WINDOW', self._close_settings)
        self._settings.open()

    def save_set_changes(self, new_name: str) -> None:
        """
        Saves the changes made to username
        Args:
            new_name(str): Changed name
        """
        self.user.name = new_name
        self._db_control.change_username(new_name, self.user.email)

    def _close_settings(self) -> None:
        """
        Closes the settings window.
        """
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
        """
        Validates user credentials.
        Args:
            email(str): Email of user
            password(str): Password of user
        Returns:
            str
        """
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
        """
        Checks whether the given email already exists or not.
        Args:
            email(str): Email to check
        Returns:
            bool
        """
        return self._db_control.email_exists(email)

    def add_user(self, name: str, email: str, password: str) -> None:
        """
        Adds user to the database.
        Args:
            name(str): Name of new user
            email(str): Email of new user
            password(str): Password of new user
        """
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
        """
        Open the chat window.
        """
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

    def send_msg(self, msg: str) -> None:
        """
        Sends a message to the server.
        Args:
             msg(str): Message to send
        """
        self._socket.send(msg)

    def display_msg(self, msg: str) -> None:
        """
        Displays the received from server message.
        Args:
             msg(str): Message to display
        """
        self._chat_window.add_message(msg)

    def change_participants_label(self, label: str) -> None:
        """
        Changes the label that shows the number of participants.
        Args:
             label(str): New label to set
        """
        self._chat_window.set_participants_label(label)

    def handle_server_err(self) -> None:
        """
        Handles the server error occurence.
        """
        self.close_chat_window()
        self._chat_window.show_server_error()

    def close_chat_window(self) -> None:
        """
        Close the chat window.
        """
        self._socket.close()
        self._chat_window.destroy()
        self.deiconify_main_window()
