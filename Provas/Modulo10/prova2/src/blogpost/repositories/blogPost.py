from models import BlogPost
from sqlalchemy.orm import Session

class BlogPostRepository:
    def __init__(self, db: Session):
        self.db = db

    def get(self, blogPost_id):
        return self.db.query(BlogPost).get(blogPost_id)

    def get_all(self):
        return self.db.query(BlogPost).all()
    
    def add(self, blogPost: BlogPost):
        blogPost.id = None
        self.db.add(blogPost)
        self.db.flush()
        self.db.commit()
        return{"message": "blogPost created successfully"}

    def update(self,blogPost_id, blogPost: BlogPost):
        blogPostdb = self.db.query(BlogPost).filter(BlogPost.id == blogPost_id).first()
        if blogPostdb is None:
            return {"message": "BlogPost not found"}
        blogPost = blogPost.__dict__
        blogPost.pop("_sa_instance_state")
        blogPost.pop("id")
        self.db.query(BlogPost).filter(BlogPost.id == blogPost_id).update(blogPost)
        self.db.flush()
        self.db.commit()
        return {"message": "BlogPost updated successfully"}

    def delete(self, blogPost_id):
        blogPost = self.db.query(BlogPost).filter(BlogPost.id == blogPost_id).first()
        if blogPost is None:
            return {"message": "blogPost not found"}
        self.db.query(BlogPost).filter(BlogPost.id == blogPost_id).delete()
        self.db.flush()
        self.db.commit()
        return {"message": "blogPost deleted successfully"}