def up():
    """CREATE TABLE gamereviews.game_prices (
	id integer PRIMARY KEY NOT NULL,
	game_id integer,
	FOREIGN KEY (game_id) REFERENCES gamereviews.games(id),
	value decimal
);"""


def down():
    "DROP TABLE gamereviews.game_prices;"
