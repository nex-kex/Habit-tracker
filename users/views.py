from rest_framework import generics
from .models import CustomUser
from .serializers import CustomUserSerializer, CustomUserCreateSerializer
from rest_framework.permissions import AllowAny, IsAuthenticated
from .permissions import IsUser


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
    permission_classes = [IsUser, IsAuthenticated]


class CustomUserRetrieveView(generics.RetrieveAPIView):
    """Класс для получения информации об определённом пользователе."""

    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer
    permission_classes = [IsUser, IsAuthenticated]


class CustomUserDestroyView(generics.DestroyAPIView):
    """Класс для удаления пользователя."""

    queryset = CustomUser.objects.all()
    permission_classes = [IsUser, IsAuthenticated]
