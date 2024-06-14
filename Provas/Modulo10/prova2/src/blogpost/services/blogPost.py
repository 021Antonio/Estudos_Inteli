from fastapi import HTTPException
from sqlalchemy.orm import Session
from repositories.blogPost import BlogPostRepository
from models.blogPost import BlogPost
from schemas.blogPost import BlogPost as BlogPostSchema

class BlogPostService:
    def __init__(self,db: Session):
        self.repository = BlogPostRepository(db)

    def get(self, blogPost_id):
        blogPost = self.repository.get(blogPost_id)
        if blogPost is None:
            raise HTTPException(status_code=404, detail="blogPost not found")
        return blogPost

    def get_all(self):
        return self.repository.get_all()

    def add(self, blogPost: BlogPostSchema):
        blogPost = BlogPost(**blogPost.dict())
        return self.repository.add(blogPost)

    def update(self, blogPost_id, blogPost: BlogPostSchema):
        usblogPost = BlogPost(**blogPost.dict())
        return self.repository.update(blogPost_id, blogPost)

    def delete(self, blogPost_id):
        return self.repository.delete(blogPost_id)
