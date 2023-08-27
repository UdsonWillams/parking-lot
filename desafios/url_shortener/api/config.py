from pydantic import BaseSettings


class Settings(BaseSettings):
    # Postgres
    DB_NAME: str = "shortner_db"
    DB_USER: str = "postgres"
    DB_PASSWORD: str = "passwd@123"
    DB_HOST: str = "localhost"
    DB_PORT: int = 5432

    class Config:
        env_file = ".env"
