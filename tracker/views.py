from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from django.db.models import Q

from .serializers import HabitSerializer
from .models import Habit
from .pagination import MyPagination
from users.permissions import IsAuthor


class HabitViewSet(viewsets.ModelViewSet):
    """ViewSet класс для CRUD привычек."""

    serializer_class = HabitSerializer
    pagination_class = MyPagination
    queryset = Habit.objects.all()

    def get_permissions(self):
        if self.action in ["create", "list"]:
            self.permission_classes = [IsAuthenticated]
        elif self.action in ["update", "retrieve", "partial_update", "destroy"]:
            self.permission_classes = [IsAuthenticated, IsAuthor]
        return [permission() for permission in self.permission_classes]

    def get_queryset(self):
        return Habit.objects.filter(Q(is_public=True) | Q(user=self.request.user))
