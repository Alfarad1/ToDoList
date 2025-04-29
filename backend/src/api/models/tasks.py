from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.ext.declarative import declarative_base

from models.base import Base

class Task(Base):
    __tablename__ = 'tasks'

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    text = Column(String)
    completed = Column(Boolean, default=False)
    todolist_id = Column(Integer)