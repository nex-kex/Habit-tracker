from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from tracker.models import Habit
from users.models import CustomUser


class HabitTestCase(APITestCase):

    def setUp(self):
        super().setUp()
        self.user = CustomUser.objects.create_user(
            password="password",
            username="test_username",
        )
        self.habit = Habit.objects.create(
            place="Парк",
            user=self.user,
            scheduled_time="20:00:00",
            action="Выйти на прогулку с собакой",
            is_enjoyable=False,
            period="12:00:00",
            reward="Купить пирожные",
            duration="00:01:00",
            is_public=True,
        )
        self.client.force_authenticate(user=self.user)

    def test_habits_create(self):
        """Создание привычки."""
        url = reverse("tracker:habits-list")
        data = {
            "place": "Ванная",
            "scheduled_time": "22:00:00",
            "action": "Принять горячую ванну",
            "is_enjoyable": True,
            "period": "7 00:00:00",
            "duration": "00:02:00",
            "is_public": False,
        }
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data["action"], "Принять горячую ванну")

    def test_habits_list(self):
        """Получение списка привычек."""
        url = reverse("tracker:habits-list")
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data["results"]), 1)
        self.assertEqual(response.data["results"][0]["place"], "Парк")
        self.assertEqual(response.data["results"][0]["action"], "Выйти на прогулку с собакой")

    def test_public_habits_list(self):
        """Получение списка публичных привычек."""
        url = reverse("tracker:public-habits")
        response = self.client.get(url)
        self.assertEqual(len(response.data["results"]), 1)

    def test_habits_read(self):
        """Получение информации об одной привычке."""
        response = self.client.get(reverse("tracker:habits-detail", args=[self.habit.id]))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["place"], "Парк")
        self.assertEqual(str(self.habit), "Выйти на прогулку с собакой")

    def test_habit_update(self):
        """Обновление привычки."""
        url = reverse("tracker:habits-detail", args=[self.habit.id])
        data = {
            "place": "Улица",
        }
        response = self.client.patch(url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["place"], "Улица")

    def test_course_destroy(self):
        """Удаление привычки."""
        response = self.client.delete(reverse("tracker:habits-detail", args=[self.habit.id]))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(Habit.objects.filter(id=self.habit.id).exists())
