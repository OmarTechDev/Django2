from abc import ABC,abstractmethod

class ServiceBaseInterface(ABC):
    @abstractmethod
    def operate(self,data:dict)-> dict:
        pass
