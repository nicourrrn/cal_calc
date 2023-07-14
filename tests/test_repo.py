from cal_calc import models
from cal_calc.repos.json import JsonRepo 

products = [
        models.Product(name="Молоко", fats = 3.5, saturated_fats=2.2, proteins=3.0,
                       carbohydrates=4.7, sugars=4.7, salt=0.125)
]

days = [
        models.Day(meals=[models.Meal(product_id=1, amount=100)]), 
        models.Day(meals=[models.Meal(product_id=1, amount=140)]), 
        models.Day(meals=[models.Meal(product_id=1, amount=105)]), 
        models.Day(meals=[]), 
        models.Day(meals=[]), 
]

def test_json_repo():
    repo = JsonRepo()
    repo.dumps(days)
    repo.loads()


