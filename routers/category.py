from typing import List
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from ..schemas import category as schemas
from ..crud import category as crud
from ..database import get_db


router = APIRouter(prefix="/category", tags=["category"])


@router.post("/", response_model=schemas.CategoryResponse)
def create_category(category: schemas.CategoryCreate, db: Session = Depends(get_db)):
    return crud.create_category(db, category)


@router.get("/", response_model=List[schemas.CategoryResponse])
def read_categories(db: Session = Depends(get_db)):
    return crud.get_categories(db)


@router.put("/{category_id}", response_model=schemas.CategoryResponse)
def update_category(
    category_id: int, category: schemas.CategoryCreate, db: Session = Depends(get_db)
):
    return crud.update_category(db, category_id, category)


@router.delete("/{category_id}")
def delete_category(category_id: int, db: Session = Depends(get_db)):
    return crud.delete_category(db, category_id)
