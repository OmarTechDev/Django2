# main_app/handlers/validator_handler.py

import importlib
from main_app.request_validator.estate_validator_setting import VALIDATORS


class ValidatorHandler:

    @staticmethod
    def load_validators(view_name, method_name):
        validator_paths = VALIDATORS.get(view_name, {}).get(method_name, [])
        validators = []
        for path in validator_paths:
            module_name, class_name = path.rsplit('.', 1)  # Divide en "modulo.clase"
            module = importlib.import_module(module_name)  # Importa el módulo
            validator_class = getattr(module, class_name)  # Obtén la clase
            validators.append(validator_class())          # Instancia la clase
        return validators

    @staticmethod
    def execute_validators(validators, data:dict):
        for validator in validators:
            validator.validate(data)
