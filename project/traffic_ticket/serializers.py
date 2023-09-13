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

    def create(self, validated_data):
        traffic_violation_data = validated_data.pop('traffic_violation')
        ticket = ticket.objects.create(**validated_data)

        for violation_data in traffic_violation_data:
            traffic_violation, created = traffic_violation.objects.get_or_create(**violation_data)
            ticket.traffic_violation.add(traffic_violation)

        return ticket
