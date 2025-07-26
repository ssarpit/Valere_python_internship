# SQLAlchemy/router.py
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from db import get_db
from services import create_user, get_users,get_user_by_id
from schemas import UserCreate, Userread

router = APIRouter()

@router.post("/user", response_model=Userread)
def create_user_route(user: UserCreate, db: Session = Depends(get_db)):
    db_user = create_user(db, user.name, user.email)
    return db_user

@router.get("/users", response_model=list[Userread])
def get_all_users_route(db: Session = Depends(get_db)):
    return get_users(db)

@router.get('/user/{user_id}',response_model=Userread)
def get_user_by_id_route(user_id:int,db:Session=Depends(get_db)):
    user = get_user_by_id(db,user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user