import mysql.connector
from client.config import config


class DatabaseUserTable:
    """
    Class for interacting with the user table in the database.

    Provides methods to connect to the database, execute queries, and close the connection.

    Attributes:
        connection: The connection to the MySQL database.
        cursor: The cursor object for executing MySQL queries.

    Methods:
        connect() -> None:
            Establishes a connection to the MySQL database using the configuration settings.

        execute_query(query: str) -> None:
            Executes a SQL query that does not return a result set.

        execute_and_return_result(query: str) -> str:
            Executes a SQL query that returns a single result and returns that result.

        _close_connection() -> None:
            Commits any pending transactions and closes the database connection.
    """
    def __init__(self) -> None:
        """
        Initialize a new DatabaseUserTable object.
        """
        self.connection = None
        self.cursor = None

    def connect(self) -> None:
        """
        Establishes a connection to the MySQL database using the configuration settings.
        """
        self.connection = mysql.connector.connect(user=config.DB_USER,
                                                  password=config.DB_PASSWORD,
                                                  host=config.DB_HOST,
                                                  port=config.DB_PORT,
                                                  database=config.DB_NAME)
        self.cursor = self.connection.cursor()

    def execute_query(self, query: str) -> None:
        """
        Executes a SQL query that does not return a result set.

        Args:
            query (str): The SQL query to execute.
        """
        self.connect()
        self.cursor.execute(query)
        self._close_connection()

    def execute_and_return_result(self, query: str) -> str:
        """
        Executes a SQL query that returns a single result and returns that result.

        Args:
            query (str): The SQL query to execute.

        Returns:
            str: The result of the query.
        """
        self.connect()
        self.cursor.execute(query)
        result = self.cursor.fetchone()[0]
        self._close_connection()
        return result

    def _close_connection(self) -> None:
        """
        Commits any pending transactions and closes the database connection.
        """
        self.connection.commit()
        self.connection.close()
