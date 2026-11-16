from fastapi import Depends, FastAPI

from .dependencies import get_query_token, get_token_header
from .internal import admin
from .routers import items, users, dish

from contextlib import asynccontextmanager
from sqlalchemy.ext.asyncio import async_sessionmaker
from .database import make_engine
from .settings import Settings

@asynccontextmanager
async def lifespan(app: FastAPI):
    settings = Settings()
    engine = make_engine(settings.database_url.get_secret_value())
    app.state.engine = engine
    app.state.session_factory = async_sessionmaker(engine, expire_on_commit=False)
    yield
    await engine.dispose()

app = FastAPI(dependencies=[Depends(get_query_token)], lifespan=lifespan)


app.include_router(users.router)
app.include_router(items.router)
app.include_router(dish.router)
app.include_router(
    admin.router,
    prefix="/admin",
    tags=["admin"],
    dependencies=[Depends(get_token_header)],
    responses={418: {"description": "I'm a teapot"}},
)

@app.get("/")
async def root():
    return {"message": "Hello Bigger Applications!"}
