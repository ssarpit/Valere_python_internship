# app/crud/crud_submission.py
from sqlalchemy.orm import Session
from sqlalchemy import func
from app.db import models
from app.schemas import submission as submission_schema

def create_submission(db: Session, submission: submission_schema.SubmissionCreate, user_id: int, contest_id: int):
    db_submission = models.Submission(
        code=submission.code,
        language=submission.language,
        challenge_id=submission.challenge_id,
        user_id=user_id,
        contest_id=contest_id
    )
    db.add(db_submission)
    db.commit()
    db.refresh(db_submission)
    return db_submission

def update_submission_result(db: Session, submission_id: int, result: dict):
    db_submission = db.query(models.Submission).filter(models.Submission.id == submission_id).first()
    if db_submission:
        db_submission.status = result["status"]
        db_submission.execution_time = result["execution_time"]
        db_submission.score = result["score"]
        db.commit()
        db.refresh(db_submission)
    return db_submission

def update_contest_participation_score(db: Session, user_id: int, contest_id: int):
    participation = db.query(models.ContestParticipation).filter(
        models.ContestParticipation.user_id == user_id,
        models.ContestParticipation.contest_id == contest_id
    ).first()

    if not participation:
        participation = models.ContestParticipation(user_id=user_id, contest_id=contest_id)
        db.add(participation)
        db.commit()
        db.refresh(participation)

    subquery = db.query(
        models.Submission.challenge_id,
        func.max(models.Submission.score).label('max_score')
    ).filter(
        models.Submission.user_id == user_id,
        models.Submission.contest_id == contest_id
    ).group_by(models.Submission.challenge_id).subquery()

    total_score = db.query(func.sum(subquery.c.max_score)).scalar() or 0
    
    last_submission = db.query(models.Submission).filter(
        models.Submission.user_id == user_id,
        models.Submission.contest_id == contest_id
    ).order_by(models.Submission.submitted_at.desc()).first()
    
    if last_submission and participation.contest:
        time_diff = last_submission.submitted_at - participation.contest.start_time
        participation.total_time_seconds = time_diff.total_seconds()

    participation.total_score = total_score
    db.commit()
    db.refresh(participation)
    return participation

def get_leaderboard(db: Session, contest_id: int):
    return db.query(models.ContestParticipation).filter(
        models.ContestParticipation.contest_id == contest_id
    ).order_by(
        models.ContestParticipation.total_score.desc(),
        models.ContestParticipation.total_time_seconds.asc()
    ).all()