from fastapi import FastAPI
from fastapi.exceptions import RequestValidationError
from sqlalchemy.exc import IntegrityError
import uvicorn
from core.exceptions import (
    validation_exception_handler,
    db_exception_handler,
    generic_exception_handler,
)


from routes import users, todos, tasks, auth

app = FastAPI()
app.include_router(users.router)
app.include_router(todos.router)
# app.include_router(tasks.router)
app.include_router(auth.router)

# Register handlers
app.add_exception_handler(RequestValidationError, validation_exception_handler)
app.add_exception_handler(IntegrityError, db_exception_handler)
app.add_exception_handler(Exception, generic_exception_handler)

from sqladmin import Admin, ModelView
from models.users import User
from core.database import engine

admin = Admin(app, engine)

class UserAdmin(ModelView, model=User):
    column_list = [User.id, User.username, User.email, User.is_admin]

admin.add_view(UserAdmin)

from fastapi.middleware.cors import CORSMiddleware

origins = [
    "http://localhost:5173",  # Vite's default dev server
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,  
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def home():
    return "Hello!"

if __name__ == "__main__":
    uvicorn.run("main:app", reload=True)
