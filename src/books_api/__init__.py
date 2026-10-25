from fastapi import FastAPI, Request
from .router import router
from .core import engine, Session

app = FastAPI()
app.include_router(router)

@app.middleware("http")
async def database_session_middleware(request: Request, call_next):
    with Session.begin() as session:
        request.state.session = session
        response = await call_next(request)

    return response