from sqlmodel import select, desc
from .model import Book
from datetime import datetime
from .schemas import BookCreateModel, BookUpdateModel


class BookService:
    async def get_all_books(self, session) -> list[Book]:
        statement = select(Book).order_by(desc(Book.created_at))
        results = await session.exec(statement)
        return results.all()

    async def get_book_by_id(self, session, book_uid) -> dict:
        statement = select(Book).where(Book.uid == book_uid)
        results = await session.exec(statement)
        return results.first()


    async def create_book(self, session, book_data: BookCreateModel) -> Book:
        book_data_dict = book_data.model_dump()

        new_book = Book(**book_data_dict)

        new_book.published_date = datetime.strptime(
            book_data_dict["published_date"], "%Y-%m-%d"
        )

        session.add(new_book)
        await session.commit()
        await session.refresh(new_book)
        return new_book

    async def update_book(self, session, book_uid, book_data: BookUpdateModel) -> dict:
        statement = select(Book).where(Book.uid == book_uid)
        results = await session.exec(statement)
        book = results.first()
        if book:
            book_data_dict = book_data.model_dump()
            for key, value in book_data_dict.items():
                setattr(book, key, value)
            session.add(book)
            await session.commit()
            await session.refresh(book)
        return book

    async def delete_book(self, session, book_uid) -> bool:
        statement = select(Book).where(Book.uid == book_uid)
        results = await session.exec(statement)
        book = results.first()
        if book:
            await session.delete(book)
            await session.commit()
            return True
        return False
