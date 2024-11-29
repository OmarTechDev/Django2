from rest_framework.serializers import ModelSerializer

from main_app.models import Estate
from main_app.models.booking import Booking
from rest_framework import serializers

class BookingSerializer(ModelSerializer):
    #estate_id = serializers.PrimaryKeyRelatedField(queryset=Estate.objects.all())
    class Meta:
        model= Booking
        fields= ['id','register_date','days','total_amount','start_date','end_date',
                    'is_paid','estate_id']