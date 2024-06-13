from models import User
from sqlalchemy.orm import Session

class UserRepository:
    def __init__(self, db: Session):
        self.db = db

    def get(self, user_id):
        return self.db.query(User).get(user_id)

    def get_all(self):
        return self.db.query(User).all()
    
    def add(self, user: User):
        user.id = None
        self.db.add(user)
        self.db.flush()
        self.db.commit()
        return{"message": "User created successfully"}

    def update(self,user_id, user: User):
        userdb = self.db.query(User).filter(User.id == user_id).first()
        if userdb is None:
            return {"message": "User not found"}
        user = user.__dict__
        user.pop("_sa_instance_state")
        user.pop("id")
        self.db.query(User).filter(User.id == user_id).update(user)
        self.db.flush()
        self.db.commit()
        return {"message": "User updated successfully"}

    def delete(self, user_id):
        user = self.db.query(User).filter(User.id == user_id).first()
        if user is None:
            return {"message": "User not found"}
        self.db.query(User).filter(User.id == user_id).delete()
        self.db.flush()
        self.db.commit()
        return {"message": "User deleted successfully"}