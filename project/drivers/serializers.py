from rest_framework import serializers
from drivers.models import Driver, Classification
from accounts.serializers import CustomUserSerializer

class ClassificationSerializer(serializers.ModelSerializer):

    class Meta:
        model = Classification
        fields = '__all__' 


class DriverSerializer(serializers.ModelSerializer):
    officer = CustomUserSerializer(read_only=True)
    # classification = serializers.SerializerMethodField()

    class Meta:
        model = Driver
        fields = '__all__'
        read_only_fields = ('officer',)  # It should be a tuple

    def get_classification(self, obj):
        classification = obj.classification  # Get the related Classification object
        if classification:
            # Serialize the Classification object using the ClassificationSerializer
            classification_data = ClassificationSerializer(classification).data
            return classification_data
        return None  # Return None if there is no related Classification

    def to_representation(self, instance):
        # Override to_representation to include classification like officer
        representation = super().to_representation(instance)
        classification_data = representation.pop('classification', None)
        if classification_data:
            representation['classification'] = classification_data
        return representation