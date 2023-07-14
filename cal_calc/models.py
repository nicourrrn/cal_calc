from dataclasses import dataclass
from datetime import date, time

@dataclass
class Product:
    name: str
    # per 100 g. 
    fats: float
    saturated_fats: float
    proteins: float
    carbohydrates: float
    sugars: float
    solt: float

@dataclass
class Meal:
    product: Product
    amount: float 
    time: time

@dataclass
class Day:
    date: date
    meals: list[Meal]
