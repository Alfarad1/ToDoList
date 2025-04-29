from fastapi import APIRouter

from models.todolists import ToDoList

# import backend.src.api.services.service as service

router = APIRouter(prefix="/todolists")

# @router.get("/")
# def get_all_for_user(userID: int) -> list[ToDoList]:
#     return service.get_todolists_for_user(userID)

# @router.get("/{todolist_id}")
# def get_todolist(todolist_id: int) -> ToDoList | None:
#     return service.get_todolist(todolist_id)

# @router.post("/", status_code=201)
# def create(todolist: ToDoList):
#     return service.create_todolist(todolist)