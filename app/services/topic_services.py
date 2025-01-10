from sqlalchemy.orm import Session
# from app.crud.topics import get_topic_by_name, create_topic

# def get_or_create_topic(db: Session, name: str, description: str = ""):
#     """
#     Obtiene un tema existente o lo crea si no existe.
#     """
#     topic = get_topic_by_name(db, name)
#     if not topic:
#         topic = create_topic(db, {"name": name, "description": description})
#     return topic
