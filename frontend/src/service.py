from model import User, Task, Todolist
import fake as data

def get_all_users() -> list[User]:
    return data.get_all_users()

def get_user(name: str) -> User | None:
    return data.get_user(name)

def create_user(user: User) -> User:
    return data.create_user(user)

def delete_user(user_id: int) -> None:
    return data.delete_user(user_id)

def get_tasks_for_user(list_id: int) -> list[Task]:
    return data.get_tasks_for_user(list_id)


def create_task(task: Task) -> Task:
    return data.create_task(task)

def modify_task(task: Task) -> Task | None:
    return data.modify_task(task)
        
def delete_task(task_id: int) -> None:
    return data.delete_task(task_id)

def create_todolist(todolist: Todolist) -> Todolist:
    return data.create_todolist(todolist)