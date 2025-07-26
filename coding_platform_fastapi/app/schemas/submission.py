# app/schemas/submission.py
from pydantic import BaseModel
from datetime import datetime
from typing import List, Optional

class SubmissionBase(BaseModel):
    code: str
    language: str = "python"

class SubmissionCreate(SubmissionBase):
    challenge_id: int

class SubmissionResultDetail(BaseModel):
    test_case: int
    status: str
    output: str
    expected: str

class Submission(SubmissionBase):
    id: int
    user_id: int
    challenge_id: int
    contest_id: Optional[int]
    status: str
    execution_time: Optional[float]
    score: int
    submitted_at: datetime

    class Config:
        from_attributes = True

class SubmissionResult(Submission):
    details: Optional[List[SubmissionResultDetail]] = None