from pydantic import BaseModel
from dotenv import load_dotenv
import os

"""
Loads environment variables from the project root `.env` (using python-dotenv)
and exposes a simple typed `settings` object that the rest of the backend can import.
"""

# Resolve the absolute path to the project root, then to the .env file
ROOT_DIR = os.path.dirname(os.path.dirname(__file__))
ENV_PATH = os.path.join(ROOT_DIR, ".env")

#Load all key=value pairs in .env into process environment variables.
# If .env is missing, defaults (below) will be used.
load_dotenv(dotenv_path=ENV_PATH)

class Settings(BaseModel):
    """
    Small strongly-typed settings model.
    If an env var is missing, we fall back to a safe default.
    """
    port: int = int(os.getenv("PORT", "8000"))
    api_base_url: str = os.getenv("API_BASE_URL", "http://127.0.0.1:8000")

settings = Settings()