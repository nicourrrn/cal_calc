from pydantic import BaseModel, Field
from datetime import date, time 
from typing import Optional
from cal_calc.__init__ import products 

class Product(BaseModel):
    id: int = Field(default_factory=lambda: len(products))
    name: str
    # per 100 g. 
    fats: float
    saturated_fats: float
    proteins: float
    carbohydrates: float
    sugars: float
    solt: Optional[float] = 0

class Meal(BaseModel):
    product_id: int
    amount: float 
    time: str = Field(default_factory=lambda: str(time()))

class Day(BaseModel):
    date: str = Field(default_factory=lambda: str(date.today()))
    meals: list[Meal]
