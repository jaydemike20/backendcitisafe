from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from traffic_ticket.models import penalty, violation, traffic_violation, ticket
from traffic_ticket.serializers import PenaltySerializers, ViolationSerializers, TrafficViolationSerializers, TicketSerializers
from rest_framework.permissions import IsAuthenticated

from accounts.permissions import EnforcerPermission, AdminPermission, TreasurerPermission

from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework import status

# Create your views here.

class PenaltyListCreateAPIView(ListCreateAPIView):
    serializer_class = PenaltySerializers
    queryset = penalty.objects.all()

class PenaltyRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = PenaltySerializers
    queryset = penalty.objects.all()


class ViolationListCreateAPIView(ListCreateAPIView):
    serializer_class = ViolationSerializers
    queryset = violation.objects.all()

class ViolationRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = ViolationSerializers
    queryset = violation.objects.all()


class TrafficViolationListCreateAPIView(ListCreateAPIView):
    serializer_class = TrafficViolationSerializers
    queryset = traffic_violation.objects.all()

class TrafficViolationRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = TrafficViolationSerializers
    queryset = traffic_violation.objects.all()


class TicketListCreateAPIView(ListCreateAPIView):
    serializer_class = TicketSerializers
    queryset = ticket.objects.all()

class TicketRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = TicketSerializers
    queryset = ticket.objects.all()