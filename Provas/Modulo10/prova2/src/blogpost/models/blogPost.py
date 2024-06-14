from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from .base import Base

class BlogPost(Base):
    __tablename__ = 'blog_post'

    id = Column(Integer, primary_key=True, autoincrement=True)
    tittle = Column(String, unique=True)
    content = Column(String, unique=True)


    def __repr__(self):
        return f"BlogPost(id={self.id}, tittle={self.tittle}, content={self.content}"