from pydantic import BaseModel, Field

class CategoryBase(BaseModel):
   name: str
    
class CategoryCreate(CategoryBase):
    name : str = Field(strip_whitespace=True , min_length=1)

class CategoryResponse(CategoryBase):
    id: int
    class Config:
         from_attributes = True