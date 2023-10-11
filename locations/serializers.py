from rest_framework import serializers

from locations.models import Location
from users.serializers import UserSerializer


class LocationsSerializer(serializers.ModelSerializer):
    user = UserSerializer(source='location', read_only=True)

    class Meta:
        model = Location
        read_only_fields = ('pk', 'user',)
        fields = (
            'pk',
            'name',
            'user',
        )
