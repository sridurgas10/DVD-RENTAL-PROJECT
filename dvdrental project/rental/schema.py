from pydantic import BaseModel
from datetime import datetime

class RentalBase(BaseModel):
    inventory_id: int
    customer_id: int
    staff_id: int
    rental_date: datetime
    return_date:datetime
    last_update:datetime

class RentalCreate(RentalBase):
    pass 


class RentalOut(RentalBase):
    rental_id: int
    class config:
        orm_mode=True


#get_overdue_rentals(days INT) → Returns rentals not returned within given days.

class OverdueRental(BaseModel):
    rental_id: int
    return_date: datetime
   
class StaffPerformance(BaseModel):
    staff_id:int
    count:int