from pydantic import BaseModel, ConfigDict, EmailStr
from typing import Optional

class UserBase(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    username: str
    email: str
    name: str


class UserCreate(UserBase):
    model_config = ConfigDict(from_attributes=True)
    email: EmailStr
    username: str
    name: Optional[str] = None
    is_admin: bool = False
    password: str  # Notice: password is only for creating, not for returning
    hashed_password: str = None
    is_active: bool = False
    confirmation_token: str


class UserRead(UserBase):
    model_config = ConfigDict(from_attributes=True)
    id: int

class UserUpdate(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    username: Optional[str] = None
    email: Optional[EmailStr] = None
    password: Optional[str] = None
    name: Optional[str] = None
    is_admin: Optional[bool] = None
    is_active: Optional[bool] = None
    confirmation_token: Optional[str] = None

class UserFilter(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    id: Optional[int] = None
    email: Optional[EmailStr] = None
    username: Optional[str] = None
    name: Optional[str] = None
    is_admin: Optional[bool] = None
    is_active: Optional[bool] = None
    confirmation_token: Optional[str] = None