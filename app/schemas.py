from pydantic import BaseModel, EmailStr


class User(BaseModel):
    vk_id: str
    email: EmailStr
    avatar: str


class UserCreate(User):
    token: str


class UserUpdate(User):
    pass


class UserOut(BaseModel):
    id: int
    vk_id: int
    first_name: str
    last_name: str
    avatar: str


class Token(BaseModel):
    id: int
    token: str
