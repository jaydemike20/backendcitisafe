from rest_framework import serializers
from traffic_ticket.models import penalty, violation, traffic_violation, ticket

class PenaltySerializers(serializers.ModelSerializer):
    class Meta:
        model = penalty
        fields = '__all__'

class ViolationSerializers(serializers.ModelSerializer):
    class Meta:
        model = violation
        fields = '__all__'

class TrafficViolationSerializers(serializers.ModelSerializer):

    class Meta:
        model = traffic_violation
        fields = '__all__'

class TicketSerializers(serializers.ModelSerializer):

    class Meta:
        model = ticket
        fields = '__all__'


