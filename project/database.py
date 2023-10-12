import sqlite3
import bcrypt
import base64


class DatabaseUserTable:
    def __init__(self):
        self.connection = None
        self.cursor = None

    def connect(self):
        self.connection = sqlite3.connect('users.db')
        self.cursor = self.connection.cursor()

    # def create_table(self):
    #     query = '''CREATE TABLE user (
    #             id INTEGER PRIMARY KEY AUTOINCREMENT,
    #             name TEXT NOT NULL,
    #             email TEXT NOT NULL,
    #             password TEXT NOT NULL)'''
    #     self.cursor.execute(query)

    # for logging in
    def check_email_existence(self, email):
        query = f"SELECT COUNT(*) FROM user WHERE email = '{email}'"
        self.cursor.execute(query)
        result = self.cursor.fetchone()[0]
        if not result:
            return False
        return True

    # if email is present in table check password matching
    def check_password_matching(self, email, password):
        query = f'SELECT password WHERE email = {email}'
        self.cursor.execute(query)
        real_password = self.cursor.fetchone()[0]
        bin_password = base64.b64decode(real_password)
        if bcrypt.checkpw(password.encode('utf-8'), bin_password):
            return True
        return False

    # for signing up
    def add_user(self, name, email, password):
        hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
        str_hashed_password = base64.b64encode(hashed_password).decode('utf-8')
        query = f'INSERT INTO user (name, email, password) VALUES ({name}, {email}, {str_hashed_password})'
        self.cursor.execute(query)
        self.connection.commit()

    # for settings
    def get_name_by_email(self, email):
        query = f'SELECT name FROM user WHERE email = {email}'
        self.cursor.execute(query)
        name = self.cursor.fetchone()[0]
        return name

    def close_connection(self):
        self.connection.commit()
        self.connection.close()


