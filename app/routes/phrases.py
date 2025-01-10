from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.db.database import SessionLocal
from app.schemas.phrases import PhraseCreate, PhraseIn, PhraseOut
from app.crud.phrases import create_phrase, get_all_phrases
from app.services.phrase_services import add_phrase_with_analysis

import logging

router = APIRouter()

# Dependencia para obtener la sesión de la base de datos
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/", response_model=PhraseOut)
def add_phrase(phrase: PhraseIn, db: Session = Depends(get_db)):
    
    result = add_phrase_with_analysis(db, phrase)
    logging.info("Endpoint '/' was called")

    return add_phrase_with_analysis(db, phrase)
    # return create_phrase(db, phrase)

@router.get("/", response_model=list[PhraseOut])
def list_phrases(db: Session = Depends(get_db)):
    return get_all_phrases(db)
