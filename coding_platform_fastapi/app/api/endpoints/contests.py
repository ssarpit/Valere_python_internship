# app/api/endpoints/contests.py
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List

from app.crud import crud_contest
from app.schemas.contest import Contest, ContestCreate
from app.db import models
from app.api import deps

router = APIRouter()

@router.post("/", response_model=Contest, status_code=status.HTTP_201_CREATED)
def create_contest(
    contest: ContestCreate,
    db: Session = Depends(deps.get_db),
    current_user: models.User = Depends(deps.get_current_admin_user),
):
    return crud_contest.create_contest(db=db, contest=contest, user_id=current_user.id)

@router.get("/", response_model=List[Contest])
def read_contests(
    skip: int = 0, limit: int = 10, db: Session = Depends(deps.get_db),
    current_user: models.User = Depends(deps.get_current_user)
):
    return crud_contest.get_contests(db, skip=skip, limit=limit)

@router.get("/{contest_id}", response_model=Contest)
def read_contest(
    contest_id: int, db: Session = Depends(deps.get_db),
    current_user: models.User = Depends(deps.get_current_user)
):
    db_contest = crud_contest.get_contest(db, contest_id=contest_id)
    if db_contest is None:
        raise HTTPException(status_code=404, detail="Contest not found")
    return db_contest