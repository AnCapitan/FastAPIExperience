from typing import List

from fastapi import APIRouter, Form
from .models import Item, User
from .schemas import ItemIn, GetItem, ItemOut

from starlette.staticfiles import StaticFiles
from starlette.templating import Jinja2Templates

app_router = APIRouter(tags=["item"])
user_router = APIRouter(tags=["user"])


@user_router.get("/user", response_model=List[User])
async def get_items():
    users = await Item.objects.all()
    return users


@app_router.get("/items", response_model=List[Item])
async def get_items():
    items = await Item.objects.all()
    return items


@app_router.get("/items/{item_pk}", response_model=GetItem)
async def get_item(item_pk=int):
    item = await Item.objects.select_related('user').get(pk=item_pk)
    return item


@app_router.post("/items", response_model=ItemOut)
async def create_item(title: str = Form(...), description: str = Form(...)):
    post = ItemIn(title=title, description=description)
    user = await User.objects.first()
    return await Item.objects.create(user=user, **post.dict())
