import re

from exceptions.base_exceptions import BadURLException, ShorteningErrorException
from fastapi import status
from requests import get

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
    if response.ok:
        return response.text.strip()
    raise ShorteningErrorException(
        response.content, status_code=status.HTTP_400_BAD_REQUEST
    )


def short_url(url):
    url = _clean_url(url)
    response = get(API_URL, params=dict(url=url))
    if response.ok:
        return response.text.strip()
    raise ShorteningErrorException(
        response.content, status_code=status.HTTP_400_BAD_REQUEST
    )


def _clean_url(url: str):
    if not url.startswith(("http://", "https://")):
        url = f"http://{url}"
    if not URL_REGEX.match(url):
        raise BadURLException(
            {"error": f"{url} is not valid"}, status_code=status.HTTP_400_BAD_REQUEST
        )
    return url
