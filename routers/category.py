from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session
from ..schemas import category as schemas
from ..crud import category as crud
from ..database import SessionLocal


router = APIRouter(prefix="/category" , tags=["category"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
        
@router.post("/", response_model=schemas.CategoryResponse)
def create_category(category: schemas.CategoryCreate, db:Session = Depends(get_db)):
  return crud.create_category(db,category)