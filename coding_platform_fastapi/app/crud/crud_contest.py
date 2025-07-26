# app/crud/crud_contest.py
from sqlalchemy.orm import Session
from ..db import models
from ..schemas import contest as contest_schema

def get_contest(db: Session, contest_id: int):
    return db.query(models.Contest).filter(models.Contest.id == contest_id).first()

def get_contests(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Contest).offset(skip).limit(limit).all()

def create_contest(db: Session, contest: contest_schema.ContestCreate, user_id: int):
    db_contest = models.Contest(**contest.dict(), created_by_id=user_id)
    db.add(db_contest)
    db.commit()
    db.refresh(db_contest)
    return db_contest