from model import User, Task, Todolist

_users = [User(id=0, 
               name="George", 
               email="test1@test.com", 
               pass_hash="aaabbb"),
          User(id=1, 
               name="Lisa", 
               email="test2@test.com", 
               pass_hash="bbbccc")]

_todolists = [Todolist(id=0,
                       title="The list", 
                       user_id=0),
              Todolist(id=1,
                       title="", 
                       user_id=1)]

_tasks = [Task(id=0,
               list_id=0, 
               name="Task 1", 
               text="Do stuff", 
               completed=True),
          Task(id=1,
               list_id=0, 
               name="Task 2", 
               text="Do more stuff", 
               completed=False),
          Task(id=2,
               list_id=1, 
               name="My Task 1", 
               text="Do this", 
               completed=True),
          Task(id=3,
               list_id=1, 
               name="My Task 2", 
               text="Do that", 
               completed=False)]

def get_all_users() -> list[User]:
    """Возврат всех пользователей"""
    return _users

def get_user(name: str) -> User | None:
    """Возвращает одного пользователя по имени, либо ничего, если он не был найден."""
    for _user in _users:
        if _user.name == name:
            return _user
    return None

def create_user(user: User) -> User:
    """Создает нового пользователя, либо ничего, если пользователь с таким именем уже есть."""
    for _user in _users:
        if user.name == _user.name:
            return
    _users.append(user)
    return user

def delete_user(user_id: int) -> None:
    """Удаляет пользователя по id."""
    for _user in _users:
        if user_id == _user.id:
            _users.remove(_user)

def get_tasks_for_user(list_id: int) -> list[Task]:
    """Возвращает список задач для списка с указанным id."""
    res = []
    for _task in _tasks:
        if _task.list_id == list_id:
            res.append(_task)
    return res


def create_task(task: Task) -> Task:
    """Создает задачу."""
    _tasks.append(task)
    return task

def modify_task(task: Task) -> Task | None:
    """Редактирует задачу, если задача с таким id есть в списке, иначе не делает ничего."""
    for _task in _tasks:
        if _task.id == task.id:
            _tasks[task.id] = task
            return _task[task.id]
        
def delete_task(task_id: int) -> None:
    """Удаляет задачу, если задача с таким id есть в списке, иначе не делает ничего."""
    for _task in _tasks:
        if _task.id == task_id:
            _tasks.remove(_task)


def create_todolist(todolist: Todolist) -> Todolist:
    """Создает список задач."""
    _todolists.append(todolist)
    return todolist

    