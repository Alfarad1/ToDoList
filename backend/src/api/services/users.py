from schemas.users import UserBase, UserCreate, UserRead, UserFilter, UserUpdate
import crud.users
from sqlalchemy.orm import Session

from fastapi import HTTPException

from core.security import hash_password
from core.celery import send_confirmation_email
import uuid

def get_all_users(db : Session) -> list[UserBase] | None:  
    return crud.users.get_all_users(db)

def get_user(user_id: int, db : Session) -> UserBase | None:
    user = crud.users.get_user(user_id, db)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user

def create_user(user: UserCreate, db : Session) -> UserBase | None:
    existing_user = crud.users.filter_users(UserFilter(email=user.email), db)
    if existing_user:
        raise HTTPException(
            status_code=400,
            detail="Email is already in use by another user."
        )
    
    existing_user = crud.users.filter_users(UserFilter(username=user.username), db)
    if existing_user:
        raise HTTPException(
            status_code=400,
            detail="Username is already in use by another user."
        )

    user.hashed_password = hash_password(user.password)

    confirmation_token = str(uuid.uuid4())
    user.confirmation_token = confirmation_token
    send_confirmation_email(user.email, user.username, user.id, confirmation_token)
    crud.users.create_user(user, db)

    return 
def delete_user(user_id: int, db : Session) -> None:
    user = crud.users.get_user(user_id, db)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return crud.users.delete_user(user, db)

def update_user(user_id: int, user_new_data: UserUpdate, db : Session) -> UserBase | None:
    db_user = crud.users.get_user(user_id, db)
    if not db_user:
        raise HTTPException(status_code=404, detail="User not found")
    
    if user_new_data.email:
        existing_user = crud.users.filter_users(UserFilter(email=user_new_data.email), db)
        if existing_user and existing_user.id != user_id:
            raise HTTPException(
                status_code=400,
                detail="Email is already in use by another user."
            )
        db_user.email = user_new_data.email

    if user_new_data.name:
        db_user.name = user_new_data.name

    if user_new_data.password:
        db_user.hashed_password = hash_password(user_new_data.password)

    return crud.users.update_user(db_user, db)
        
def confirm_email(user_id: int, confirmation_token:str, db : Session):
    user = crud.users.filter_one_user(UserFilter(id=user_id), db)
    if not user:
        raise HTTPException(status_code=404, detail="User not found.")
    if user.is_active:
        raise HTTPException(status_code=400, detail="User is already activated.")
    if user.confirmation_token != confirmation_token:
        raise HTTPException(status_code=400, detail="Invalid token.")
    user.is_active = True
    user.confirmation_token = None
    db.commit()
    return {"message": "Email confirmed."}