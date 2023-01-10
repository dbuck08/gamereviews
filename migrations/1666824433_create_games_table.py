"""
Create or destroy the gamereviews.games table.
"""
from db import connection


def up():
    """
    Create the gamereviews.games table.
    """
    conn = connection()
    with conn.cursor() as curs:
        curs.execute("""
            CREATE TABLE gamereviews.games (
                id integer PRIMARY KEY NOT NULL,
                title varchar(80),
                description varchar(300),
                avatar varchar,
                category varchar,
                publisher integer,
                FOREIGN KEY (publisher) REFERENCES gamereviews.publishers(id),
                developer integer,
                FOREIGN KEY (developer) REFERENCES gamereviews.developers(id),
                published_on TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            );
        """)
    conn.close()


def down():
    """
    Destroy the gamereviews.games table.
    """
    conn = connection()
    with conn.cursor() as curs:
        curs.execute("DROP TABLE gamereviews.games;")
    conn.close()
