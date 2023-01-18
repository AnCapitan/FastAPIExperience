from fastapi import FastAPI
import uvicorn

from auth.router import auth_router
from blog.router import blog_router

app = FastAPI(
    title="Experience blog"
)
# app.include_router(
#     fastapi_users.get_auth_router(auth_backend),
#     prefix="/auth/jwt",
#     tags=["auth"],
# )
# app.include_router(
#     fastapi_users.get_register_router(UserRead, UserCreate),
#     prefix="/auth",
#     tags=["auth"],
# )

app.include_router(auth_router)
app.include_router(blog_router)

if __name__ == '__main__':
    uvicorn.run("main:app", host="localhost", port=8000, reload=True)