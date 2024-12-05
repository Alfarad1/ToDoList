from fastapi import FastAPI
import uvicorn

from routes import users, todolists, tasks

app = FastAPI()
app.include_router(users.router)
app.include_router(todolists.router)
app.include_router(tasks.router)

@app.get("/")
async def home():
    return "Hello!"

if __name__ == "__main__":
    uvicorn.run("main:app", reload=True)