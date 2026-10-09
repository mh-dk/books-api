from fastapi.exceptions import HTTPException

class BookNotFound(HTTPException):
    def __init__(self, status_code, id: str, headers = None):
        super().__init__(status_code, f"no book with id {id} was found", headers)