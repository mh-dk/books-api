from typing import Annotated
from fastapi import Request, Depends
from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase, sessionmaker, Session as SqlAlchemySession
from books_api import config

engine = create_engine(config.SQLALCHEMY_URL)
Session = sessionmaker(engine)

class Base(DeclarativeBase):
    ...

def get_database_session(request: Request):
    return request.state.session

type DbSession = Annotated[SqlAlchemySession, Depends(get_database_session)]