from pydantic import BaseModel

class BlogPost(BaseModel):
    id: int
    tittle: str
    content: str
    

    class Config:
        orm_mode = True