from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.orm import Session
from jose import JWTError, jwt
from pydantic import ValidationError
from app.db.database import SessionLocal
from app.db import models
from app.core.config import settings
from app.schemas import token as token_schema
from app.crud import crud_user

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/auth/login")

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

def get_current_user(db: Session = Depends(get_db), token: str = Depends(oauth2_scheme)):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(token, settings.SECRET_KEY, algorithms=[settings.ALGORITHM])
        username: str = payload.get("sub")
        if username is None:
            raise credentials_exception
        token_data = token_schema.TokenData(username=username)
    except (JWTError, ValidationError):
        raise credentials_exception
    user = crud_user.get_user_by_username(db, username=token_data.username)
    if user is None:
        raise credentials_exception
    return user

def get_current_admin_user(current_user: models.User = Depends(get_current_user)):
    if current_user.role != "admin":
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="The user doesn't have enough privileges"
        )
    return current_user