from pydantic_settings import BaseSettings
from functools import lru_cache

class Settings(BaseSettings):
    # If environment variables with the same name exist, the following will be overwritten.
    API_V1_STR: str = "/api/v1"
    PROJECT_NAME: str = "Tic-Tac-Toe API"

@lru_cache()
def get_settings():
    return Settings().dict()