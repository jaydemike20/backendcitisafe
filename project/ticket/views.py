from django.shortcuts import render
from ticket.serializers import penaltySerializers, violationSerializer, traffic_violationSerializer, ticketSerializer
from ticket.models import penalty, violation, traffic_violation, ticket
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from accounts.permissions import EnforcerPermission, AdminPermission, TreasurerPermission
from rest_framework.permissions import IsAuthenticated

# Create your views here.

class penaltyListCreateAPIView(ListCreateAPIView):
    serializer_class = penaltySerializers
    queryset = penalty.objects.all()
    # permission_classes = [IsAuthenticated & (AdminPermission)]


class penaltyRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = penaltySerializers
    queryset = penalty.objects.all()
    # permission_classes = [IsAuthenticated & (AdminPermission)]
    


class violationListCreateAPIView(ListCreateAPIView):
    serializer_class = violationSerializer
    queryset = violation.objects.all()
    # permission_classes = [IsAuthenticated & (AdminPermission)]


class violationRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = violationSerializer
    queryset = violation.objects.all()
    permission_classes = [IsAuthenticated & (AdminPermission)]



class trafficviolationListCreateAPIView(ListCreateAPIView):
    serializer_class = traffic_violationSerializer
    queryset = traffic_violation.objects.all()
    # permission_classes = [IsAuthenticated & (AdminPermission)]


class trafficviolationRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = traffic_violationSerializer
    queryset = traffic_violation.objects.all()
    permission_classes = [IsAuthenticated & (AdminPermission)]


class ticketListCreateAPIView(ListCreateAPIView):
    serializer_class = ticketSerializer
    queryset = ticket.objects.all()
    # permission_classes = [IsAuthenticated & (EnforcerPermission)]

    # def get_queryset(self):
    #     # Filter traffic tickets based on the logged-in officer
    #     return ticket.objects.filter(user_ID=self.request.user)

    def perform_create(self, serializer):
        # Set the user as the authenticated user when creating a driver instance
        serializer.save(user_ID=self.request.user)


class ticketRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = ticketSerializer
    queryset = ticket.objects.all()
    permission_classes = [IsAuthenticated & (AdminPermission | EnforcerPermission | TreasurerPermission)]
