from fastapi import HTTPException, status
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session
from ..models import category as models
from ..schemas import category as schemas

def create_category(db: Session, category: schemas.CategoryCreate):
    db_category = models.Category(**category.model_dump())
    db.add(db_category)
    try:
        db.commit()
        db.refresh(db_category)
        return db_category
    except IntegrityError:
        db.rollback()
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Category name already exists."
        )
    except Exception:
        db.rollback()
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Internal server error"
        )

def get_categories(db:Session):
    return db.query(models.Category).all()

def update_category(db:Session, category_id:int, category:schemas.CategoryCreate):
    db_category = db.query(models.Category).filter(models.Category.id == category_id).first()

    if db_category is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Category with id {category_id} not found"
        )
    for key, value in category.model_dump().items():
        setattr(db_category,key,value)
    db.commit()
    db.refresh(db_category)
    return db_category

def delete_category(db:Session, category_id:int):
    db_category = db.query(models.Category).filter(models.Category.id == category_id).first()
    if db_category is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Category with id {category_id} not found"
        )
    category_name = db_category.name
    db.delete(db_category)
    db.commit()
    return {"message:" f"Category {category_name} deleted!"}
    
