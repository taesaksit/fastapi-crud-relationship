# Create / Update ต้องค้น category_id ก่อนเสมอ
from fastapi import HTTPException, status
from sqlalchemy.orm import Session
from ..models import book as models
from ..schemas import book as schemas
from ..models import category as models_category

def validate_category_id(db: Session, category_id: int):
    
    category = db.query(models_category.Category).filter(models_category.Category.id == category_id).first()
    
    if category is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Category ID {category_id} not found"
        )
    return category

def craete_book(db:Session, book:schemas.BookCreate):
    # validate category_id ก่อน
    validate_category_id(db,book.category_id)
    
    db_book = models.Book(**book.model_dump())
    db.add(db_book)
    db.commit()
    db.refresh(db_book)
    return db_book

def get_books(db: Session):
   return  db.query(models.Book).all()