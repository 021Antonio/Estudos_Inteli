from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from schemas.user import User as UserSchema
from services.user import UserService
from databases import database

router = APIRouter()

@router.get("/teste")
async def teste():
    return {"message": "Hello World"}

@router.get("/users/{user_id}")
async def get_user(user_id: int, db: Session = Depends(database.get_db)):
    userService = UserService(db)
    return userService.get(user_id)

@router.get ("/users")
async def get_users(db: Session = Depends(database.get_db)):
    userService = UserService(db)
    return userService.get_all()

@router.post("/users")
async def create_user(user: UserSchema, db: Session = Depends(database.get_db)):
    userService = UserService(db)
    return userService.add(user=user)

@router.put("/users/{user_id}")
async def update_user(user_id: int, user: UserSchema, db: Session = Depends(database.get_db)):
    userService = UserService(db)
    return userService.update(user_id, user=user)

@router.delete("/users/{user_id}")
async def delete_user(user_id: int, db: Session = Depends(database.get_db)):
    userService = UserService(db)
    return userService.delete(user_id)
