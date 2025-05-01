from sqlalchemy.orm import Session
from models.todos import Todo
from schemas.todos import TodoBase, TodoFilter, TodoCreate


def filter_todos(filters: TodoFilter, db: Session) -> list[Todo] | None:
    query = db.query(Todo)

    if filters.id:
        query = query.filter(Todo.id == filters.id)
    if filters.owner_id:
        query = query.filter(Todo.owner_id == filters.owner_id)
    if filters.is_completed:
        query = query.filter(Todo.is_completed == filters.is_completed)
    return query.all()

def create_todo(todo: Todo, db: Session) -> TodoBase:
    db.add(todo)
    db.commit()
    db.refresh(todo)
    return todo

def delete_todo(todo: Todo, db: Session) -> None:
    db.delete(todo)
    db.commit()
    return None

def update_todo(todo: Todo, db: Session) -> TodoBase:
    db.commit()
    db.refresh(todo)
    return todo