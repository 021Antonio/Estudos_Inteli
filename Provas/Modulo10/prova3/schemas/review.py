# schemas/review.py

from pydantic import BaseModel

class Review(BaseModel):
    id: int
    nome: str
    review: str
    estrelas: float
    serie_filme: str

    class Config:
        orm_mode = True