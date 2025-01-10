from typing import Optional
from pydantic import BaseModel

class TopicBase(BaseModel):
    name: str
    description: Optional[str]

class TopicCreate(TopicBase):
    pass

class TopicOut(TopicBase):
    id: int

    class Config:
        orm_mode = True