from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from schemas.blogPost import BlogPost as BlogPostSchema
from services.blogPost import BlogPostService
from databases import database
from log.loggin_config import LoggerSetup
import logging

logger_setup = LoggerSetup()

LOGGER = logging.getLogger(__name__)

router = APIRouter()

@router.get("/")
async def teste():
    LOGGER.info("Teste")
    return {"message": "Hello World"}

@router.post("/blogPost")
async def create_blogPost(blogPost: BlogPostSchema, db: Session = Depends(database.get_db)):
    blogPostService = BlogPostService(db)
    LOGGER.warning("Post criado")
    return blogPostService.add(blogPost=blogPost)

@router.get("/blogPost/{blogPost_id}")
async def get_user(user_id: int, db: Session = Depends(database.get_db)):
    blogPostService = BlogPostService(db)
    LOGGER.warning("Post encontrado")
    return blogPostService.get(blogPost_id)

@router.get ("/blogPost")
async def get_blogPost(db: Session = Depends(database.get_db)):
    blogPostervice = blogPostService(db)
    LOGGER.warning("Todos os posts encontrados")
    return blogPostService.get_all()

@router.put("/blogPost/{blogPost_id}")
async def update_blogPost(blogPost_id: int, blogPost: BlogPostSchema, db: Session = Depends(database.get_db)):
    blogPostService = BlogPostService(db)
    LOGGER.warning("Post atualizado")
    return blogPostService.update(blogPost_id, blogPost=blogPost)

@router.delete("/blogPost/{blogPost_id}")
async def delete_blogPost(blogPost_id: int, db: Session = Depends(database.get_db)):
    blogPostService = BlogPostService(db)
    LOGGER.warning("Post deletado")
    return blogPostService.delete(blogPost_id)
