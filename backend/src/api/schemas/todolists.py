from pydantic import BaseModel

class ToDoList(BaseModel):
    id: int
    user_id: int
    title: str

    class Config:
        orm_mode = True