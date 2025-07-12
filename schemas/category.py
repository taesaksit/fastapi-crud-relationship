from typing import Literal
from pydantic import BaseModel

class CategoryBase(BaseModel):
   name: str
    
class CategoryCreate(CategoryBase):
    pass

class CategoryResponse(CategoryBase):
    id: int
    class config:
        orm_mode = True