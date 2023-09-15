from rest_framework import serializers
from vehicles.models import vehicle, vehicle_type, registered_owner
from drivers.serializers import DriverSerializer
from accounts.serializers import CustomUserSerializer

class VehicleTypeSerializers(serializers.ModelSerializer):
    class Meta:
        model = vehicle_type
        fields = '__all__'

class RegisteredOwnerSerializers(serializers.ModelSerializer):
    class Meta:
        model = registered_owner
        fields = '__all__'

# accessible by enforcer and admin

class VehicleSerializers(serializers.ModelSerializer):

    vehicle_type_ID = VehicleTypeSerializers()
    owner_ID = RegisteredOwnerSerializers()
    officer = CustomUserSerializer(read_only=True)

    class Meta:
        model = vehicle
        fields = '__all__'
        read_only_fields = ('officer',)  # It should be a tuple
