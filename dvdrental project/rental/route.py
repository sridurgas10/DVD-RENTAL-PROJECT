from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from dbconnection import get_db
from . import crud, schema

rental_router = APIRouter(prefix="/rentals", tags=["Rentals"])

@rental_router.post("/", response_model=schema.RentalOut)
def create_rental(rental: schema.RentalCreate, db: Session = Depends(get_db)):
    return crud.create_rental(db, rental)

@rental_router.put("/return/{rental_id}", response_model=schema.RentalOut)
def return_rental(rental_id: int, rental: schema.RentalCreate,db: Session = Depends(get_db)):
    returned = crud.return_rental(db, rental,rental_id)
    if not returned:
        raise HTTPException(status_code=404, detail="Rental not found")
    return returned

@rental_router.get("/", response_model=list[schema.RentalOut])
def list_rentals(db: Session = Depends(get_db)):
    return crud.get_all_rentals(db)

@rental_router.get("/{rental_id}", response_model=schema.RentalOut)
def get_rental(rental_id: int, db: Session = Depends(get_db)):
    rental = crud.get_rental(db, rental_id)
    if not rental:
        raise HTTPException(status_code=404, detail="Rental not found")
    return rental

@rental_router.get("/overdue/", response_model=list[schema.RentalOut])
def overdue_rentals( db: Session = Depends(get_db)):
    return crud.get_overdue_rentals(db)


@rental_router.get("/reports/staff_performance /",response_model=list[schema.StaffPerformance])
def staff_rental(db:Session=Depends(get_db)):
    return crud.staff_performance(db)