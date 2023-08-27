from datetime import datetime

from pydantic import BaseModel
from sqlalchemy import Column, DateTime, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class ShortUrlRef(Base):
    __tablename__ = "shortener_api_url_reference"
    id = Column(Integer, primary_key=True, index=True)
    raw_url = Column(String, unique=True, index=True)
    shorted_url = Column(String, unique=True, index=False)
    expiration_date = Column(DateTime, unique=False, index=False)

    def __repr__(self) -> str:
        return (
            f"Url | id:{self.id} | "
            f"raw_url: {self.raw_url} | "
            f"shorted_url: {self.shorted_url} | "
            f"expiration_date: {self.expiration_date}|"
        )


class ShortUrlModel(BaseModel):
    id: int | None
    raw_url: str
    shorted_url: str
    expiration_date: datetime

    class Config:
        orm_mode = True
