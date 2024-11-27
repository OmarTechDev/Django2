from main_app.handlers.errors.type_400.bad_request import BadRequestError
from main_app.request_validator.validator_interface.estate_interface import ValidatorInterface

class EstateValidator2(ValidatorInterface):

    def validate(self, data: dict) -> bool:
        if data.get("rooms") <= 0:
            raise BadRequestError("Validator - Estate: El precio es inferior a 1")
        else:
            return True
