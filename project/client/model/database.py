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

    def close_connection(self) -> None:
        self.connection.commit()
        self.connection.close()
