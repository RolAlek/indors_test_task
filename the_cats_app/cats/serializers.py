from rest_framework import serializers
import webcolors

from .models import Cat


class HexColorToName(serializers.Field):
    def to_representation(self, value):
        return value
    
    def to_internal_value(self, data):
        try:
            data = webcolors.hex_to_name(data)
        except ValueError as exc:
            raise serializers.ValidationError(
                'There is no name for this color.'
            ) from exc
        return data

class CatSerializer(serializers.ModelSerializer):
    color = HexColorToName()
    class Meta:
        model = Cat
        fields = ["name", "color", "hairiness", "years"]
