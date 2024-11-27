from abc import abstractmethod

from main_app.services.service_interface import ServiceBaseInterface

class EstateInterface(ServiceBaseInterface):

    @abstractmethod
    def operate_external(self,data:dict)->dict:
        pass