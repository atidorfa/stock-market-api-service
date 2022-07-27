import os
from functools import lru_cache
from typing import Dict, Any
from dotenv import dotenv_values
from pydantic import BaseSettings


class Settings(BaseSettings):
    # APP Description
    APP_ID: int
    APP_DESC: str
    APP_VERSION: str
    API_TOKEN: str

    # DB config
    DB_USER: str
    DB_PASSWD: str
    DB: str
    DB_PORT: str
    DB_HOST: str
    DB_POOL_SIZE: int = 5  # default value
    DB_POOL_MAX_SIZE: int = 20
    DB_LOG_QUERY: bool = False

    # Redis config
    REDIS_URL: str

    REDIS_CLIENT_EXPIRATION_TIME: int = 900  # 15 minutes
    REDIS_DEFAULT_EXPIRATION_TIME: int = 600  # 10 minutes
    REDIS_PERIODWEEKS_EXPIRATION_TIME: int = 3600  # 60 minutes
    REDIS_RT_EXPIRATION = 300  # 5 minutos, tiempo de cache para mensajes de realtime

    supported_leagues = {"WC", "CL", "BL1", "DED", "BSA", "PD", "FL1", "ELC", "PPL", "EC", "SA", "PL", "CLI"}

    class Config:
        case_sensitive = True
        env_file_encoding = 'utf-8'
        extra = "ignore"

        @classmethod
        def customise_sources(cls, init_settings, env_settings, file_secret_settings, ):
            return init_settings, external_settings_source, env_settings, file_secret_settings,


def external_settings_source(settings: BaseSettings) -> Dict[str, Any]:
    config = {
        **dotenv_values(dotenv_path=os.getenv("DB_SETTINGS")),
        **dotenv_values(dotenv_path=os.getenv("DB_CREDENTIALS")),
        **dotenv_values(dotenv_path=os.getenv("REDIS_SETTINGS")),
        **dotenv_values(dotenv_path=os.getenv("APP_SETTINGS")),
    }
    return config


@lru_cache()
def get_settings():
    return Settings()


if __name__ == "__main__":
    s = Settings()
    print("Debug settings", s)
