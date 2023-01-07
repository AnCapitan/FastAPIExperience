import datetime
import ormar
from db import database, metadata


class User(ormar.Model):
    class Meta:
        tablename = "user"
        database = database
        metadata = metadata

    id: int = ormar.Integer(primary_key=True, unique=True)
    vk_id: int = ormar.Integer(unique=True)
    first_name: str = ormar.String(max_length=50)
    last_name: str = ormar.String(max_length=50)
    email: str = ormar.String(index=True, unique=True, nullable=False, max_length=150)
    phone: str = ormar.String(max_length=11, unique=True, nullable=True)
    avatar: str = ormar.String(max_length=350, nullable=True)


class Item(ormar.Model):
    class Meta:
        tablename = "item"
        database = database
        metadata = metadata

    id: int = ormar.Integer(primary_key=True)
    title: str = ormar.String(max_length=100)
    description = ormar.String(max_length=500)
    created_at: datetime.datetime = ormar.DateTime(pydantic_only=True, default=datetime.datetime.now)
    user = ormar.ForeignKey(User)
