from pydantic import BaseModel

class MistakeBase(BaseModel):
    mistake: str
    correct_text: str

class MistakeCreate(MistakeBase):
    pass

class MistakeOut(MistakeBase):
    id: int

    class Config:
        orm_mode = True
