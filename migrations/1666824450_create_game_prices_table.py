"""
Create or destroy the gamereviews.game_prices table.
"""
from db import connection

def up():
    """
    Create the gamereviews.game_prices table.
    """
    conn = connection()
    with conn.cursor() as curs:
        curs.execute("""
            CREATE TABLE gamereviews.game_prices (
                id integer PRIMARY KEY NOT NULL,
                game_id integer,
                FOREIGN KEY (game_id) REFERENCES gamereviews.games(id),
                value decimal
            );
        """)
    conn.close()


def down():
    """
    Destroy the gamereviews.game_prices table.
    """
    conn = connection()
    with conn.cursor() as curs:
        curs.execute("DROP TABLE gamereviews.game_prices;")
    conn.close()
