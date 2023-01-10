"""
Creates or destroys the gamereviews.reviews table.
"""
from db import connection


def up():
    """
    Create the gamereviews.reviews table.
    """
    conn = connection()
    with conn.cursor() as curs:
        curs.execute("""
            CREATE TABLE gamereviews.reviews (
                id integer PRIMARY KEY NOT NULL,
                game_id integer,
                FOREIGN KEY (game_id) REFERENCES gamereviews.games(id),
                reviewer_id integer,
                FOREIGN KEY (reviewer_id) REFERENCES gamereviews.users(id),
                title varchar(80),
                content varchar,
                score integer,
                CHECK (score >= 0 AND score <= 100)
            );
        """)
    conn.close()


def down():
    """
    Destroy the gamereviews.reviews table.
    """
    conn = connection()
    with conn.cursor() as curs:
        curs.execute("DROP TABLE gamereviews.reviews;")
    conn.close()
