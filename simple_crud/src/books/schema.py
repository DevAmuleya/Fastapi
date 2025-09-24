from pydantic import BaseModel
from typing import List


class Book(BaseModel):
    id: int
    title: str
    author: str
    publisher: str
    published_date: str
    pages: int
    language: str


class PatchRequestModel(BaseModel):
    id: int
    title: str
    author: str
    language: str
