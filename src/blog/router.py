from fastapi import APIRouter, HTTPException, Depends, Form
from sqlalchemy import insert, select
from sqlalchemy.ext.asyncio import AsyncSession

from auth.models import User
from blog.models import Item
from blog.schemas import ItemCreate
from database import get_async_session

blog_router = APIRouter(tags=["blog"])


@blog_router.post("/account")
async def create_item(
        session: AsyncSession = Depends(get_async_session),
        # user: User = Depends(current_user),
        name: str = Form(...),
        description: str = Form(...),

):
    item_create = ItemCreate(name=name, description=description, )
    query = insert(Item).values(**item_create.dict())
    await session.execute(query)
    await session.commit()
    return {"status": "create item"}


@blog_router.get("/account")
async def get_item(
        session: AsyncSession = Depends(get_async_session),
        # user: User = Depends(current_user),
):
    stmt = await session.execute(select(Item))
    result = stmt.all()
    return result

@blog_router.get("/account/{pk:int}")
async def single_item(
        pk: int,
        session: AsyncSession = Depends(get_async_session),

):
    stmt = await session.execute(select(Item).where(Item.title == 'first trav'))
    data = (stmt.first())
    if data is None:
        return {"error": 'данных нет'}
    else:
        return data

@blog_router.get("/account/test/{pk:int}")
async def single_user(
        pk: int,
        session: AsyncSession = Depends(get_async_session),

):
    stmt = await session.execute(select(user).where(item.c.id == 1))
    data = (stmt.all())[0]
    print(data)
    return data