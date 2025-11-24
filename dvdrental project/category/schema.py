from pydantic import BaseModel
from datetime import datetime

class CategoryBase(BaseModel):
  name:str
  last_update:datetime

class CategoryCreate(CategoryBase):
  pass

class CategoryOut(CategoryBase):
  category_id:int
  class config:
    orm_mode=True