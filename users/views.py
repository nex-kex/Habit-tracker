from rest_framework import generics
from rest_framework.permissions import AllowAny, IsAuthenticated

from .models import CustomUser
from .permissions import IsUser
from .serializers import CustomUserCreateSerializer, CustomUserSerializer


class CustomUserCreateView(generics.CreateAPIView):
    """Класс для создания пользователя."""

    queryset = CustomUser.objects.all()
    serializer_class = CustomUserCreateSerializer
    permission_classes = [AllowAny]

    def perform_create(self, serializer):
        user = serializer.save(is_active=True)
        user.set_password(user.password)
        user.save()


class CustomUserUpdateView(generics.UpdateAPIView):
    """Класс для обновления пользователя."""

    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer
    permission_classes = [IsAuthenticated, IsUser]


class CustomUserRetrieveView(generics.RetrieveAPIView):
    """Класс для получения информации об определённом пользователе."""

    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer
    permission_classes = [IsAuthenticated, IsUser]


class CustomUserDestroyView(generics.DestroyAPIView):
    """Класс для удаления пользователя."""

    queryset = CustomUser.objects.all()
    permission_classes = [IsAuthenticated, IsUser]
