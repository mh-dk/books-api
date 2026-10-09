from typing import Annotated

from . import models, service
from fastapi import APIRouter, Query

router = APIRouter()

@router.get("/", response_model=models.BooksOut)
def get_all_books(pagination: Annotated[models.Pagination, Query()]):
    books = service.get_books(pagination)
    return {
        "books": books,
        "page_start": pagination.page_start,
        "page_size": pagination.page_size,
        "length": len(books)
    }

@router.post("/", response_model=models.BookOut)
def add_a_new_book(model: models.Book):
    book = service.new_book(
        model
    )

    return book

@router.patch("/", response_model=models.Book)
def update_a_book(id: str, model: models.UpdateBook):
    return service.update_book(id, model)

@router.delete("/")
def delete_a_book(id:str):
    service.delete_book(id)
    return {
        "ok": True
    }