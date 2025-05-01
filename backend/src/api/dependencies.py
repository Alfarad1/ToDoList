from sqlalchemy.orm import Session
from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from jose import JWTError
from core.security import decode_access_token
from core.database import SessionLocal
from models.users import User


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close_all()

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")

def get_current_user(token: str = Depends(oauth2_scheme), db: Session = Depends(get_db)) -> User:
    try:
        payload = decode_access_token(token)
        username: str = payload.get("sub")
        if username is None:
            raise HTTPException(status_code=401, detail="Invalid token")
    except JWTError:
        raise HTTPException(status_code=401, detail="Invalid token")

    user: User = db.query(User).filter(User.username == username).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    return user

def current_user_id(current_user: User = Depends(get_current_user)) -> int:
    return current_user.id

def admin_required(current_user: User = Depends(get_current_user)) -> None:
    if not current_user.is_admin:
        raise HTTPException(status_code=403, detail="Not authorized")
    return None

def is_admin(current_user: User = Depends(get_current_user)) -> bool:
    if current_user.is_admin:
        return True
    return False