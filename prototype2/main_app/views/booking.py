from rest_framework.response import Response
from rest_framework.viewsets import ViewSet
from rest_framework import status
from Booking.models import Booking
from Booking.serializer import BookingSerializer
from Booking.service import BookingService

class BookingViewSet(ViewSet):

    def list(self,request):
        serializer = BookingSerializer(Booking.objects.all(),many=True)
        return Response(status=status.HTTP_200_OK,data= serializer.data)
    def retrieve(self,request,pk:int):
        serializer = BookingSerializer(Booking.objects.get(pk=pk))
        return Response(status=status.HTTP_200_OK,data= serializer.data)

    def create(self,request):
        serializer = BookingSerializer(data = request.data)
        serializer.is_valid(raise_exception=True)
        estate = serializer.validated_data["estate_id"]
        print(estate)
        if BookingService.verify_available(estate):
            print("esta disponible")
            serializer.save()
        else:
            print("no esta disponible")
        return Response(status=status.HTTP_200_OK,data=serializer.data)
        #recibo la informacion
        # consultar al servicio que la habitacion este disponible.
        # consultar que el pago se hizo. al servicio
    def update(self,request,pk:int):
        serializer = BookingSerializer(instance=Booking.objects.get(pk=pk),data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(status=status.HTTP_200_OK, data=serializer.data)

    def partial_update(self,request,pk:int):
        serializer = BookingSerializer(instance=Booking.objects.get(pk=pk),data=request.data,partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(status=status.HTTP_200_OK, data=serializer.data)

    def destroy(self,request,pk:int):
        try:
            product = Booking.objects.get(pk=pk)
            product.delete()
            return Response(status=status.HTTP_200_OK, data={pk: "eliminado"})
        except Booking.DoesNotExist:
            return Response(status=status.HTTP_200_OK, data={pk:"no existe"})
