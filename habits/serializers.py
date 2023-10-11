from rest_framework import serializers

from habits.models import Habit
from locations.models import Location


class HabitsSerializer(serializers.ModelSerializer):
    location = serializers.CharField()

    class Meta:
        model = Habit
        read_only_fields = ('pk', 'owner',)
        fields = (
            'pk',
            'owner',
            'location',
            'time_to_behave',
            'behavior',
            'is_satisfying',
            'is_good',
            'connected_habit',
            'period_days',
            'reward',
            'time_to_complete',
            'is_public',
        )

    def create(self, validated_data):
        location_name = validated_data.pop('location')
        user = self.context['request'].user
        location, _ = Location.objects.get_or_create(
            name=location_name,
            user=user
        )
        validated_data['owner'] = user
        habit = Habit.objects.create(
            location=location, **validated_data
        )

        return habit
