from sqlalchemy.orm import Session
# from app.db.models import Topic
from app.schemas import TopicCreate

# def create_topic(db: Session, topic_data: TopicCreate):
#     new_topic = Topic(**topic_data.dict())
#     db.add(new_topic)
#     db.commit()
#     db.refresh(new_topic)
#     return new_topic

# def get_all_topics(db: Session):
#     return db.query(Topic).all()

# def get_topic_by_name(db: Session, name: str):
#     return db.query(Topic).filter(Topic.name == name).first()