# from pydantic import BaseModel
# from typing import List, Optional

# # Esquema para Topic
# class TopicBase(BaseModel):
#     name: str
#     description: Optional[str]

# class TopicCreate(TopicBase):
#     pass

# class TopicOut(TopicBase):
#     id: int

#     class Config:
#         orm_mode = True

# # Esquema para Mistake
# class MistakeBase(BaseModel):
#     mistake: str
#     correct_text: str

# class MistakeCreate(MistakeBase):
#     pass

# class MistakeOut(MistakeBase):
#     id: int

#     class Config:
#         orm_mode = True

# # Esquema para Phrase
# class PhraseBase(BaseModel):
#     original_text: str
#     correct_text: Optional[str]
#     topic_to_study: Optional[int]

# class PhraseCreate(PhraseBase):
#     mistakes: Optional[List[int]]

# class PhraseOut(PhraseBase):
#     id: int
#     mistakes: List[MistakeOut] = []

#     class Config:
#         orm_mode = True

# # Esquema para Vocabulary
# class VocabularyBase(BaseModel):
#     text: str
#     translation: Optional[str]
#     alternatives: Optional[List[str]]

# class VocabularyCreate(VocabularyBase):
#     pass

# class VocabularyOut(VocabularyBase):
#     id: int

#     class Config:
#         orm_mode = True
