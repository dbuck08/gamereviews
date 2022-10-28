def up():
    """CREATE TABLE gamereviews.reviews (
	id integer PRIMARY KEY NOT NULL,
	game_id integer,
	FOREIGN KEY (game_id) REFERENCES gamereviews.games(id),
	reviewer_id integer,
	FOREIGN KEY (reviewer_id) REFERENCES gamereviews.users(id),
	title varchar(80),
	content varchar,
	score integer,
	CHECK (score >= 0 AND score <= 100)
);"""


def down():
    "DROP TABLE gamereviews.reviews;"
