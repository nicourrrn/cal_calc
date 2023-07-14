from pydantic import BaseModel, Field
from datetime import date, time 
from typing import Optional


class Product(BaseModel):
    name: str
    # per 100 g. 
    fats: float
    saturated_fats: float
    proteins: float
    carbohydrates: float
    sugars: float
    solt: Optional[float] = 0

class Meal(BaseModel):
    product: Product
    amount: float 
    time: time = Field(default_factory=lambda: time())

class Day(BaseModel):
    date: date = Field(default_factory=lambda: date.today())
    meals: list[Meal]
