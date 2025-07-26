# SQLAlchemy/services.py
from db import SessionLocal
from fastapi import HTTPException
from sqlalchemy.orm import Session
from model import User

def create_user(db: Session, name: str, email: str):
    # Check if email already exists
    existing_user = db.query(User).filter(User.email == email).first()
    if existing_user:
        raise HTTPException(status_code=400, detail="Email already registered")

    user = User(name=name, email=email)
    db.add(user)
    db.commit()
    db.refresh(user)
    return user
def get_users(db: Session):
    return db.query(User).all()

def get_user_by_id(db: Session, user_id: int):
    return db.query(User).filter(User.id == user_id).first()

def delete_data(user_id:int):
   with SessionLocal() as session:
      user=session.get(User,user_id)
      if user:
         session.delete(user)
         session.commit()

def delete_all_users():
    db = SessionLocal()
    try:
        db.query(User).delete()   # This deletes all rows
        db.commit()
    finally:
        db.close()