# from typing import Union, List
from pydantic import BaseModel
#
#
class User(BaseModel):
    user_id: str
    first_name: str
    last_name: str


class UserCreate(BaseModel):
    user_id: int
    first_name: str
    last_name: str
    avatar: str


# class UserUpdate(User):
#     pass
#
#
# class UserOut(BaseModel):
#     user_id: int
#     first_name: str
#     last_name: str
#     avatar: str
#
#
# class Token(BaseModel):
#     access_token: str
#     token_type: str
#
#
# class TokenData(BaseModel):
#     id_vk: Union[str, None] = None
#     scopes: List[str] = []
#
#