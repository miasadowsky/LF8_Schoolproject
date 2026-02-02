from fastapi import FastAPI, HTTPException, Query
from fastapi.middleware.cors import CORSMiddleware
from typing import Optional
from .config import settings
from . import data

"""
FastAPI application exposing a mock API:
- GET /health     -> quick status check
- GET /genres     -> list of genres (in-memory)
- GET /movies     -> list of movies with basic filtering/sorting
- GET /movies/{id}-> single movie by ID

Notes:
- This is a DEVELOPMENT SHELL, not the final API.
- There is NO persistence (no DB); data resets on server restart.
- When your teammate's real API is ready, you can:
    A) change the frontend's API_BASE_URL to point at the real API, or
    B) turn this app into a proxy that forwards requests to the real API.
"""

app = FastAPI(title="Horror Movie Facts (Mock)", version="0.1.0")

# Enable CORS (Cross-Origin Resource Sharing) for development:
# - This allows opening frontend/index.html directly from file://
# - and lets the browser call http://127.0.0.1:8000 without being blocked.
# IMPORTANT: In production it should be restrict allow_origins to known hosts
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],    # DEV ONLY: allow all origins for simplicity
    allow_credentials=True,
    allow_methods=["*"],    # all HTTP methods (GET, POST, etc.)
    allow_headers=["*"],    # allow any custom headers
)

@app.get("/health")
def health():
    """
    Lightweight health check endpoint.
    Returns a minimal JSON indicating the server is alive
    and that this is the mock implementation.
    """
    return {"status": "ok", "mock": True}


@app.get("/genres")
def list_genres():
    """
    Return the mock genre list as-is.

    Response shape (array):
      [{ "id": number, "name": string }, ...]
    """
    return data.GENRES


@app.get("/movies")
def list_movies(
    q: Optional[str] = None,
    genre_id: Optional[int] = None,
    order: str = Query("title_asc", enum=["title_asc", "year_desc", "scary_desc", "gore_desc"])
):
    """
    List movies with optional filtering and sorting.

    Query parameters:
    - q: optional search string to filter by title (case-insensitive substring match)
    - genre_id: optional genre ID to filter movies by genre
    - order: sorting order, one of:
      - "title_asc" (default): sort by title ascending
      - "year_desc": sort by release year descending
      - "scary_desc": sort by scary level descending
      - "gore_desc": sort by gore level descending

    Response shape (array):
      [{ "id": number, "title": string, "genres": [number], ... }, ...]
    """
    movies = list(data.MOVIES)

    if q:
        movies = [m for m in movies if q.lower() in m["title"].lower()]
    if genre_id:
        movies = [m for m in movies if genre_id in m["genres"]]

    # Sorting
    if order == "scary_desc":
        movies.sort(key=lambda m: m.get("scary_level", 0), reverse=True)
    elif order == "gore_desc":
        movies.sort(key=lambda m: m.get("gore_level", 0), reverse=True)
    elif order == "year_desc":
        movies.sort(key=lambda m: (m.get("release_year") or 0), reverse=True)
    else:
        movies.sort(key=lambda m: m.get("title","").lower())

    # Expand genre objects (id+name) for the UI
    genre_by_id = {g["id"]: g for g in data.GENRES}
    for m in movies:
        m["genre_objects"] = [genre_by_id[g] for g in m["genres"] if g in genre_by_id]
    return movies

@app.get("/movies/{movie_id}")
def get_movie(movie_id: int):
    """
    Return a single movie by its numeric id.
    If not found, respond with HTTP 404.

    Response shape (object):
      Includes "genre_objects" like the list endpoint.
    """
    for m in data.MOVIES:
        if m["id"] == movie_id:
            genre_by_id = {g["id"]: g for g in data.GENRES}
            m["genre_objects"] = [genre_by_id[g] for g in m["genres"] if g in genre_by_id]
            return m
    raise HTTPException(status_code=404, detail="Movie not found")

# Run with:
#   uvicorn backend.main:app --reload --port 8000