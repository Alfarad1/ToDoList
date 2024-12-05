from fastapi import APIRouter

from model import Todolist

import service

router = APIRouter(prefix="/todolists")

@router.get("/")
def get_all_for_user(user_id: int) -> list[Todolist]:
    return service.get_todolists_for_user(user_id)

@router.post("/", status_code=201)
def create(todolist: Todolist):
    return service.create_todolist(todolist)