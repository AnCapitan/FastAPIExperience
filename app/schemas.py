from pydantic import BaseModel


class UserIn(BaseModel):
    username: str


class UserBase(BaseModel):
    user_id: int
    username: str


class NoteIn(BaseModel):
    text: str
    completed: bool
    user_id: int


class NoteBase(BaseModel):
    id: int
    text: str
    completed: bool
    user_id: int

# class ItemBase(BaseModel):
#     title: str
#     description: str | None = None
#
#
# class ItemCreate(ItemBase):
#     pass
#
#
# class Item(ItemBase):
#     id: int
#     owner_id: int
#
#     class Config:
#         orm_mode = True
#
#
# class UserRead(schemas.BaseUser[uuid.UUID]):
#     items: list[Item] = []
#
#     class Config:
#         orm_mode = True
#
#
# class UserCreate(schemas.BaseUserCreate):
#     pass
#
#
# class UserUpdate(schemas.BaseUserUpdate):
#     pass
