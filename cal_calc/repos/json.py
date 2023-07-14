from cal_calc.models import Day
from cal_calc.repos import base
import json

class JsonRepo(base.AbstractBaseRepo):
    def __init__(self, filename: str = "days.json"):
        self.filename = filename 
        
    def loads(self) -> list[Day]:
        file = open(self.filename, 'r')
        try: content: str = file.read()
        except FileExistsError:
            raise Exception("Invalid file") 
        return [Day(**d) for d in json.loads(content)]
        
    def dumps(self, days: list[Day]):
        json.dump(days, open(self.filename, 'w'), default=lambda d: d.model_dump()) 

