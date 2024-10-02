# src/routers/produtos.py

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from schemas.review import Review as ReviewSchema
from services.review import ReviewService
from databases import database

router = APIRouter()

@router.get("/review/{review_id}")
async def get_review(review_id: int, db: Session = Depends(database.get_db)):
    reviewService = ReviewService(db)
    return reviewService.get(review_id)

@router.get("/review")
async def get_review(db: Session = Depends(database.get_db)):
    reviewService = ReviewService(db)
    return reviewService.get_all()

@router.post("/review")
async def create_review(review: ReviewSchema, db: Session = Depends(database.get_db)):
    reviewService = ReviewService(db)
    return reviewService.add(review=review)

@router.put("/review/{review_id}")
async def update_review(review_id: int, review: ReviewSchema, db: Session = Depends(database.get_db)):
    reviewService = ReviewService(db)
    return reviewService.update(review_id, review=review)
    

@router.delete("/review/{review_id}")
async def delete_review(review_id: int, db: Session = Depends(database.get_db)):
    reviewService = ReviewService(db)
    return reviewService.delete(review_id)