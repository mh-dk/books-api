from typing import Type, TypeVar
from sqlalchemy.orm import Session
from books_api.core import Base
from . import models

T = TypeVar("T", bound=Base)

def query_pagiantion(entity: Type[T], model: models.PaginationIn, session: Session):
    total = session.query(entity).count()
    items = (
        session.query(entity)
        .offset(max(model.page_start-1, 0)*model.page_size)
        .limit(max(model.page_start, 1)*model.page_size)
    )

    return models.PaginationOut(
        items=items.all(),
        page_start=model.page_start,
        page_size=model.page_size,
        total_in_page=items.count(),
        total=total
    )