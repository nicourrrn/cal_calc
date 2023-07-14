from json import loads

from cal_calc.models import Day, Product
from cal_calc.repos import base

class JsonRepo(base.AbstractBaseRepo):
    def __init__(self, filename: str = "days.json"):
        self.filename = filename 
        
    def loads(self) -> base.AbstractBaseRepo.Data: 
        file = open(self.filename, 'r')
        try: content: str = file.read()
        except FileExistsError:
            raise Exception("Invalid file") 
        return self.Data(**loads(content))
        
    def dumps(self, days: list[Day], products: list[Product]):
        with open(self.filename, 'w') as file:
            file.write(self.Data(products=products, days=days).model_dump_json())

