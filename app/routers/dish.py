from fastapi import APIRouter, Depends
from sqlalchemy import text

from ..database import SessionDep

router = APIRouter(
    prefix="/dish",
    tags=["dish", "dishes"],
    responses={404: {"description": "Not found"}},
)

@router.get("/")
async def read_items():
    return ""

@router.get("test")
async def read_items_dish_test():
    return "DISH test"

@router.get("dbtest")
async def read_items_from_db():
    return "DISH test"

@router.get("dbtest2")
async def db_test(session: SessionDep):
    result = await session.execute(text("SELECT version()"))
    return {"postgres": result.scalar_one()}
