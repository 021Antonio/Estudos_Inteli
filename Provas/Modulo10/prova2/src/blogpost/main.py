from fastapi import FastAPI 
from routes import blogPost

app = FastAPI()

app.include_router(blogPost.router)
