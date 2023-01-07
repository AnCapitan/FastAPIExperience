from starlette.staticfiles import StaticFiles
from starlette.templating import Jinja2Templates
from starlette.requests import Request
from fastapi import APIRouter
from . import schemas

auth_router = APIRouter(tags=["auth"])
auth_router.mount("/static", StaticFiles(directory="frontend/static"), name="static")
templates = Jinja2Templates(directory="frontend/templates/app")
# http://REDIRECT_URI#access_token=TOKEN3&expires_in=TIME&user_id=ID



@auth_router.get("/")
async def vk_auth(request: Request):
    return templates.TemplateResponse("auth_vk.html", {"request": request})


@auth_router.post("/vk/auth", response_model=schemas.Token)
async def vk_auth(user: schemas.UserCreate):
    return {}
