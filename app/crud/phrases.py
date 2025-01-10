from sqlalchemy.orm import Session
from app.db.models import Phrase
from app.schemas import PhraseCreate

def create_phrase(db: Session, phrase_data: PhraseCreate):
    new_phrase = Phrase(**phrase_data.dict())
    db.add(new_phrase)
    db.commit()
    db.refresh(new_phrase)
    return new_phrase

def get_all_phrases(db: Session):
    return db.query(Phrase).all()
