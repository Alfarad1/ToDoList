from pydantic import BaseModel

class User(BaseModel):
    id: int
    name: str
    email: str
    pass_hash: str


class Todolist(BaseModel):
    id: int
    user_id: int
    title: str

class Task(BaseModel):
    id: int
    name: str
    text: str
    completed: bool
    list_id: int
