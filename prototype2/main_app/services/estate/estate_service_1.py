from main_app.services.estate.estate_interface import EstateInterface


class EstateService1(EstateInterface):

    def operate(self,data:dict) -> dict:
        #operar informacion de manera interna
        return data

    def operate_external(self,data:dict) ->dict:
        #consumir un servicio externo
        return data