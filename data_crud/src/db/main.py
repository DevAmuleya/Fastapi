from sqlmodel import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.asyncio import AsyncEngine
from sqlmodel.ext.asyncio.session import AsyncSession
from src.config import Config
from sqlmodel import SQLModel
from typing import AsyncGenerator

engine = AsyncEngine(create_engine(Config.DATABASE_URL, echo=True))


async def init_db():
    async with engine.begin() as conn:

        # await conn.execute(text("SELECT 1"))  # simple statement
        # print("✅ Database connected")

        from src.books.model import Book

        await conn.run_sync(SQLModel.metadata.create_all)


async def get_session() -> AsyncGenerator[AsyncEngine, None]:

    Session = sessionmaker(bind=engine, class_=AsyncSession, expire_on_commit=False)

    async with Session() as session:
        yield session
