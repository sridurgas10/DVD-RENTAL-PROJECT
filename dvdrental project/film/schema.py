from pydantic import BaseModel

class FilmBase(BaseModel):
    title: str
    description: str 
    release_year: int 
    language_id: int 
    rental_duration: int
    rental_rate: float 
    length: int 
    replacement_cost: float 
    rating: str

class FilmCreate(FilmBase):
    pass

class FilmOut(FilmBase):
    film_id: int
  
    class config:
        orm_mode=True

class FilmAvailabilityView(BaseModel):
    film_id: int
    title: str
    available_stock: int
    
    class config:
        orm_mode=True

class TopFilms(BaseModel):
    film_id:int
    title:str
    count:int        
  