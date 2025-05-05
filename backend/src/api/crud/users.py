from sqlalchemy.orm import Session
from models.users import User
from schemas.users import UserCreate, UserBase, UserRead, UserUpdate, UserFilter


def get_all_users(db : Session) -> list[UserBase] | None:
    return db.query(User).all()

def get_user(user_id: int, db : Session) -> UserBase | None:
    return db.query(User).filter(User.id == user_id).first()

def filter_users(filters: UserFilter, db: Session) -> list[User]:
    query = db.query(User)

    if filters.email:
        query = query.filter(User.email == filters.email)
    if filters.username:
        query = query.filter(User.username == filters.username)
    if filters.name:
        query = query.filter(User.name.ilike(f"%{filters.name}%"))
    if filters.is_admin is not None:
        query = query.filter(User.is_admin == filters.is_admin)
    if filters.confirmation_token:
        query = query.filter(User.confirmation_token == filters.confirmation_token)
    if filters.is_active:
        query = query.filter(User.is_active == filters.is_active)
    return query.all()

def filter_one_user(filters: UserFilter, db: Session) -> User | None:
    users = filter_users(filters, db)
    return users[0]

def create_user(user: UserCreate, db : Session) -> UserBase | None:
    new_user =  User(
        username=user.username,
        email=user.email,
        hashed_password=user.hashed_password,
        name=user.name,
        is_admin=False
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

def delete_user(user: User, db : Session) -> None:
    db.delete(user)
    db.commit()
    return None

def update_user(user: User, db: Session) -> UserBase:
    db.commit()
    db.refresh(user)
    return user