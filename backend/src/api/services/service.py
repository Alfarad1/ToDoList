from schemas.users import UserBase, UserCreate, UserRead
# , Task, ToDoList
# import fake as data
import crud.data as data
import crud.users
from sqlalchemy.orm import Session


def get_all_users(db: Session) -> list[UserBase]:
    return crud.users.get_all_users(db)

def get_user(user_id: int) -> UserBase | None:
    return data.get_user(user_id)

# def create_user(user: UserCreate) -> User:
#     return data.create_user(user)

# def delete_user(user_id: int) -> None:
#     return data.delete_user(user_id)

# def get_tasks_for_todolist(list_id: int) -> list[Task]:
#     return data.get_tasks_for_todolist(list_id)

# def create_task(task: Task) -> Task:
#     return data.create_task(task)

# def modify_task(task: Task) -> Task | None:
#     return data.modify_task(task)
        
# def delete_task(task_id: int) -> None:
#     return data.delete_task(task_id)

# def get_todolists_for_user(user_id: int) -> list[ToDoList]:
#     return data.get_todolists_for_user(user_id)

# def get_todolist(user_id:int, todolist_id: int) -> ToDoList | None:
#     return data.get_todolist(user_id, todolist_id)

# def create_todolist(todolist: ToDoList) -> ToDoList:
#     return data.create_todolist(todolist)

# def get_tasks_for_user(list_id: int) -> list[Task]:
#     return data.get_tasks_for_user(list_id)

# def create_task(task: Task) -> Task:
#     return data.create_task(task)

# def modify_task(task: Task) -> Task | None:
#     return data.modify_task(task)

# def delete_task(task_id: int) -> None:
#     return data.delete_task(task_id)