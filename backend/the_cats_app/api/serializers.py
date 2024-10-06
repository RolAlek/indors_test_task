import datetime

from django.contrib.auth import get_user_model
from rest_framework import serializers
import webcolors

from cats.models import Cat

User = get_user_model()


class HexColorToName(serializers.Field):
    def to_representation(self, value):
        return value

    def to_internal_value(self, data):
        try:
            data = webcolors.hex_to_name(data)
        except ValueError as exc:
            raise serializers.ValidationError(
                "There is no name for this color."
            ) from exc
        return data


class CatSerializer(serializers.ModelSerializer):
    color = HexColorToName()
    age = serializers.SerializerMethodField()

    class Meta:
        model = Cat
        fields = [
            "name",
            "color",
            "hairiness",
            "birth_year",
            "owner",
            "age",
        ]
        read_only_fields = ["owner"]

    def create(self, validated_data):
        validated_data["owner"] = self.context["request"].user
        return super().create(validated_data)

    def validate_birth_year(self, value):
        if value > datetime.date.today().year:
            raise serializers.ValidationError(
                "Birth year can't be in the future",
            )
        return value

    def get_age(self, obj):
        return datetime.date.today().year - obj.birth_year


class UserRegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            "email",
            "password",
            "username",
            "first_name",
            "last_name",
        ]
        extra_kwargs = {
            "password": {"write_only": True},
            "email": {"required": True},
            "first_name": {"required": True},
            "last_name": {"required": True},
        }

    def create(self, validated_data):
        password = validated_data.pop('password')
        user = User.objects.create_user(**validated_data)
        user.set_password(password)
        user.save()
        return user
