from fastapi import APIRouter, Depends

from dependencies import get_db, get_current_user, admin_required
from sqlalchemy.orm import Session

from services.users import *

from schemas.users import UserCreate, UserBase, UserRead, UserUpdate
from models.users import User

router = APIRouter(prefix="/users",
                   tags=["users"])

@router.get("/", response_model=list[UserRead], dependencies=[Depends(admin_required)])
def get_all(db: Session = Depends(get_db)):
    return get_all_users(db)

@router.get("/me", response_model=UserRead)
def read_current_user(current_user: User = Depends(get_current_user)):
    return current_user

@router.get("/{user_id}", response_model=UserRead)
def get_one(user_id: int, db: Session = Depends(get_db)) -> UserBase | None:
    return get_user(user_id, db)

@router.post("/", status_code=201, response_model=UserRead)
def create(user: UserCreate, db: Session = Depends(get_db)):
    return create_user(user, db)

@router.delete("/{user_id}", status_code=204)
def delete(user_id: int, db: Session = Depends(get_db)):
    return delete_user(user_id, db)

@router.put("/{user_id}", response_model=UserRead)
def update(user_id: int, user: UserUpdate, db: Session = Depends(get_db)):
    return update_user(user_id, user, db)

