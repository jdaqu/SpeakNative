from app.db.database import Base, engine
from app.db.models import Phrase

def init_db():
    # Crea todas las tablas definidas en los modelos
    Base.metadata.create_all(bind=engine)

if __name__ == "__main__":
    init_db()
