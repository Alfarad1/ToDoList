from schemas.todos import TodoBase, TodoFilter, TodoCreate, TodoRead, TodoUpdate
from models.todos import Todo
import crud.todos
from sqlalchemy.orm import Session

from fastapi import HTTPException

def _get_todo(todo_id: int, current_user_id: int, is_admin:bool, db: Session) -> Todo:
    filters = TodoFilter(id=todo_id)
    if not is_admin:
        filters.owner_id = current_user_id
    
    todo = crud.todos.filter_todos(filters, db)
    if not todo:
        raise HTTPException(status_code=404,
                            detail="Todo not found.")
    return todo[0]

def get_todos_for_user(current_user_id: int, db: Session) -> list[TodoBase] | None:
    filters = TodoFilter(owner_id=current_user_id) 
    return crud.todos.filter_todos(filters, db)

def get_todo(todo_id: int, current_user_id: int, is_admin:bool, db: Session) -> TodoRead:
    return _get_todo(todo_id, current_user_id, is_admin, db)

def create_todo(todo: TodoCreate, current_user_id: int, db: Session) -> TodoRead:
    new_todo = Todo(title=todo.title,
                    description=todo.description,
                    is_completed=False,
                    owner_id=current_user_id)
    return crud.todos.create_todo(new_todo, db)

def delete_todo(todo_id: int, current_user_id: int, is_admin:bool, db: Session) -> None:
    return crud.todos.delete_todo(_get_todo(todo_id, current_user_id, is_admin, db), db)

def update_todo(todo_id: int, todo_new_data: TodoUpdate, is_admin: bool, current_user_id: int, db: Session) -> TodoRead:
    db_todo = _get_todo(todo_id, current_user_id, is_admin, db)
    if not db_todo:
        raise HTTPException(status_code=404, detail="Todo not found")
    
    if todo_new_data.title:
        db_todo.title = todo_new_data.title

    if todo_new_data.description:
        db_todo.description = todo_new_data.description

    if not todo_new_data.is_completed == None:
        db_todo.is_completed = todo_new_data.is_completed

    return crud.todos.update_todo(db_todo, db)