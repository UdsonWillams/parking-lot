import re
from datetime import datetime, timedelta
from uuid import uuid4

from api.db.db_orm import ShortUrlModel
from api.db.repository.postgres_shortner_repository import PostgresUserRepository
from api.exceptions.base_exceptions import BadURLException, ShorteningErrorException
from fastapi import status
from httpx import get

URL_REGEX = re.compile(
    r"(?i)\b((?:https?://|www\d{0,3}[.]|[a-z0-9.\-]+[.]"
    r"[a-z]{2,4}/)(?:[^\s()<>]+|\(([^\s()<>]+|(\([^\s()<>]+\)"
    r"))*\))+(?:\(([^\s()<>]+|(\([^\s()<>]+\)))*\)|[^\s`!()"
    r'\[\]{};:\'".,<>?«»“”‘’]))'
)
API_URL = "http://tinyurl.com/api-create.php"


def tiny_url(url):
    url = _clean_url(url)
    response = get(API_URL, params=dict(url=url))
    if response.status_code == status.HTTP_200_OK:
        return response.text.strip()
    raise ShorteningErrorException(
        response.content, status_code=status.HTTP_400_BAD_REQUEST
    )


def short_url(url):
    MONTH = 4
    url = _clean_url(url)
    shorted_url = str(uuid4()).split("-")[-1]
    data = ShortUrlModel(
        raw_url=url,
        shorted_url=shorted_url,
        expiration_date=datetime.now() + timedelta(weeks=MONTH),
    )
    url_db = PostgresUserRepository()
    if new_url := url_db.create(data):
        return new_url


def redirect_to_encrypted_url(url: str):
    url = _clean_url(url)
    url_db = PostgresUserRepository()
    if raw_url := url_db.get_by_encrypted_url(url):
        return raw_url


def _clean_url(url: str):
    if not url.startswith(("http://", "https://")):
        url = f"http://{url}"
    if not URL_REGEX.match(url):
        raise BadURLException(
            {"error": f"{url} is not valid"}, status_code=status.HTTP_400_BAD_REQUEST
        )
    return url
