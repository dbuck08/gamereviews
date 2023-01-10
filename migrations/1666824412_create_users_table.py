"""
Create or destroy the gamereviews.users table.
"""
from db import connection


def up():
    """
    Create the gamereviews.users table.
    """
    conn = connection()
    with conn.cursor() as curs:
        curs.execute("""
            CREATE TABLE gamereviews.users (
                id integer PRIMARY KEY NOT NULL,
                email varchar(80),
                password varchar
            );
        """)
    conn.close()


def down():
    """
    Destroy the gamereviews.users table.
    """
    conn = connection()
    with conn.cursor() as curs:
        curs.execute("DROP TABLE gamereviews.users;")
    conn.close()
