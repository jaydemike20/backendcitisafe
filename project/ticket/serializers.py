from rest_framework import serializers
from ticket.models import penalty, violation, traffic_violation, ticket
from accounts.serializers import CustomUserSerializer
from drivers.serializers import DriverSerializer
from vehicles.serializers import VehicleSerializers
from datetime import datetime

class penaltySerializers(serializers.ModelSerializer):
    class Meta:
        model = penalty
        fields = "__all__"

class violationSerializer(serializers.ModelSerializer):
    penalty_info = penaltySerializers(source='penalty_ID', read_only=True)
    vehicle_types = serializers.CharField(source='vehicle_type', read_only=True)

    class Meta:
        model = violation
        fields = '__all__'


    
    
# class traffic_violationSerializer(serializers.ModelSerializer):

#     violations_info = violationSerializer(many=True, read_only=True)


#     class Meta:
#         model = traffic_violation
#         fields = "__all__"

# class ticketSerializer(serializers.ModelSerializer):
#     user_ID = CustomUserSerializer(read_only=True)
#     driver_info = DriverSerializer(source='driver_ID', read_only=True)
#     violation_info = traffic_violationSerializer(source='violations', read_only=True)
#     vehicle_info = VehicleSerializers(source='vehicle', read_only=True)

#     date_issued = serializers.DateTimeField(format='%Y-%m-%d %H:%M:%S')


#     def to_internal_value(self, data):
#         # Convert the input date formats to the internal format ('YYYY-MM-DD')
#         data['date_issued'] = datetime.strptime(data['date_issued'], '%Y-%m-%d %H:%M:%S').date()
#         return super().to_internal_value(data)

#     def validate_dateissued(self, value):
#         # Validation logic for birthdate
#         return value
    
         
#     class Meta:
#         model = ticket
#         fields = "__all__"
#         read_only_fields = ('user_ID',)
class traffic_violationSerializer(serializers.ModelSerializer):
    violations_info = serializers.SerializerMethodField()

    def get_violations_info(self, obj):
        return [violation.violation_type for violation in obj.violation_id.all()]

    class Meta:
        model = traffic_violation
        fields = "__all__"


class ticketSerializer(serializers.ModelSerializer):
    user_ID = CustomUserSerializer(read_only=True)
    driver_info = DriverSerializer(source='driver_ID', read_only=True)
    violation_info = traffic_violationSerializer(source='violations', read_only=True)
    vehicle_info = VehicleSerializers(source='vehicle', read_only=True)
 

    class Meta:
        model = ticket
        fields = "__all__"
        read_only_fields = ('user_ID',)
