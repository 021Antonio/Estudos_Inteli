from sqlalchemy import Column, Integer, String
from database.database import db

class User(db.Model):
  __tablename__ = 'pedidos'

  id = Column(Integer, primary_key=True, autoincrement=True)
  name = Column(String(50), nullable=False)
  item = Column(String(50), nullable=False)
  descricao = Column(String(50), nullable=False)

  def __repr__(self):
    return f'<User:[id:{self.id}, name:{self.name}, item:{self.item}, descricao:{self.descricao}]>'
  
  def serialize(self):
    return {
      "id": self.id,
      "name": self.name,
      "item": self.item,
      "descricao": self.descricao}