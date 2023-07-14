from cal_calc import models
from cal_calc.repos.json import JsonRepo 

from datetime import date 

days = [
        models.Day(date=date.today() , meals=[]), 
        models.Day(date=date.today() , meals=[]), 
        models.Day(date=date.today() , meals=[]), 
        models.Day(date=date.today() , meals=[]), 
        models.Day(date=date.today() , meals=[]), 
        models.Day(date=date.today() , meals=[]), 
        models.Day(date=date.today() , meals=[]), 
]

def test_json_repo():
    repo = JsonRepo()
    repo.dumps(days)
    repo.loads()


