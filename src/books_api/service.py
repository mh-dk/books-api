from uuid import uuid4
from .exceptions import BookNotFound
from . import models

books: dict[str, models.Book] = {}

def new_book(
    model: models.Book
):
    id = str(uuid4())
    books[id] = model

    return models.BookOut(
        id=id,
        **model.model_dump()
    )

def get_books(
    pagination: models.Pagination
):
    return [
        models.BookOut(
            id=id,
            **book.model_dump()
        )
        for i, (id, book) in enumerate(books.items())
        if  (i >= max(pagination.page_start-1, 0)*pagination.page_size)
            and
            (i <= max(pagination.page_start, 1)*pagination.page_size)
    ]

def get_book(
    id: str
):
    book = books.get(id)

    if not book:
        raise BookNotFound(404, id)

    return book

def update_book(
    id: str,
    model: models.UpdateBook
):
    book = books.get(id)
    if not book:
        raise BookNotFound(404, id)

    changes = model.model_dump(exclude_unset=True)
    for property, value in changes.items():
        setattr(book, property, value)

    return book

def delete_book(
    id: str
):
    book = books.pop(id, None)

    if not book:
        raise BookNotFound(404, id)