from django.urls import path
from rest_framework.permissions import AllowAny
from rest_framework_simplejwt.views import TokenObtainPairView
from users.apps import UsersConfig

from . import views


app_name = UsersConfig.name


urlpatterns = [
    # token
    path("token/", TokenObtainPairView.as_view(permission_classes=(AllowAny,)), name="token"),
    # users CRUD
    path("create/", views.CustomUserCreateView.as_view(), name="user-create"),
    path("<int:pk>/", views.CustomUserRetrieveView.as_view(), name="user-detail"),
    path("<int:pk>/update/", views.CustomUserUpdateView.as_view(), name="user-update"),
    path("<int:pk>/delete/", views.CustomUserDestroyView.as_view(), name="user-delete"),
]
