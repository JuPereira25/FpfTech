from rest_framework import serializers
from .models import Client

class ClientSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(max_length=70)
    age = serializers.IntegerField(
        min_value=18,
        max_value=100
    )

    class Meta:
        model = Client
        fields = ['id', 'name', 'age', 'created_at']