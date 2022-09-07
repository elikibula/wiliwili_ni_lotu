from rest_framework import serializers
from datahub.models import DatahubLewenilotu

class DatahubLewenilotuSerializer(serializers.ModelSerializer):
    class Meta:
        model = DatahubLewenilotu
        fields = '__all__'