from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic import BaseModel, PostgresDsn


class DatabaseConfig(BaseModel):
    url: PostgresDsn
    echo: bool = (False,)
    echo_pool: bool = (False,)
    pool_size: int = (3,)
    max_overflow: int = (5,)


class Settings(BaseSettings):
    db: DatabaseConfig
    model_config = SettingsConfigDict(
        env_file=".env", env_nested_delimiter="__", env_prefix="FASTAPI__"
    )


settings = Settings()
