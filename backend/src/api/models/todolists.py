from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.ext.declarative import declarative_base

from models.base import Base

class ToDoList(Base):
    __tablename__ = 'todolists'

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer)
    username = Column(String, unique=True, index=True)
    email = Column(String, unique=True, index=True)
    title = Column(String)
    hashed_password = Column(String)
