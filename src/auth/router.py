from sqlalchemy import select, insert
from sqlalchemy.ext.asyncio import AsyncSession
from starlette.staticfiles import StaticFiles
from starlette.templating import Jinja2Templates
from starlette.requests import Request
import requests as req
from fastapi import APIRouter, Depends
from decouple import config

from database import get_async_session
from .schemas import UserCreate
from .models import User

auth_router = APIRouter(tags=["auth"])

templates = Jinja2Templates(directory="frontend/templates/app", auto_reload=True, autoescape=False)
auth_router.mount("/static", StaticFiles(directory="frontend/static"), name="static")


@auth_router.get("/")
async def main_page(request: Request):
    return templates.TemplateResponse("main_page.html", {"request": request})


@auth_router.get("/verify", )
async def verify(request: Request, session: AsyncSession = Depends(get_async_session)):
    auth_code = str(request.url).replace(f'{config("REDIRECT_URI")}?code=', '')
    auth_token = f"https://oauth.vk.com/access_token?client_id={config('CLIENT_ID')}&client_secret={config('CLIENT_SECRET')}&redirect_uri={config('REDIRECT_URI')}&code={auth_code}"
    data = req.get(auth_token).json()
    user_id: int = (data['user_id'])
    if await session.execute(select(User).where(User.user_id == user_id)) is None:
        return {"Response": "Вы уже в БД"}
    else:
        url = f"https://api.vk.com/method/users.get?user_ids={data['user_id']}&fields=photo_200&access_token={data['access_token']}&v=5.131"
        print(req.get(url).json())
        request = req.get(url).json()["response"][0]
        print('*' * 100)
        user = UserCreate(
            user_id=request["id"],
            last_name=request["first_name"],
            first_name=request["last_name"],
            avatar=request["photo_200"])
        print('*' * 100)
        stmt = insert(User).values(**user.dict())
        print('*' * 100)
        await session.execute(stmt)
        print('*' * 100)
        await session.commit()
        return templates.TemplateResponse("verify.html", {"request": request})






# @app_router.get("/items", response_model=List[Item])
# async def get_items():
#     items = await Item.objects.all()
#     return items
#
#
# @app_router.get("/items/{item_pk}", response_model=GetItem)
# async def get_item(item_pk=int):
#     item = await Item.objects.select_related('user').get(pk=item_pk)
#     return item
#
#
# @app_router.post("/items", response_model=ItemOut)
# async def create_item(title: str = Form(...), description: str = Form(...)):
#     post = ItemIn(title=title, description=description)
#     user_id = 214366260
#     user = await User.objects.get(id_vk=user_id)
#     return await Item.objects.create(user=user, **post.dict())
