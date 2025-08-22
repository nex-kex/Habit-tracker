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

    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

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
