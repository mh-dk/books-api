from fastapi import APIRouter
from .books.views import router as books_router

router = APIRouter()

router.include_router(books_router, prefix="/books")