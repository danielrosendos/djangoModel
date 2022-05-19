from rest_framework import serializers

class ResponseSerializer(serializers.Serializer):
    message = serializers.CharField(required=False)
    data = serializers.ListField(required=False)