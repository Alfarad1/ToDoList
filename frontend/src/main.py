from fastapi import FastAPI
import uvicorn

from routes import users

app = FastAPI()
app.include_router(users.router)

@app.get("/")
async def home():
    return "Hello!"

if __name__ == "__main__":
    uvicorn.run("main:app", reload=True)