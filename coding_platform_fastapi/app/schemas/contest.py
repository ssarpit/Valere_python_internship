# app/schemas/contest.py
from pydantic import BaseModel
from datetime import datetime
from typing import List
from .challenge import Challenge

class ContestBase(BaseModel):
    title: str
    description: str
    start_time: datetime
    end_time: datetime

class ContestCreate(ContestBase):
    pass

class Contest(ContestBase):
    id: int
    created_by_id: int
    challenges: List[Challenge] = []

    class Config:
        from_attributes = True