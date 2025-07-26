# app/db/database.py
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

# Define the database URL for SQLite
DATABASE_URL = "sqlite:///./coding_platform.db"

# Create the SQLAlchemy engine
# connect_args is needed only for SQLite to allow multi-threaded access
engine = create_engine(
    DATABASE_URL, connect_args={"check_same_thread": False}
)

# Create a session factory
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base class for declarative models
Base = declarative_base()
