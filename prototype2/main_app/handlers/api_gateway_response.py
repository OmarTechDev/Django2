from rest_framework.response import Response
from rest_framework import status

from main_app.const.types import ResponseBody
from main_app.handlers.errors.custom_error import CustomError

class ApiGateWayResponse:
    @staticmethod
    def response(body: ResponseBody,code: int):
        return Response(status=code,data = body)

    @staticmethod
    def exception_response(exc):
        if isinstance(exc,CustomError):
            return ApiGateWayResponse.response(exc.to_dict(),code= exc.status_code)
        return ApiGateWayResponse.response({"body": str(exc),"message":"error"},code=status.HTTP_500_INTERNAL_SERVER_ERROR)

    @staticmethod
    def success_response(data:dict):
        return ApiGateWayResponse.response({"body":data, "message":"success"}, code= status.HTTP_200_OK)