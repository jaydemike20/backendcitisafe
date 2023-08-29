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
    permission_classes = [IsAuthenticated & (EnforcerPermission)]


    # def get_queryset(self):
    #     # Return only the drivers associated with the authenticated user
    #     return Driver.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        # Set the user as the authenticated user when creating a driver instance
        serializer.save(user=self.request.user)


class DriverRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = DriverSerializer
    queryset = Driver.objects.all()    
    permission_classes = [IsAuthenticated & (AdminPermission | EnforcerPermission)]
    