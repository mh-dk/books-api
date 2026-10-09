from pydantic import BaseModel
from datetime import date

# [------- data models -------]
class Book(BaseModel):
    title: str
    author: str
    release_date: date
    number_of_pages: int

# [------- api models -------]
class BookOut(Book):
    id: str

class BooksOut(BaseModel):
    books: list[BookOut]
    page_start: int
    page_size: int
    length: int

class UpdateBook(BaseModel):
    title: str | None = None
    author: str | None = None
    release_date: date | None = None
    number_of_pages: int | None = None

class Pagination(BaseModel):
    page_start: int
    page_size: int