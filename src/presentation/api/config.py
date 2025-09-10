from pydantic import BaseModel
from pydantic_settings import BaseSettings, SettingsConfigDict

from src.infrastructure.db.config import DBConfig


class APIConfig(BaseModel):
    host: str
    port: int
    reload: bool
    reload_dirs: list[str]


class Config(BaseSettings):
    model_config = SettingsConfigDict(
        env_file='.env',
        env_file_encoding='utf-8',
        env_nested_delimiter='__',
        extra='ignore',
    )

    api: APIConfig
    db: DBConfig
