from pydantic import BaseSettings, Field


class Settings(BaseSettings):
    database_name: str = Field("DATABASE_NAME", env="DATABASE_NAME")
    database_user: str = Field("DATABASE_USER", env="DATABASE_USER")
    database_password: str = Field("DATABASE_PASSWORD", env="DATABASE_PASSWORD")
    database_host: str = Field("DATABASE_HOST", env="DATABASE_HOST")
    database_port: int = Field(5432, env="DATABASE_PORT")

    class Config:
        env_file = ".env"


settings = Settings()
