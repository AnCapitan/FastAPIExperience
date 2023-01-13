from datetime import timedelta

from fastapi import Depends, FastAPI, HTTPException
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from pydantic import BaseModel


fake_users_db = {
    "Jin": {
        "id": 1,
        "user_id": 15234,
        "first_name": "Jin",
        "last_name": "Jordan",
        "avatar": "johndoe@example.com",
        "hashed_password": "$2b$12$EixZaYVK1fsbw1ZfbX3OXePaWxn96p36WQoeG6Lruj3vjPGga31lW",
        "disabled": False,
    },
    "Alex": {
        "id": 2,
        "user_id": 3464373,
        "first_name": "Alex",
        "last_name": "Gordan",
        "avatar": "Gordan@example.com",
        "hashed_password": "$2b$12$EixZaYVK1fsbw1ZfbX3OXePaWxn96p36WQoeG6Lruj3vjPGga31lW",
        "disabled": False,
    },
}


app = FastAPI()

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

class Token(BaseModel):
    access_token: str
    token_type: str


