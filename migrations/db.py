"""
Keeps the database configuration in a common location for other modules to utilize.
"""
import psycopg2


def connection():
    """
    Establishes a connection to the database.
    """
    # We have to pass an empty string in order to be able to use the PG* environment variables
    conn = psycopg2.connect("")
    return conn
