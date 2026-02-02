# In-memory mock data for now (no database).
# Replace with real DB/API later.

GENRES = [
    {"id": 1, "name": "Horror"},
    {"id": 2, "name": "Supernatural"},
    {"id": 3, "name": "Gore"},
    {"id": 4, "name": "Psychological"},
]

# Mocked movies with fixed factual levels (NOT user reviews)
# Each movie references genres by ID. The backend will "expand" these to full {id, name} objects for convenience in the UI
MOVIES = [
    {
        "id": 1,
        "title": "Saw (2004)",
        "release_year": 2004,
        "runtime_min": 103,
        "country": "USA",
        "synopsis": "Jigsaw and deadly games.",
        "poster_url": None,
        "imdb_url": None,
        "scary_level": 3,
        "gore_level": 5,
        "genres": [1, 3],
    },
    {
        "id": 2,
        "title": "The Conjuring",
        "release_year": 2013,
        "runtime_min": 112,
        "country": "USA",
        "synopsis": "Paranormal investigators.",
        "poster_url": None,
        "imdb_url": None,
        "scary_level": 4,
        "gore_level": 1,
        "genres": [1, 2],
    },
    {
        "id": 3,
        "title": "Hereditary",
        "release_year": 2018,
        "runtime_min": 127,
        "country": "USA",
        "synopsis": "Family tragedy and occult presence.",
        "poster_url": None,
        "imdb_url": None,
        "scary_level": 4,
        "gore_level": 2,
        "genres": [1, 4],
    },
]