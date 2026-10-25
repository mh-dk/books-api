from typing import Annotated
from fastapi import APIRouter, Query
from books_api import core
from books_api.database import models as database_models
from . import models, service

router = APIRouter()

@router.get("/", response_model=database_models.PaginationOut[models.BookOut])
def get_all_books(
    pagination: Annotated[database_models.PaginationIn, Query()],
    session: core.DbSession
):
    return service.get_books(pagination, session)

@router.post("/", response_model=models.BookOut)
def add_a_new_book(
    model: models.BookIn,
    session: core.DbSession
):
    book = service.new_book(
        model,
        session
    )

    return book

@router.patch("/", response_model=models.BookOut)
def update_a_book(
    id: str, 
    model: models.UpdateBook,
    session: core.DbSession
):
    return service.update_book(id, model, session)

@router.delete("/")
def delete_a_book(
    id:str,
    session: core.DbSession
):
    service.delete_book(id, session)

    return {
        "ok": True
    }