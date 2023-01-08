import uvicorn
from fastapi import FastAPI
from app.api import app_router, user_router
from app.auth import auth_router
from db import database, metadata, engine

app = FastAPI()



metadata.create_all(engine)
app.state.database = database


@app.on_event("startup")
async def startup() -> None:
    database_ = app.state.database
    if not database_.is_connected:
        await database_.connect()


@app.on_event("shutdown")
async def shutdown() -> None:
    database_ = app.state.database
    if database_.is_connected:
        await database_.disconnect()


app.include_router(auth_router)
app.include_router(app_router)
app.include_router(user_router)

if __name__ == '__main__':
    uvicorn.run("main:app", host="localhost", log_level="info", reload=True, port=8080)
