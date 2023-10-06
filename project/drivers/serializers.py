from rest_framework import serializers
from drivers.models import Driver, Classification
from accounts.serializers import CustomUserSerializer
from datetime import datetime

class ClassificationSerializer(serializers.ModelSerializer):

    class Meta:
        model = Classification
        fields = '__all__' 



class DriverSerializer(serializers.ModelSerializer):
    officer = CustomUserSerializer(read_only=True)
    birthdate = serializers.DateField(format='%Y/%m/%d')
    expiration_date = serializers.DateField(format='%Y/%m/%d')


    def to_internal_value(self, data):
        # Convert the input date formats to the internal format ('YYYY-MM-DD')
        data['birthdate'] = datetime.strptime(data['birthdate'], '%Y/%m/%d').date()
        data['expiration_date'] = datetime.strptime(data['expiration_date'], '%Y/%m/%d').date()
        return super().to_internal_value(data)

    def validate_birthdate(self, value):
        # Validation logic for birthdate
        return value

    def validate_expiration_date(self, value):
        # Validation logic for expiration_date
        return value


    class Meta:
        model = Driver
        fields = '__all__'
        read_only_fields = ('officer',)  # It should be a tuple
