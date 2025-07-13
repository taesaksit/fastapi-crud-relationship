from pydantic import BaseModel,Field
from typing import  Optional
from .category import CategoryResponse

class BookBase(BaseModel):
    title: str
    author: Optional[str]
    category_id: int
    
class BookCreate(BookBase):
    title: str = Field(strip_whitespace=True, min_length=3)

class BookResponse(BookBase):
    id: int
    category: Optional[CategoryResponse]
    class Config:
        from_attributes = True