from django.shortcuts import render
from ticket.serializers import penaltySerializers, violationSerializer, traffic_violationSerializer, ticketSerializer
from ticket.models import penalty, violation, traffic_violation, ticket
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

# Create your views here.

class penaltyListCreateAPIView(ListCreateAPIView):
    serializer_class = penaltySerializers
    queryset = penalty.objects.all()

class penaltyRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = penaltySerializers
    queryset = penalty.objects.all()


class violationListCreateAPIView(ListCreateAPIView):
    serializer_class = violationSerializer
    queryset = violation.objects.all()

class violationRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = violationSerializer
    queryset = violation.objects.all()


class trafficviolationListCreateAPIView(ListCreateAPIView):
    serializer_class = traffic_violationSerializer
    queryset = traffic_violation.objects.all()

class trafficviolationRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = traffic_violationSerializer
    queryset = traffic_violation.objects.all()

class ticketListCreateAPIView(ListCreateAPIView):
    serializer_class = ticketSerializer
    queryset = ticket.objects.all()



    def perform_create(self, serializer):
        # Set the user as the authenticated user when creating a driver instance
        serializer.save(user_ID=self.request.user)


class ticketRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = ticketSerializer
    queryset = ticket.objects.all()
