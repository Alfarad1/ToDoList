from pydantic import BaseModel
from typing import Optional

class TodoBase(BaseModel):
    title: str
    description: str
    is_completed: bool
    id: int

class TodoRead(BaseModel):
    title: str
    description: str
    is_completed: bool

class TodoUpdate(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None
    is_completed: Optional[bool] = None

class TodoCreate(BaseModel):
    title: str
    description: str

class TodoFilter(BaseModel):
    id: Optional[int] = None
    owner_id: Optional[int] = None
    is_completed: Optional[bool] = None

    class Config:
        orm_mode = True