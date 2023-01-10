"""
Create or destroy the gamereviews.publishers table.
"""
from db import connection


def up():
    """
    Create the gamereviews.publishers table.
    """
    conn = connection()
    with conn.cursor() as curs:
        curs.execute("""
            CREATE TABLE gamereviews.publishers (
                id integer PRIMARY KEY NOT NULL,
                name varchar,
                description varchar, 
                avatar varchar,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            );
        """)
    conn.close()


def down():
    """
    Destroy the gamereviews.publishers table.
    """
    conn = connection()
    with conn.cursor() as curs:
        curs.execute("DROP TABLE gamereviews.publishers;")
    conn.close()
