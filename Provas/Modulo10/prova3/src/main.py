from fastapi import FastAPI
from db import engine  
from models.base import Base
from routes import review  
from models.review import Review  
app = FastAPI()

app.include_router(review.router)

def create_tables():
    Base.metadata.create_all(bind=engine)

@app.on_event("startup")
async def startup_event():
    create_tables()
