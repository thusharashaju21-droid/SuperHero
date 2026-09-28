from rest_framework import serializers
from hero.models import SuperHero

class HeroSerializer(serializers.Serializer):

    id = serializers.CharField(read_only=True)

    name = serializers.CharField()

    power = serializers.CharField()

    universe = serializers.CharField()

    city = serializers.CharField()

    team = serializers.CharField()