from pydantic import BaseModel
from typing import List

class VocabularyBase(BaseModel):
    text: str
    translation: str | None = None
    alternatives: List[str] | None = None

class VocabularyCreate(VocabularyBase):
    pass

class VocabularyOut(VocabularyBase):
    id: int

    class Config:
        orm_mode = True
