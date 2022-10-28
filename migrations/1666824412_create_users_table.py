def up():
    """CREATE TABLE gamereviews.users (
	id integer PRIMARY KEY NOT NULL,
	email varchar(80),
	password varchar
);"""


def down():
    "DROP TABLE gamereviews.users;"
