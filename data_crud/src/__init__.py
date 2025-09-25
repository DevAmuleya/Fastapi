from fastapi import FastAPI
from src.db.main import init_db
from contextlib import asynccontextmanager
from src.books.routes import book_router


@asynccontextmanager
async def lifespan(app: FastAPI):

    # Startup code here
    print("Starting up...")

    await init_db()
    yield
    # Shutdown code here
    print("Shutting down...")


version = "v1"

app = FastAPI(
    title="Simple CRUD Webserver",
    description="A simple CRUD webserver built with FastAPI",
    version=version,
    lifespan=lifespan,
)


app.include_router(book_router, prefix="/api/{version}/books", tags=["books"])
