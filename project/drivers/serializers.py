from rest_framework import serializers
from drivers.models import Driver, Classification

class ClassificationSerializer(serializers.ModelSerializer):

    class Meta:
        model = Classification
        fields = '__all__'


class DriverSerializer(serializers.ModelSerializer):
    
    classification_type = Classification()

    class Meta:
        model = Driver
        fields = '__all__'

    
