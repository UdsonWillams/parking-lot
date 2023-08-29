import logging
from datetime import datetime

from api.config import Settings
from api.db.db_orm import (
    ShortUrlModel,
    ShortUrlRef,
)
from api.db.repository.exceptions import (
    CreateUrlException,
    DeleteUrlException,
    ExpirationTimeException,
    UrlNotFoundException,
)
from fastapi import status
from sqlalchemy import (
    column,
    create_engine,
    insert,
)
from sqlalchemy.orm import sessionmaker

settings = Settings()
logger = logging.getLogger(__name__)

SQLALCHEMY_DATABASE_URL = (
    f"postgresql://{settings.DB_USER}:"
    f"{settings.DB_PASSWORD}@"
    f"{settings.DB_HOST}:"
    f"{settings.DB_PORT}/"
    f"{settings.DB_NAME}"
)


class PostgresUserRepository:
    def __init__(self):
        engine = create_engine(SQLALCHEMY_DATABASE_URL)
        session_local = sessionmaker(autocommit=False, autoflush=False, bind=engine)
        self.db = session_local()

    def get_by_id(self, url_id: str) -> ShortUrlRef:
        url: ShortUrlRef
        if url := self.db.query(ShortUrlRef).get(url_id):
            if url.expiration_date < datetime.now():
                self.delete_by_id(url_id)
                raise ExpirationTimeException()
            return url
        raise UrlNotFoundException(
            status_code=status.HTTP_404_NOT_FOUND, detail={"error": "url_not_found"}
        )

    def get_by_shorted_url(self, shorted_url: str) -> ShortUrlRef:
        url = (
            self.db.query(ShortUrlRef)
            .filter(ShortUrlRef.shorted_url == shorted_url)
            .first()
        )
        url: ShortUrlRef
        if url:
            if url.expiration_date < datetime.now():
                self.delete_by_shorted_url(shorted_url)
                raise ExpirationTimeException(
                    status_code=status.HTTP_400_BAD_REQUEST,
                    detail={"error": "expiration time has passed"},
                )
            return url
        raise UrlNotFoundException(
            status_code=status.HTTP_404_NOT_FOUND, detail={"error": "url_not_found"}
        )

    def create(self, data: ShortUrlModel) -> str:
        try:
            insert_data = insert(ShortUrlRef).returning(column("id"))
            insert_values = insert_data.values(data.dict())
            result = self.db.execute(insert_values)
            encrypted_url = dict(result.fetchone()).get("encrypted_url")
            self.db.commit()
        except Exception as e:
            logger.error(f"Erro ao criar usuario no Postgres | Erro: {e}")
            raise CreateUrlException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail={"error": "error_to_create_url"},
            )
        return encrypted_url

    # def update(self, url_new_data: ShortUrlModel):
    #     pass

    def delete_by_id(self, encrypted_url: str):
        try:
            encrypted_url = self.get_by_shorted_url(encrypted_url)
            self.db.delete(encrypted_url)
            self.db.commit()
        except Exception as e:
            logger.error(f"Erro ao criar usuario no Postgres | Erro: {e}")
            raise DeleteUrlException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail={"error": "error_to_delete_url"},
            )

    def delete_by_shorted_url(self, shorted_url: str):
        try:
            shorted_url = self.get_by_shorted_url(shorted_url)
            self.db.delete(shorted_url)
            self.db.commit()
        except Exception as e:
            logger.error(f"Erro ao criar usuario no Postgres | Erro: {e}")
            raise DeleteUrlException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail={"error": "error_to_delete_url"},
            )
