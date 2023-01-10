"""
Create or destroy the gamereviews.developers table.
"""
from db import connection


def up():
    """
    Create the gamereviews.developers table.
    """
    conn = connection()
    with conn.cursor() as curs:
        curs.execute("""
            CREATE TABLE gamereviews.developers (
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
    Destroy the gamereviews.developers table.
    """
    conn = connection()
    with conn.cursor() as curs:
        curs.execute("DROP TABLE gamereviews.developers;")
    conn.close()
