from fastapi import FastAPI
from typing import List
from src.books.routes import book_router

version = "v1"

app = FastAPI(
    title="Simple CRUD Webserver",
    description="A simple CRUD webserver built with FastAPI",
    version=version,
    contact={"name": "DevAmuleya", "email": "abdulganiyua723@gmail.com"},
)


app.include_router(book_router, prefix="/api/{version}/books", tags=["books"])
