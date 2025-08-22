from rest_framework.serializers import ValidationError


class HabitValidator:
    def __call__(self, attrs):
        reward = attrs.get("reward")
        habit_reward = attrs.get("habit_reward")
        if reward or habit_reward:
            if reward is not None and habit_reward is not None:
                raise ValidationError("Можно выбрать только одно: вознаграждение или привычку.")
        else:
            raise ValidationError("Нужно выбрать вознаграждение или привычку-вознаграждение.")
