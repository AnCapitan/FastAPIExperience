from typing import List
from fastapi import APIRouter
from database import database
from .models import note, user
from .schemas import NoteBase, NoteIn, UserBase, UserIn

app_router = APIRouter()


# @app_router.post("/users/{user_id}/items/", response_model=schemas.Item)
# def create_item_for_user(user_id: int, item: schemas.ItemCreate, db: Session = Depends(get_db)):
#     return crud.create_user_item(db=db, item=item, user_id=user_id)
#
#
# @app_router.get("/items/", response_model=List[schemas.Item], )
# def read_items(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
#     items = crud.get_items(db, skip=skip, limit=limit)
#     return items
#
#
# @app_router.post("/users/", response_model=schemas.User)
# def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
#     db_user = crud.get_user_by_username(db, username=user.username)
#     if db_user:
#         raise HTTPException(status_code=400, detail="Email already registered")
#     return crud.create_user(db=db, user=user)
#
#


# @app_router.get("/users/{user_id}", response_model=schemas.User)
# def read_user(user_id: int, db: Session = Depends(get_db)):
#     db_user = crud.get_user(db, user_id=user_id)
#     if db_user is None:
#         raise HTTPException(status_code=404, detail="User not found")
#     return db_user

@app_router.get("/notes/", response_model=List[NoteBase])
async def read_notes():
    query = note.select()
    return await database.fetch_all(query)

@app_router.get("/user/", response_model=List[UserBase])
async def read_notes():
    query = user.select()
    print(query)
    print('***************************')
    print(user.select())
    return await database.fetch_one(query)

@app_router.post("/notes/", response_model=NoteBase)
async def create_note(note_in: NoteIn):
    query = note.insert().values(text=note_in.text, completed=note_in.completed, user_id=1)
    last_record_id = await database.execute(query)
    return {**note.dict(), "id": last_record_id}
