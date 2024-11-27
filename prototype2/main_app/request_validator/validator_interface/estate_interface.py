from abc import ABC,abstractmethod

class ValidatorInterface(ABC):
    @abstractmethod
    def validate(self,data:dict)-> bool:
        pass
