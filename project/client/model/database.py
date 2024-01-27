import mysql.connector
from client.config import config


class DatabaseUserTable:
    def __init__(self) -> None:
        self.connection = None
        self.cursor = None

    def connect(self) -> None:
        self.connection = mysql.connector.connect(user=config.DB_USER,
                                                  password=config.DB_PASSWORD,
                                                  host=config.DB_HOST,
                                                  port=config.DB_PORT,
                                                  database=config.DB_NAME)
        self.cursor = self.connection.cursor()

    def execute_query(self, query: str) -> None:
        self.connect()
        self.cursor.execute(query)
        self.close_connection()

    def execute_and_return_result(self, query: str) -> str:
        self.connect()
        self.cursor.execute(query)
        result = self.cursor.fetchone()[0]
        self.close_connection()
        return result

    # for logging in
    # def check_email_existence(self, email: str) -> bool:
    #     self.connect()
    #     query = f"SELECT COUNT(*) FROM user WHERE email = '{email}'"
    #     self.cursor.execute(query)
    #     result = self.cursor.fetchone()[0]
    #     self.close_connection()
    #     if not result:
    #         return False
    #     return True

    # if email is present in table check password matching
    # def check_password_matching(self, email: str, password: str) -> bool:
    #     query = f"SELECT password FROM user WHERE email = '{email}'"
    #     self.cursor.execute(query)
    #     real_password = self.cursor.fetchone()[0]
    #     bin_password = base64.b64decode(real_password)
    #     self.close_connection()
    #     if bcrypt.checkpw(password.encode('utf-8'), bin_password):
    #         return True
    #     return False

    # for signing up
    # def add_user(self, name: str, email: str, password: str) -> None:
    #     self.connect()
    #     # TODO move all this encryption logic into commands classes
    #     hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
    #     str_hashed_password = base64.b64encode(hashed_password).decode('utf-8')
    #     query = f"INSERT INTO user (name, email, password) VALUES ('{name}', '{email}', '{str_hashed_password}')"
    #     self.cursor.execute(query)
    #     self.connection.commit()

    # for settings
    # def get_name_by_email(self, email: str) -> str:
    #     query = f"SELECT name FROM user WHERE email = '{email}'"
    #     self.cursor.execute(query)
    #     name = self.cursor.fetchone()[0]
    #     return name

    # def change_user_name(self, name: str, email: str) -> None:
    #     query = f"UPDATE user SET name = '{name}' WHERE email = '{email}'"
    #     self.cursor.execute(query)
    #     self.connection.commit()

    def close_connection(self) -> None:
        self.connection.commit()
        self.connection.close()
