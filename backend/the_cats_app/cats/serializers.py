import datetime

import webcolors
from rest_framework import serializers

from .models import Cat


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
