from django.shortcuts import render
from .models import *
from .serializers import *
from rest_framework import generics

# Create your views here.
class CatCreateView(generics.CreateAPIView):
    queryset = Cat.objects.all()
    serializer_class = CatSerializer

class CatListView(generics.ListAPIView):
    queryset = Cat.objects.all().order_by('-id')
    serializer_class = CatSerializer

class CatUpdateView(generics.RetrieveUpdateAPIView):
    lookup_field = 'id'
    queryset = Cat.objects.all()
    serializer_class = CatUpdateSerializer
    

class CatDeleteView(generics.DestroyAPIView):
    lookup_field = 'id'
    queryset = Cat.objects.all()
    serializer_class = CatSerializer 

class CatRetrieveView(generics.RetrieveAPIView):
    lookup_field = 'id'
    queryset = Cat.objects.all()
    serializer_class = CatSerializer  


     
   
