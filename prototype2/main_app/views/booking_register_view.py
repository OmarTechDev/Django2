from pickletools import uint1

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from main_app.serializers.booking.booking_writer_serializer import BookingSerializer
from main_app.services.booking.booking_service import BookingService1


@api_view(['POST'])
def register_booking(request):
    serializer = BookingSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    data = serializer.validated_data
    result = BookingService1().operate(data)
    print("result", result)
    return Response(status=status.HTTP_200_OK,data =result)