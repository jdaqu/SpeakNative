# from sqlalchemy.orm import Session
# from models import Phrase, Topic, Mistake, Vocabulary

# # CRUD for Topics
# def create_topic(db: Session, name: str, description: str):
#     topic = Topic(name=name, description=description)
#     db.add(topic)
#     db.commit()
#     db.refresh(topic)
#     return topic

# def get_all_topics(db: Session):
#     return db.query(Topic).all()

# # CRUD for Mistakes
# def create_mistake(db: Session, mistake: str, correct_text: str):
#     new_mistake = Mistake(mistake=mistake, correct_text=correct_text)
#     db.add(new_mistake)
#     db.commit()
#     db.refresh(new_mistake)
#     return new_mistake

# # CRUD for Phrases
# from sqlalchemy.orm import Session
# from models import Phrase, Mistake, Topic

# def create_phrase(db: Session, original_text: str, correct_text: str, topic_id: int, mistake_ids: list):
#     # Create the phrase
#     phrase = Phrase(original_text=original_text, correct_text=correct_text, topic_to_study=topic_id)
#     db.add(phrase)
#     db.commit()
#     db.refresh(phrase)

#     # Link mistakes to the phrase
#     for mistake_id in mistake_ids:
#         mistake = db.query(Mistake).filter(Mistake.id == mistake_id).first()
#         if mistake:
#             phrase.mistakes.append(mistake)

#     db.commit()
#     return phrase

# def get_all_phrases(db: Session):
#     return db.query(Phrase).all()

# # CRUD for Vocabulary
# def create_vocabulary(db: Session, text: str, translation: str, alternatives: list):
#     vocab = Vocabulary(text=text, translation=translation, alternatives=alternatives)
#     db.add(vocab)
#     db.commit()
#     db.refresh(vocab)
#     return vocab

# def get_all_vocabulary(db: Session):
#     return db.query(Vocabulary).all()

# def get_topic_by_name(db: Session, name: str):
#     return db.query(Topic).filter(Topic.name == name).first()