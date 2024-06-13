from fastapi import HTTPException
from sqlalchemy.orm import Session
from repositories.user import UserRepository
from models.user import User
from schemas.user import User as UserSchema

class UserService:
    def __init__(self,db: Session):
        self.repository = UserRepository(db)

    def get(self, user_id):
        user = self.repository.get(user_id)
        if user is None:
            raise HTTPException(status_code=404, detail="User not found")
        return user

    def get_all(self):
        return self.repository.get_all()

    def add(self, user: UserSchema):
        user = User(**user.dict())
        return self.repository.add(user)

    def update(self, user_id, user: UserSchema):
        user = User(**user.dict())
        return self.repository.update(user_id, user)

    def delete(self, user_id):
        return self.repository.delete(user_id)
