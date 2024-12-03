from fastapi import APIRouter

from model import User

import service

router = APIRouter(prefix="/users")

@router.get("/")
def get_all():
    return service.get_all_users()

@router.get("/{user_id}")
def get_one(user_id: int) -> User:
    return service.get_user(user_id)

@router.post("/", status_code=201)
def create(user: User):
    return service.create_user(user)

@router.delete("/{user_id}")
def delete(user_id: int):
    return service.delete_user(user_id)