from sqlalchemy.orm import Session
# from app.db.models import Vocabulary
from app.schemas import VocabularyCreate

# def create_vocabulary(db: Session, vocabulary_data: VocabularyCreate):
#     new_vocabulary = Vocabulary(**vocabulary_data.dict())
#     db.add(new_vocabulary)
#     db.commit()
#     db.refresh(new_vocabulary)
#     return new_vocabulary

# def get_all_vocabulary(db: Session):
#     return db.query(Vocabulary).all()
