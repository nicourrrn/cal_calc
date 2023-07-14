from cal_calc.models import Day

from abc import abstractmethod


class AbstractBaseRepo:
    
    @abstractmethod
    def loads(self) -> list[Day]:
        ...

    @abstractmethod
    def dumps(self, entries: list[Day]):
        ...


