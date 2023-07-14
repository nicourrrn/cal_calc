from cal_calc import models
from cal_calc.repos.json import JsonRepo 

from datetime import date 

days = [
        models.Day(date.today() , []), 
        models.Day(date.today() , []), 
        models.Day(date.today() , []), 
        models.Day(date.today() , []), 
        models.Day(date.today() , []), 
]

def test_json_repo():
    repo = JsonRepo()
    repo.dumps(days)
    repo.loads()


