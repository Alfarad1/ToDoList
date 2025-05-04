from fastapi import APIRouter, Depends
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session

from dependencies import get_db

from schemas.token import Token, RefreshToken, AccessToken
import services.auth

router = APIRouter(prefix="/auth",
                   tags=["auth"])

@router.post("/login", response_model=Token)
def login(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    return services.auth.login(form_data, db)

@router.post("/refresh", response_model=AccessToken)
def refresh_token(request: RefreshToken):
    return services.auth.refresh(request)