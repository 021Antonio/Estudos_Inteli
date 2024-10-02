# review.py
from sqlalchemy import Column, Integer, String, Double, DateTime
from sqlalchemy.ext.declarative import declarative_base
from .base import Base

class Review(Base):
    __tablename__ = 'review'

    id = Column(Integer, primary_key=True, autoincrement=True)
    nome = Column(String)
    review = Column(String)
    estrelas = Column(Double)
    serie_filme = Column(String)

    def __repr__(self):
        return f"<Review(nome='{self.nome}', review='{self.review}, id={self.id}', serie_filme='{self.serie_filme}')>"