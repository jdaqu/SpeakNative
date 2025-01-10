from database import SessionLocal
# from models import Phrase, Topic, Mistake
from models import Phrase

db = SessionLocal()

# Fetch and print phrases
phrases = db.query(Phrase).all()
print("Phrases:", phrases)

# Fetch and print topics
# topics = db.query(Topic).all()
# print("Topics:", topics)

# # Fetch and print mistakes
# mistakes = db.query(Mistake).all()
# print("Mistakes:", mistakes)

db.close()
