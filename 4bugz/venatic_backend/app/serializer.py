from rest_framework import serializers
from .models import User


class UserRegistration_Serializer(serializers.ModelSerializer):
    # here we validate the password of the user to register him or her
    password2 = serializers.CharField(
        style={"input_type": "password", "write_only": True}
    )

    class Meta:
        model = User
        fields = "__all__"
        extra_kwargs = {"password": {"write_only": True}}

    def validate(self, attrs):
        password = attrs.get("password")
        password2 = attrs.get("password2")
        if password != password2:
            raise serializers.ValidationError(
                "Password and conform password doesnot match "
            )
        return super().validate(attrs)

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)


# userlogin serializer.
class UserLogin_Serializer(serializers.ModelSerializer):
    email = serializers.EmailField(max_length=255)

    class Meta:
        model = User
        fields = ["email", "password"]

class Userprofileserializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields="__all__"

from .models import ActionUser,ResourceUploader


class ActionUser_Serialization(serializers.ModelSerializer):
    class Meta:
        model = ActionUser
        fields = "__all__"

class Resource_Serialization(serializers.ModelSerializer):
    class Meta:
        model = ResourceUploader
        fields = "__all__" 


class ActionUserDetail_Serializer(serializers.ModelSerializer):
    class Meta:
        model=ActionUser
        fields = "_all_"
        depth=1        
        
