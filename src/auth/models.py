import datetime
import ormar
from database import database, metadata


class User(ormar.Model):
    class Meta:
        tablename = "user"
        database = database
        metadata = metadata

    id: int = ormar.Integer(unique=True, primary_key=True)
    user_id: int = ormar.Integer(unique=True)
    first_name: str = ormar.String(max_length=50)
    last_name: str = ormar.String(max_length=50)
    avatar: str = ormar.String(max_length=350, nullable=True)
    disabled = ormar.Boolean(default=False, nullable=False)


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
