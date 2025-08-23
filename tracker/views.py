from rest_framework import viewsets, generics
from rest_framework.permissions import IsAuthenticated

from .serializers import HabitSerializer
from .models import Habit
from .pagination import MyPagination
from users.permissions import IsAuthor


class HabitViewSet(viewsets.ModelViewSet):
    """ViewSet класс для CRUD привычек пользователя."""

    serializer_class = HabitSerializer
    pagination_class = MyPagination

    def get_permissions(self):
        if self.action in ["create", "list"]:
            self.permission_classes = [IsAuthenticated]
        elif self.action in ["update", "retrieve", "partial_update", "destroy"]:
            self.permission_classes = [IsAuthenticated, IsAuthor]
        return [permission() for permission in self.permission_classes]

    def get_queryset(self):
        return Habit.objects.filter(user=self.request.user)


class UserHabitListView(generics.ListAPIView):
    """Класс для отображения списка публичных привычек."""

    serializer_class = HabitSerializer
    pagination_class = MyPagination
    queryset = Habit.objects.filter(is_public=True)
