from queue import Full
from sqlalchemy.orm import Session
from app.schemas.phrases import PhraseIn, PhraseOut
from app.services.ai_processing import process_with_ai
from app.crud.phrases import create_phrase
# from app.crud.mistakes import create_mistake
# from app.crud.topics import get_topic_by_name, create_topic
from app.schemas import PhraseCreate
from datetime import datetime

def add_phrase_with_analysis(db: Session, phrase_data: PhraseIn) -> dict:
    """
    Agrega una frase a la base de datos y analiza errores y temas utilizando IA.
    """
    # Procesa el texto con IA
    ai_response = process_with_ai(phrase_data.original_text)

    # Extrae información de la respuesta de IA
    correct_form = ai_response["response"].get("Correct form to say")
    # mistakes = ai_response["response"].get("What error did you have?")
    # topics_to_study = ai_response["response"].get("Topics to study")

    print("=========================")
    print("RESPONSE", ai_response)
    print("==========================")

    print("=========================")
    print("CORRECT FORM", correct_form)
    print("==========================")

    # Crea la frase en la base de datos
    new_phrase = create_phrase(db, PhraseCreate(
        original_text=phrase_data.original_text,
        user_id=phrase_data.user_id,
        correct_text=correct_form,
    ))

# # TODO: ADD THE TOPICS AND MISTAKES

#     # Crea los errores asociados
#     if mistakes:
#         for mistake in mistakes.split("\n"):
#             create_mistake(db, {"mistake": mistake, "correct_text": correct_form})

#     # Maneja los temas
#     if topics_to_study:
#         for topic_name in topics_to_study.split("\n"):
#             topic = get_topic_by_name(db, topic_name)
#             if not topic:
#                 topic = create_topic(db, {"name": topic_name, "description": ""})
#             new_phrase.topic_to_study = topic.id

    db.commit()
    db.refresh(new_phrase)

    return PhraseOut(
        user_id=1,
        id=new_phrase.id,
        original_text=new_phrase.original_text,
        correct_text=new_phrase.correct_text,
        mistakes=[],  # Asignar correctamente si implementas errores
        topics_to_study=[],  # Asignar correctamente si implementas temas
        datetime_submitted=datetime.now(),
    )

    # return {"phrase": new_phrase, "analysis": ai_response}