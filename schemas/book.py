from pydantic import BaseModel
from typing import  Optional
from .category import CategoryResponse

class BookBase(BaseModel):
    title: str
    author: Optional[str]
    category_id: int
    
class BookCreate(BookBase):
    pass

class BookResponse(BookBase):
    id: int
    category: Optional[CategoryResponse]
    class Config:
        from_attributes = True