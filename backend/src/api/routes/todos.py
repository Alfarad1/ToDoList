from fastapi import APIRouter, Depends

from dependencies import get_db, get_current_user, admin_required, current_user_id, is_admin
from sqlalchemy.orm import Session
from schemas.todos import TodoBase, TodoRead, TodoCreate, TodoUpdate
from models.todos import Todo
import services.todos

router = APIRouter(prefix="/todos",
                   tags=["todos"])

@router.get("/", response_model=list[TodoRead])
def get_all_for_user(db: Session = Depends(get_db), current_user_id: int = Depends(current_user_id)) -> list[TodoBase]:
    return services.todos.get_todos_for_user(current_user_id, db)

@router.get("/{todo_id}")
def get_todo(todo_id: int, db: Session = Depends(get_db), current_user_id: int = Depends(current_user_id), is_admin: bool = Depends(is_admin)) -> TodoRead:
    return services.todos.get_todo(todo_id, current_user_id, is_admin, db)

@router.post("/", status_code=201)
def create_todo(todo: TodoCreate, db: Session = Depends(get_db), current_user_id: int = Depends(current_user_id)) -> TodoRead:
    return services.todos.create_todo(todo, current_user_id, db)

@router.delete("/{todo_id}", status_code=204)
def delete(todo_id: int, db: Session = Depends(get_db), current_user_id: int = Depends(current_user_id), is_admin: bool = Depends(is_admin)):
    return services.todos.delete_todo(todo_id, current_user_id, is_admin, db)

@router.put("/{todo_id}", response_model=TodoRead)
def update(todo_id: int, todo: TodoUpdate, current_user_id: int = Depends(current_user_id), db: Session = Depends(get_db), is_admin: bool = Depends(is_admin)):
    return services.todos.update_todo(todo_id, todo, current_user_id, is_admin, db)