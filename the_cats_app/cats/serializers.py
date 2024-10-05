from rest_framework import serializers

from .models import Cat


class CatSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cat
        # fields = ["name", "color", "hairiness", "birth_date"]
        fields = '__all__'
