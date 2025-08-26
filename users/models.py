from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):

    email = models.EmailField(verbose_name="Email", blank=True, null=True, unique=True)
    phone = models.IntegerField(verbose_name="Номер телефона", blank=True, null=True, unique=True)

    tg_username = models.CharField(verbose_name="Имя пользователя в Телеграм", blank=True, null=True)
    tg_chat_id = models.CharField(verbose_name="ID чата в Телеграм", blank=True, null=True)

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"
        ordering = ["username"]

    def __str__(self):
        return self.username
