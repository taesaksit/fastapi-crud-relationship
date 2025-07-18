from typing import List
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from ..schemas import book as schemas
from ..crud import book as crud
from ..database import get_db

router = APIRouter(prefix="/book", tags=["book"])


@router.post("/", response_model=schemas.BookResponse)
def create_book(book: schemas.BookCreate, db: Session = Depends(get_db)):
    return crud.craete_book(db, book)


@router.get("/", response_model=List[schemas.BookResponse])
def read_books(db: Session = Depends(get_db)):
    return crud.get_books(db)


@router.put("/{book_id}", response_model=schemas.BookResponse)
def update_book(book_id: int, book: schemas.BookCreate, db: Session = Depends(get_db)):
    return crud.update_book(db, book_id, book)


@router.delete("/{book_id}")
def delete_book(book_id: int, db: Session = Depends(get_db)):
    return crud.delete_book(db, book_id)
