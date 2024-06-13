from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from .base import Base

class User(Base):
    __tablename__ = 'user'

    id = Column(Integer, primary_key=True, autoincrement=True)
    email = Column(String, unique=True)
    username = Column(String, unique=True)
    name = Column(String)
    password = Column(String)


    def __repr__(self):
        return f"User(id={self.id}, email={self.email}, username={self.username}, name={self.name}, password={self.password})"