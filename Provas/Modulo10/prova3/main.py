# main.py

from fastapi import FastAPI
from routes import review

app = FastAPI()

app.include_router(review.router)
