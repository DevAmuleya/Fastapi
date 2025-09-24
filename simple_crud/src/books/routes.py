from fastapi import APIRouter, HTTPException
from typing import List
from src.books.book_data import books
from src.books.schema import Book, PatchRequestModel

book_router = APIRouter()


@book_router.get("/", response_model=List[Book])
async def get_all_books() -> List[Book]:
    return books


@book_router.get("/{book_id}", response_model=Book)
async def get_book(book_id) -> dict:
    for book in books:

        if book["id"] == book_id:
            return book


@book_router.post("/", response_model=Book)
async def create_book(book_data: Book) -> dict:
    new_book = book_data.model_dump()
    books.append(new_book)

    return new_book


@book_router.patch("/{book_id}", response_model=Book)
async def update_book(book_id: int, book_patch: PatchRequestModel) -> dict:
    for book in books:
        if book["id"] == book_id:

            book.update(book_patch.model_dump())
            return book

    raise HTTPException(status_code=404, detail="Book not found")


@book_router.put("/{book_id}", response_model=Book)
async def replace_book(book_id: int, book: Book) -> dict:
    pass


@book_router.delete("/{book_id}")
async def delete_book(book_id: int) -> dict:
    for book in books:
        if book["id"] == book_id:
            books.remove(book)
            return {"message": "Book deleted successfully"}
    raise HTTPException(status_code=404, detail="Book not found")
