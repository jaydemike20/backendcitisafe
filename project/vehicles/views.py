from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from vehicles.models import vehicle, vehicle_type, registered_owner
from vehicles.serializers import VehicleSerializers, VehicleTypeSerializers, RegisteredOwnerSerializers
from rest_framework.permissions import IsAuthenticated
from accounts.permissions import EnforcerPermission, AdminPermission, TreasurerPermission


# Create your views here.

# access only by admin
class VehicleTypeListCreateAPIView(ListCreateAPIView):
    serializer_class = VehicleTypeSerializers
    queryset = vehicle_type.objects.all()
    permission_classes = [IsAuthenticated & (AdminPermission)]

class VehicleTypeRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = VehicleTypeSerializers
    queryset = vehicle_type.objects.all()
    permission_classes = [IsAuthenticated & (AdminPermission)]


# access only by enforcer
class RegisteredOwnerListCreateAPIView(ListCreateAPIView):
    serializer_class = RegisteredOwnerSerializers
    queryset = registered_owner.objects.all()
    permission_classes = [IsAuthenticated & (EnforcerPermission | AdminPermission)]

class RegisteredOwnerRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = RegisteredOwnerSerializers
    queryset = registered_owner.objects.all()
    permission_classes = [IsAuthenticated & (EnforcerPermission | AdminPermission)]
    
class VehicleListCreateAPIView(ListCreateAPIView):
    serializer_class = VehicleSerializers
    queryset = vehicle.objects.all()
    permission_classes = [IsAuthenticated & (AdminPermission | EnforcerPermission | TreasurerPermission)]

    def perform_create(self, serializer):
        # Set the user as the authenticated user when creating a driver instance
        serializer.save(officer=self.request.user)    

class VehicleRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = VehicleSerializers
    queryset = vehicle.objects.all()
    permission_classes = [IsAuthenticated & (AdminPermission | EnforcerPermission | TreasurerPermission)]
