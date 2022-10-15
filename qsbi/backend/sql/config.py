import pathlib

from pydantic import BaseSettings

# Project Directories
ROOT: pathlib.Path = pathlib.Path(__file__).resolve().parent.parent


class Settings(BaseSettings):
    QSBI_DB_URL: str = "sqlite:///example.db"
    QSBI_DB_URL_ASYNC: str = "sqlite+aiosqlite:///example.db"

    class Config:
        case_sensitive: bool = True


settings: Settings = Settings()
