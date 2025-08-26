from rest_framework import serializers

from .models import Habit
from .validators import (HabitDurationValidator, HabitHasHabitRewardValidator,
                         HabitPeriodValidator, HabitRewardValidator,
                         RewardHabitValidator)


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
        exclude = ["user"]
        extra_kwargs = {
            "user": {"required": False},
            "is_enjoyable": {"required": True},
            "period": {"required": True},
            "duration": {"required": True},
            "is_public": {"required": True},
        }
