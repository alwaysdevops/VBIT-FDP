from sqlalchemy import Column, Integer, String, DateTime, func
from .database import Base


class Participant(Base):
    __tablename__ = "participants"

    id = Column(Integer, primary_key=True, index=True)
    first_name = Column(String(length=100), nullable=True)
    last_name = Column(String(length=100), nullable=True)
    email = Column(String(length=255), unique=True, index=True, nullable=False)
    phone = Column(String(length=50), nullable=True)
    organization = Column(String(length=255), nullable=True)
    notes = Column(String(length=2000), nullable=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
