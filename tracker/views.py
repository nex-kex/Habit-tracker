from rest_framework import viewsets
from .serializers import HabitSerializer
from .models import Habit
from .pagination import MyPagination


class HabitViewSet(viewsets.ModelViewSet):
    """ViewSet класс для CRUD привычек."""

    serializer_class = HabitSerializer
    pagination_class = MyPagination
    queryset = Habit.objects.all()
