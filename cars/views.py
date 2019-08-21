from django.shortcuts import render
from rest_framework import generics
from cars.serializers import *
from cars.models import Car


class CarCreateView(generics.CreateAPIView):
    serializer_class = CarDetailSerializer

class CarListView(generics.ListAPIView):
    serializer_class = CarsListSerializer
    queryset = Car.objects.all()

class CarDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = CarDetailSerializer
    queryset = Car.objects.all()