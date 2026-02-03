import sqlite3
from passlib.hash import argon2
import secrets_handling
from pprint import pprint
from tabulate import tabulate

DB_FILE = "horror.db"

con = sqlite3.connect(DB_FILE)
cur = con.cursor()

def write_example_data():
    """
    Insert example data into tables created by data.py
    """

    cur.executemany("""INSERT OR REPLACE INTO genres
        (genreid, name)
        VALUES (?, ?)
        """,
        [(1, 'Horror'),
         (2, 'Supernatural'),
         (3, 'Gore'),
         (4, 'Psychological')]
    )

    cur.executemany("""INSERT OR REPLACE INTO movies
        (movieid, release_year, runtime_min, country, synopsis, poster_url, imdb_url, scary_level, gore_level, genres)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        """,
        [(1, 'Saw (2004)', 2004, 103, 'USA', 'Jigsaw and deadly games.', None, None, 3, 5, [1,3]),
         (2, 'The Conjouring', 2013, 112, 'USA', 'Paranormal investigators.', None, None, 4, 1, [1,2]),
         (3, 'Hereditary', 2018, 127, 'USA', 'Family tragedy and occult presence.', None, None, 4, 2, [1,4])
        ]
    )

    con.commit()