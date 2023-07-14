from cal_calc.models import Day
import base
import json

class JsonRepo(base.AbstractBaseRepo):
    def __init__(self, filename: str = "days.json"):
        self.file = open(filename, 'rw')
        
    def loads(self) -> list[Day]:
        try: content: str = self.file.read()
        except FileExistsError:
            raise Exception("Invalid file") 
        return [Day(**d) for d in json.loads(content)]
        
    def dumps(self, days: list[Day]):
        json.dumps(days, default=lambda d: d.__dict__) 

