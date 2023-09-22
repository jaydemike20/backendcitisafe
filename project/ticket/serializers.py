from rest_framework import serializers
from ticket.models import penalty, violation, traffic_violation, ticket


class penaltySerializers(serializers.ModelSerializer):
    class Meta:
        model = penalty
        fields = "__all__"

class violationSerializer(serializers.ModelSerializer):
    class Meta:
        model = violation
        fields = '__all__'

class traffic_violationSerializer(serializers.ModelSerializer):
    class Meta:
        model = traffic_violation
        fields = "__all__"

class ticketSerializer(serializers.ModelSerializer):
    class Meta:
        model = ticket
        fields = "__all__"