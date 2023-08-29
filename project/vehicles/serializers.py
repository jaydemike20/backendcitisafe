from rest_framework import serializers
from vehicles.models import vehicle, vehicle_type, registered_owner

class VehicleTypeSerializers(serializers.ModelSerializer):
    class Meta:
        model = vehicle_type
        fields = '__all__'

class RegisteredOwnerSerializers(serializers.ModelSerializer):
    class Meta:
        model = registered_owner
        fields = '__all__'

class VehicleSerializers(serializers.ModelSerializer):
    class Meta:
        model = vehicle
        fields = '__all__'    