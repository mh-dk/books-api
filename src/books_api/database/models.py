from typing import Generic, TypeVar
from pydantic import BaseModel

T = TypeVar("T")

class PaginationIn(BaseModel):
    page_start: int
    page_size: int

class PaginationOut(BaseModel, Generic[T]):
    items: list[T]
    page_start: int
    page_size: int
    total: int
    total_in_page: int