from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from drivers.models import Classification, Driver
from drivers.serializers import ClassificationSerializer, DriverSerializer
from rest_framework.permissions import IsAuthenticated

from accounts.permissions import EnforcerPermission, AdminPermission


# Create your views here.

class ClassificationListCreateAPIView(ListCreateAPIView):
    serializer_class = ClassificationSerializer
    queryset = Classification.objects.all()
    permission_classes = [AdminPermission]

class ClassificationRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = ClassificationSerializer
    queryset = Classification.objects.all()
    permission_classes = [AdminPermission]

class DriverListCreateAPIView(ListCreateAPIView):
    serializer_class = DriverSerializer
    queryset = Driver.objects.all()
    # permission_classes = [IsAuthenticated & (EnforcerPermission)]



class DriverRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = DriverSerializer
    queryset = Driver.objects.all()    
    permission_classes = [IsAuthenticated & (AdminPermission | EnforcerPermission)]
    