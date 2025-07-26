# app/db/models.py
import datetime
from sqlalchemy import (
    Column, Integer, String, DateTime, Float,
    Boolean, ForeignKey, Text
)
from sqlalchemy.orm import relationship
from .database import Base

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True, nullable=False)
    email = Column(String, unique=True, index=True, nullable=False)
    hashed_password = Column(String, nullable=False)
    is_active = Column(Boolean, default=True)
    role = Column(String, default="user") # Can be 'user' or 'admin'

    submissions = relationship("Submission", back_populates="user")
    contest_participations = relationship("ContestParticipation", back_populates="user")
    created_contests = relationship("Contest", back_populates="created_by")

class Contest(Base):
    __tablename__ = "contests"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True, nullable=False)
    description = Column(Text)
    start_time = Column(DateTime, nullable=False)
    end_time = Column(DateTime, nullable=False)
    created_by_id = Column(Integer, ForeignKey("users.id"))

    created_by = relationship("User", back_populates="created_contests")
    challenges = relationship("Challenge", back_populates="contest", cascade="all, delete-orphan")
    participants = relationship("ContestParticipation", back_populates="contest", cascade="all, delete-orphan")

class Challenge(Base):
    __tablename__ = "challenges"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True, nullable=False)
    description = Column(Text, nullable=False)
    difficulty = Column(String, default="Easy")
    contest_id = Column(Integer, ForeignKey("contests.id"))

    contest = relationship("Contest", back_populates="challenges")
    submissions = relationship("Submission", back_populates="challenge")
    test_cases = relationship("TestCase", back_populates="challenge", cascade="all, delete-orphan")

class TestCase(Base):
    __tablename__ = "test_cases"
    id = Column(Integer, primary_key=True, index=True)
    challenge_id = Column(Integer, ForeignKey("challenges.id"))
    input = Column(Text, nullable=False)
    expected_output = Column(Text, nullable=False)
    is_hidden = Column(Boolean, default=False)

    challenge = relationship("Challenge", back_populates="test_cases")

class Submission(Base):
    __tablename__ = "submissions"
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    challenge_id = Column(Integer, ForeignKey("challenges.id"))
    contest_id = Column(Integer, ForeignKey("contests.id"), nullable=True)
    code = Column(Text, nullable=False)
    language = Column(String, nullable=False, default="python")
    status = Column(String, default="Pending")
    execution_time = Column(Float, nullable=True)
    score = Column(Integer, default=0)
    submitted_at = Column(DateTime, default=datetime.datetime.utcnow)

    user = relationship("User", back_populates="submissions")
    challenge = relationship("Challenge", back_populates="submissions")

class ContestParticipation(Base):
    __tablename__ = "contest_participation"
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    contest_id = Column(Integer, ForeignKey("contests.id"))
    total_score = Column(Integer, default=0)
    total_time_seconds = Column(Float, default=0.0)

    user = relationship("User", back_populates="contest_participations")
    contest = relationship("Contest", back_populates="participants")
