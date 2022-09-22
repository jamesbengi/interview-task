import email
from unittest.util import _MAX_LENGTH
from rest_framework import serializers
class TaskSerializer(serializers.Serializer):
    fullnames=serializers.CharField(max_length=100)
    email=serializers.EmailField()
    phone=serializers.CharField(max_length=100)
    address=serializers.CharField(max_length=100)
    