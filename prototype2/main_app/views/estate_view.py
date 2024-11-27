from wsgiref.validate import validator

from rest_framework.viewsets import ViewSet
from main_app.handlers.api_gateway_response import ApiGateWayResponse
from main_app.models.estate import Estate
from main_app.request_validator.estate_validator_1 import EstateValidator1
from main_app.request_validator.estate_validator_2 import EstateValidator2
from main_app.serializers.estate_serializer import EstateSerializer
from main_app.services.estate.estate_service_1 import EstateService1


class EstateViewSet(ViewSet):

    def list(self,request):
        serializer = EstateSerializer(Estate.objects.all(),many=True)
        return ApiGateWayResponse.success_response(serializer.data)

    def retrieve(self,request,pk:int):
        serializer = EstateSerializer(Estate.objects.get(pk=pk))
        return ApiGateWayResponse.success_response(serializer.data)

    def create(self,request):
        try:
            serializer = EstateSerializer(data = request.data)
            serializer.is_valid(raise_exception=True)
            data = serializer.validated_data
            #validators = ["verify.validador1", "verify.validador1"]
            validators = [
                EstateValidator1(),
                EstateValidator2()
            ]
            for validator in validators:
                validator.validate(data)

            service = EstateService1()
            data = service.operate(data)
            #concepto por reflexion instanciar los validadores,
            serializer = EstateSerializer(data=data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return ApiGateWayResponse.success_response(serializer.data)
        except Exception as e:
            return ApiGateWayResponse.exception_response(e)

    def update(self,request,pk:int):
        try:
            serializer = EstateSerializer(instance=Estate.objects.get(pk=pk),data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return ApiGateWayResponse.success_response(serializer.data)
        except Exception as e:
            return ApiGateWayResponse.exception_response(e)

    def partial_update(self,request,pk:int):
        try:
            serializer = EstateSerializer(instance=Estate.objects.get(pk=pk),data=request.data,partial=True)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return ApiGateWayResponse.success_response(serializer.data)
        except Exception as e:
            return ApiGateWayResponse.exception_response(e)

    def destroy(self,request,pk:int):
        try:
            product = Estate.objects.get(pk=pk)
            product.delete()
            return ApiGateWayResponse.success_response("registro eliminado")
        except Exception as e:
        #except Estate.DoesNotExist:
            return ApiGateWayResponse.exception_response(e)

    # @action(detail=False, methods=['get'], url_path='owner/(?P<owner_id>[^/.]+)')
    # def estates_by_owner(self, request, owner_id):
    #     estates = Estate.objects.filter(owner_id=owner_id)
    #     serializer = EstateSerializer(estates, many=True)
    #     return Response(status=status.HTTP_200_OK, data=serializer.data)



