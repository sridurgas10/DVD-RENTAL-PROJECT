from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from dbconnection import get_db
from . import crud, schema

category_router = APIRouter(prefix="/category", tags=["Category"])

@category_router.get("/", response_model=list[schema.CategoryOut])
def list_category(db: Session = Depends(get_db)):
    return crud.get_all_category(db)

@category_router.get("/{category_id}", response_model=schema.CategoryOut)
def get_category(category_id: int, db: Session = Depends(get_db)):
    category = crud.get_category(db, category_id)
    if not category:
        raise HTTPException(status_code=404, detail="Category not found")
    return category

@category_router.post("/", response_model=schema.CategoryOut)
def create_category(category: schema.CategoryCreate, db: Session = Depends(get_db)):
    return crud.create_category(db, category)

@category_router.put("/{category_id}", response_model=schema.CategoryOut)
def update_category(category_id: int, category: schema.CategoryCreate, db: Session = Depends(get_db)):
    updated_category = crud.update_category(db, category_id, category)
    if not updated_category:
        raise HTTPException(status_code=404, detail="Category not found")
    return updated_category

@category_router.delete("/{category_id}", response_model=schema.CategoryOut)
def delete_customer(category_id: int, db: Session = Depends(get_db)):
    deleted_category = crud.delete_category(db, category_id)
    if not deleted_category:
        raise HTTPException(status_code=404, detail="Category not found")
    return deleted_category
