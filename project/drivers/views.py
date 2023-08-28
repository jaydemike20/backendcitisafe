from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from drivers.models import Classification, Driver
from drivers.serializers import ClassificationSerializer, DriverSerializer

# Create your views here.

class ClassificationListCreateAPIView(ListCreateAPIView):
    serializer_class = ClassificationSerializer
    queryset = Classification.objects.all()


class ClassificationRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = ClassificationSerializer
    queryset = Classification.objects.all()


class DriverListCreateAPIView(ListCreateAPIView):
    serializer_class = DriverSerializer
    queryset = Driver.objects.all()


class DriverRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = DriverSerializer
    queryset = Driver.objects.all()    