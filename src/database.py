from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

# Use a local SQLite DB file for simplicity. For production use an env-configured DB.
SQL_URL = "sqlite:///./app.db"

engine = create_engine(SQL_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

def init_db():
    from . import models
    Base.metadata.create_all(bind=engine)
