from pydantic import BaseModel
from typing import List
from datetime import datetime, date
import uuid


class Book(BaseModel):
    uid: uuid.UUID
    title: str
    author: str
    publisher: str
    published_date: date
    pages: int
    language: str
    created_at: datetime
    updated_at: datetime


class BookCreateModel(BaseModel):
    title: str
    author: str
    publisher: str
    published_date: str
    pages: int
    language: str


class BookUpdateModel(BaseModel):
    title: str
    author: str
    publisher: str
    pages: int
    language: str
