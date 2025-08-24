from rest_framework import serializers

from .models import Habit
from .validators import (
    HabitPeriodValidator,
    RewardHabitValidator,
    HabitDurationValidator,
    HabitRewardValidator,
    HabitHasHabitRewardValidator,
)


class HabitSerializer(serializers.ModelSerializer):
    class Meta:
        model = Habit
        validators = [
            HabitPeriodValidator(),
            HabitDurationValidator(),
            RewardHabitValidator(),
            HabitRewardValidator(),
            HabitHasHabitRewardValidator(),
        ]
        fields = "__all__"
        extra_kwargs = {
            "is_enjoyable": {"required": True},
            "period": {"required": True},
            "duration": {"required": True},
            "is_public": {"required": True},
        }
