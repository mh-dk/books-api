from datetime import date
from pydantic import BaseModel
from sqlalchemy import INTEGER, VARCHAR, DATE
from sqlalchemy.orm import Mapped, mapped_column
from books_api.core import Base

# [------- orm models -------]
class Book(Base):
    __tablename__ = "books"

    id: Mapped[int] = mapped_column(INTEGER, primary_key=True)
    title: Mapped[str] = mapped_column(VARCHAR(200))
    author: Mapped[str] = mapped_column(VARCHAR(100))
    release_date: Mapped[date] = mapped_column(DATE)
    number_of_pages: Mapped[int] = mapped_column(INTEGER)

# [------- api models -------]
class BookIn(BaseModel):
    title: str
    author: str
    release_date: date
    number_of_pages: int

class BookOut(BaseModel):
    id: int
    title: str
    author: str
    release_date: date
    number_of_pages: int

class UpdateBook(BaseModel):
    title: str | None = None
    author: str | None = None
    release_date: date | None = None
    number_of_pages: int | None = None