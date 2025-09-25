from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from src.books.service import BookService
from src.books.schemas import Book, BookCreateModel, BookUpdateModel
from src.db.main import get_session

book_router = APIRouter()
book_service = BookService()


@book_router.get("/", response_model=list[Book])
async def get_books(session: AsyncSession = Depends(get_session)):
    books = await book_service.get_all_books(session)
    return books


@book_router.get("/{book_uid}", response_model=Book)
async def get_book(book_uid: str, session: AsyncSession = Depends(get_session)):
    book = await book_service.get_book_by_id(session, book_uid)
    if not book:
        raise HTTPException(status_code=404, detail="Book not found")
    return book


@book_router.post("/", response_model=Book, status_code=201)
async def create_book(
    book_data: BookCreateModel, session: AsyncSession = Depends(get_session)
):
    new_book = await book_service.create_book(session, book_data)
    return new_book


@book_router.patch("/{book_uid}", response_model=Book)
async def update_book(
    book_uid: str,
    book_data: BookUpdateModel,
    session: AsyncSession = Depends(get_session),
):
    updated_book = await book_service.update_book(session, book_uid, book_data)
    if not updated_book:
        raise HTTPException(status_code=404, detail="Book not found")
    return updated_book


@book_router.delete("/{book_uid}", status_code=204)
async def delete_book(book_uid: str, session: AsyncSession = Depends(get_session)):
    success = await book_service.delete_book(session, book_uid)
    if not success:
        raise HTTPException(status_code=404, detail="Book not found")
    return None
