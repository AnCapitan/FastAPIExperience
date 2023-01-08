from typing import List

from starlette.requests import Request
from starlette.templating import Jinja2Templates

templates = Jinja2Templates(directory="frontend/templates/app")
from fastapi import APIRouter, Form
from .models import Item, User
from .schemas import ItemIn, GetItem, ItemOut


app_router = APIRouter(tags=["item"])
user_router = APIRouter(tags=["user"])



@app_router.get("/")
async def main_page(request:Request):
    return templates.TemplateResponse("main_page.html", {"request": request})



@user_router.get("/user", response_model=List[User])
async def get_users():
    users = await User.objects.all()
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
    user_id = 214366260
    user = await User.objects.get(id_vk=user_id)
    return await Item.objects.create(user=user, **post.dict())
