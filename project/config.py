from decouple import Config, RepositoryEnv


config = Config(RepositoryEnv('.env'))

DB_HOST = config('DB_HOST')
DB_USER = config("DB_USER")
DB_PASSWORD = config('DB_PASSWORD')
DB_PORT = 3306
DB_NAME = config('DB_NAME')
