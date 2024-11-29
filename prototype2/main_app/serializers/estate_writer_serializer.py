from rest_framework.serializers import ModelSerializer
from main_app.models.estate import Estate
from rest_framework import serializers

class EstateWriterSerializer(ModelSerializer):
    class Meta:
        model = Estate
        fields= ['id','name','rooms','bathrooms','floors','price','is_available']
