from pydantic import BaseModel

from pydantic import BaseModel
from typing import Optional, List
from datetime import datetime

class PhraseBase(BaseModel):
    original_text: str
    user_id: int

class PhraseIn(PhraseBase):
    pass

class PhraseCreate(PhraseBase):
    
    correct_text: str

class PhraseOut(PhraseBase):
    id: int
    correct_text: Optional[str] = None  # La corrección o traducción
    mistakes: Optional[List[str]] = []  # Lista de errores detectados (si aplica)
    topics_to_study: Optional[List[str]] = []  # Temas recomendados
    datetime_submitted: datetime

    class Config:
        orm_mode = True


# class PhraseBase(BaseModel):
#     original_text: str
#     correct_text: str | None = None
#     topic_to_study: int | None = None

# class PhraseCreate(PhraseBase):
#     text: str

# class PhraseOut(PhraseBase):
#     id: int

#     class Config:
#         orm_mode = True
