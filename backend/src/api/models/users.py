from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.orm import relationship

from models.base import Base

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    username = Column(String, unique=True, index=True)
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String)
    name = Column(String)
    is_admin = Column(Boolean, index=True, default=False)
    is_active = Column(Boolean, index=True, default=False)
    confirmation_token = Column(String, nullable=True)

    todos = relationship("Todo", back_populates="owner", cascade="all, delete-orphan")