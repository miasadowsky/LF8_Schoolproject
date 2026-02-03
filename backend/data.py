import sqlite3
from pprint import pprint
import re

DB_FILE = "horror.db"

con = sqlite3.connect(DB_FILE)
cur = con.cursor()


## Create tables

print("This script creates the required db tables.")
print("Existing tables are not changed.")
print("WARNING: schema changes are not applied!")
## For now no migration script exists. Please delete the old db when needed
print()

cur.execute("""CREATE TABLE IF NOT EXISTS genres ( 
	genreid INTEGER NOT NULL PRIMARY KEY,
	name TEXT NOT NULL
);
""")

cur.execute("""CREATE TABLE IF NOT EXISTS movies (
	movieid INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
	release_year INTEGER NOT NULL, 
    runtime_min INTEGER NOT NULL, 
    country TEXT NOT NULL, 
	synopsis TEXT NOT NULL, 
	poster_url TEXT, 
	imdb_url TEXT,
    scary_level INTEGER,
    gore_level INTEGER,
    genres INTEGER,
    FOREIGN KEY(genres) REFERENCES genres(genreid)
);
""")
