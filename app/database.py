import psycopg2
from psycopg2 import pool
import config

class Database:
    _connection_pool = None

    @staticmethod
    def initialize():
        Database._connection_pool = pool.SimpleConnectionPool(1, 
                                                              10,
                                                              user=config.DB_USER,
                                                              password=config.DB_PASSWORD,
                                                              database=config.DB_NAME,
                                                              host=config.DB_HOST,
                                                              port=config.DB_PORT)

    @staticmethod
    def get_connection():
        return Database._connection_pool.getconn()

    @staticmethod
    def return_connection(connection):
        Database._connection_pool.putconn(connection)

    @staticmethod
    def close_all_connections():
        Database._connection_pool.closeall()

def query_db(query, params=None, fetch_one=False):
    connection = Database.get_connection()
    cursor = connection.cursor()
    cursor.execute(query, params or ())

    if fetch_one:
        result = cursor.fetchone()
    else:
        result = cursor.fetchall()

    cursor.close()
    Database.return_connection(connection)
    return result

# Initialize database connection pool
Database.initialize()
