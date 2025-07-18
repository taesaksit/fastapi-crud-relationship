from pydantic import BaseModel,Field
from typing import  Optional
from .category import CategoryResponse

class BookBase(BaseModel):
    title: str
    author: Optional[str]
    
class BookCreate(BookBase):
    title: str = Field(strip_whitespace=True, min_length=3)
    category_id: int
    
class BookResponse(BookBase):
    id: int
    category:CategoryResponse
    
    class Config:
        from_attributes = True