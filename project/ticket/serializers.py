from rest_framework import serializers
from ticket.models import penalty, violation, traffic_violation, ticket
from accounts.serializers import CustomUserSerializer

class penaltySerializers(serializers.ModelSerializer):
    class Meta:
        model = penalty
        fields = "__all__"

class violationSerializer(serializers.ModelSerializer):
    penalty_ID = penaltySerializers(read_only=True)
    penalty = serializers.IntegerField(write_only=True)

    class Meta:
        model = violation
        fields = '__all__'

    
    
class traffic_violationSerializer(serializers.ModelSerializer):
    class Meta:
        model = traffic_violation
        fields = "__all__"

class ticketSerializer(serializers.ModelSerializer):
    user_ID = CustomUserSerializer(read_only=True)

    class Meta:
        model = ticket
        fields = "__all__"
        read_only_fields = ('user_ID',)
    