from main_app.handlers.errors.custom_error import CustomError


class GatewayTimeoutError(CustomError):
    def __init__(self, message="Se agoto el tiempo de espera"):
        super().__init__(message, 504)