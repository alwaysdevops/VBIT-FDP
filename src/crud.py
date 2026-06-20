from sqlalchemy.orm import Session
from . import models, schemas
from typing import List, Optional


def get_participant(db: Session, participant_id: int) -> Optional[models.Participant]:
    return db.query(models.Participant).filter(models.Participant.id == participant_id).first()


def get_participant_by_email(db: Session, email: str) -> Optional[models.Participant]:
    return db.query(models.Participant).filter(models.Participant.email == email).first()


def list_participants(db: Session, skip: int = 0, limit: int = 100) -> List[models.Participant]:
    return db.query(models.Participant).offset(skip).limit(limit).all()


def create_participant(db: Session, participant: schemas.ParticipantCreate) -> models.Participant:
    db_participant = models.Participant(
        first_name=participant.first_name,
        last_name=participant.last_name,
        email=participant.email,
        phone=participant.phone,
        organization=participant.organization,
        notes=participant.notes,
    )
    db.add(db_participant)
    db.commit()
    db.refresh(db_participant)
    return db_participant
