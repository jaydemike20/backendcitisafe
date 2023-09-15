from rest_framework import serializers
from drivers.models import Driver, Classification
from accounts.serializers import CustomUserSerializer

class ClassificationSerializer(serializers.ModelSerializer):

    class Meta:
        model = Classification
        fields = '__all__' 


class DriverSerializer(serializers.ModelSerializer):
    officer = CustomUserSerializer(read_only=True)

    class Meta:
        model = Driver
        fields = '__all__'
        read_only_fields = ('officer',)  # It should be a tuple

