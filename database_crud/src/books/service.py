from sqlmodel.ext.asyncio.session import AsyncSession
from .schemas import BookCreateModel, BookUpdateModel
from src.books.model import Book
from sqlmodel import select, desc
from typing import List
from datetime import datetime


class BookService:
    async def get_all_books(self, session: AsyncSession) -> List[Book]:
        statement = select(Book).order_by(desc(Book.created_at))
        results = await session.exec(statement)
        return results.all()

    async def get_book_by_uid(self, book_uid: str, session: AsyncSession) -> dict:
        statement = select(Book).where(Book.uid == book_uid)
        result = await session.exec(statement)

        book = result.first()
        return book if book is not None else None

    async def create_book(
        self, book_data: BookCreateModel, session: AsyncSession
    ) -> dict:

        book_data_dict = book_data.model_dump()

        new_book = Book(**book_data_dict)

        new_book.published_date = datetime.strptime(
            book_data_dict["published_date"], "%Y-%m-%d"
        )

        session.add(new_book)
        await session.commit()

        return new_book

    async def update_book(
        self, book_uid: str, update_data: BookUpdateModel, session: AsyncSession
    ) -> dict:
        book_to_update = await self.get_book_by_uid(book_uid, session)

        if book_to_update is not None:

            update_data_dict = update_data.model_dump()

            for key, value in update_data_dict.items():
                setattr(book_to_update, key, value)

            await session.commit()

            return book_to_update
        else:
            return None

    async def delete_book(self, book_uid: str, session: AsyncSession) -> None:
        book_to_delete = await self.get_book_by_uid(book_uid, session)

        if book_to_delete:
            session.delete(book_to_delete)
            await session.commit()
            return book_to_delete
        return None

    async def patch_book(self, book_uid: str, book_data, session: AsyncSession) -> dict:
        pass
