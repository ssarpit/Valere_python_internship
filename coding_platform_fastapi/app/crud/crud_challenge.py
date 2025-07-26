from sqlalchemy.orm import Session
from app.db import models
from app.schemas import challenge as challenge_schema

def create_contest_challenge(db: Session, challenge: challenge_schema.ChallengeCreate, contest_id: int):
    db_challenge = models.Challenge(
        title=challenge.title,
        description=challenge.description,
        difficulty=challenge.difficulty,
        contest_id=contest_id
    )
    db.add(db_challenge)
    db.commit()
    db.refresh(db_challenge)
    for tc_data in challenge.test_cases:
        db_tc = models.TestCase(**tc_data.dict(), challenge_id=db_challenge.id)
        db.add(db_tc)
    db.commit()
    db.refresh(db_challenge)
    return db_challenge