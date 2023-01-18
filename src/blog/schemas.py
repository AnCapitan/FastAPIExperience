from datetime import datetime
from pydantic import BaseModel


class ItemOut(BaseModel):
    name: str
    description: str



class ItemCreate(BaseModel):
    name: str
    description: str
