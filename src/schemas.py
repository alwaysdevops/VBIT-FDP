from pydantic import BaseModel, EmailStr, Field
from typing import Optional
from datetime import datetime


class ParticipantCreate(BaseModel):
    first_name: Optional[str] = None
    last_name: Optional[str] = None
    email: EmailStr
    phone: Optional[str] = Field(None, max_length=50)
    organization: Optional[str] = None
    notes: Optional[str] = None


class ParticipantRead(BaseModel):
    id: int
    first_name: Optional[str]
    last_name: Optional[str]
    email: EmailStr
    phone: Optional[str]
    organization: Optional[str]
    notes: Optional[str]
    created_at: Optional[datetime]

    class Config:
        orm_mode = True
