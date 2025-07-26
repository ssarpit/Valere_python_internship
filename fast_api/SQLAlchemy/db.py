from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base 
DATABASE_URL="sqlite:///sqlite.db"
engine=create_engine(DATABASE_URL,echo=True)

SessionLocal=sessionmaker(bind=engine,expire_on_commit=False)
Base=declarative_base()
def get_db():
    db=SessionLocal()
    try:
        yield db

    finally:
        db.close()