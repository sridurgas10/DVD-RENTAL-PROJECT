from pydantic import BaseModel
from datetime import datetime

class CustomerBase(BaseModel):
    first_name: str
    last_name: str
    email: str
    store_id :int
    address_id :int
    activebool:bool
    create_date :datetime
    last_update :datetime

class CustomerCreate(CustomerBase):
    pass    

class CustomerOut(CustomerBase):
    customer_id: int
    class config:
        orm_mode=True

class TopCustomer(BaseModel):
    customer_id:int
    first_name:str
    last_name:str  
    total_amount:float    

class CustomerRental(BaseModel):
    customer_id:int
    total_rentals:int
    payment:float
