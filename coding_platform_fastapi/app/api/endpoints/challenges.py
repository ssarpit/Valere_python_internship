# app/api/endpoints/challenges.py
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.crud import crud_challenge, crud_contest
from app.schemas.challenge import Challenge, ChallengeCreate
from app.db import models
from app.api import deps

router = APIRouter()

@router.post("/", response_model=Challenge, status_code=status.HTTP_201_CREATED)
def create_challenge_for_contest(
    contest_id: int,
    challenge: ChallengeCreate,
    db: Session = Depends(deps.get_db),
    current_user: models.User = Depends(deps.get_current_admin_user),
):
    contest = crud_contest.get_contest(db, contest_id)
    if not contest:
        raise HTTPException(status_code=404, detail="Contest not found")
    return crud_challenge.create_contest_challenge(db=db, challenge=challenge, contest_id=contest_id)

@router.get("/{challenge_id}", response_model=Challenge)
def read_challenge(
    challenge_id: int,
    db: Session = Depends(deps.get_db),
    current_user: models.User = Depends(deps.get_current_user)
):
    challenge = db.query(models.Challenge).filter(models.Challenge.id == challenge_id).first()
    if not challenge:
        raise HTTPException(status_code=404, detail="Challenge not found")
    return challenge