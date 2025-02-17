from fastapi import APIRouter

from model import Todolist

import service

router = APIRouter(prefix="/todolists")

@router.get("/")
def get_all_for_user(userID: int) -> list[Todolist]:
    return service.get_todolists_for_user(userID)

@router.get("/{todolist_id}")
def get_todolist(todolist_id: int) -> Todolist | None:
    return service.get_todolist(todolist_id)

@router.post("/", status_code=201)
def create(todolist: Todolist):
    return service.create_todolist(todolist)