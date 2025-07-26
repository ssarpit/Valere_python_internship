# app/schemas/challenge.py
from pydantic import BaseModel
from typing import List

class TestCaseBase(BaseModel):
    input: str
    expected_output: str
    is_hidden: bool = False

class TestCaseCreate(TestCaseBase):
    pass

class TestCase(TestCaseBase):
    id: int
    challenge_id: int

    class Config:
        from_attributes = True

class ChallengeBase(BaseModel):
    title: str
    description: str
    difficulty: str = "Easy"

class ChallengeCreate(ChallengeBase):
    test_cases: List[TestCaseCreate]

class Challenge(ChallengeBase):
    id: int
    contest_id: int
    test_cases: List[TestCase] = []

    class Config:
        from_attributes = True
