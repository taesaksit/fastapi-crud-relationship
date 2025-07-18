# Create / Update ต้องค้น category_id ก่อนเสมอ
from fastapi import HTTPException, status
from sqlalchemy.orm import Session
from ..models import book as models
from ..schemas import book as schemas
from ..models import category as models_category


# Util validation
def validate_category_id(db: Session, category_id: int):
    category = (
        db.query(models_category.Category)
        .filter(models_category.Category.id == category_id)
        .first()
    )
    if category is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Category ID {category_id} not found",
        )
    return category


# CREATE
def craete_book(db: Session, book: schemas.BookCreate):

    validate_category_id(db, book.category_id)
    db_book = models.Book(**book.model_dump())
    db.add(db_book)
    db.commit()
    db.refresh(db_book)
    return db_book


# READ
def get_books(db: Session):
    return db.query(models.Book).all()


# UPDATE
def update_book(db: Session, book_id: int, book: schemas.BookCreate):
    db_book = db.query(models.Book).filter(models.Book.id == book_id).first()
    validate_category_id(db, book.category_id)  # Reuse function Validate category_id

    if db_book is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Book with id {book_id} not found",
        )

    for key, value in book.model_dump().items():
        setattr(db_book, key, value)
    try:
        db.commit()
        db.refresh(db_book)
        return db_book
    except Exception:
        db.rollback()
        raise HTTPException(
            status_code=status.HTTP_500_INTERN, detail="Faild to update book"
        )


# DELETE
def delete_book(db: Session, book_id: int):
    db_book = db.query(models.Book).filter(models.Book.id == book_id).first()
    if db_book is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Book with id {book_id} not found",
        )
    book_name = db_book.title
    db.delete(db_book)
    db.commit()
    return {"message:" f"Book {book_name} deleted!"}
