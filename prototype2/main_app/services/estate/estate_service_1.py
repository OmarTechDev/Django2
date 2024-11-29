from main_app.repositories.register_estate import RegisterEstate
from main_app.services.estate.estate_interface import EstateInterface


class EstateService1(EstateInterface):

    def operate(self,data:dict) -> dict:
        #operar informacion de manera interna
        # se transforma ladata
        register = RegisterEstate()
        result = register.save_estate(data)
        return result

    def operate_external(self,data:dict) ->dict:
        #consumir un servicio externo
        return data