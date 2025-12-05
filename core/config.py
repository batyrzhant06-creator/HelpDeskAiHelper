# app/core/config.py
import os
from pydantic import BaseSettings


class Settings(BaseSettings):
    DATABASE_URL: str = "mysql+pymysql://user:password@localhost:3306/helpdesk"

    # сюда потом можно добавить ключи для AI и т.д.
    # OPENAI_API_KEY: str | None = None

    class Config:
        env_file = ".env"


settings = Settings()
