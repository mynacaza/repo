from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic import BaseModel, PostgresDsn, EmailStr


class DatabaseConfig(BaseModel):
    url: PostgresDsn
    echo: bool = False
    echo_pool: bool = False
    pool_size: int = 3
    max_overflow: int = 5


class JWTModel(BaseModel):
    secret: str
    algorithm: str
    expire: int


class SMTPConfig(BaseModel):
    host: str = "smtp.gmail.com"
    port: int = 587
    user: EmailStr = "asdasdsasd501@gmail.com"
    password: str


class Settings(BaseSettings):
    db: DatabaseConfig
    jwt: JWTModel
    smtp: SMTPConfig
    model_config = SettingsConfigDict(
        env_file=".env",
        env_prefix="FASTAPI__",
        env_nested_delimiter="__",
        extra="ignore",
    )


settings = Settings()
