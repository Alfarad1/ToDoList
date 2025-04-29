from pydantic import BaseModel

class Task(BaseModel):
    id: int
    name: str
    text: str
    completed: bool
    list_id: int

    class Config:
        orm_mode = True