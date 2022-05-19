from rest_framework import serializers

from ..Models.UserModel import UserModel

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserModel
        fields = "__all__"


class UpdateUserSerializar(serializers.Serializer):
    username = serializers.CharField(
        max_length=255
    )
    new_username = serializers.CharField(
        max_length=255,
        required=False
    )
    email = serializers.EmailField(
        max_length=255
    )
