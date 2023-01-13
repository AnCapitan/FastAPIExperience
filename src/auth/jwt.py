from jose import jwt
from datetime import datetime, timedelta
from decouple import config
from fastapi import APIRouter


token_router = APIRouter(tags=["token"])



@token_router.get('/token')
def create_access_token(payload: dict, expires_delta: timedelta | None = None):
    payload_copy = payload.copy()
    if expires_delta:
        expires = datetime.utcnow() + expires_delta
    else:
        expires = datetime.utcnow() + timedelta(minutes=15)
    payload_copy.update({"exp": expires})
    token = jwt.encode(payload_copy, config('SECRET_KEY'), algorithm=config('ALGORITHM'))
    print(token)
    return token


def decode_token(token: str):
    return jwt.decode(token, config('SECRET_KEY'), config('ALGORITHM'))

