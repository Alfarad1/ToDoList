# from fastapi import APIRouter, Depends

# from dependencies import get_db, get_current_user, admin_required
# from sqlalchemy.orm import Session

# from services.tasks import *

# from schemas.tasks import Task
# from models.tasks import Task

# # import backend.src.api.services.service as service

# router = APIRouter(prefix="/tasks")

# # @router.get("/")
# # def get_tasks(todolistID: int) -> list[Task]:
# #     return service.get_tasks_for_todolist(todolistID)

# # @router.post("/", status_code=201)
# # def create(task: Task):
# #     return service.create_task(task)

# # @router.put("/")
# # def modify(task: Task):
# #     return service.modify_task(task)

# # @router.delete("/{task_id}")
# # def modify(task_id: int):
# #     return service.delete_task(task_id)