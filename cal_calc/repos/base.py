from pydantic import BaseModel

from cal_calc.models import Day, Product

from abc import abstractmethod


class AbstractBaseRepo:
    
    class Data(BaseModel):
        products: list[Product]
        days: list[Day]

    @abstractmethod
    def loads(self) -> Data:
        ...

    @abstractmethod
    def dumps(self, days: list[Day], products: list[Product]):
        ...


