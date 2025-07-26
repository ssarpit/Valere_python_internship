# app/api/endpoints/submissions.py
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.crud import crud_submission
from app.schemas.submission import SubmissionCreate, SubmissionResult
from app.db import models
from app.services import code_executor, leaderboard_manager
from app.api import deps

router = APIRouter()

@router.post("/", response_model=SubmissionResult, status_code=status.HTTP_201_CREATED)
async def submit_code(
    submission: SubmissionCreate,
    db: Session = Depends(deps.get_db),
    current_user: models.User = Depends(deps.get_current_user),
):
    challenge = db.query(models.Challenge).filter(models.Challenge.id == submission.challenge_id).first()
    if not challenge:
        raise HTTPException(status_code=404, detail="Challenge not found")
    if not challenge.contest_id:
        raise HTTPException(status_code=400, detail="This challenge is not part of a contest")

    db_submission = crud_submission.create_submission(
        db=db, submission=submission, user_id=current_user.id, contest_id=challenge.contest_id
    )
    test_cases = [(tc.input, tc.expected_output) for tc in challenge.test_cases]
    result = code_executor.execute_python_code(submission.code, test_cases)
    updated_submission = crud_submission.update_submission_result(
        db=db, submission_id=db_submission.id, result=result
    )
    crud_submission.update_contest_participation_score(
        db=db, user_id=current_user.id, contest_id=challenge.contest_id
    )
    leaderboard_data = crud_submission.get_leaderboard(db, contest_id=challenge.contest_id)
    leaderboard_json = [
        {"username": p.user.username, "score": p.total_score, "time_seconds": round(p.total_time_seconds, 2)}
        for p in leaderboard_data
    ]
    await leaderboard_manager.manager.broadcast({"leaderboard": leaderboard_json}, challenge.contest_id)
    result_schema = SubmissionResult.from_orm(updated_submission)
    result_schema.details = result['details']
    return result_schema