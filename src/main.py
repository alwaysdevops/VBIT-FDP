from fastapi import FastAPI, HTTPException, Depends
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
from . import crud, models, schemas
from .database import SessionLocal, init_db
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("src")

app = FastAPI(title="Event Registration Service", version="0.1.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.on_event("startup")
def startup_event():
    init_db()
    logger.info("Database initialized")


@app.get("/health")
def health():
    return {"status": "ok"}


@app.post("/register", response_model=schemas.ParticipantRead, status_code=201)
def register(participant: schemas.ParticipantCreate, db: Session = Depends(get_db)):
    existing = crud.get_participant_by_email(db, participant.email)
    if existing:
        raise HTTPException(status_code=400, detail="Email already registered")
    created = crud.create_participant(db, participant)
    return created


@app.get("/registrations", response_model=list[schemas.ParticipantRead])
def list_regs(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return crud.list_participants(db, skip=skip, limit=limit)


@app.get("/registrations/{reg_id}", response_model=schemas.ParticipantRead)
def get_registration(reg_id: int, db: Session = Depends(get_db)):
    reg = crud.get_participant(db, reg_id)
    if not reg:
        raise HTTPException(status_code=404, detail="Registration not found")
    return reg
