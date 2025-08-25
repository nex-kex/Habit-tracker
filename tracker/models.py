from datetime import timedelta

from django.db import models

from users.models import CustomUser


class Habit(models.Model):

    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name="habits", verbose_name="Пользователь")
    place = models.CharField(max_length=30, verbose_name="Место")
    scheduled_time = models.TimeField(verbose_name="Время")
    action = models.CharField(max_length=60, verbose_name="Действие")
    is_enjoyable = models.BooleanField(default=False, verbose_name="Признак приятной привычки")
    habit_reward = models.ForeignKey(
        "self",
        on_delete=models.SET_NULL,
        related_name="habits_rewarded",
        blank=True,
        null=True,
        verbose_name="Связанная привычка",
    )
    period = models.DurationField(default=timedelta(days=1), verbose_name="Периодичность")
    reward = models.CharField(max_length=60, blank=True, null=True, verbose_name="Вознаграждение")
    duration = models.DurationField(default=timedelta(minutes=15), verbose_name="Время на выполнение")
    is_public = models.BooleanField(default=True, verbose_name="Признак публичности")

    class Meta:
        verbose_name = "Привычка"
        verbose_name_plural = "Привычки"

    def __str__(self):
        return self.action
