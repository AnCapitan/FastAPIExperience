from starlette.staticfiles import StaticFiles
from starlette.templating import Jinja2Templates
import requests as req
from starlette.requests import Request
from fastapi import APIRouter

from settings import CLIENT_ID, CLIENT_SECRET, REDIRECT_URI
from .schemas import UserCreate
from .models import User
from . import schemas

auth_router = APIRouter(tags=["auth"])
auth_router.mount("/static", StaticFiles(directory="frontend/static"), name="static")
templates = Jinja2Templates(directory="frontend/templates/app")

SECRET_KEY = "09d25e094faa6ca2556c818166b7a9563b93f7099f6f0f4caa6cf63b88e8d3e7"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30



@auth_router.get("/verify")
async def verify(request: Request):
    auth_code = str(request.url).replace(f'{REDIRECT_URI}?code=', '')
    auth_token = f"https://oauth.vk.com/access_token?client_id={CLIENT_ID}&client_secret={CLIENT_SECRET}&redirect_uri={REDIRECT_URI}&code={auth_code}"
    print(req.get(auth_token).json())
    return templates.TemplateResponse("verify.html", {"request": request})


@auth_router.get("/auth_user", response_model=UserCreate)
async def create_user(token):
    user_id = 214366260
    method = 'users.get'
    url = f"https://api.vk.com/method/{method}?user_ids={user_id}&fields=photo_200&access_token={token}&v=5.131"
    request = req.get(url).json()["response"][0]
    user = UserCreate(
        id_vk=request["id"],
        last_name=request["first_name"],
        first_name=request["last_name"],
        avatar=request["photo_200"])
    return await User.objects.create(**user.dict())
