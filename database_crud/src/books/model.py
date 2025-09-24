from sqlmodel import SQLModel, Field, Column
from datetime import datetime, date
import sqlalchemy.dialects.postgresql as pg
import uuid


class Book(SQLModel, table=True):
    uid: uuid.UUID = Field(
        sa_column=Column(
            pg.UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, nullable=False
        )
    )
    title: str
    author: str
    publisher: str
    published_date: date
    pages: int
    language: str
    created_at: datetime = Field(sa_column=Column(pg.TIMESTAMP, default=datetime.now))
    updated_at: datetime = Field(sa_column=Column(pg.TIMESTAMP, default=datetime.now))

    def __repr__(self):
        return f"<Book title={self.title}>"
