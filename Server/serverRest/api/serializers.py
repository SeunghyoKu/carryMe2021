from rest_framework import serializers
from .models import Example

# Serializer: response 형태 정해주기

class BaseExampleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Example
        fields = ['id', 'title', 'numView']