from rest_framework import serializers
from vehicles.models import vehicle, vehicle_type

class VehicleTypeSerializers(serializers.ModelSerializer):
    class Meta:
        model = vehicle_type
        fields = '__all__'

class VehicleSerializers(serializers.ModelSerializer):

    class Meta:
        model = vehicle
        fields = '__all__'

