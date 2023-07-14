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
    time: str = Field(default_factory=lambda: str(time()))

class Day(BaseModel):
    date: str = Field(default_factory=lambda: str(date.today()))
    meals: list[Meal]
