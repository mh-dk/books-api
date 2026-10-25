import os
from typing import overload
from dotenv import load_dotenv

@overload
def config(name:str) -> str: ...

@overload
def config(name:str, default:str) -> str: ...

def config(name:str, default:str | None = None) -> str | None:
    result = os.environ.get(name, default)

    if (not result) and (not default):
        raise ValueError(f"environment variable {name} is needed and missing.")

    return result

load_dotenv(override=True)

SQLALCHEMY_URL = config("SQLALCHEMY_URL")