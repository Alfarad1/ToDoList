from fastapi import FastAPI
from fastapi.exceptions import RequestValidationError
from sqlalchemy.exc import IntegrityError
import uvicorn
from core.exceptions import (
    validation_exception_handler,
    db_exception_handler,
    generic_exception_handler,
)


from routes import users, todolists, tasks, auth

app = FastAPI()
app.include_router(users.router)
app.include_router(todolists.router)
app.include_router(tasks.router)
app.include_router(auth.router)

# Register handlers
app.add_exception_handler(RequestValidationError, validation_exception_handler)
app.add_exception_handler(IntegrityError, db_exception_handler)
app.add_exception_handler(Exception, generic_exception_handler)

@app.get("/")
async def home():
    return "Hello!"

if __name__ == "__main__":
    uvicorn.run("main:app", reload=True)