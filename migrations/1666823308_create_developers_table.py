def up():
    """CREATE TABLE gamereviews.developers (
	id integer PRIMARY KEY NOT NULL,
	name varchar,
	description varchar, 
	avatar varchar,
	created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
	updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP);"""


def down():
    "DROP TABLE gamereviews.developers"
