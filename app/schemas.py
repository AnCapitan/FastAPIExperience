from typing import Union, List

from pydantic import BaseModel, EmailStr


class User(BaseModel):
    id_vk: str
    first_name: str
    last_name: str


class UserCreate(BaseModel):
    user_id: int
    first_name: str
    last_name: str
    avatar: str


class UserUpdate(User):
    pass


class UserOut(BaseModel):
    id: int
    vk_id: int
    first_name: str
    last_name: str
    avatar: str


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    id_vk: Union[str, None] = None
    scopes: List[str] = []


class ItemIn(BaseModel):
    title: str
    description: str


class ItemOut(BaseModel):
    title: str
    description: str
    user: User


class GetItem(BaseModel):
    user: User
    title: str
    description: str
