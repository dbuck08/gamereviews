def up():
    """CREATE TABLE gamereviews.games (
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
);"""


def down():
    "DROP TABLE gamereviews.games;"
