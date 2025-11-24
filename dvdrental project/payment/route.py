from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from dbconnection import get_db
from . import crud, schema

payment_router = APIRouter(prefix="/payments", tags=["Payments"])

@payment_router.post("/", response_model=schema.PaymentOut)
def create_payment(payment: schema.PaymentCreate, db: Session = Depends(get_db)):
    return crud.create_payment(db, payment)

@payment_router.get("/{payment_id}", response_model=schema.PaymentOut)
def get_payment(payment_id: int, db: Session = Depends(get_db)):
    payment = crud.get_payment(db, payment_id)
    if not payment:
        raise HTTPException(status_code=404, detail="Payment not found")
    return payment

@payment_router.get("/", response_model=list[schema.PaymentOut])
def list_payments(db: Session = Depends(get_db)):
    return crud.get_all_payments(db)

@payment_router.get("/customer/{customer_id}", response_model=list[schema.PaymentOut])
def customer_payments(customer_id: int, db: Session = Depends(get_db)):
    return crud.get_customer_payments(db, customer_id)
