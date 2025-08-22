from rest_framework.serializers import ValidationError
from datetime import timedelta

from tracker.models import Habit


class HabitRewardValidator:
    def __call__(self, attrs):
        reward = attrs.get("reward")
        habit_reward = attrs.get("habit_reward")
        if reward or habit_reward:
            if reward is not None and habit_reward is not None:
                raise ValidationError("Можно выбрать только одно: вознаграждение или привычку.")
        raise ValidationError("Нужно выбрать вознаграждение или привычку-вознаграждение.")


class HabitDurationValidator:
    def __call__(self, attrs):
        duration = attrs.get("duration")
        if duration > timedelta(seconds=120):
            raise ValidationError("Привычка должна занимать не более 2 минут.")


class HabitHasHabitRewardValidator:
    def __call__(self, attrs):
        habit_reward = attrs.get("habit_reward")
        if habit_reward is not None:
            habit = Habit.filter(pk=habit_reward).first()
            if habit.is_enjoyable is False:
                raise ValidationError("В качестве вознаграждения можно выбрать только приятную привычку.")


class RewardHabitValidator:
    def __call__(self, attrs):
        if attrs.get("is_enjoyable") is True:
            reward = attrs.get("reward")
            habit_reward = attrs.get("habit_reward")
            if reward or habit_reward:
                raise ValidationError("У приятной привычки не может быть вознаграждения.")


class HabitPeriodValidator:
    def __call__(self, attrs):
        period = attrs.get("period")
        if period > timedelta(days=7):
            raise ValidationError("Нельзя выполнять привычку реже, чем 1 раз в 7 дней.")
