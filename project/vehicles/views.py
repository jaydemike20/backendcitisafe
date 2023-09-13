from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from vehicles.models import vehicle, vehicle_type, registered_owner
from vehicles.serializers import VehicleSerializers, VehicleTypeSerializers, OwnerSerializers
from rest_framework.permissions import IsAuthenticated
from accounts.permissions import EnforcerPermission, AdminPermission


# Create your views here.

# accessible only by admin
class VehicleTypeListCreateAPIView(ListCreateAPIView):
    serializer_class = VehicleTypeSerializers
    queryset = vehicle_type.objects.all()
    # permission_classes = [IsAuthenticated & (AdminPermission)]

class VehicleTypeRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = VehicleTypeSerializers
    queryset = vehicle_type.objects.all()
    # permission_classes = [IsAuthenticated & (AdminPermission)]

class OwnerListCreateAPIView(ListCreateAPIView):
    serializer_class = OwnerSerializers
    queryset = registered_owner.objects.all()
    # permission_classes = [IsAuthenticated & (EnforcerPermission)]

class OwnerRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = OwnerSerializers
    queryset = registered_owner.objects.all()
    # permission_classes = [IsAuthenticated & (EnforcerPermission)]


class VehicleListCreateAPIView(ListCreateAPIView):
    serializer_class = VehicleSerializers
    queryset = vehicle.objects.all()
    # permission_classes = [IsAuthenticated & (EnforcerPermission | AdminPermission)]

class VehicleRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = VehicleSerializers
    queryset = vehicle.objects.all()
    # permission_classes = [IsAuthenticated & (EnforcerPermission | AdminPermission)]