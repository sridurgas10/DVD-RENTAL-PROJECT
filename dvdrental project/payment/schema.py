from pydantic import BaseModel
from datetime import datetime
from decimal import Decimal

class PaymentBase(BaseModel):
    customer_id: int
    staff_id: int
    rental_id: int
    amount: Decimal
    payment_date: datetime

class PaymentCreate(PaymentBase):
    pass

class PaymentOut(PaymentBase):
    payment_id: int
    class config:
        orm_mode=True
