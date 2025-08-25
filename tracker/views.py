from rest_framework import generics, viewsets
from rest_framework.permissions import IsAuthenticated

from users.permissions import IsAuthor

from .models import Habit
from .pagination import MyPagination
from .serializers import HabitSerializer
from .tasks import send_tg_notification


class HabitViewSet(viewsets.ModelViewSet):
    """ViewSet класс для CRUD привычек пользователя."""

    serializer_class = HabitSerializer
    pagination_class = MyPagination

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
        send_tg_notification.delay(self.request.user.id)

    def get_permissions(self):
        if self.action in ["create", "list"]:
            self.permission_classes = [IsAuthenticated]
        elif self.action in ["update", "retrieve", "partial_update", "destroy"]:
            self.permission_classes = [IsAuthenticated, IsAuthor]
        return [permission() for permission in self.permission_classes]

    def get_queryset(self):
        return Habit.objects.filter(user=self.request.user)


class PublicHabitListView(generics.ListAPIView):
    """Класс для отображения списка публичных привычек."""

    serializer_class = HabitSerializer
    pagination_class = MyPagination
    queryset = Habit.objects.filter(is_public=True)
