from sqlalchemy.orm import Session
# from app.db.models import Mistake
from app.schemas import MistakeCreate

# def create_mistake(db: Session, mistake_data: MistakeCreate):
#     new_mistake = Mistake(**mistake_data.dict())
#     db.add(new_mistake)
#     db.commit()
#     db.refresh(new_mistake)
#     return new_mistake

# def get_all_mistakes(db: Session):
#     return db.query(Mistake).all()
