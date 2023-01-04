import uvicorn
from fastapi import FastAPI
from starlette.staticfiles import StaticFiles
from starlette.templating import Jinja2Templates

from app import models
from database import engine, SessionLocal
from app.api import *

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

app.mount("/static", StaticFiles(directory="frontend/static"), name="static")
templates = Jinja2Templates(directory="frontend/templates")


# def get_db():
#     db = SessionLocal()
#     try:
#         yield db
#     finally:
#         db.close()


app.include_router(app_router)
if __name__ == '__main__':
    uvicorn.run("main:app", host="127.0.0.1", log_level="info", reload=True, port=8080)
