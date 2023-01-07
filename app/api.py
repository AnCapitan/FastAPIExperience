from typing import List

from fastapi import APIRouter
from .models import Item, User

from starlette.staticfiles import StaticFiles
from starlette.templating import Jinja2Templates

app_router = APIRouter(tags=["item"])



@app_router.get("/items", response_model=List[Item])
async def get_items():
    items = await Item.objects.all()
    return items


@app_router.post("/items", response_model=Item)
async def create_item(item: Item):
    await item.save()
    return item

