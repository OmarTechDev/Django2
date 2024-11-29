from main_app.handlers.errors.type_400.bad_request import BadRequestError
from main_app.request_validator.validator_interface.estate_interface import ValidatorInterface

class EstateValidator1(ValidatorInterface):

    def validate(self,data:dict) -> bool:
        print("entro",data.get("price"))
        if data.get("price") <=0:
            raise BadRequestError("Validator - Estate: El precio es inferior a 1")
        else:
            return True