from starlette.staticfiles import StaticFiles
from starlette.templating import Jinja2Templates
from starlette.requests import Request
import requests as req
from fastapi import APIRouter
from decouple import config
from .schemas import UserCreate
from .models import User

auth_router = APIRouter(tags=["auth"])
auth_router.mount("/static", StaticFiles(directory="frontend/static"), name="static")
templates = Jinja2Templates(directory="frontend/templates/app")




@auth_router.get("/verify")
async def verify(request: Request):
    auth_code = str(request.url).replace(f'{config("REDIRECT_URI")}?code=', '')
    auth_token = f"https://oauth.vk.com/access_token?client_id={config('CLIENT_ID')}&client_secret={config('CLIENT_SECRET')}&redirect_uri={config('REDIRECT_URI')}&code={auth_code}"
    data = req.get(auth_token).json()
    user_id: int = data['user_id']
    try:
        if data['user_id'] == dict(await User.objects.get(user_id=user_id))['user_id']:
            return {}
    except:
        url = f"https://api.vk.com/method/users.get?user_ids={data['user_id']}&fields=photo_200&access_token={data['access_token']}&v=5.131"
        request = req.get(url).json()["response"][0]
        user = UserCreate(
            user_id=request["id"],
            last_name=request["first_name"],
            first_name=request["last_name"],
            avatar=request["photo_200"])
        return await User.objects.create(**user.dict())
    return templates.TemplateResponse("verify.html", {"request": request})



