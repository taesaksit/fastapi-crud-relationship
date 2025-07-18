from pydantic import BaseModel, Field
from typing import Optional, List


class BookBase(BaseModel):
    title: str
    author: Optional[str]


class CategoryBase(BaseModel):
    name: str


class CategoryCreate(CategoryBase):
    name: str = Field(strip_whitespace=True, min_length=1)


class CategoryResponse(CategoryBase):
    id: int
    books: List[BookBase] 

    class Config:
        from_attributes = True 
