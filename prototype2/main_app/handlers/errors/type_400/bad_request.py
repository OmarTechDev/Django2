from main_app.handlers.errors.custom_error import CustomError

class BadRequestError(CustomError):
    def __init__(self, message="invalid parameters"):
        super().__init__(message, 400)