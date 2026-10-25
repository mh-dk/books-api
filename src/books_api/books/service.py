from sqlalchemy.orm import Session
from books_api.exceptions import BookNotFound
from . import models
from books_api.database import (
    models as database_models, 
    service as database_service
)

def new_book(
    model: models.BookIn,
    session: Session
):
    book = models.Book(
        title=model.title,
        author=model.author,
        release_date=model.release_date,
        number_of_pages=model.number_of_pages 
    )
    session.add(book)
    session.flush()
    return models.BookOut(
        id=book.id,
        **model.model_dump()
    )

def get_books(
    pagination: database_models.PaginationIn,
    session: Session
):
    return database_service.query_pagiantion(
        models.Book, 
        pagination, 
        session
    )

def get_book(
    id: str,
    session: Session
):
    book = session.get(models.Book, id)

    if not book:
        raise BookNotFound(404, id)

    return models.BookOut(
        id=book.id,
        title=book.title,
        author=book.author,
        release_date=book.release_date,
        number_of_pages=book.number_of_pages 
    )

def update_book(
    id: str,
    model: models.UpdateBook,
    session: Session
):
    book = session.get(models.Book, id)
    if not book:
        raise BookNotFound(404, id)

    changes = model.model_dump(exclude_unset=True)
    for property, value in changes.items():
        setattr(book, property, value)

    return models.BookOut(
        id=book.id,
        title=book.title,
        author=book.author,
        release_date=book.release_date,
        number_of_pages=book.number_of_pages     
    )

def delete_book(
    id: str,
    session: Session
):
    book = session.get(models.Book, id)
    if not book:
        raise BookNotFound(404, id)

    session.delete(book)