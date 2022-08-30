from .models import *
from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from timezone_field.rest_framework import TimeZoneSerializerField

class CatSerializer(ModelSerializer):
   
    class Meta:
        model = Cat
        fields = '__all__'


class CatUpdateSerializer(ModelSerializer):
    
    class Meta:
        model = Cat
        fields = ['zone',]        