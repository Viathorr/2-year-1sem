from .db_command import *


class DBControl:
    def __init__(self, check_password_matching_command: CheckPasswordMatchingCommand,
                 get_name_command: GetNameByEmailCommand, check_email_existence_command: CheckEmailExistenceCommand,
                 add_user_command: AddUserCommand, change_name_command: ChangeUsernameCommand):
        self._check_password_matching_command = check_password_matching_command
        self._get_name_command = get_name_command
        self._check_email_existence_command = check_email_existence_command
        self._add_user_command = add_user_command
        self._change_name_command = change_name_command

    def email_exists(self, email: str):
        self._check_email_existence_command.execute(email=email)

    def add_user(self, name: str, email: str, password: str):
        self._add_user_command.execute(name=name, email=email, password=password)

    def login_check(self, email: str, password: str):
        if self._check_email_existence_command.execute(email=email) and self._check_password_matching_command.execute(email=email, password=password):
            name = self._get_name_command.execute(email=email)
            return name
        else:
            raise Exception('Invalid email or password. Please try again.')

    def change_username(self, new_name: str, email: str):
        self._change_name_command.execute(name=new_name, email=email)

    def add_new_user(self, name: str, email: str, password: str):
        self._add_user_command.execute(name=name, email=email, password=password)
